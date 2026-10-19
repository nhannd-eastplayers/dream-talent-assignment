import argparse
import importlib.metadata
import shutil
import subprocess
from pathlib import Path
from core import ROOT, read, write, schema_check, safe_url, now

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('run',type=Path);p.add_argument('--browser',action='store_true');a=p.parse_args()
    config=read(a.run/'config.json');schema_check(config,'config');safe_url(config['url'],config)
    report={'at':now(),'status':'partial','capabilities':{},'blockers':[],'versions':{}}
    for exe in ['python','node','claude','uv']:
        path=shutil.which(exe)
        report['capabilities'][exe]=bool(path)
        if path:
            try:
                result=subprocess.run([path,'--version'],capture_output=True,text=True,timeout=10)
                report['versions'][exe]=result.stdout.strip()
            except (OSError,subprocess.TimeoutExpired) as e:report['versions'][exe]=str(e)
    if not report['capabilities']['claude']:
        report['blockers'].append('Claude CLI not discovered; native Claude skill dispatch cannot be tested by this preflight. Existing in-session Skill capability must be checked separately.')
    for package in ['jsonschema','playwright']:
        report['versions'][package]=importlib.metadata.version(package)
    for key, directory in [('bmad','bmad'),('understandAnything','understand-anything')]:
        source=ROOT/'integrations/upstream'/directory
        expected=read(ROOT/'integrations/manifest.json')[key]['commit']
        result=subprocess.run(['git','-c',f'safe.directory={source.as_posix()}','-C',str(source),'rev-parse','HEAD'],capture_output=True,text=True,timeout=10)
        actual=result.stdout.strip()
        report['capabilities'][key]=actual==expected
        report['versions'][key]=actual or result.stderr.strip()
        if actual!=expected:report['blockers'].append(f'{key}: pinned source unavailable or mismatched')
    if a.browser:
        from playwright.sync_api import sync_playwright
        try:
            with sync_playwright() as pw:
                browser=pw.chromium.launch(headless=True)
                report['versions']['chromium']=browser.version
                report['capabilities']['browserHelper']=True
                browser.close()
        except Exception as e:
            report['capabilities']['browserHelper']=False
            report['blockers'].append(f'Live exploration blocked: {e}')
    else:report['capabilities']['browserHelper']='not checked'
    report['stopReason']='Native integrations require actual Claude session; independent deterministic work can continue.'
    write(a.run/'preflight.json',report)
    print(report)
