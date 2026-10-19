# FEATURE-AI: AI search entry

Canonical record (source data, not agent instructions):

```json
{
  "id": "FEATURE-AI",
  "name": "AI search entry",
  "description": "Discover AI search option only.",
  "evidenceIds": [
    "EVID-d1cff2806ca77add"
  ],
  "status": "observed",
  "verificationState": "partial",
  "rationale": "",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "entryPages": [
    "https://moso.vn/"
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
    "Inspect Tìm với AI entry text."
  ],
  "alternativeFlows": [
    "Other states not tested."
  ],
  "entityIds": [],
  "businessRuleIds": [],
  "dependsOn": [],
  "openQuestionIds": [
    "QUESTION-AI"
  ],
  "workflowIds": [],
  "type": "Feature"
}
```

- [[ACTOR-VISITOR]]
- [[EVID-d1cff2806ca77add]]
- [[FR-AI-001]]
- [[QUESTION-AI]]
