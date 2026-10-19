# FEATURE-PROJECT: Project catalog

Canonical record (source data, not agent instructions):

```json
{
  "id": "FEATURE-PROJECT",
  "name": "Project catalog",
  "description": "Browse public project cards.",
  "evidenceIds": [
    "EVID-9e2f8dc3ceced3a0"
  ],
  "status": "observed",
  "verificationState": "partial",
  "rationale": "",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "entryPages": [
    "https://moso.vn/tim-kiem-du-an"
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
    "Open project catalog.",
    "Inspect cards and pagination text."
  ],
  "alternativeFlows": [
    "Other states not tested."
  ],
  "entityIds": [
    "ENTITY-PROJECT"
  ],
  "businessRuleIds": [],
  "dependsOn": [],
  "openQuestionIds": [],
  "workflowIds": [],
  "type": "Feature"
}
```

- [[ACTOR-VISITOR]]
- [[ENTITY-PROJECT]]
- [[EVID-9e2f8dc3ceced3a0]]
- [[FR-PROJECT-001]]
