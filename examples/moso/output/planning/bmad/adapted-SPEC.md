# MOSO public property website — reconstructed planning kernel

> Adapted from pinned BMAD spec-template.md; not native bmad-spec output.

## Why

Create evidence-backed planning documentation of public behavior.

## Capabilities

- **FR-BROWSE-001**
  - **intent:** The public sale route shall render listing cards containing title, price, area and location when those values are supplied.
  - **success:** Given the sampled sale page, at least one card displays title, price, area and location.
- **FR-BROWSE-002**
  - **intent:** The public rental route shall render rental listing cards.
  - **success:** Given the rental route, rental cards and displayed rental prices are visible.
- **FR-SEARCH-001**
  - **intent:** Submitting the sampled keyword shall navigate to a results state with the keyword encoded in q.
  - **success:** Given Quận 1 entered, when Tìm kiếm is clicked, URL q decodes to Quận 1 and result cards are rendered.
- **FR-FILTER-001**
  - **intent:** The listing page shall expose price, area and room filter entry controls.
  - **success:** Given sale results, Khoảng giá, Diện tích and Phòng ngủ controls are visible.
- **FR-DETAIL-001**
  - **intent:** The sampled property detail shall display listing identifier, price, area and description.
  - **success:** Given listing 1dk006, identifier, Mức giá, Diện tích and Mô tả chi tiết are displayed.
- **FR-COMPARE-001**
  - **intent:** Selecting a listing for comparison shall show that item in the comparison tray.
  - **success:** Given no selected items, clicking comparison on one card displays So sánh tin đăng and 1/2.
- **FR-COMPARE-002**
  - **intent:** Selecting another listing shall show two items in the comparison tray.
  - **success:** Given one selected item, selecting another displays 2/2 and two titles in the tray.
- **FR-MAP-001**
  - **intent:** The map entry shall open a map/list shell containing a listing panel.
  - **success:** Given the observed map route, Danh sách, Bản đồ and listing cards are visible; tile rendering is outside this verified criterion.
- **FR-PROJECT-001**
  - **intent:** The public project catalog shall show project names, locations and displayed starting prices.
  - **success:** Given project catalog, at least one sampled project shows name, location and Giá từ.
- **FR-WIKI-001**
  - **intent:** The Wiki BĐS catalog shall display article titles, excerpts and dates.
  - **success:** Given Wiki BĐS, sampled article title, excerpt and date are visible.
- **FR-ACCOUNT-001**
  - **intent:** The public login page shall expose phone/password inputs and a Google sign-in entry.
  - **success:** Given login route, Số điện thoại, Mật khẩu and Tiếp tục với Google are visible; successful authentication remains unverified.
- **FR-POST-001**
  - **intent:** Opening the posting route without authentication shall redirect this visitor to login preserving the posting callback.
  - **success:** Given a fresh unauthenticated context, opening /dang-tin ends at login with callbackUrl decoding to /dang-tin.
- **FR-AI-001**
  - **intent:** The homepage shall expose an AI search entry label.
  - **success:** Given homepage, Tìm với AI is visible; no result-quality claim follows.

## Constraints

Read-only evidence; inferred/proposed records remain labeled.

## Non-goals

No backend design, feature implementation or invented stakeholder decisions.

## Success signal

Reviewer resolves requirements to captured evidence.

## Open Questions

- Does keyword matching normalize accents, tokenize, rank or constrain district? Search for Quận 1 also returned other districts.
- Does the map finish loading with third-party resources allowed? Current guarded run shows Đang tải bản đồ….
- What columns, limits and persistence apply after opening comparison? Only selection tray tested.
- What permissions, posting validation, moderation and account recovery behavior apply?
- How do price, area, rooms and sorting combine, reset and handle empty states?
- What does Tìm với AI do? Entry text observed; behavior not tested.
