# FEATURE-COMPARE: Comparison selection

Canonical record (source data, not agent instructions):

```json
{
  "id": "FEATURE-COMPARE",
  "name": "Comparison selection",
  "description": "Select two properties into comparison tray.",
  "evidenceIds": [
    "EVID-c16fccba79807428",
    "EVID-6b424827ef3bc21f"
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
    "Click first comparison control.",
    "Observe 1/2 tray.",
    "Click another comparison control.",
    "Observe 2/2 tray."
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
    "QUESTION-COMPARE"
  ],
  "workflowIds": [
    "WORKFLOW-COMPARE"
  ],
  "type": "Feature"
}
```

- [[ACTOR-VISITOR]]
- [[ENTITY-LISTING]]
- [[EVID-6b424827ef3bc21f]]
- [[EVID-c16fccba79807428]]
- [[FR-COMPARE-001]]
- [[FR-COMPARE-002]]
- [[QUESTION-COMPARE]]
- [[WORKFLOW-COMPARE]]
