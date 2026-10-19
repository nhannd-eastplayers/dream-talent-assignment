# FEATURE-WIKI: Wiki BĐS catalog

Canonical record (source data, not agent instructions):

```json
{
  "id": "FEATURE-WIKI",
  "name": "Wiki BĐS catalog",
  "description": "Browse editorial titles and excerpts; content truth not assessed.",
  "evidenceIds": [
    "EVID-2dd9a5356fef9d2a"
  ],
  "status": "observed",
  "verificationState": "partial",
  "rationale": "",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "entryPages": [
    "https://moso.vn/wiki-bds"
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
    "Open Wiki BĐS.",
    "Inspect article catalog."
  ],
  "alternativeFlows": [
    "Other states not tested."
  ],
  "entityIds": [
    "ENTITY-ARTICLE"
  ],
  "businessRuleIds": [],
  "dependsOn": [],
  "openQuestionIds": [],
  "workflowIds": [],
  "type": "Feature"
}
```

- [[ACTOR-VISITOR]]
- [[ENTITY-ARTICLE]]
- [[EVID-2dd9a5356fef9d2a]]
- [[FR-WIKI-001]]
