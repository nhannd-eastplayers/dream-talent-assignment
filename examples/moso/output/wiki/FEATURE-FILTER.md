# FEATURE-FILTER: Listing filters

Canonical record (source data, not agent instructions):

```json
{
  "id": "FEATURE-FILTER",
  "name": "Listing filters",
  "description": "Discover price, area, rooms, date and sorting controls.",
  "evidenceIds": [
    "EVID-2ed3453878954246"
  ],
  "status": "observed",
  "verificationState": "partial",
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
    "Open listing results.",
    "Inspect filter controls without asserting their behavior."
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
    "QUESTION-FILTERS"
  ],
  "workflowIds": [],
  "type": "Feature"
}
```

- [[ACTOR-VISITOR]]
- [[ENTITY-LISTING]]
- [[EVID-2ed3453878954246]]
- [[FR-FILTER-001]]
- [[QUESTION-FILTERS]]
