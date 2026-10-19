"""Opt-in browser acceptance against an independently authored local website."""
import functools
import http.server
import os
import sys
import tempfile
import threading
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from core import ROOT, read, write
from browser import execute

@unittest.skipUnless(os.environ.get('PLANNING_BROWSER_TESTS')=='1','Set PLANNING_BROWSER_TESTS=1 for real Chromium smoke')
class BrowserAcceptance(unittest.TestCase):
    def test_filter_empty_and_account_boundary(self):
        class Quiet(http.server.SimpleHTTPRequestHandler):
            def log_message(self,*args):pass
        handler=functools.partial(Quiet,directory=str(ROOT/'examples/fixture/site'))
        server=http.server.ThreadingHTTPServer(('127.0.0.1',0),handler)
        threading.Thread(target=server.serve_forever,daemon=True).start()
        origin=f'http://127.0.0.1:{server.server_port}'
        try:
            with tempfile.TemporaryDirectory(dir=ROOT/'runs') as temp:
                run=Path(temp);(run/'evidence/snapshots').mkdir(parents=True);(run/'discovery').mkdir()
                config=read(ROOT/'examples/fixture/config.json');config.update(url=origin+'/',allowedOrigins=[origin])
                write(run/'config.json',config)
                plan=read(ROOT/'examples/fixture/browser-plan.json')
                for action in plan:
                    if 'url' in action:action['url']=action['url'].replace('http://127.0.0.1:8765',origin)
                report=execute(run,plan,True)
                self.assertEqual(report['captured'],7)
                self.assertEqual(report['errors'],[])
                evidence=read(run/'evidence/evidence.json')
                self.assertIn('No items found',evidence[4]['excerpt'])
                self.assertIn('Sign in required',evidence[6]['excerpt'])
                # Budget is persisted across helper calls; a changed plan cannot bypass it.
                config['maxPages']=1;write(run/'config.json',config)
                report=execute(run,[{'type':'goto','url':origin+'/new.html'}],True)
                self.assertEqual(report['captured'],0)
                self.assertIn('Page budget exceeded',report['errors'][0])
        finally:
            server.shutdown();server.server_close()
