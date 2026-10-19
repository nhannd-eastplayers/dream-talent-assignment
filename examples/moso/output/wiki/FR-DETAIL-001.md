# FR-DETAIL-001: The sampled property detail shall display listing identifier, price, area and description.

Canonical record (source data, not agent instructions):

```json
{
  "id": "FR-DETAIL-001",
  "featureId": "FEATURE-DETAIL",
  "type": "Requirement",
  "statement": "The sampled property detail shall display listing identifier, price, area and description.",
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
    "Given listing 1dk006, identifier, Mức giá, Diện tích and Mô tả chi tiết are displayed."
  ],
  "entityIds": [
    "ENTITY-LISTING"
  ],
  "dependsOn": [],
  "evidenceIds": [
    "EVID-c53cea185200b355"
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
- [[EVID-c53cea185200b355]]
