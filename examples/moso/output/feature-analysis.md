# Feature analysis

| Feature | Status | Verification | Evidence |
|---|---|---|---|
| FEATURE-BROWSE: Sale/rental browsing | observed | verified | EVID-2ed3453878954246, EVID-b99f369160410cdc |
| FEATURE-SEARCH: Keyword search | observed | partial | EVID-2ed3453878954246, EVID-d7638348983a20d4 |
| FEATURE-FILTER: Listing filters | observed | partial | EVID-2ed3453878954246 |
| FEATURE-DETAIL: Property detail | observed | verified | EVID-c53cea185200b355 |
| FEATURE-COMPARE: Comparison selection | observed | partial | EVID-c16fccba79807428, EVID-6b424827ef3bc21f |
| FEATURE-MAP: Map entry | observed | partial | EVID-bfd8734194d79384 |
| FEATURE-PROJECT: Project catalog | observed | partial | EVID-9e2f8dc3ceced3a0 |
| FEATURE-WIKI: Wiki BĐS catalog | observed | partial | EVID-2dd9a5356fef9d2a |
| FEATURE-ACCOUNT: Account entry | observed | blocked | EVID-bfc607d5c14c32ab |
| FEATURE-POST: Posting entry | observed | blocked | EVID-34527de780364f37 |
| FEATURE-AI: AI search entry | observed | partial | EVID-d1cff2806ca77add |

Coverage relative to discovered sample only. Blocked denotes completion beyond the public entry; entry itself may be observed. Discovered pages not selected for exploration remain outside this verified sample.

### FEATURE-BROWSE — Sale/rental browsing

Inspect public listing cards.

Status: observed; verification: verified. Evidence: EVID-2ed3453878954246, EVID-b99f369160410cdc.

**Actors**

- ACTOR-VISITOR

**Entry pages**

- https://moso.vn/mua-ban-nha-dat

**Entry conditions**

- Public website reachable.

**Inputs**

- Visitor navigation or read-only query

**Outputs**

- Rendered page state

**Main flow**

- Open sale or rental route.
- Inspect rendered listing cards.

**Alternatives and unverified states**

- Other states not tested.

**Entities**

- ENTITY-LISTING


### FEATURE-SEARCH — Keyword search

Submit public query; search semantics remain unknown.

Status: observed; verification: partial. Evidence: EVID-2ed3453878954246, EVID-d7638348983a20d4.

**Actors**

- ACTOR-VISITOR

**Entry pages**

- https://moso.vn/mua-ban-nha-dat

**Entry conditions**

- Public website reachable.

**Inputs**

- Visitor navigation or read-only query

**Outputs**

- Rendered page state

**Main flow**

- Fill q with Quận 1.
- Click Tìm kiếm.
- Observe q URL and changed results.

**Alternatives and unverified states**

- Other states not tested.

**Entities**

- ENTITY-LISTING

**Workflows**

- WORKFLOW-SEARCH

**Open questions**

- QUESTION-SEARCH


### FEATURE-FILTER — Listing filters

Discover price, area, rooms, date and sorting controls.

Status: observed; verification: partial. Evidence: EVID-2ed3453878954246.

**Actors**

- ACTOR-VISITOR

**Entry pages**

- https://moso.vn/mua-ban-nha-dat

**Entry conditions**

- Public website reachable.

**Inputs**

- Visitor navigation or read-only query

**Outputs**

- Rendered page state

**Main flow**

- Open listing results.
- Inspect filter controls without asserting their behavior.

**Alternatives and unverified states**

- Other states not tested.

**Entities**

- ENTITY-LISTING

**Open questions**

- QUESTION-FILTERS


### FEATURE-DETAIL — Property detail

Read one listing’s visible descriptive fields.

Status: observed; verification: verified. Evidence: EVID-c53cea185200b355.

**Actors**

- ACTOR-VISITOR

**Entry pages**

- https://moso.vn/ban-nha-mat-tien-thach-thi-thanh-quan-1-tphcm-6-phong-ngu-gia-125-ty-1dk006

**Entry conditions**

- Public website reachable.

**Inputs**

- Visitor navigation or read-only query

**Outputs**

- Rendered page state

**Main flow**

- Follow listing link.
- Inspect identifier, price, area and description.

**Alternatives and unverified states**

- Other states not tested.

**Entities**

- ENTITY-LISTING


### FEATURE-COMPARE — Comparison selection

Select two properties into comparison tray.

Status: observed; verification: partial. Evidence: EVID-c16fccba79807428, EVID-6b424827ef3bc21f.

**Actors**

- ACTOR-VISITOR

**Entry pages**

- https://moso.vn/mua-ban-nha-dat

**Entry conditions**

- Public website reachable.

**Inputs**

- Visitor navigation or read-only query

**Outputs**

- Rendered page state

**Main flow**

- Click first comparison control.
- Observe 1/2 tray.
- Click another comparison control.
- Observe 2/2 tray.

**Alternatives and unverified states**

- Other states not tested.

**Entities**

- ENTITY-LISTING

**Workflows**

- WORKFLOW-COMPARE

**Open questions**

- QUESTION-COMPARE


### FEATURE-MAP — Map entry

Open map/list route; map loading unverified.

Status: observed; verification: partial. Evidence: EVID-bfd8734194d79384.

**Actors**

- ACTOR-VISITOR

**Entry pages**

- https://moso.vn/mua-ban-nha-dat?xem=ban-do

**Entry conditions**

- Public website reachable.

**Inputs**

- Visitor navigation or read-only query

**Outputs**

- Rendered page state

**Main flow**

- Open map link.
- Observe map shell and listing panel.

**Alternatives and unverified states**

- Other states not tested.

**Entities**

- ENTITY-LISTING

**Open questions**

- QUESTION-MAP


### FEATURE-PROJECT — Project catalog

Browse public project cards.

Status: observed; verification: partial. Evidence: EVID-9e2f8dc3ceced3a0.

**Actors**

- ACTOR-VISITOR

**Entry pages**

- https://moso.vn/tim-kiem-du-an

**Entry conditions**

- Public website reachable.

**Inputs**

- Visitor navigation or read-only query

**Outputs**

- Rendered page state

**Main flow**

- Open project catalog.
- Inspect cards and pagination text.

**Alternatives and unverified states**

- Other states not tested.

**Entities**

- ENTITY-PROJECT


### FEATURE-WIKI — Wiki BĐS catalog

Browse editorial titles and excerpts; content truth not assessed.

Status: observed; verification: partial. Evidence: EVID-2dd9a5356fef9d2a.

**Actors**

- ACTOR-VISITOR

**Entry pages**

- https://moso.vn/wiki-bds

**Entry conditions**

- Public website reachable.

**Inputs**

- Visitor navigation or read-only query

**Outputs**

- Rendered page state

**Main flow**

- Open Wiki BĐS.
- Inspect article catalog.

**Alternatives and unverified states**

- Other states not tested.

**Entities**

- ENTITY-ARTICLE


### FEATURE-ACCOUNT — Account entry

Inspect phone/password and Google entry controls.

Status: observed; verification: blocked. Evidence: EVID-bfc607d5c14c32ab.

**Actors**

- ACTOR-VISITOR

**Entry pages**

- https://moso.vn/login?callbackUrl=%2F

**Entry conditions**

- Public website reachable.

**Inputs**

- Visitor navigation or read-only query

**Outputs**

- Rendered page state

**Main flow**

- Open login page.
- Inspect controls; submit no credentials.

**Alternatives and unverified states**

- Other states not tested.

**Open questions**

- QUESTION-AUTH


### FEATURE-POST — Posting entry

Observe unauthenticated posting redirect.

Status: observed; verification: blocked. Evidence: EVID-34527de780364f37.

**Actors**

- ACTOR-VISITOR

**Entry pages**

- https://moso.vn/dang-tin

**Entry conditions**

- Public website reachable.

**Inputs**

- Visitor navigation or read-only query

**Outputs**

- Rendered page state

**Main flow**

- Open Đăng tin.
- Observe login redirect preserving callback.

**Alternatives and unverified states**

- Other states not tested.

**Entities**

- ENTITY-LISTING

**Business rules**

- RULE-POST-ENTRY

**Open questions**

- QUESTION-AUTH


### FEATURE-AI — AI search entry

Discover AI search option only.

Status: observed; verification: partial. Evidence: EVID-d1cff2806ca77add.

**Actors**

- ACTOR-VISITOR

**Entry pages**

- https://moso.vn/

**Entry conditions**

- Public website reachable.

**Inputs**

- Visitor navigation or read-only query

**Outputs**

- Rendered page state

**Main flow**

- Inspect Tìm với AI entry text.

**Alternatives and unverified states**

- Other states not tested.

**Open questions**

- QUESTION-AI

