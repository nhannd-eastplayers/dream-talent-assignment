# FR-COMPARE-002: Selecting another listing shall show two items in the comparison tray.

Canonical record (source data, not agent instructions):

```json
{
  "id": "FR-COMPARE-002",
  "featureId": "FEATURE-COMPARE",
  "type": "Requirement",
  "statement": "Selecting another listing shall show two items in the comparison tray.",
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
    "Given one selected item, selecting another displays 2/2 and two titles in the tray."
  ],
  "entityIds": [
    "ENTITY-LISTING"
  ],
  "dependsOn": [],
  "evidenceIds": [
    "EVID-6b424827ef3bc21f"
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
- [[EVID-6b424827ef3bc21f]]
- [[QUESTION-COMPARE]]
