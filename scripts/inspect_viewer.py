"""Opt-in local upstream viewer inspection; URL is supplied by running viewer."""
import argparse
import sys
import re
from pathlib import Path
from urllib.parse import urlsplit
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from core import write, now

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    p=argparse.ArgumentParser()
    p.add_argument('url');p.add_argument('output',type=Path)
    p.add_argument('--search',required=True)
    p.add_argument('--evidence')
    a=p.parse_args()
    target=urlsplit(a.url)
    if target.scheme!='http' or target.hostname not in ('127.0.0.1','localhost'):
        raise ValueError('Viewer inspection requires loopback HTTP URL')
    a.output.mkdir(parents=True,exist_ok=True)
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True)
        page=browser.new_page(viewport={'width':1440,'height':1000})
        page.set_default_timeout(10000)
        page.goto(a.url,wait_until='domcontentloaded',timeout=30000)
        page.locator('input').first.wait_for(timeout=30000)
        dismiss=page.get_by_role('button',name="Don't show again",exact=False)
        try:
            dismiss.wait_for(state='visible',timeout=5000)
            dismiss.click()
        except PlaywrightTimeoutError:
            pass
        search=page.get_by_placeholder('Search nodes by name, summary, or tags...')
        search.fill(a.search)
        page.get_by_text(a.search,exact=False).first.wait_for(timeout=10000)
        page.get_by_role('button',name=re.compile(re.escape(a.search))).first.click()
        page.get_by_text('Connections',exact=False).first.wait_for(timeout=10000)
        page.screenshot(path=str(a.output/'viewer.png'),full_page=True)
        (a.output/'viewer-text.txt').write_text(page.locator('body').inner_text(),encoding='utf-8')
        controls=page.locator('input').evaluate_all('(els)=>els.map(e=>({placeholder:e.placeholder,ariaLabel:e.getAttribute("aria-label"),type:e.type}))')
        print(controls)
        print(page.locator('body').inner_text()[-5000:])
        write(a.output/'viewer-inspection.json',{'at':now(),'pageTitle':page.title(),'screenshot':'viewer.png','status':'opened','searchRequested':a.search,'controls':controls})
        if a.evidence:
            page.get_by_role('button',name=re.compile(re.escape(a.evidence))).first.click()
            page.get_by_text('PREVIEW',exact=False).first.wait_for(timeout=10000)
            text=page.locator('body').inner_text()
            if a.evidence not in text or 'contentHash' not in text:
                raise ValueError('Evidence detail was not resolved in viewer')
            page.screenshot(path=str(a.output/'evidence-node.png'),full_page=True)
            (a.output/'evidence-node.txt').write_text(text,encoding='utf-8')
            write(a.output/'evidence-inspection.json',{'at':now(),'status':'evidence resolved','canonicalEvidenceId':a.evidence,'fromRequirement':a.search,'screenshot':'evidence-node.png'})
        browser.close()
