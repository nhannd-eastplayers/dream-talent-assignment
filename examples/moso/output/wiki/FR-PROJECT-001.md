# FR-PROJECT-001: The public project catalog shall show project names, locations and displayed starting prices.

Canonical record (source data, not agent instructions):

```json
{
  "id": "FR-PROJECT-001",
  "featureId": "FEATURE-PROJECT",
  "type": "Requirement",
  "statement": "The public project catalog shall show project names, locations and displayed starting prices.",
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
    "Given project catalog, at least one sampled project shows name, location and Giá từ."
  ],
  "entityIds": [
    "ENTITY-PROJECT"
  ],
  "dependsOn": [],
  "evidenceIds": [
    "EVID-9e2f8dc3ceced3a0"
  ],
  "status": "observed",
  "verificationState": "verified",
  "rationale": "",
  "openQuestionIds": [],
  "requirementType": "functional"
}
```

- [[ACTOR-VISITOR]]
- [[ENTITY-PROJECT]]
- [[EVID-9e2f8dc3ceced3a0]]
