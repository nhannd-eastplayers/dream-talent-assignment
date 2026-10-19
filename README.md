# Planning Agent workflow repository

Reusable **Claude Code project skill** for public-website planning: evidence → feature model → BMAD-assisted planning → SRS → Understand-Anything graph. Python scripts perform deterministic validation and exports; the reasoning agent remains Claude Code. No separate Claude API application, backend or product rebuild.

**Current status: partial, with real artifacts.** Moso has 13 reconstructed requirements across 11 discovered features; the independent library fixture has 5 requirements. Both exports passed the pinned upstream graph schema. The official upstream viewer was opened, a Moso requirement selected, and its evidence resolved. BMAD templates and memory script were actually used in explicitly adapted mode. Native Claude skill dispatch and UA semantic article-analyzer execution remain blocked/unverified; this build session ran in Codex, with no discovered Claude CLI or uv. Do not present it as a fully verified combined Claude workflow.

Start with [setup](docs/setup.md), [integration record](docs/integration-spike.md), [implementation status](docs/implementation-status.md), and [demo](docs/demo.md). Original brief: [REPO_SPEC.md](REPO_SPEC.md).

## Xem ví dụ Moso có sẵn

Kết quả đã nằm trong repository; không cần chạy lại phân tích hay đăng nhập Claude Code để xem.

- [SRS — 13 yêu cầu](examples/moso/output/SRS.md)
- [Phân tích tính năng](examples/moso/output/feature-analysis.md)
- [Báo cáo thực thi và giới hạn](examples/moso/output/run-report.md)
- [Báo cáo chất lượng](examples/moso/output/quality-report.md)
- [Ma trận truy vết](examples/moso/output/traceability.csv)
- [Ảnh graph đã kiểm tra](examples/moso/output/graph/inspection/viewer.png)

Để mở **Knowledge Graph tương tác**, cần Python 3.11, Git, Node.js 22 và pnpm 10.6.2. Chạy PowerShell từ thư mục gốc repository. Nếu chưa thiết lập môi trường:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.\.venv\Scripts\python.exe scripts/setup_integrations.py

Push-Location integrations/upstream/understand-anything
pnpm.cmd install --frozen-lockfile --ignore-scripts
pnpm.cmd --filter @understand-anything/core build
Pop-Location
```

Sau đó, mỗi lần muốn xem graph Moso, chạy từ thư mục gốc repository:

```powershell
$env:GRAPH_DIR=(Resolve-Path examples/moso/output/wiki).Path
Push-Location integrations/upstream/understand-anything/understand-anything-plugin/packages/dashboard
pnpm.cmd exec vite --host 127.0.0.1
```

Giữ terminal đang chạy. Mở **đầy đủ URL ở dòng `Dashboard URL`**, gồm cả `?token=...`; không chỉ mở địa chỉ `Local`. Cổng và token lấy từ terminal mỗi lần khởi động, không dùng lại URL của phiên trước. Dừng viewer bằng `Ctrl+C`, rồi chạy `Pop-Location` để trở về thư mục gốc.

Trong viewer:

1. Đóng hộp hướng dẫn ban đầu nếu xuất hiện.
2. Tìm `FR-COMPARE-001`, bấm kết quả để xem yêu cầu và các liên kết.
3. Xem backlink `FEATURE-COMPARE`, rồi bấm `EVID-c16fccba79807428` để đọc bằng chứng: URL, thao tác, đoạn trích và hash.
4. Đối chiếu quan hệ nghiệp vụ có kiểu trong [canonical.json](examples/moso/output/graph/canonical.json); viewer biểu diễn các bản ghi bằng article và liên kết chung. [ID mapping](examples/moso/output/graph/id-mapping.json) giữ ánh xạ ID.

Thông báo `Knowledge graph freshness could not be verified` xuất hiện vì wiki sinh ra không có Git commit hash; cảnh báo này đã được ghi nhận trong lần kiểm tra viewer. Trạng thái tích hợp native vẫn là **partial** như mô tả đầu README. Chi tiết cài đặt và xử lý môi trường: [docs/setup.md](docs/setup.md).

## Quick start

Prerequisites: Python 3.11, Git; Chromium installed by Playwright. The official graph viewer additionally requires Node 22 and pnpm 10.6.2. Native end-to-end usage requires an authenticated Claude Code installation and verified installed upstream skills; a subscription does not imply separate API credits.

Windows PowerShell, from repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.\.venv\Scripts\python.exe -m playwright install chromium
.\.venv\Scripts\python.exe scripts/setup_integrations.py
.\.venv\Scripts\python.exe scripts/planning.py validate-artifacts examples/moso/output --derived
$env:PLANNING_BROWSER_TESTS='1'
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

On Unix replace `.venv\Scripts\python.exe` with `.venv/bin/python`; omit the PowerShell env syntax or use `PLANNING_BROWSER_TESTS=1` before the test command. Dependencies are pinned in requirements-lock.txt; upstream SHA pins live in integrations/manifest.json. Do not commit fetched upstream checkouts, credentials or raw runs.

## Claude entry

Project-local skill: [.claude/skills/analyze-system/SKILL.md](.claude/skills/analyze-system/SKILL.md). Documented Claude syntax, **not end-to-end tested here**:

```text
/analyze-system examples/moso/config.json
/analyze-system https://example.com/
/analyze-system examples/moso/config.json --resume runs/my-run
```

Claude Code automatically discovers project skills from `.claude/skills/<name>/SKILL.md`. This format/argument syntax was checked against [official Claude skills documentation](https://code.claude.com/docs/en/skills). Whether the running agent exposes native Skill dispatch must be verified in that session. Do not assume writing another skill's name invokes it.

## Tested deterministic workflow

Use a unique run ID; init does not overwrite existing runs:

```powershell
.\.venv\Scripts\python.exe scripts/planning.py init-run examples/moso/config.json --id my-run
.\.venv\Scripts\python.exe scripts/preflight.py runs/my-run --browser
.\.venv\Scripts\python.exe scripts/browser.py runs/my-run examples/moso/browser-plan.json
```

The reasoning agent then inspects inventory/evidence, creates an origin-safe bounded exploration plan, and writes `knowledge/system.json` and `requirements/requirements.json` under the run, using schemas. The scripts deliberately do not invent those findings. The checked-in case studies contain the actual reviewed canonical inputs, so exports can be reproduced without recrawling.

```powershell
.\.venv\Scripts\python.exe scripts/planning.py validate-artifacts runs/my-run
.\.venv\Scripts\python.exe scripts/integrate.py bmad runs/my-run
.\.venv\Scripts\python.exe scripts/planning.py render runs/my-run
.\.venv\Scripts\python.exe scripts/planning.py build-canonical-graph runs/my-run
.\.venv\Scripts\python.exe scripts/planning.py export-knowledge runs/my-run
.\.venv\Scripts\python.exe scripts/planning.py export-traceability runs/my-run
.\.venv\Scripts\python.exe scripts/integrate.py ua runs/my-run
.\.venv\Scripts\python.exe scripts/planning.py validate-artifacts runs/my-run --derived
```

`integrate.py bmad` is an accurately labeled asset adaptation; `integrate.py ua` executes real upstream deterministic phases without claiming semantic subagent execution. See [mappings](.claude/skills/analyze-system/references/graph-mapping.md). Commands above were exercised on both recorded runs; they are not a substitute for the reasoning stage.

## Configuration, outputs and resume

Copy config/default.json and set URL/allowedOrigins. Budgets: maxPages, maxDepth, maxActionsPerPage, maxRuntimeMinutes, maxRepairIterations (≤2), requestDelayMs. allowMutations must remain false. Private/local network targets are rejected except explicit loopback test config plus helper `--fixture`. Third-party resources are blocked; map loading may therefore be partial. Browser helper actions and limitations are documented in [workflow reference](.claude/skills/analyze-system/references/workflow.md).

Raw artifacts: `runs/<id>/`; reviewed examples: `examples/moso/output/` and `examples/fixture/output/`. Open SRS.md, feature-analysis.md, quality-report.md and run-report.md. Canonical graph: graph/canonical.json; upstream viewer graph: wiki/.ua/knowledge-graph.json; ID sidecar: graph/id-mapping.json; evidence: evidence/evidence.json and snapshots. Canonical types are not claimed to be upstream types.

Checkpoint using `planning.py checkpoint RUN --stage analyze --state completed --inputs ... --artifacts ...`. Resume with `planning.py resume RUN`. Input/output hashes invalidate changed stages and downstream states; stale files remain for audit. Completed hash-valid stages can be skipped. Manifest records run state and errors; integration blockers keep overall status partial. The agent deadline is advisory; helper/subprocess operations are bounded separately.

## Review and limits

This is a Planning Agent because it reconstructs scope, actors, workflows, requirements, uncertainty and traceability before implementation. It implements no Moso features. Public UI evidence does not establish backend enforcement, internal schemas, algorithms, legal truth, business goals or SLAs. Authenticated flows and mutations are excluded. Evidence sampling does not prove exhaustive feature discovery.

Agent review is recorded for all 13 Moso requirements and 5 fixture requirements. No independent human sign-off, accuracy percentage, video or native Claude execution is claimed. [Evaluation](docs/evaluation.md) states exactly what was checked.
