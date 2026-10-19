# Software Requirements Specification

## 1. Metadata and sources
Run: moso-20261019

Analysis date: 2026-10-19T07:45:46.424839+00:00

Source: https://moso.vn/

- EVID-d1cff2806ca77add: [MOSO - AI Proptech Mua Bán Nhà Đất & Đăng Tin Bất Động Sản](https://moso.vn/); captured 2026-10-19T07:46:18.947844+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-d1cff2806ca77add.txt.
- EVID-2ed3453878954246: [Mua Bán Nhà Đất, Bất Động Sản Giá Tốt | MOSO VN AI Proptech](https://moso.vn/mua-ban-nha-dat); captured 2026-10-19T07:46:53.527245+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-2ed3453878954246.txt.
- EVID-b99f369160410cdc: [Cho Thuê Nhà Đất, Mặt Bằng, Căn Hộ | MOSO VN AI Proptech](https://moso.vn/cho-thue-nha-dat); captured 2026-10-19T07:46:54.888739+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-b99f369160410cdc.txt.
- EVID-9e2f8dc3ceced3a0: [Dự án bất động sản sơ cấp: bảng giá, tiến độ, so sánh dự án | MOSO](https://moso.vn/tim-kiem-du-an); captured 2026-10-19T07:46:56.501840+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-9e2f8dc3ceced3a0.txt.
- EVID-34527de780364f37: [Đăng Nhập Tài Khoản | MOSO](https://moso.vn/login?callbackUrl=%2Fdang-tin); captured 2026-10-19T07:46:58.170481+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-34527de780364f37.txt.
- EVID-bfc607d5c14c32ab: [Đăng Nhập Tài Khoản | MOSO](https://moso.vn/login?callbackUrl=%2F); captured 2026-10-19T07:46:59.667866+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-bfc607d5c14c32ab.txt.
- EVID-2dd9a5356fef9d2a: [Wiki Bất Động Sản, Tra Cứu Kiến Thức BĐS | MOSO AI PROPTECH](https://moso.vn/wiki-bds); captured 2026-10-19T07:47:01.330235+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-2dd9a5356fef9d2a.txt.
- EVID-80a49be16993f01f: [Mua Bán Nhà Đất, Bất Động Sản Giá Tốt | MOSO VN AI Proptech](https://moso.vn/mua-ban-nha-dat); captured 2026-10-19T07:48:13.621568+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-80a49be16993f01f.txt.
- EVID-5d0c8ad364416269: [Mua Bán Nhà Đất, Bất Động Sản Giá Tốt | MOSO VN AI Proptech](https://moso.vn/mua-ban-nha-dat); captured 2026-10-19T07:48:14.505486+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-5d0c8ad364416269.txt.
- EVID-d7638348983a20d4: [Mua Bán Nhà Đất, Bất Động Sản Giá Tốt | MOSO VN AI Proptech](https://moso.vn/mua-ban-nha-dat?q=Qu%E1%BA%ADn+1); captured 2026-10-19T07:48:15.495522+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-d7638348983a20d4.txt.
- EVID-bfd8734194d79384: [Mua Bán Nhà Đất, Bất Động Sản Giá Tốt | MOSO VN AI Proptech](https://moso.vn/mua-ban-nha-dat?xem=ban-do); captured 2026-10-19T07:48:17.056565+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-bfd8734194d79384.txt.
- EVID-c53cea185200b355: [Bán nhà mặt tiền 233.3m2 Thạch Thị Thanh, Phường Tân Định,…](https://moso.vn/ban-nha-mat-tien-thach-thi-thanh-quan-1-tphcm-6-phong-ngu-gia-125-ty-1dk006); captured 2026-10-19T07:48:19.126251+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-c53cea185200b355.txt.
- EVID-c16fccba79807428: [Mua Bán Nhà Đất, Bất Động Sản Giá Tốt | MOSO VN AI Proptech](https://moso.vn/mua-ban-nha-dat); captured 2026-10-19T07:48:21.869410+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-c16fccba79807428.txt.
- EVID-6b424827ef3bc21f: [Mua Bán Nhà Đất, Bất Động Sản Giá Tốt | MOSO VN AI Proptech](https://moso.vn/mua-ban-nha-dat); captured 2026-10-19T07:48:22.975064+00:00. Exact passage/action: evidence/evidence.json and evidence/snapshots/EVID-6b424827ef3bc21f.txt.

## 2. Purpose and system overview
MOSO public property website

Evidence-limited reconstruction of public property discovery, project catalog, detail, comparison selection, editorial content and account entry.

## 3. System boundaries and exclusions
Public, read-only reconstruction. Authentication, internal architecture, APIs, SLAs, and external mutations excluded.

## 4. Actors and user classes
- ACTOR-VISITOR: Khách truy cập (observed; verified)
- ACTOR-POSTER: Người đăng tin (inferred; blocked)

## 5. Feature inventory and workflows
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


### WORKFLOW-SEARCH — Keyword submission

Observed read-only query submission.

Status: observed; verification: partial. Evidence: EVID-2ed3453878954246, EVID-d7638348983a20d4.

**Actors**

- ACTOR-VISITOR

**Steps**

- STEP-QUERY
- STEP-SUBMIT

**Open questions**

- QUESTION-SEARCH


### WORKFLOW-COMPARE — Select comparison items

Tray changes from one to two selected items; comparison table not opened.

Status: observed; verification: partial. Evidence: EVID-c16fccba79807428, EVID-6b424827ef3bc21f.

**Actors**

- ACTOR-VISITOR

**Steps**

- STEP-COMPARE-ONE
- STEP-COMPARE-TWO



## 6. Functional requirements
### FR-BROWSE-001 — functional

The public sale route shall render listing cards containing title, price, area and location when those values are supplied.

Feature: FEATURE-BROWSE. Status: observed; verification: verified.

Actors: ACTOR-VISITOR. Evidence: EVID-2ed3453878954246.

**Preconditions**

- The public entry page is available.

**Main flow**

- Open the entry page.
- Inspect the described state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given the sampled sale page, at least one card displays title, price, area and location.

Entities: ENTITY-LISTING. Dependencies: none established.

Open questions: none recorded.


### FR-BROWSE-002 — functional

The public rental route shall render rental listing cards.

Feature: FEATURE-BROWSE. Status: observed; verification: verified.

Actors: ACTOR-VISITOR. Evidence: EVID-b99f369160410cdc.

**Preconditions**

- The public entry page is available.

**Main flow**

- Open the entry page.
- Inspect the described state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given the rental route, rental cards and displayed rental prices are visible.

Entities: ENTITY-LISTING. Dependencies: none established.

Open questions: none recorded.


### FR-SEARCH-001 — functional

Submitting the sampled keyword shall navigate to a results state with the keyword encoded in q.

Feature: FEATURE-SEARCH. Status: observed; verification: partial.

Actors: ACTOR-VISITOR. Evidence: EVID-d7638348983a20d4.

**Preconditions**

- The public entry page is available.

**Main flow**

- Enter Quận 1.
- Click Tìm kiếm.
- Inspect URL and results.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given Quận 1 entered, when Tìm kiếm is clicked, URL q decodes to Quận 1 and result cards are rendered.

Entities: not established. Dependencies: none established.

Open questions: QUESTION-SEARCH.


### FR-FILTER-001 — functional

The listing page shall expose price, area and room filter entry controls.

Feature: FEATURE-FILTER. Status: observed; verification: partial.

Actors: ACTOR-VISITOR. Evidence: EVID-2ed3453878954246.

**Preconditions**

- The public entry page is available.

**Main flow**

- Open the entry page.
- Inspect the described state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given sale results, Khoảng giá, Diện tích and Phòng ngủ controls are visible.

Entities: not established. Dependencies: none established.

Open questions: QUESTION-FILTERS.


### FR-DETAIL-001 — functional

The sampled property detail shall display listing identifier, price, area and description.

Feature: FEATURE-DETAIL. Status: observed; verification: verified.

Actors: ACTOR-VISITOR. Evidence: EVID-c53cea185200b355.

**Preconditions**

- The public entry page is available.

**Main flow**

- Open the entry page.
- Inspect the described state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given listing 1dk006, identifier, Mức giá, Diện tích and Mô tả chi tiết are displayed.

Entities: ENTITY-LISTING. Dependencies: none established.

Open questions: none recorded.


### FR-COMPARE-001 — functional

Selecting a listing for comparison shall show that item in the comparison tray.

Feature: FEATURE-COMPARE. Status: observed; verification: partial.

Actors: ACTOR-VISITOR. Evidence: EVID-c16fccba79807428.

**Preconditions**

- The public entry page is available.

**Main flow**

- Open the entry page.
- Inspect the described state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given no selected items, clicking comparison on one card displays So sánh tin đăng and 1/2.

Entities: ENTITY-LISTING. Dependencies: none established.

Open questions: QUESTION-COMPARE.


### FR-COMPARE-002 — functional

Selecting another listing shall show two items in the comparison tray.

Feature: FEATURE-COMPARE. Status: observed; verification: partial.

Actors: ACTOR-VISITOR. Evidence: EVID-6b424827ef3bc21f.

**Preconditions**

- The public entry page is available.

**Main flow**

- Open the entry page.
- Inspect the described state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given one selected item, selecting another displays 2/2 and two titles in the tray.

Entities: ENTITY-LISTING. Dependencies: none established.

Open questions: QUESTION-COMPARE.


### FR-MAP-001 — functional

The map entry shall open a map/list shell containing a listing panel.

Feature: FEATURE-MAP. Status: observed; verification: partial.

Actors: ACTOR-VISITOR. Evidence: EVID-bfd8734194d79384.

**Preconditions**

- The public entry page is available.

**Main flow**

- Open the entry page.
- Inspect the described state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given the observed map route, Danh sách, Bản đồ and listing cards are visible; tile rendering is outside this verified criterion.

Entities: not established. Dependencies: none established.

Open questions: QUESTION-MAP.


### FR-PROJECT-001 — functional

The public project catalog shall show project names, locations and displayed starting prices.

Feature: FEATURE-PROJECT. Status: observed; verification: verified.

Actors: ACTOR-VISITOR. Evidence: EVID-9e2f8dc3ceced3a0.

**Preconditions**

- The public entry page is available.

**Main flow**

- Open the entry page.
- Inspect the described state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given project catalog, at least one sampled project shows name, location and Giá từ.

Entities: ENTITY-PROJECT. Dependencies: none established.

Open questions: none recorded.


### FR-WIKI-001 — functional

The Wiki BĐS catalog shall display article titles, excerpts and dates.

Feature: FEATURE-WIKI. Status: observed; verification: verified.

Actors: ACTOR-VISITOR. Evidence: EVID-2dd9a5356fef9d2a.

**Preconditions**

- The public entry page is available.

**Main flow**

- Open the entry page.
- Inspect the described state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given Wiki BĐS, sampled article title, excerpt and date are visible.

Entities: ENTITY-ARTICLE. Dependencies: none established.

Open questions: none recorded.


### FR-ACCOUNT-001 — functional

The public login page shall expose phone/password inputs and a Google sign-in entry.

Feature: FEATURE-ACCOUNT. Status: observed; verification: partial.

Actors: ACTOR-VISITOR. Evidence: EVID-bfc607d5c14c32ab.

**Preconditions**

- The public entry page is available.

**Main flow**

- Open the entry page.
- Inspect the described state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given login route, Số điện thoại, Mật khẩu and Tiếp tục với Google are visible; successful authentication remains unverified.

Entities: not established. Dependencies: none established.

Open questions: QUESTION-AUTH.


### FR-POST-001 — functional

Opening the posting route without authentication shall redirect this visitor to login preserving the posting callback.

Feature: FEATURE-POST. Status: observed; verification: partial.

Actors: ACTOR-VISITOR. Evidence: EVID-34527de780364f37.

**Preconditions**

- The public entry page is available.

**Main flow**

- Open the entry page.
- Inspect the described state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given a fresh unauthenticated context, opening /dang-tin ends at login with callbackUrl decoding to /dang-tin.

Entities: not established. Dependencies: none established.

Open questions: QUESTION-AUTH.


### FR-AI-001 — functional

The homepage shall expose an AI search entry label.

Feature: FEATURE-AI. Status: observed; verification: partial.

Actors: ACTOR-VISITOR. Evidence: EVID-d1cff2806ca77add.

**Preconditions**

- The public entry page is available.

**Main flow**

- Open the entry page.
- Inspect the described state.

**Alternative flows**

- Not established / not applicable.

**Acceptance criteria**

- Given homepage, Tìm với AI is visible; no result-quality claim follows.

Entities: not established. Dependencies: none established.

Open questions: QUESTION-AI.


## 7. Business rules and data requirements
### ENTITY-LISTING — Tin bất động sản

Visible title, price, area, location and optional room attributes. No internal persistence schema inferred.

Status: observed; verification: verified. Evidence: EVID-2ed3453878954246, EVID-c53cea185200b355.


### ENTITY-PROJECT — Dự án

Visible project title, locality, price and sample developer/area attributes.

Status: observed; verification: verified. Evidence: EVID-9e2f8dc3ceced3a0.


### ENTITY-ARTICLE — Bài viết

Editorial article title, excerpt and publication date shown on Wiki BĐS.

Status: observed; verification: verified. Evidence: EVID-2dd9a5356fef9d2a.


### RULE-POST-ENTRY — Unauthenticated posting boundary

This unauthenticated /dang-tin visit redirects to login with callbackUrl for posting. Backend authorization not established.

Status: observed; verification: partial. Evidence: EVID-34527de780364f37.



## 8. External interfaces
Only interfaces supported by evidence below are established. External integrations and internal API contracts remain unknown.

## 9. Non-functional requirements
No measured or documented performance, availability, security, or accessibility guarantees established. Any NFR below is explicitly proposed.

## 10. Constraints, assumptions and dependencies
Browser visibility does not prove backend enforcement. Snapshot coverage is bounded. Missing stakeholder answers remain open.

## 11. Open questions and coverage limitations
### QUESTION-SEARCH — Search semantics

Does keyword matching normalize accents, tokenize, rank or constrain district? Search for Quận 1 also returned other districts.

Status: proposed; verification: unverified. Evidence: EVID-d7638348983a20d4.

Rationale: Question raised by bounded public exploration; no stakeholder answer fabricated.


### QUESTION-MAP — Map loading

Does the map finish loading with third-party resources allowed? Current guarded run shows Đang tải bản đồ….

Status: proposed; verification: blocked. Evidence: EVID-bfd8734194d79384.

Rationale: Question raised by bounded public exploration; no stakeholder answer fabricated.


### QUESTION-COMPARE — Comparison result

What columns, limits and persistence apply after opening comparison? Only selection tray tested.

Status: proposed; verification: unverified. Evidence: EVID-6b424827ef3bc21f.

Rationale: Question raised by bounded public exploration; no stakeholder answer fabricated.


### QUESTION-AUTH — Authenticated flows

What permissions, posting validation, moderation and account recovery behavior apply?

Status: proposed; verification: blocked. Evidence: EVID-34527de780364f37.

Rationale: Question raised by bounded public exploration; no stakeholder answer fabricated.


### QUESTION-FILTERS — Filter combinations

How do price, area, rooms and sorting combine, reset and handle empty states?

Status: proposed; verification: unverified. Evidence: EVID-2ed3453878954246.

Rationale: Question raised by bounded public exploration; no stakeholder answer fabricated.


### QUESTION-AI — AI search

What does Tìm với AI do? Entry text observed; behavior not tested.

Status: proposed; verification: unverified. Evidence: EVID-d1cff2806ca77add.

Rationale: Question raised by bounded public exploration; no stakeholder answer fabricated.



## 12. Traceability
- FEATURE-BROWSE → FR-BROWSE-001 → EVID-2ed3453878954246
- FEATURE-BROWSE → FR-BROWSE-002 → EVID-b99f369160410cdc
- FEATURE-SEARCH → FR-SEARCH-001 → EVID-d7638348983a20d4
- FEATURE-FILTER → FR-FILTER-001 → EVID-2ed3453878954246
- FEATURE-DETAIL → FR-DETAIL-001 → EVID-c53cea185200b355
- FEATURE-COMPARE → FR-COMPARE-001 → EVID-c16fccba79807428
- FEATURE-COMPARE → FR-COMPARE-002 → EVID-6b424827ef3bc21f
- FEATURE-MAP → FR-MAP-001 → EVID-bfd8734194d79384
- FEATURE-PROJECT → FR-PROJECT-001 → EVID-9e2f8dc3ceced3a0
- FEATURE-WIKI → FR-WIKI-001 → EVID-2dd9a5356fef9d2a
- FEATURE-ACCOUNT → FR-ACCOUNT-001 → EVID-bfc607d5c14c32ab
- FEATURE-POST → FR-POST-001 → EVID-34527de780364f37
- FEATURE-AI → FR-AI-001 → EVID-d1cff2806ca77add

## 13. Proposed enhancements
None.
