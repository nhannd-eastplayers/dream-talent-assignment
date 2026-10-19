"""Explicit read-only browser helper. JSON action plan in; snapshots/evidence out.

Supports goto, click (read-only controls only), fill, select, snapshot. No eval,
shell, arbitrary JavaScript, form POSTs, uploads, or credential persistence.
"""
import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlsplit
from playwright.sync_api import sync_playwright
from core import read, write, schema_check, safe_url, now, digest

def execute(run, plan, fixture=False):
    config = read(run / 'config.json')
    schema_check(config, 'config')
    if fixture != config['allowLocalFixture']:
        raise ValueError('Explicit --fixture required for local fixture configurations')
    budget_path = run / 'evidence/browser-budget.json'
    from datetime import datetime, timezone
    budget = read(budget_path) if budget_path.exists() else {'startedAt': now(), 'actionsByUrl': {}}
    elapsed = (datetime.now(timezone.utc) - datetime.fromisoformat(budget['startedAt'])).total_seconds()
    deadline = time.monotonic() + max(0, config['maxRuntimeMinutes'] * 60 - elapsed)
    evidence_path = run / 'evidence/evidence.json'
    evidence = read(evidence_path) if evidence_path.exists() else []
    inventory_path = run / 'discovery/pages.json'
    inventory = read(inventory_path) if inventory_path.exists() else []
    visited = {x['url'] for x in inventory}
    count = 0
    errors = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context(service_workers='block')
        context.set_default_timeout(12000)
        def guard(route):
            request = route.request
            try:
                safe_url(request.url, config)
                if request.is_navigation_request() and request.frame == page.main_frame:
                    if request.url not in visited and len(visited) >= config['maxPages']:
                        raise ValueError('Page budget exceeded')
                    visited.add(request.url)
                if request.method not in ('GET', 'HEAD', 'OPTIONS'):
                    raise ValueError('Mutating network method blocked')
                route.continue_()
            except (ValueError, OSError):
                route.abort()
        context.route('**/*', guard)
        page = context.new_page()
        for action in plan:
            if time.monotonic() >= deadline:
                errors.append('Browser deadline reached')
                break
            kind = action['type']
            try:
                if kind == 'goto':
                    safe_url(action['url'], config)
                    if not isinstance(action.get('depth', 0), int) or not 0 <= action.get('depth', 0) <= config['maxDepth']:
                        raise ValueError('Depth budget exceeded')
                    if action['url'] not in visited and len(visited) >= config['maxPages']:
                        raise ValueError('Page budget exceeded')
                    page.goto(action['url'], wait_until='domcontentloaded', timeout=min(20000, max(1, int((deadline-time.monotonic())*1000))))
                    safe_url(page.url, config)
                    visited.add(page.url)
                elif kind in ('click', 'fill', 'select'):
                    action_url = page.url
                    if budget['actionsByUrl'].get(action_url, 0) >= config['maxActionsPerPage']:
                        raise ValueError('Action budget exceeded')
                    # Caller must supply readOnly=true after semantic inspection.
                    if action.get('readOnly') is not True:
                        raise ValueError('Read-only action attestation required')
                    locator = page.locator(action['selector'])
                    if kind == 'fill' and locator.get_attribute('type') in ('password', 'file', 'tel'):
                        raise ValueError('Sensitive input not allowed')
                    budget['actionsByUrl'][action_url] = budget['actionsByUrl'].get(action_url, 0) + 1
                    if kind == 'click':
                        href = locator.get_attribute('href')
                        if href:
                            from urllib.parse import urljoin
                            safe_url(urljoin(page.url, href), config)
                            if urljoin(page.url, href) not in visited and len(visited) >= config['maxPages']:
                                raise ValueError('Page budget exceeded')
                        locator.click(no_wait_after=True)
                    elif kind == 'fill':
                        locator.fill(action['value'])
                    else:
                        locator.select_option(action['value'])
                    safe_url(page.url, config)
                    visited.add(page.url)
                elif kind != 'snapshot':
                    raise ValueError('Unsupported browser action')
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise ValueError('Browser deadline reached')
                page.wait_for_timeout(min(config['requestDelayMs'], int(remaining*1000)))
                text = page.locator('body').inner_text()
                text = re.sub(r'(?<!\d)(?:\+84|0)[ .-]?(?:\d[ .-]?){9}(?!\d)', '[redacted phone]', text)
                text = re.sub(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', '[redacted email]', text)
                # Read DOM only, no arbitrary page script execution.
                links = page.locator('a[href]').evaluate_all('(els) => els.map(e => ({text:e.innerText,href:e.href}))')
                title = page.title()
                controls = page.locator('button,input,select,[role="button"]').evaluate_all('(els) => els.slice(0,100).map(e => ({tag:e.tagName,id:e.id,type:e.type,role:e.getAttribute("role"),name:e.getAttribute("name"),placeholder:e.getAttribute("placeholder"),text:e.innerText,ariaLabel:e.getAttribute("aria-label")}))')
                token = digest({'url': page.url, 'action': action, 'text': text})[:16]
                eid = 'EVID-' + token
                snapshot = f'evidence/snapshots/{eid}.txt'
                (run / snapshot).write_text(text, encoding='utf-8')
                excerpt = action.get('excerpt') or text[:1200]
                if not excerpt or excerpt not in text:
                    raise ValueError('Requested excerpt absent from page')
                record = {'id': eid, 'sourceType': 'fixture' if fixture else 'browser', 'url': page.url, 'capturedAt': now(),
                    'pageTitle': title, 'excerpt': excerpt, 'locator': action.get('selector', 'body'), 'snapshotPath': snapshot,
                    'action': json.dumps(action, ensure_ascii=False), 'result': 'Rendered text captured; behavior limited to this action',
                    'contentHash': hashlib.sha256((run / snapshot).read_bytes()).hexdigest()}
                if eid not in {e['id'] for e in evidence}:
                    evidence.append(record)
                inventory.append({'url': page.url, 'title': title, 'depth': action.get('depth', 0), 'evidenceId': eid,
                    'controls': controls,
                    'links': [l for l in links if f"{urlsplit(l['href']).scheme}://{urlsplit(l['href']).netloc}" in config['allowedOrigins']]})
                count += 1
            except Exception as e:
                errors.append(f'{action}: {type(e).__name__}: {e}')
            write(evidence_path, evidence)
            write(inventory_path, inventory)
            write(budget_path, budget)
        browser.close()
    report = {'captured': count, 'errors': errors, 'finishedAt': now(), 'stopReason': 'plan exhausted' if not errors else 'plan ended with failures',
        'limitations': 'Third-party origins and non-read network methods blocked. Overall agent deadline advisory; helper operations individually bounded.'}
    write(run / 'evidence/browser-report.json', report)
    return report

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('run', type=Path)
    p.add_argument('plan', type=Path)
    p.add_argument('--fixture', action='store_true')
    a = p.parse_args()
    report = execute(a.run, read(a.plan), a.fixture)
    print(json.dumps(report, ensure_ascii=False))
    sys.exit(1 if report['errors'] else 0)
