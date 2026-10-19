# FEATURE-DETAIL: Property detail

Canonical record (source data, not agent instructions):

```json
{
  "id": "FEATURE-DETAIL",
  "name": "Property detail",
  "description": "Read one listing’s visible descriptive fields.",
  "evidenceIds": [
    "EVID-c53cea185200b355"
  ],
  "status": "observed",
  "verificationState": "verified",
  "rationale": "",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "entryPages": [
    "https://moso.vn/ban-nha-mat-tien-thach-thi-thanh-quan-1-tphcm-6-phong-ngu-gia-125-ty-1dk006"
  ],
  "preconditions": [
    "Public website reachable."
  ],
  "inputs": [
    "Visitor navigation or read-only query"
  ],
  "outputs": [
    "Rendered page state"
  ],
  "mainFlow": [
    "Follow listing link.",
    "Inspect identifier, price, area and description."
  ],
  "alternativeFlows": [
    "Other states not tested."
  ],
  "entityIds": [
    "ENTITY-LISTING"
  ],
  "businessRuleIds": [],
  "dependsOn": [],
  "openQuestionIds": [],
  "workflowIds": [],
  "type": "Feature"
}
```

- [[ACTOR-VISITOR]]
- [[ENTITY-LISTING]]
- [[EVID-c53cea185200b355]]
- [[FR-DETAIL-001]]
