# FR-FILTER-001: Selecting Science and applying Filter shall retain River atlas.

Canonical record (source data, not agent instructions):

```json
{
  "id": "FR-FILTER-001",
  "featureId": "FEATURE-FILTER",
  "type": "Requirement",
  "statement": "Selecting Science and applying Filter shall retain River atlas.",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "preconditions": [
    "The public entry page is available."
  ],
  "mainFlow": [
    "Select Science.",
    "Click Filter.",
    "Read results."
  ],
  "alternativeFlows": [],
  "acceptanceCriteria": [
    "Given Science selected, when Filter is clicked, River atlas — Science is displayed."
  ],
  "entityIds": [
    "ENTITY-ITEM"
  ],
  "dependsOn": [],
  "evidenceIds": [
    "EVID-8e992d4583300047",
    "EVID-cdf9f41e0c909818"
  ],
  "status": "observed",
  "verificationState": "verified",
  "rationale": "",
  "openQuestionIds": [],
  "requirementType": "functional"
}
```

- [[ACTOR-VISITOR]]
- [[ENTITY-ITEM]]
- [[EVID-8e992d4583300047]]
- [[EVID-cdf9f41e0c909818]]
