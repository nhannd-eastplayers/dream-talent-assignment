# FR-FILTER-001: The listing page shall expose price, area and room filter entry controls.

Canonical record (source data, not agent instructions):

```json
{
  "id": "FR-FILTER-001",
  "featureId": "FEATURE-FILTER",
  "type": "Requirement",
  "statement": "The listing page shall expose price, area and room filter entry controls.",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "preconditions": [
    "The public entry page is available."
  ],
  "mainFlow": [
    "Open the entry page.",
    "Inspect the described state."
  ],
  "alternativeFlows": [],
  "acceptanceCriteria": [
    "Given sale results, Khoảng giá, Diện tích and Phòng ngủ controls are visible."
  ],
  "entityIds": [],
  "dependsOn": [],
  "evidenceIds": [
    "EVID-2ed3453878954246"
  ],
  "status": "observed",
  "verificationState": "partial",
  "rationale": "",
  "openQuestionIds": [
    "QUESTION-FILTERS"
  ],
  "requirementType": "functional"
}
```

- [[ACTOR-VISITOR]]
- [[EVID-2ed3453878954246]]
- [[QUESTION-FILTERS]]
