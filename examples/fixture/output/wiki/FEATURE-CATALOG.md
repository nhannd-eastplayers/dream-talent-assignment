# FEATURE-CATALOG: Browse catalog

Canonical record (source data, not agent instructions):

```json
{
  "id": "FEATURE-CATALOG",
  "name": "Browse catalog",
  "description": "Find catalog items.",
  "evidenceIds": [
    "EVID-9ea047ea81cbbcba"
  ],
  "status": "observed",
  "verificationState": "verified",
  "rationale": "",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "entryPages": [
    "http://127.0.0.1:8765/"
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
    "Open catalog.",
    "Read item title."
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
- [[EVID-9ea047ea81cbbcba]]
- [[FR-CATALOG-001]]
