# Understand-Anything mapping

Pinned route inspected: understand-anything-plugin/skills/understand-knowledge/SKILL.md. A Karpathy-pattern wiki needs index.md plus multiple linked Markdown articles; CLAUDE.md, log.md and raw/ complete the exported three-layer convention.

Every canonical node becomes one wiki page `<ID>.md` with `[[ID]]` outgoing links, canonical record JSON and its original type/status/evidence references. Index category becomes an upstream topic. Real parser emits `article:<ID>` IDs; mapping is verified after merge. Canonical Requirement remains an article in upstream UI, not an invented upstream Requirement node type.

All canonical relation types become `related` through wikilinks. Exact relation types, edge IDs, rationale and provenance remain in graph/canonical.json. graph/id-mapping.json maps canonical IDs to upstream IDs and files. CSV/JSON traceability includes feature, requirement, evidence and upstream article ID. Nothing is silently discarded from canonical artifacts.

`python scripts/integrate.py ua RUN` executes upstream parser and merger with argument arrays and 60-second timeouts, validates mapping/endpoints, writes wiki/.ua/knowledge-graph.json and meta.json, retains intermediate execution evidence. This is actual deterministic integration; semantic article-analyzer dispatch is separately blocked until a Claude session runs it. Native `/understand-knowledge` is documented upstream but not tested in this environment.

The upstream core's KnowledgeGraphSchema is compiled then applied directly, without sanitize/drop behavior, by check_upstream_schema.py. Official viewer launch and inspection instructions live in docs/setup.md. In UI search for requirement ID; inspect its neighboring article and evidence. Open wiki/<ID>.md for exact JSON and graph/canonical.json for typed edges. The graph ID mapping is the authority if display labels are shortened.
