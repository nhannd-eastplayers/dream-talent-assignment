# Integration spike — actual execution record

Date: 19 October 2026 (Asia/Saigon). Runtime: Codex on Windows, not Claude Code. No native Claude/uv executable discovered by preflight. No separate API application was built or used.

## Provenance and license

| Integration | Inspected source | Pin | License |
|---|---|---|---|
| BMAD | [official repository](https://github.com/bmad-code-org/BMAD-METHOD), V6.12 checkout | 6.12.4; bab9082c3e884e0d72c759bcd1a6d90bcc01be84 | MIT, BMad Code, LLC; retain notice |
| Understand-Anything | [official repository](https://github.com/Egonex-AI/Understand-Anything) | 2.9.7; f2d0164f72fe678805c34245a6df36acededfebd | MIT; retain upstream copyright notices |

Read actual README, licenses, skill files, parser/merger, core schema and dashboard launch instructions from fetched checkouts. Local installs stay under integrations/upstream/ and do not modify user-level Claude settings. Source pins are not an assertion that every upstream feature was tested.

## BMAD: tested adaptation; native blocked

Actual initial source fetch:

```text
git clone --depth 1 --branch V6.12 https://github.com/bmad-code-org/BMAD-METHOD.git integrations/upstream/bmad
```

Selected pinned assets: bmad-product-brief/assets/brief-template.md, bmad-spec/assets/spec-template.md and src/scripts/memlog.py. Native product-brief/spec skills were inspected; they require generated _bmad config/customization resolution, uv and reasoning-agent activation. Do not assume old PRD skill names or installer flags: the inspected source provides bmad-product-brief and bmad-spec.

Actual mini execution on library fixture, followed by Moso:

```text
python scripts/integrate.py bmad runs/fixture-20261019
python scripts/integrate.py bmad runs/moso-20261019
```

Both exited 0. Adapter copied exact upstream templates and license, recorded hashes, invoked real memlog `init --workspace ... --field topic=...` and `append --workspace ... --type capability|question|event --text ...` with argument arrays, and produced brief.md, adapted-SPEC.md, .memlog.md and execution.json. Full argv/stdout/stderr/exit records are retained under each curated planning/bmad/ directory.

Adaptation deliberately reuses brief audience/scope/unknowns and the five-field planning kernel. It does not claim native activation, stakeholder coaching, PRD creation or BMAD config setup. Missing stakeholder answers are recorded open questions. Application SRS transformation adds full requirement/acceptance data, sources, uncertainty, data/interfaces, exclusions and traceability; a brief or SPEC is never mislabeled SRS.

Status: **tested asset adaptation / native Claude execution blocked**.

## Understand-Anything: real graph route and viewer

Actual initial fetch:

```text
git clone --depth 1 https://github.com/Egonex-AI/Understand-Anything.git integrations/upstream/understand-anything
```

Inspected skill: understand-anything-plugin/skills/understand-knowledge/SKILL.md. It detects Karpathy-pattern Markdown with index.md, wikilinks and optional raw/schema/log layers. Export supplies all those conventions. Parser's article IDs are `article:<file-stem>`, not canonical business type names. Default output directory is .ua; legacy .understand-anything wins when present.

The first tiny integration fixture used the library’s linked canonical wiki. Actual invocations (via timeout-bound wrapper, complete commands retained):

```text
python <pinned-skill>/parse-knowledge-base.py <run>/wiki
python <pinned-skill>/merge-knowledge-graph.py <run>/wiki
```

Both exited 0 on both cases. Fixture: 25 nodes, 87 edges. Moso: 59 nodes, 215 edges. Retained scan manifests, merge outputs and logs show zero semantic analysis batches; none were manufactured. Save phase copied validated assembled graph into wiki/.ua/knowledge-graph.json and wrote meta.json. Canonical graph sidecars preserve business node/edge types and traceability.

Native semantic Phase 3 dispatch to article-analyzer was **not executed**. The real deterministic graph is valid without those additional inferred claims; this is not proof of the complete native analysis skill. The original fixture has more than two pages because it exercises all required canonical mappings; it remains a small controlled knowledge base.

Exact viewer compatibility: built pinned core with `pnpm.cmd --filter @understand-anything/core build`, then applied its `KnowledgeGraphSchema.safeParse` directly to both graphs. Both passed without sanitizing or dropping unsupported data. Recorded in docs/test-results.txt.

Viewer release fast path at `releases/download/v2.9.7/understand-anything-viewer.tgz` returned 404. Supported source fallback succeeded: pnpm 10.6.2 frozen-lockfile install (scripts disabled), core build, then upstream dashboard `GRAPH_DIR=<run>/wiki pnpm.cmd exec vite --host 127.0.0.1`. It printed an access-token URL. Graph was loaded in actual Chromium; FR-COMPARE-001 selected, FEATURE-COMPARE backlink and evidence wikilink inspected, then EVID-c16fccba79807428 opened with source/action/excerpt/hash preview. Actual screenshots and text live under examples/moso/output/graph/inspection/. No custom viewer or Mermaid substitute is used.

Viewer showed a freshness warning because this generated knowledge wiki has no repository commit hash. This warning is retained; it is not a graph schema failure. Generated graph relations are for business analysis, not code impact analysis.

Status: **tested deterministic route, exact schema and upstream viewer / native semantic phase blocked**.

## Browser and generality

No connected CUA browser was available. The explicitly supported helper fallback uses Playwright 1.55.0 and Chromium 140.0.7339.16. Moso had 15 distinct retained rendered states across representative routes/actions (one duplicate state was deduplicated by stable capture ID). No login, posting, messaging, account creation or contact reveal was performed. Map shell remained loading under third-party origin restrictions; only entry/shell behavior is claimed.

Library fixture actually exercised navigation, Science filtering, Art empty results, detail and unavailable account flow. Generic scripts contain no Moso URL, real-estate selectors or domain assumptions. Fixture expected set was authored manually and checked independently of exporter structure.

## What remains

In an authenticated Claude Code environment: test actual custom invocation, native Skill dispatch and installed upstream activation, then run UA semantic analysis and update execution records. This is the only honest route to claiming a fully verified combined native workflow. Continue deterministic work independently; do not replace these blockers with simulated success.
