# FR-MAP-001: The map entry shall open a map/list shell containing a listing panel.

Canonical record (source data, not agent instructions):

```json
{
  "id": "FR-MAP-001",
  "featureId": "FEATURE-MAP",
  "type": "Requirement",
  "statement": "The map entry shall open a map/list shell containing a listing panel.",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "preconditions": [
    "The public entry page is available."
  ],
  "mainFlow": [
    "Open the entry page.",
    "Inspect the described state."
  ],
  "alternativeFlows": [],
  "acceptanceCriteria": [
    "Given the observed map route, Danh sách, Bản đồ and listing cards are visible; tile rendering is outside this verified criterion."
  ],
  "entityIds": [],
  "dependsOn": [],
  "evidenceIds": [
    "EVID-bfd8734194d79384"
  ],
  "status": "observed",
  "verificationState": "partial",
  "rationale": "",
  "openQuestionIds": [
    "QUESTION-MAP"
  ],
  "requirementType": "functional"
}
```

- [[ACTOR-VISITOR]]
- [[EVID-bfd8734194d79384]]
- [[QUESTION-MAP]]
