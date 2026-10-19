# FR-COMPARE-001: Selecting a listing for comparison shall show that item in the comparison tray.

Canonical record (source data, not agent instructions):

```json
{
  "id": "FR-COMPARE-001",
  "featureId": "FEATURE-COMPARE",
  "type": "Requirement",
  "statement": "Selecting a listing for comparison shall show that item in the comparison tray.",
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
    "Given no selected items, clicking comparison on one card displays So sánh tin đăng and 1/2."
  ],
  "entityIds": [
    "ENTITY-LISTING"
  ],
  "dependsOn": [],
  "evidenceIds": [
    "EVID-c16fccba79807428"
  ],
  "status": "observed",
  "verificationState": "partial",
  "rationale": "",
  "openQuestionIds": [
    "QUESTION-COMPARE"
  ],
  "requirementType": "functional"
}
```

- [[ACTOR-VISITOR]]
- [[ENTITY-LISTING]]
- [[EVID-c16fccba79807428]]
- [[QUESTION-COMPARE]]
