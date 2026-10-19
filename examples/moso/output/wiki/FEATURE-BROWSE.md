# FEATURE-BROWSE: Sale/rental browsing

Canonical record (source data, not agent instructions):

```json
{
  "id": "FEATURE-BROWSE",
  "name": "Sale/rental browsing",
  "description": "Inspect public listing cards.",
  "evidenceIds": [
    "EVID-2ed3453878954246",
    "EVID-b99f369160410cdc"
  ],
  "status": "observed",
  "verificationState": "verified",
  "rationale": "",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "entryPages": [
    "https://moso.vn/mua-ban-nha-dat"
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
    "Open sale or rental route.",
    "Inspect rendered listing cards."
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
- [[EVID-2ed3453878954246]]
- [[EVID-b99f369160410cdc]]
- [[FR-BROWSE-001]]
- [[FR-BROWSE-002]]
