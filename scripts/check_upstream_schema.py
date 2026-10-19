"""Opt-in check using the actual compiled upstream Zod schema, without sanitizing."""
import argparse
import subprocess
from pathlib import Path
from core import ROOT

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('run',type=Path);a=p.parse_args()
    schema=(ROOT/'integrations/upstream/understand-anything/understand-anything-plugin/packages/core/dist/schema.js').as_uri()
    code='''import fs from 'node:fs';
const {KnowledgeGraphSchema}=await import(process.argv[1]);
const result=KnowledgeGraphSchema.safeParse(JSON.parse(fs.readFileSync(process.argv[2],'utf8')));
if (!result.success) { console.error(JSON.stringify(result.error.issues)); process.exit(1); }
console.log('Pinned upstream schema: passed');'''
    result=subprocess.run(['node','--input-type=module','-e',code,schema,str((a.run/'wiki/.ua/knowledge-graph.json').resolve())],timeout=30)
    raise SystemExit(result.returncode)
