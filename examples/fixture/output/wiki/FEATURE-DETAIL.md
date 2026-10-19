# FEATURE-DETAIL: Item detail

Canonical record (source data, not agent instructions):

```json
{
  "id": "FEATURE-DETAIL",
  "name": "Item detail",
  "description": "Read item metadata.",
  "evidenceIds": [
    "EVID-337e164078942bbe"
  ],
  "status": "observed",
  "verificationState": "verified",
  "rationale": "",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "entryPages": [
    "http://127.0.0.1:8765/detail.html"
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
    "Follow detail link.",
    "Read category and format."
  ],
  "alternativeFlows": [
    "Other states not tested."
  ],
  "entityIds": [
    "ENTITY-ITEM"
  ],
  "businessRuleIds": [],
  "dependsOn": [],
  "openQuestionIds": [],
  "workflowIds": [],
  "type": "Feature"
}
```

- [[ACTOR-VISITOR]]
- [[ENTITY-ITEM]]
- [[EVID-337e164078942bbe]]
- [[FR-DETAIL-001]]
