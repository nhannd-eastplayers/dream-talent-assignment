# FR-ACCOUNT-001: The public account page shall show that sign-in is required.

Canonical record (source data, not agent instructions):

```json
{
  "id": "FR-ACCOUNT-001",
  "featureId": "FEATURE-ACCOUNT",
  "type": "Requirement",
  "statement": "The public account page shall show that sign-in is required.",
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
    "Given Account is opened, the sign-in-required message is visible."
  ],
  "entityIds": [],
  "dependsOn": [],
  "evidenceIds": [
    "EVID-ea991741f8ce8955"
  ],
  "status": "observed",
  "verificationState": "partial",
  "rationale": "",
  "openQuestionIds": [
    "QUESTION-AUTH"
  ],
  "requirementType": "functional"
}
```

- [[ACTOR-VISITOR]]
- [[EVID-ea991741f8ce8955]]
- [[QUESTION-AUTH]]
