# FEATURE-SEARCH: Keyword search

Canonical record (source data, not agent instructions):

```json
{
  "id": "FEATURE-SEARCH",
  "name": "Keyword search",
  "description": "Submit public query; search semantics remain unknown.",
  "evidenceIds": [
    "EVID-2ed3453878954246",
    "EVID-d7638348983a20d4"
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
    "Fill q with Quận 1.",
    "Click Tìm kiếm.",
    "Observe q URL and changed results."
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
    "QUESTION-SEARCH"
  ],
  "workflowIds": [
    "WORKFLOW-SEARCH"
  ],
  "type": "Feature"
}
```

- [[ACTOR-VISITOR]]
- [[ENTITY-LISTING]]
- [[EVID-2ed3453878954246]]
- [[EVID-d7638348983a20d4]]
- [[FR-SEARCH-001]]
- [[QUESTION-SEARCH]]
- [[WORKFLOW-SEARCH]]
