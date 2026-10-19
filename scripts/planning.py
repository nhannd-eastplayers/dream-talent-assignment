import argparse
import sys
from pathlib import Path
from core import init_run, validate, canonical, export_wiki, traceability, render, checkpoint, resume

def main():
    p = argparse.ArgumentParser(description='Planning workflow deterministic operations')
    p.add_argument('command', choices=['init-run', 'validate-artifacts', 'build-canonical-graph', 'export-knowledge', 'export-traceability', 'render', 'checkpoint', 'resume'])
    p.add_argument('path', type=Path)
    p.add_argument('--id')
    p.add_argument('--derived', action='store_true')
    p.add_argument('--stage')
    p.add_argument('--state', default='completed', choices=['pending', 'running', 'completed', 'partial', 'failed', 'blocked'])
    p.add_argument('--inputs', nargs='*', default=[])
    p.add_argument('--artifacts', nargs='*', default=[])
    p.add_argument('--error', default='')
    a = p.parse_args()
    if a.command == 'init-run':
        print(init_run(a.path, a.id))
    elif a.command == 'resume':
        print(resume(a.path))
    elif a.command == 'checkpoint':
        checkpoint(a.path, a.stage, a.state, a.inputs, a.artifacts, a.error)
    else:
        result = {'validate-artifacts': lambda r: validate(r, a.derived), 'build-canonical-graph': canonical,
            'export-knowledge': export_wiki, 'export-traceability': traceability, 'render': render}[a.command](a.path)
        if a.command == 'validate-artifacts':
            print(result)

if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError) as e:
        print(f'ERROR: {e}', file=sys.stderr)
        sys.exit(1)
