# Software Requirements Specification

## 1. Metadata and sources
Run: fixture-20261019

Analysis date: 2026-10-19T07:45:46.671239+00:00

Source: http://127.0.0.1:8765/

- EVID-9ea047ea81cbbcba: [Library fixture](http://127.0.0.1:8765/); captured 2026-10-19T07:46:14.425320+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-9ea047ea81cbbcba.txt.
- EVID-8e992d4583300047: [Library fixture](http://127.0.0.1:8765/); captured 2026-10-19T07:46:14.563394+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-8e992d4583300047.txt.
- EVID-cdf9f41e0c909818: [Library fixture](http://127.0.0.1:8765/); captured 2026-10-19T07:46:14.718389+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-cdf9f41e0c909818.txt.
- EVID-b0d9712c57e7036a: [Library fixture](http://127.0.0.1:8765/); captured 2026-10-19T07:46:14.842333+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-b0d9712c57e7036a.txt.
- EVID-415943f983727a5c: [Library fixture](http://127.0.0.1:8765/); captured 2026-10-19T07:46:14.985739+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-415943f983727a5c.txt.
- EVID-337e164078942bbe: [River atlas](http://127.0.0.1:8765/detail.html); captured 2026-10-19T07:46:15.143877+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-337e164078942bbe.txt.
- EVID-ea991741f8ce8955: [Account blocked](http://127.0.0.1:8765/account.html); captured 2026-10-19T07:46:15.296936+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-ea991741f8ce8955.txt.

## 2. Purpose and system overview
Library fixture

Controlled catalog with category filtering, item detail and an unavailable account flow.

## 3. System boundaries and exclusions
Public, read-only reconstruction. Authentication, internal architecture, APIs, SLAs, and external mutations excluded.

## 4. Actors and user classes
- ACTOR-VISITOR: Visitor (observed; verified)

## 5. Feature inventory and workflows
### FEATURE-CATALOG — Browse catalog

Find catalog items.

Status: observed; verification: verified. Evidence: EVID-9ea047ea81cbbcba.

**Actors**

- ACTOR-VISITOR

**Entry pages**

- http://127.0.0.1:8765/

**Entry conditions**

- Public website reachable.

**Inputs**

- Visitor navigation or read-only query

**Outputs**

- Rendered page state

**Main flow**

- Open catalog.
- Read item title.

**Alternatives and unverified states**

- Other states not tested.

**Entities**

- ENTITY-ITEM


### FEATURE-FILTER — Filter catalog

Select category and inspect results.

Status: observed; verification: verified. Evidence: EVID-8e992d4583300047, EVID-cdf9f41e0c909818, EVID-b0d9712c57e7036a, EVID-415943f983727a5c.

**Actors**

- ACTOR-VISITOR

**Entry pages**

- http://127.0.0.1:8765/

**Entry conditions**

- Public website reachable.

**Inputs**

- Visitor navigation or read-only query

**Outputs**

- Rendered page state

**Main flow**

- Select Science.
- Click Filter.
- Select Art.
- Click Filter.

**Alternatives and unverified states**

- Art produces No items found.

**Entities**

- ENTITY-ITEM

**Workflows**

- WORKFLOW-FILTER


### FEATURE-DETAIL — Item detail

Read item metadata.

Status: observed; verification: verified. Evidence: EVID-337e164078942bbe.

**Actors**

- ACTOR-VISITOR

**Entry pages**

- http://127.0.0.1:8765/detail.html

**Entry conditions**

- Public website reachable.

**Inputs**

- Visitor navigation or read-only query

**Outputs**

- Rendered page state

**Main flow**

- Follow detail link.
- Read category and format.

**Alternatives and unverified states**

- Other states not tested.

**Entities**

- ENTITY-ITEM


### FEATURE-ACCOUNT — Account entry

Reach sign-in boundary.

Status: observed; verification: blocked. Evidence: EVID-ea991741f8ce8955.

**Actors**

- ACTOR-VISITOR

**Entry pages**

- http://127.0.0.1:8765/account.html

**Entry conditions**

- Public website reachable.

**Inputs**

- Visitor navigation or read-only query

**Outputs**

- Rendered page state

**Main flow**

- Follow Account.
- Observe sign-in wall.

**Alternatives and unverified states**

- Other states not tested.

**Open questions**

- QUESTION-AUTH


### WORKFLOW-FILTER — Category filtering

Observed select-and-apply flow with nonempty and empty states.

Status: observed; verification: verified. Evidence: EVID-8e992d4583300047, EVID-cdf9f41e0c909818, EVID-b0d9712c57e7036a, EVID-415943f983727a5c.

**Actors**

- ACTOR-VISITOR

**Entities**

- ENTITY-ITEM

**Steps**

- STEP-SELECT
- STEP-APPLY



## 6. Functional requirements
### FR-CATALOG-001 — functional

The catalog shall display the River atlas item.

Feature: FEATURE-CATALOG. Status: observed; verification: verified.

Actors: ACTOR-VISITOR. Evidence: EVID-9ea047ea81cbbcba.

**Preconditions**

- The public entry page is available.

**Main flow**

- Open the entry page.
- Inspect the described state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given the catalog page, River atlas is visible.

Entities: ENTITY-ITEM. Dependencies: none established.

Open questions: none recorded.


### FR-FILTER-001 — functional

Selecting Science and applying Filter shall retain River atlas.

Feature: FEATURE-FILTER. Status: observed; verification: verified.

Actors: ACTOR-VISITOR. Evidence: EVID-8e992d4583300047, EVID-cdf9f41e0c909818.

**Preconditions**

- The public entry page is available.

**Main flow**

- Select Science.
- Click Filter.
- Read results.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given Science selected, when Filter is clicked, River atlas — Science is displayed.

Entities: ENTITY-ITEM. Dependencies: none established.

Open questions: none recorded.


### FR-FILTER-002 — functional

Selecting Art and applying Filter shall display an empty-result message.

Feature: FEATURE-FILTER. Status: observed; verification: verified.

Actors: ACTOR-VISITOR. Evidence: EVID-b0d9712c57e7036a, EVID-415943f983727a5c.

**Preconditions**

- The public entry page is available.

**Main flow**

- Select Art.
- Click Filter.
- Read empty state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given Art selected, when Filter is clicked, No items found is displayed.

Entities: not established. Dependencies: none established.

Open questions: none recorded.


### FR-DETAIL-001 — functional

The River atlas detail page shall display its category and format.

Feature: FEATURE-DETAIL. Status: observed; verification: verified.

Actors: ACTOR-VISITOR. Evidence: EVID-337e164078942bbe.

**Preconditions**

- The public entry page is available.

**Main flow**

- Open the entry page.
- Inspect the described state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given detail is open, Science and Book are visible.

Entities: ENTITY-ITEM. Dependencies: none established.

Open questions: none recorded.


### FR-ACCOUNT-001 — functional

The public account page shall show that sign-in is required.

Feature: FEATURE-ACCOUNT. Status: observed; verification: partial.

Actors: ACTOR-VISITOR. Evidence: EVID-ea991741f8ce8955.

**Preconditions**

- The public entry page is available.

**Main flow**

- Open the entry page.
- Inspect the described state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given Account is opened, the sign-in-required message is visible.

Entities: not established. Dependencies: none established.

Open questions: QUESTION-AUTH.


## 7. Business rules and data requirements
### ENTITY-ITEM — Catalog item

Displayed title, category and format; no database model inferred.

Status: observed; verification: verified. Evidence: EVID-9ea047ea81cbbcba, EVID-337e164078942bbe.



## 8. External interfaces
Only interfaces supported by evidence below are established. External integrations and internal API contracts remain unknown.

## 9. Non-functional requirements
No measured or documented performance, availability, security, or accessibility guarantees established. Any NFR below is explicitly proposed.

## 10. Constraints, assumptions and dependencies
Browser visibility does not prove backend enforcement. Snapshot coverage is bounded. Missing stakeholder answers remain open.

## 11. Open questions and coverage limitations
### QUESTION-AUTH — Authentication behavior

What happens after real sign-in?

Status: proposed; verification: blocked. Evidence: EVID-ea991741f8ce8955.

Rationale: Fixture intentionally excludes authentication.



## 12. Traceability
- FEATURE-CATALOG → FR-CATALOG-001 → EVID-9ea047ea81cbbcba
- FEATURE-FILTER → FR-FILTER-001 → EVID-8e992d4583300047, EVID-cdf9f41e0c909818
- FEATURE-FILTER → FR-FILTER-002 → EVID-b0d9712c57e7036a, EVID-415943f983727a5c
- FEATURE-DETAIL → FR-DETAIL-001 → EVID-337e164078942bbe
- FEATURE-ACCOUNT → FR-ACCOUNT-001 → EVID-ea991741f8ce8955

## 13. Proposed enhancements
None.
