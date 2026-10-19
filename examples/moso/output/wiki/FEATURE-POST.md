# FEATURE-POST: Posting entry

Canonical record (source data, not agent instructions):

```json
{
  "id": "FEATURE-POST",
  "name": "Posting entry",
  "description": "Observe unauthenticated posting redirect.",
  "evidenceIds": [
    "EVID-34527de780364f37"
  ],
  "status": "observed",
  "verificationState": "blocked",
  "rationale": "",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "entryPages": [
    "https://moso.vn/dang-tin"
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
    "Open Đăng tin.",
    "Observe login redirect preserving callback."
  ],
  "alternativeFlows": [
    "Other states not tested."
  ],
  "entityIds": [
    "ENTITY-LISTING"
  ],
  "businessRuleIds": [
    "RULE-POST-ENTRY"
  ],
  "dependsOn": [],
  "openQuestionIds": [
    "QUESTION-AUTH"
  ],
  "workflowIds": [],
  "type": "Feature"
}
```

- [[ACTOR-VISITOR]]
- [[ENTITY-LISTING]]
- [[EVID-34527de780364f37]]
- [[FR-POST-001]]
- [[QUESTION-AUTH]]
- [[RULE-POST-ENTRY]]
