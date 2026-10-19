"""Execute verified upstream deterministic assets; never impersonates Claude Code."""
import argparse
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path
from core import ROOT, read, write, validate, now

def command(args, log, timeout=60):
    result = subprocess.run([str(a) for a in args], capture_output=True, text=True, encoding='utf-8', timeout=timeout)
    log.append({'argv': [str(a) for a in args], 'exitCode': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr, 'at': now()})
    if result.returncode:
        raise RuntimeError(result.stderr or result.stdout)
    return result

def bmad(run):
    validate(run)
    upstream = ROOT / 'integrations/upstream/bmad'
    folder = run / 'planning/bmad'
    folder.mkdir(parents=True, exist_ok=True)
    k = read(run / 'knowledge/system.json'); reqs = read(run / 'requirements/requirements.json')
    assets = ['src/bmm-skills/plan/bmad-product-brief/assets/brief-template.md', 'src/bmm-skills/plan/bmad-spec/assets/spec-template.md']
    provenance = []
    for relative in assets:
        path = upstream / relative
        provenance.append({'path': relative, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
        shutil.copyfile(path, folder / path.name)
    shutil.copyfile(upstream / 'LICENSE', folder / 'UPSTREAM-LICENSE')
    log = []
    memlog = upstream / 'src/scripts/memlog.py'
    if not (folder / '.memlog.md').exists():
        command([sys.executable, memlog, 'init', '--workspace', folder, '--field', f"topic={k['system']['name']}"], log)
    command([sys.executable, memlog, 'append', '--workspace', folder, '--type', 'event', '--text', 'Adapted template execution by deterministic local exporter; native Claude Code workflow not invoked.'], log)
    for req in reqs:
        command([sys.executable, memlog, 'append', '--workspace', folder, '--type', 'capability', '--text', f"{req['id']}: {req['statement']} Evidence: {','.join(req['evidenceIds'])}; state: {req['verificationState']}"], log)
    for q in k['openQuestions']:
        command([sys.executable, memlog, 'append', '--workspace', folder, '--type', 'question', '--text', q['id'] + ': ' + q['description']], log)
    brief = f"# Product Brief: {k['system']['name']}\n\n> Adaptation of pinned BMAD brief-template.md; reconstruction, not stakeholder-approved product strategy.\n\n## Executive Summary\n\n{k['system']['description']}\n\n## The Problem\n\nDocument existing visible behavior for planning; user/business pain not established from interface evidence.\n\n## The Solution\n\nUse the evidenced feature inventory, not a proposal to rebuild the website.\n\n## Who This Serves\n\n"
    brief += '\n'.join(f"- {x['id']}: {x['name']} ({x['status']})" for x in k['actors'])
    brief += '\n\n## Success Criteria\n\nEvery reconstructed requirement has explicit evidence, bounded acceptance and uncertainty.\n\n## Scope\n\nPublic read-only sample; authentication and mutations excluded.\n\n## Unknowns\n\n' + '\n'.join('- ' + q['description'] for q in k['openQuestions'])
    (folder / 'brief.md').write_text(brief+'\n', encoding='utf-8')
    spec = f"# {k['system']['name']} — reconstructed planning kernel\n\n> Adapted from pinned BMAD spec-template.md; not native bmad-spec output.\n\n## Why\n\nCreate evidence-backed planning documentation of public behavior.\n\n## Capabilities\n\n"
    spec += '\n'.join(f"- **{r['id']}**\n  - **intent:** {r['statement']}\n  - **success:** {'; '.join(r['acceptanceCriteria'])}" for r in reqs)
    spec += '\n\n## Constraints\n\nRead-only evidence; inferred/proposed records remain labeled.\n\n## Non-goals\n\nNo backend design, feature implementation or invented stakeholder decisions.\n\n## Success signal\n\nReviewer resolves requirements to captured evidence.\n\n## Open Questions\n\n' + '\n'.join('- ' + q['description'] for q in k['openQuestions'])
    (folder / 'adapted-SPEC.md').write_text(spec+'\n', encoding='utf-8')
    write(folder / 'execution.json', {'status': 'partial', 'mode': 'actual upstream templates adapted and memlog executed', 'nativeClaudeExecution': 'blocked: Claude CLI unavailable',
        'version': read(ROOT / 'integrations/manifest.json')['bmad'], 'inputs': ['knowledge/system.json', 'requirements/requirements.json'], 'assets': provenance, 'commands': log,
        'transformation': 'Canonical requirements remain authoritative; render command expands acceptance, sources, uncertainty, data, boundaries and traceability into SRS. Brief/spec are not labeled SRS.'})

def ua(run):
    validate(run)
    skill = ROOT / 'integrations/upstream/understand-anything/understand-anything-plugin/skills/understand-knowledge'
    log = []
    for script in ['parse-knowledge-base.py', 'merge-knowledge-graph.py']:
        command([sys.executable, skill / script, run / 'wiki'], log)
    data = run / 'wiki/.ua'
    graph = read(data / 'intermediate/assembled-graph.json')
    ids = {n['id'] for n in graph['nodes']}
    if any(e['source'] not in ids or e['target'] not in ids for e in graph['edges']):
        raise ValueError('Upstream graph contains dangling edges')
    mapping = read(run / 'graph/id-mapping.json')
    if any(x['upstreamId'] not in ids for x in mapping.values()):
        raise ValueError('Canonical-to-upstream mapping is incomplete')
    write(data / 'knowledge-graph.json', graph)
    write(data / 'meta.json', {'lastAnalyzedAt': now(), 'gitCommitHash': '', 'version': '1.0.0', 'analyzedFiles': len(mapping)})
    write(run / 'graph/upstream-execution.json', {'status': 'partial', 'phases': {'detect': 'tested', 'scan': 'tested', 'analyze': 'blocked: native Claude article-analyzer unavailable; no fabricated batches', 'merge': 'tested', 'save': 'tested', 'viewer': 'pending'},
        'version': read(ROOT / 'integrations/manifest.json')['understandAnything'], 'commands': log,
        'graphPath': 'wiki/.ua/knowledge-graph.json', 'nodes': len(graph['nodes']), 'edges': len(graph['edges']),
        'loss': 'Canonical business types map to article pages; relation types collapse to related wikilinks. Full types/provenance retained in graph/canonical.json and linked detail JSON.'})
    print(f"{len(graph['nodes'])} upstream nodes; {len(graph['edges'])} edges")

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('integration', choices=['bmad', 'ua'])
    p.add_argument('run', type=Path)
    a=p.parse_args()
    {'bmad': bmad, 'ua': ua}[a.integration](a.run)
