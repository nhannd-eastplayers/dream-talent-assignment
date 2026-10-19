# Setup and verified execution

## Python and browser helper

Follow README's venv commands. Tested here: Windows, Python 3.11.4, Node v22.18.0, Playwright 1.55.0, Chromium 140.0.7339.16, jsonschema 4.23.0. Full resolved Python versions are pinned in requirements-lock.txt. Use npm.cmd/pnpm.cmd on PowerShell if script execution policy blocks npm.ps1; do not weaken the policy.

The session had no connected CUA browser. Instead the explicitly permitted browser helper was used. `browser.py RUN PLAN.json` has a JSON action-plan input and writes JSON evidence, page inventory, snapshots, budget and execution report. Supported actions: goto, snapshot, click, fill, select. Read-only interaction requires `readOnly:true`, assessed by the reasoning agent from observed controls. It never executes supplied page JavaScript or external commands; its fixed DOM readers inspect visible text, controls and links. GET semantics alone are not a proof of safety. Sensitive inputs and non-read network methods are blocked.

Smoke test: serve fixture with `python -m http.server 8765 --bind 127.0.0.1 --directory examples/fixture/site`, initialize fixture config, then run `python scripts/browser.py RUN examples/fixture/browser-plan.json --fixture`. Or run opt-in unittest browser acceptance, which manages its own loopback fixture server and random port. Do not treat package installation as Claude MCP configuration.

## Upstream sources

`python scripts/setup_integrations.py` fetches exact commits from official repositories into integrations/upstream/. It uses argument arrays, timeouts and non-forced checkout. It does not change user-level Claude settings. Both upstream projects carry MIT licenses. Copied/adapted run templates retain their license notice; full source checkouts retain original licenses. See integrations/manifest.json for SHAs and copied asset hashes in planning/bmad/execution.json.

## Official Understand-Anything viewer

The documented release-tarball route at v2.9.7 returned HTTP 404 during this session. The verified source fallback was:

```powershell
Push-Location integrations/upstream/understand-anything
pnpm.cmd install --frozen-lockfile --ignore-scripts
pnpm.cmd --filter @understand-anything/core build
Pop-Location
.\.venv\Scripts\python.exe scripts/check_upstream_schema.py examples/moso/output
$env:GRAPH_DIR=(Resolve-Path examples/moso/output/wiki).Path
Push-Location integrations/upstream/understand-anything/understand-anything-plugin/packages/dashboard
pnpm.cmd exec vite --host 127.0.0.1
```

Keep terminal running. Open the **full tokenized Dashboard URL printed by Vite**; token changes per process. Do not commit its live token or browser credentials. This is the unmodified upstream Vite viewer, not a custom hosted app. Use Ctrl+C to stop. Point GRAPH_DIR at `examples/fixture/output/wiki` to inspect fixture instead.

Manual acceptance: dismiss onboarding in the temporary browser context, search FR-COMPARE-001, click result, inspect FEATURE-COMPARE backlink and EVID-c16fccba79807428 wikilink. Click evidence to inspect exact excerpt, URL/action and hash. Details are also available as wiki/<ID>.md and typed canonical edges in graph/canonical.json.

Optional reproducible browser inspection:

```text
python scripts/inspect_viewer.py TOKENIZED-LOOPBACK-URL runs/viewer-check --search FR-COMPARE-001 --evidence EVID-c16fccba79807428
```

It records actual screenshots and rendered text. It does not use an external model or viewer replacement. The actual session screenshots are curated in examples/moso/output/graph/inspection/.

## Native Claude runtime — remaining prerequisite

No Claude CLI or uv was discovered in this environment. The custom skill was authored in verified Claude project-skill format, but its actual invocation cannot be tested by Codex in this session. Open this repository in the user's authenticated Claude Code environment and verify discovery and Skill dispatch before marking native stages tested. No separate API key or API application is required.

BMAD native installation is optional while using the accurately labeled adapted-assets route. For native use, inspect the pinned checkout's README and CLI help and use an isolated project scope; the pinned source's skill names are bmad-product-brief and bmad-spec, with uv and generated _bmad configuration dependencies. Do not replace tested adapted status with an invented native run.

UA native plugin installation is documented upstream as `/plugin marketplace add Egonex-AI/Understand-Anything` then `/plugin install understand-anything`; use project scope where the runtime offers it and verify the installed commit against this repository's pin. The upstream documented routes are `/understand-knowledge <wiki-directory>` and `/understand-dashboard <wiki-directory>`. Plugin namespace/discovery and actual invocation must be verified in that Claude session. These native invocations were **not executed here**. Deterministic parser/merger and viewer were executed directly from pinned source.
