# Feature analysis

| Feature | Status | Verification | Evidence |
|---|---|---|---|
| FEATURE-CATALOG: Browse catalog | observed | verified | EVID-9ea047ea81cbbcba |
| FEATURE-FILTER: Filter catalog | observed | verified | EVID-8e992d4583300047, EVID-cdf9f41e0c909818, EVID-b0d9712c57e7036a, EVID-415943f983727a5c |
| FEATURE-DETAIL: Item detail | observed | verified | EVID-337e164078942bbe |
| FEATURE-ACCOUNT: Account entry | observed | blocked | EVID-ea991741f8ce8955 |

Coverage relative to discovered sample only. Blocked denotes completion beyond the public entry; entry itself may be observed. Discovered pages not selected for exploration remain outside this verified sample.

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

