# BMAD mapping

Pinned version and SHA: integrations/manifest.json. Source paths below refer to integrations/upstream/bmad.

| Local stage | Verified upstream asset | Use |
|---|---|---|
| Feature synthesis | src/bmm-skills/plan/bmad-product-brief/assets/brief-template.md | Executive summary, audience, scope, success, explicit unknowns |
| Planning normalization | src/bmm-skills/plan/bmad-spec/assets/spec-template.md | Why, Capabilities, Constraints, Non-goals, Success signal |
| Decision record | src/scripts/memlog.py | Actual init/append commands with requirement/question IDs |
| SRS | Application-owned SRS template | Adds acceptance criteria, interfaces, data, uncertainty and traceability |

scripts/integrate.py bmad executes an **adaptation**, not the native product-brief/spec workflow. It copies two upstream templates and the MIT notice into run/planning/bmad, records content hashes, invokes the real upstream memory script, then deterministically renders a limited brief and planning kernel. The agent must assess the output semantically. It intentionally does not claim stakeholder discovery, native config resolution or coaching occurred.

The pinned source's bmad-product-brief and bmad-spec skills require uv, _bmad config/customization resolution and native reasoning-agent activation. Current machine has no discovered Claude CLI or uv, so native activation remains blocked. Do not relabel the adapter output as native success. Install native BMAD only in an isolated project if desired, inspect its supported installer flags with `--help`, and verify actual Claude dispatch before changing status.

Retain missing stakeholder answers as open questions. Do not force a business strategy or success metric into a reconstructed system. Upstream brief/spec are inputs to a fuller SRS, not substitutes for one.
