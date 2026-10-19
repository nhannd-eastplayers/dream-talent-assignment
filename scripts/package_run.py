"""Curate an already analyzed run; preserve evidence IDs and report partial work."""
import argparse
import hashlib
import shutil
from pathlib import Path
from core import ROOT, read, write, validate, canonical, export_wiki, traceability, render, checkpoint, now, STAGES
from integrate import ua

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('run',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
    source=a.run.resolve();output=a.output.resolve()
    if not source.is_relative_to(ROOT/'runs') or not output.is_relative_to(ROOT/'examples'):
        raise ValueError('Package from runs/ into examples/ only')
    validate(source,True)
    shutil.copytree(source,output,dirs_exist_ok=True)
    evidence=read(output/'evidence/evidence.json')
    for e in evidence:
        snapshot=output/e['snapshotPath']
        original=e['contentHash']
        snapshot.write_text(e['excerpt'],encoding='utf-8')
        e['contentHash']=hashlib.sha256(snapshot.read_bytes()).hexdigest()
        e['result']+=f'; curated exact excerpt; unrelated text removed; raw capture SHA-256 {original}'
    write(output/'evidence/evidence.json',evidence)
    canonical(output);export_wiki(output);traceability(output);render(output);ua(output)
    review=read(output/'review.json');reqs=read(output/'requirements/requirements.json')
    if {r['id'] for r in reqs}!={r['id'] for r in review['findings']}:
        raise ValueError('Review does not cover exactly the requirement set')
    validation=validate(output,True);write(output/'validation.json',dict(validation,at=now()))
    report=['# Quality report','',f"Reviewer: {review['reviewer']}",f"Review date: {review['date']}",'',
        f"Deterministic validation: passed; {len(reqs)} requirements; schema, IDs, references, snapshot hashes, SRS content, graph and traceability checked.",
        '', 'Repair passes: 1 / 2 (tightened evidence scope and integration labels before packaging).', '',
        '| Requirement | Evidence support | Ambiguity / coverage limit |','|---|---|---|']
    report += [f"| {r['id']} | {r['support']} | {r['limitation']} |" for r in review['findings']]
    report += ['', '## Unresolved', '']+['- '+x for x in review['unresolved']]
    report += ['', 'No measured semantic accuracy is claimed. This is agent review, not independent human approval.']
    (output/'quality-report.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
    pages=read(output/'discovery/pages.json');upstream=read(output/'graph/upstream-execution.json')
    inspected=(output/'graph/inspection/evidence-inspection.json').exists()
    upstream['phases']['viewer']='tested: requirement selected and evidence resolved in official upstream viewer' if inspected else 'pending'
    upstream['inspectionNote']='Screenshots show actual raw-run viewer before curated excerpt/hash export; IDs and business claims preserved. Curated graph schema is rechecked separately.' if inspected else 'Exact schema checked separately; viewer not yet inspected for this fixture.'
    write(output/'graph/upstream-execution.json',upstream)
    text=f"""# Execution report

Run: {read(output/'manifest.json')['id']}
Status: **partial**
Stop reason: native Claude dispatch and semantic integration are not verified by this deterministic adapter-mode package; independent work completed.

## Actual outputs

{len(reqs)} requirements; {len(read(output/'knowledge/system.json')['features'])} discovered features; {len(evidence)} retained browser states; {len({x['url'] for x in pages})} distinct visited URLs. Coverage is relative to discovered sample, never exhaustive.

Browser source: actual Playwright Chromium helper. Each retained state includes original URL/action/timestamp plus an exact curated excerpt. Snapshots were reduced for submission; raw capture hashes remain in result fields. No authenticated browser state, credentials or contact submissions retained. Raw browsing artifacts remain ignored in runs/.

BMAD: actual upstream templates adapted and real memory script executed. See planning/bmad/execution.json for input paths, content hashes, argv, exit codes and limitations. Native BMAD skill activation **not executed**.

Understand-Anything: real parser and merger; {upstream['nodes']} nodes and {upstream['edges']} edges. Exact upstream schema checked. Native semantic article-analyzer **not executed**. Viewer: {upstream['phases']['viewer']}.

Graph location: wiki/.ua/knowledge-graph.json; typed canonical graph and mapping: graph/. Launch official viewer using docs/setup.md. Search a requirement ID, inspect feature backlink, follow evidence wikilink; exact business relation types remain in canonical.json.

Validation: passed. Review: quality-report.md and review.json. No independent human sign-off or calibrated accuracy claimed. Full test execution is recorded in docs/test-results.txt.

Resume: open repository in authenticated Claude Code; verify custom skill discovery/dispatch, native BMAD activation and UA semantic phase. Check dependency hashes before skipping completed stages. Keep current unknowns and read-only limits. See docs/demo.md for reproducible deterministic demo.
"""
    (output/'run-report.md').write_text(text,encoding='utf-8')
    # Rebuild portable checkpoints using packaged inputs. Partial integrations remain explicit.
    m=read(output/'manifest.json')
    m['upstreamVersions']=read(ROOT/'integrations/manifest.json')
    for s in STAGES:m['stages'][s].update(state='pending',inputHash='',inputFiles={},artifacts={})
    write(output/'manifest.json',m)
    plans={
        'preflight':('partial',['config.json'],['config.json']),
        'discover':('completed',['config.json'],['discovery/pages.json']),
        'explore':('completed',['discovery/pages.json'],['evidence/evidence.json']+[e['snapshotPath'] for e in evidence]),
        'analyze':('completed',['evidence/evidence.json'],['knowledge/system.json','requirements/requirements.json','review.json']),
        'bmad':('partial',['knowledge/system.json','requirements/requirements.json'],['planning/bmad/execution.json','planning/bmad/brief.md','planning/bmad/adapted-SPEC.md']),
        'srs':('completed',['knowledge/system.json','requirements/requirements.json'],['SRS.md','feature-analysis.md']),
        'graph':('partial',['knowledge/system.json','requirements/requirements.json','evidence/evidence.json'],['graph/canonical.json','graph/id-mapping.json','wiki/.ua/knowledge-graph.json','traceability.csv']),
        'validate':('completed',['SRS.md','graph/canonical.json','traceability.csv'],['validation.json','quality-report.md']),
        'package':('partial',['quality-report.md','validation.json'],['run-report.md'])}
    for s,(state,inputs,artifacts) in plans.items():
        checkpoint(output,s,state,[output/f for f in inputs]+[ROOT/'integrations/manifest.json'],[output/f for f in artifacts],
            'Native Claude dispatch/semantic integration or independent review remains unverified' if state=='partial' else '')
    m=read(output/'manifest.json');m.update(status='partial',stopReason='Native Claude skill activation and UA semantic phase unavailable; independent deterministic artifacts and browser evidence delivered.',updatedAt=now())
    write(output/'manifest.json',m)
    print(output,validate(output,True))
