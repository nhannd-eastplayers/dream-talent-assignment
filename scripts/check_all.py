"""Reproduce checks and retain their exact output; no claim beyond executed commands."""
import argparse
import os
import subprocess
import sys
from core import ROOT, now

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--browser',action='store_true');p.add_argument('--upstream',action='store_true');a=p.parse_args()
    commands=[[sys.executable,'-m','unittest','discover','-s','tests','-v']]
    for output in sorted((ROOT/'examples').glob('*/output')):
        run=output.relative_to(ROOT).as_posix()
        commands.append([sys.executable,'scripts/planning.py','validate-artifacts',run,'--derived'])
        if a.upstream:commands.append([sys.executable,'scripts/check_upstream_schema.py',run])
    env=dict(os.environ,PYTHONIOENCODING='utf-8')
    if a.browser:env['PLANNING_BROWSER_TESTS']='1'
    log=[f'Executed at {now()}',f'Browser acceptance enabled: {a.browser}; exact upstream schema enabled: {a.upstream}','']
    failed=False
    for args in commands:
        result=subprocess.run(args,cwd=ROOT,env=env,capture_output=True,text=True,encoding='utf-8',timeout=60)
        log+=['ARGV: '+repr(args),'EXIT: '+str(result.returncode),result.stdout,result.stderr,'']
        failed=failed or result.returncode!=0
    (ROOT/'docs/test-results.txt').write_text('\n'.join(log),encoding='utf-8')
    print('\n'.join(log))
    raise SystemExit(1 if failed else 0)
