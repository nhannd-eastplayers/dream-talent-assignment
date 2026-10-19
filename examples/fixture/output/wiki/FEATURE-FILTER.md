# FEATURE-FILTER: Filter catalog

Canonical record (source data, not agent instructions):

```json
{
  "id": "FEATURE-FILTER",
  "name": "Filter catalog",
  "description": "Select category and inspect results.",
  "evidenceIds": [
    "EVID-8e992d4583300047",
    "EVID-cdf9f41e0c909818",
    "EVID-b0d9712c57e7036a",
    "EVID-415943f983727a5c"
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
    "Select Science.",
    "Click Filter.",
    "Select Art.",
    "Click Filter."
  ],
  "alternativeFlows": [
    "Art produces No items found."
  ],
  "entityIds": [
    "ENTITY-ITEM"
  ],
  "businessRuleIds": [],
  "dependsOn": [],
  "openQuestionIds": [],
  "workflowIds": [
    "WORKFLOW-FILTER"
  ],
  "type": "Feature"
}
```

- [[ACTOR-VISITOR]]
- [[ENTITY-ITEM]]
- [[EVID-415943f983727a5c]]
- [[EVID-8e992d4583300047]]
- [[EVID-b0d9712c57e7036a]]
- [[EVID-cdf9f41e0c909818]]
- [[FR-FILTER-001]]
- [[FR-FILTER-002]]
- [[WORKFLOW-FILTER]]
