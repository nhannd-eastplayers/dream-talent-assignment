# Workflow

All paths below are relative to repository root. Use `.venv/Scripts/python.exe` on Windows or `.venv/bin/python` on Unix. `python` below means that environment interpreter. There is no server or alternate model orchestrator.

## 0. Preflight

Parse a config path or URL from arguments. For URL-only input, copy config/default.json into a run-specific config, replace url and allowedOrigins with that URL's HTTP(S) origin, and retain generic budgets. Never copy case-study selectors into the reusable workflow.

Run `python scripts/planning.py init-run CONFIG --id UNIQUE-ID`. Capture actual versions, missing prerequisites and stop conditions. Check Claude skill discovery in the running Claude session; check available browser tools, or smoke-test helper `python scripts/browser.py RUN PLAN.json`. Do not call a CLI named after a skill: Markdown alone does not dispatch another skill.

Resume: `python scripts/planning.py resume RUN`. Review returned stage states. Only completed stages with intact input/output hashes may be skipped. Blocked integration stages do not prevent independent exports, but prevent declaring combined workflow fully verified.

## 1. Discover

Visit homepage and accessible sitemap using read-only browser navigation. Save discovery/pages.json and coverage-plan.md: discovered page types, representative URLs, depth, intended safe actions and explicit exclusions. Use the allowed origin guard for every target and redirect. Browser helper inventory supplies visible controls and same-origin links. Group repeated listings; never enumerate an entire catalog.

## 2. Explore

Prefer configured browser tools when available. Helper input is a JSON array:

```json
[{"type":"goto","url":"https://example.com/","depth":0},
 {"type":"snapshot","excerpt":"Exact visible passage"}]
```

After inspecting actual controls, allowed actions are `click`, `fill`, `select`, each with a verified `selector` and `readOnly:true`; fill/select also use `value`. Never attest publishing, messages, login, saved favorites, account creation, ratings or payments as read-only. Local comparison, query, filtering, tabs and pagination are permitted. Sensitive input types are blocked. Login walls are captured without entering credentials. Third-party requests are blocked by default, which may limit map functionality; record the limitation.

Run `python scripts/browser.py RUN PLAN.json` (add `--fixture` only for explicit loopback test config). It writes evidence/evidence.json, hashed snapshots, browser reports, persistent budget state and page inventory. Every operation has a timeout; page/action/depth budgets are checked. Model work has an advisory deadline, not a claimed hard model timeout. Keep input language from config for authored analysis when possible; record language deviations.

Retain errors and inaccessible states. Raw full snapshots may include public contact data; curate only necessary excerpts and redact personal details. Never alter a retained snapshot without updating its hash and explaining curation.

## 3. Analyze

Write knowledge/system.json and requirements/requirements.json using schemas/*.schema.json. Stable IDs identify system/modules, actors, features, workflows/steps, entities, business rules and questions. Each feature has purpose in description, actorIds, entryPages, preconditions, inputs, outputs, mainFlow, alternativeFlows, entityIds, businessRuleIds, dependsOn, openQuestionIds, evidenceIds and verificationState.

Make every requirement testable with acceptanceCriteria; preserve its status and verificationState. Refer to evidence supporting precisely that scope, not an unrelated page. Acceptance criteria reconstruct observed behavior rather than silently turning suggestions into facts.

## 4. BMAD planning

Read bmad-mapping.md. Native execution requires verified Claude dispatch and installed dependencies. When unavailable, use the explicitly labeled adapted mode: `python scripts/integrate.py bmad RUN`. Read/critique its outputs as reasoning agent; record unsupported assumptions and missing stakeholder answers. This executes actual pinned templates and upstream memlog script, but does not count as native BMAD skill activation.

## 5. SRS

`python scripts/planning.py validate-artifacts RUN`
`python scripts/planning.py render RUN`

The SRS expands canonical requirements through templates/srs-template.md. Do not replace it with a PRD. Semantic review checks acceptance scope, evidence support and observed versus proposed distinctions.

## 6. Graph

Read graph-mapping.md. Run in order:

```text
python scripts/planning.py build-canonical-graph RUN
python scripts/planning.py export-knowledge RUN
python scripts/planning.py export-traceability RUN
python scripts/integrate.py ua RUN
python scripts/check_upstream_schema.py RUN
```

The last command additionally needs Node and a built pinned upstream core. UA Phase 3 requires native article-analyzer dispatch. Without it, the real deterministic base graph still works, but mark semantic phase blocked. Do not fabricate successful analysis batches.

Open official upstream viewer against RUN/wiki and inspect a feature, requirement, relationships and linked evidence. Preserve wiki/.ua output paths. Keep screenshots and text from actual inspection. No custom viewer substitutes.

## 7. Validate/repair

`python scripts/planning.py validate-artifacts RUN --derived`

Review 10–15 requirements or the actual smaller set. For each: IDs, cited passages, support, ambiguity, coverage gaps, unsupported claims. Label as agent review unless a human actually reviewed it. Repair specific findings within maxRepairIterations; retain unresolved findings. A deterministic pass cannot certify semantic truth.

## 8. Package/checkpoint

Use templates/quality-report.md and templates/run-report.md. Include discovery coverage, unsuccessful actions, integration commands/versions, graph lookup instructions and next runnable stage. Curate relevant public evidence only. Report partial if either native integration remains blocked.

Checkpoint example:

```text
python scripts/planning.py checkpoint RUN --stage analyze --state completed --inputs RUN/evidence/evidence.json --artifacts RUN/knowledge/system.json RUN/requirements/requirements.json
```

For every stage include upstream manifests/config and dependency artifacts in --inputs. Use --state partial/blocked and --error for limitations. Hash checks invalidate changed dependencies and all downstream stage states. Physical stale files remain for audit but are not reusable until regenerated. Final manifest status must reflect actual integration and review results.
