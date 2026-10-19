# FEATURE-ACCOUNT: Account entry

Canonical record (source data, not agent instructions):

```json
{
  "id": "FEATURE-ACCOUNT",
  "name": "Account entry",
  "description": "Inspect phone/password and Google entry controls.",
  "evidenceIds": [
    "EVID-bfc607d5c14c32ab"
  ],
  "status": "observed",
  "verificationState": "blocked",
  "rationale": "",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "entryPages": [
    "https://moso.vn/login?callbackUrl=%2F"
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
    "Open login page.",
    "Inspect controls; submit no credentials."
  ],
  "alternativeFlows": [
    "Other states not tested."
  ],
  "entityIds": [],
  "businessRuleIds": [],
  "dependsOn": [],
  "openQuestionIds": [
    "QUESTION-AUTH"
  ],
  "workflowIds": [],
  "type": "Feature"
}
```

- [[ACTOR-VISITOR]]
- [[EVID-bfc607d5c14c32ab]]
- [[FR-ACCOUNT-001]]
- [[QUESTION-AUTH]]
