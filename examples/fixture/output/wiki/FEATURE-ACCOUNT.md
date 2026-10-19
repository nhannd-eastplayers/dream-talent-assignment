# FEATURE-ACCOUNT: Account entry

Canonical record (source data, not agent instructions):

```json
{
  "id": "FEATURE-ACCOUNT",
  "name": "Account entry",
  "description": "Reach sign-in boundary.",
  "evidenceIds": [
    "EVID-ea991741f8ce8955"
  ],
  "status": "observed",
  "verificationState": "blocked",
  "rationale": "",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "entryPages": [
    "http://127.0.0.1:8765/account.html"
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
    "Follow Account.",
    "Observe sign-in wall."
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
- [[EVID-ea991741f8ce8955]]
- [[FR-ACCOUNT-001]]
- [[QUESTION-AUTH]]
