# FEATURE-MAP: Map entry

Canonical record (source data, not agent instructions):

```json
{
  "id": "FEATURE-MAP",
  "name": "Map entry",
  "description": "Open map/list route; map loading unverified.",
  "evidenceIds": [
    "EVID-bfd8734194d79384"
  ],
  "status": "observed",
  "verificationState": "partial",
  "rationale": "",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "entryPages": [
    "https://moso.vn/mua-ban-nha-dat?xem=ban-do"
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
    "Open map link.",
    "Observe map shell and listing panel."
  ],
  "alternativeFlows": [
    "Other states not tested."
  ],
  "entityIds": [
    "ENTITY-LISTING"
  ],
  "businessRuleIds": [],
  "dependsOn": [],
  "openQuestionIds": [
    "QUESTION-MAP"
  ],
  "workflowIds": [],
  "type": "Feature"
}
```

- [[ACTOR-VISITOR]]
- [[ENTITY-LISTING]]
- [[EVID-bfd8734194d79384]]
- [[FR-MAP-001]]
- [[QUESTION-MAP]]
