# Library fixture — reconstructed planning kernel

> Adapted from pinned BMAD spec-template.md; not native bmad-spec output.

## Why

Create evidence-backed planning documentation of public behavior.

## Capabilities

- **FR-CATALOG-001**
  - **intent:** The catalog shall display the River atlas item.
  - **success:** Given the catalog page, River atlas is visible.
- **FR-FILTER-001**
  - **intent:** Selecting Science and applying Filter shall retain River atlas.
  - **success:** Given Science selected, when Filter is clicked, River atlas — Science is displayed.
- **FR-FILTER-002**
  - **intent:** Selecting Art and applying Filter shall display an empty-result message.
  - **success:** Given Art selected, when Filter is clicked, No items found is displayed.
- **FR-DETAIL-001**
  - **intent:** The River atlas detail page shall display its category and format.
  - **success:** Given detail is open, Science and Book are visible.
- **FR-ACCOUNT-001**
  - **intent:** The public account page shall show that sign-in is required.
  - **success:** Given Account is opened, the sign-in-required message is visible.

## Constraints

Read-only evidence; inferred/proposed records remain labeled.

## Non-goals

No backend design, feature implementation or invented stakeholder decisions.

## Success signal

Reviewer resolves requirements to captured evidence.

## Open Questions

- What happens after real sign-in?
