import copy
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from core import ROOT, read, write, schema_check, safe_url, validate, canonical, export_wiki, traceability, render, checkpoint, resume, STAGES

class Artifacts(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=ROOT / 'runs')
        self.run = Path(self.temp.name)
        source = ROOT / 'examples/fixture/output'
        if not source.exists():
            source = ROOT / 'runs/fixture-20261019'
        for name in ['knowledge', 'requirements', 'evidence']:
            shutil.copytree(source / name, self.run / name)
        shutil.copyfile(source / 'config.json', self.run / 'config.json')
        shutil.copyfile(source / 'manifest.json', self.run / 'manifest.json')
        (self.run / 'graph').mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def change(self, path, mutate):
        data=read(self.run/path);mutate(data);write(self.run/path,data)

    def test_fixture_reference_and_exports(self):
        expected=read(ROOT/'examples/fixture/expected.json')
        self.assertEqual(set(expected['features']), {f['id'] for f in read(self.run/'knowledge/system.json')['features']})
        self.assertEqual(set(expected['requirements']), {r['id'] for r in read(self.run/'requirements/requirements.json')})
        canonical(self.run);export_wiki(self.run);traceability(self.run);render(self.run)
        self.assertEqual(validate(self.run,True)['requirements'],5)

    def test_invalid_config(self):
        config=read(self.run/'config.json');config['maxPages']=0
        with self.assertRaises(ValueError):schema_check(config,'config')
        config=read(self.run/'config.json');config['allowMutations']=True
        with self.assertRaises(ValueError):schema_check(config,'config')

    def test_unsafe_urls(self):
        for url in ['file:///etc/passwd','http://127.0.0.1/','http://169.254.169.254/','http://[::1]/','http://localhost/','http://user:pass@example.com/']:
            origin=url.split('/',3)
            config={'allowedOrigins':['/'.join(origin[:3])],'allowLocalFixture':False}
            with self.assertRaises(ValueError):safe_url(url,config)

    def test_explicit_fixture_url(self):
        config=read(self.run/'config.json')
        self.assertEqual(safe_url(config['url'],config),config['url'])
        with self.assertRaises(ValueError):safe_url('http://10.0.0.1/',dict(config,allowedOrigins=['http://10.0.0.1']))

    def test_missing_evidence(self):
        self.change('requirements/requirements.json',lambda rs:rs[0].update(evidenceIds=[]))
        with self.assertRaisesRegex(ValueError,'lacks evidence'):validate(self.run)

    def test_inference_without_rationale(self):
        self.change('requirements/requirements.json',lambda rs:rs[0].update(status='inferred',rationale=''))
        with self.assertRaisesRegex(ValueError,'rationale'):validate(self.run)

    def test_duplicate_id(self):
        self.change('requirements/requirements.json',lambda rs:rs.append(copy.deepcopy(rs[0])))
        with self.assertRaisesRegex(ValueError,'Duplicate'):validate(self.run)

    def test_wrong_reference_type(self):
        self.change('requirements/requirements.json',lambda rs:rs[0].update(featureId='ACTOR-VISITOR'))
        with self.assertRaisesRegex(ValueError,'reference'):validate(self.run)

    def test_malformed_artifact(self):
        self.change('knowledge/system.json',lambda k:k['features'][0].update(status='certain'))
        with self.assertRaises(ValueError):validate(self.run)

    def test_snapshot_tamper(self):
        evidence=read(self.run/'evidence/evidence.json')[0]
        (self.run/evidence['snapshotPath']).write_text('changed',encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'hash mismatch'):validate(self.run)

    def test_broken_graph(self):
        canonical(self.run);export_wiki(self.run);traceability(self.run);render(self.run)
        self.change('graph/canonical.json',lambda g:g['edges'][0].update(target='MISSING'))
        with self.assertRaisesRegex(ValueError,'graph'):validate(self.run,True)

    def test_resume_changed_dependency(self):
        m=read(self.run/'manifest.json')
        for s in STAGES:m['stages'][s].update(state='pending',inputFiles={},artifacts={},inputHash='')
        write(self.run/'manifest.json',m)
        source=self.run/'config.json'
        output=self.run/'checkpoint.txt';output.write_text('one',encoding='utf-8')
        for stage in STAGES:checkpoint(self.run,stage,'completed',[source],[output])
        self.assertEqual(len(resume(self.run)['skipped']),len(STAGES))
        output.write_text('changed',encoding='utf-8')
        self.assertEqual(resume(self.run)['skipped'],[])
        self.assertTrue(all(s=='pending' for s in resume(self.run)['stages'].values()))

    def test_export_actual_upstream(self):
        upstream=ROOT/'integrations/upstream/understand-anything/understand-anything-plugin/skills/understand-knowledge'
        if not upstream.exists():self.skipTest('Fetch pinned upstream to test actual parser')
        canonical(self.run);export_wiki(self.run)
        import subprocess
        for name in ['parse-knowledge-base.py','merge-knowledge-graph.py']:
            result=subprocess.run([sys.executable,str(upstream/name),str(self.run/'wiki')],capture_output=True,timeout=30)
            self.assertEqual(result.returncode,0,result.stderr.decode())
        graph=read(self.run/'wiki/.ua/intermediate/assembled-graph.json')
        self.assertEqual(graph['kind'],'knowledge')
        ids={x['id'] for x in graph['nodes']}
        mapping=read(self.run/'graph/id-mapping.json')
        self.assertTrue(all(m['upstreamId'] in ids for m in mapping.values()))
        self.assertTrue(all(e['source'] in ids and e['target'] in ids for e in graph['edges']))

if __name__=='__main__':unittest.main()
