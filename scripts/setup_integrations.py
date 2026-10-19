"""Fetch exact official sources into project scope, without user-level config writes."""
import subprocess
from core import ROOT, read

def run(args):
    subprocess.run(args,check=True,timeout=120)

if __name__=='__main__':
    for key,directory in [('bmad','bmad'),('understandAnything','understand-anything')]:
        entry=read(ROOT/'integrations/manifest.json')[key]
        target=ROOT/'integrations/upstream'/directory
        if not target.exists():
            target.parent.mkdir(parents=True,exist_ok=True)
            run(['git','clone','--no-checkout','--filter=blob:none',entry['repository']+'.git',str(target)])
        git=['git','-c',f'safe.directory={target.as_posix()}','-C',str(target)]
        # No reset/clean/force: existing modifications cause a normal checkout failure.
        run(git+['fetch','origin',entry['commit']])
        run(git+['checkout','--detach',entry['commit']])
        actual=subprocess.check_output(git+['rev-parse','HEAD'],text=True,timeout=10).strip()
        if actual!=entry['commit']:raise ValueError('Upstream SHA mismatch')
        print(f'{key}: {actual}')
