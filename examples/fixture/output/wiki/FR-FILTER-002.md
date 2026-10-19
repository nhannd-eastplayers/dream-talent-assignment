# FR-FILTER-002: Selecting Art and applying Filter shall display an empty-result message.

Canonical record (source data, not agent instructions):

```json
{
  "id": "FR-FILTER-002",
  "featureId": "FEATURE-FILTER",
  "type": "Requirement",
  "statement": "Selecting Art and applying Filter shall display an empty-result message.",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "preconditions": [
    "The public entry page is available."
  ],
  "mainFlow": [
    "Select Art.",
    "Click Filter.",
    "Read empty state."
  ],
  "alternativeFlows": [],
  "acceptanceCriteria": [
    "Given Art selected, when Filter is clicked, No items found is displayed."
  ],
  "entityIds": [],
  "dependsOn": [],
  "evidenceIds": [
    "EVID-b0d9712c57e7036a",
    "EVID-415943f983727a5c"
  ],
  "status": "observed",
  "verificationState": "verified",
  "rationale": "",
  "openQuestionIds": [],
  "requirementType": "functional"
}
```

- [[ACTOR-VISITOR]]
- [[EVID-415943f983727a5c]]
- [[EVID-b0d9712c57e7036a]]
