# FR-BROWSE-001: The public sale route shall render listing cards containing title, price, area and location when those values are supplied.

Canonical record (source data, not agent instructions):

```json
{
  "id": "FR-BROWSE-001",
  "featureId": "FEATURE-BROWSE",
  "type": "Requirement",
  "statement": "The public sale route shall render listing cards containing title, price, area and location when those values are supplied.",
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
    "Given the sampled sale page, at least one card displays title, price, area and location."
  ],
  "entityIds": [
    "ENTITY-LISTING"
  ],
  "dependsOn": [],
  "evidenceIds": [
    "EVID-2ed3453878954246"
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
- [[EVID-2ed3453878954246]]
