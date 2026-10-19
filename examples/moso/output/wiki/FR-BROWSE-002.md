# FR-BROWSE-002: The public rental route shall render rental listing cards.

Canonical record (source data, not agent instructions):

```json
{
  "id": "FR-BROWSE-002",
  "featureId": "FEATURE-BROWSE",
  "type": "Requirement",
  "statement": "The public rental route shall render rental listing cards.",
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
    "Given the rental route, rental cards and displayed rental prices are visible."
  ],
  "entityIds": [
    "ENTITY-LISTING"
  ],
  "dependsOn": [],
  "evidenceIds": [
    "EVID-b99f369160410cdc"
  ],
  "status": "observed",
  "verificationState": "verified",
  "rationale": "",
  "openQuestionIds": [],
  "requirementType": "functional"
}
```

- [[ACTOR-VISITOR]]
- [[ENTITY-LISTING]]
- [[EVID-b99f369160410cdc]]
