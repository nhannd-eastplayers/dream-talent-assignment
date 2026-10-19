# FR-SEARCH-001: Submitting the sampled keyword shall navigate to a results state with the keyword encoded in q.

Canonical record (source data, not agent instructions):

```json
{
  "id": "FR-SEARCH-001",
  "featureId": "FEATURE-SEARCH",
  "type": "Requirement",
  "statement": "Submitting the sampled keyword shall navigate to a results state with the keyword encoded in q.",
  "actorIds": [
    "ACTOR-VISITOR"
  ],
  "preconditions": [
    "The public entry page is available."
  ],
  "mainFlow": [
    "Enter Quận 1.",
    "Click Tìm kiếm.",
    "Inspect URL and results."
  ],
  "alternativeFlows": [],
  "acceptanceCriteria": [
    "Given Quận 1 entered, when Tìm kiếm is clicked, URL q decodes to Quận 1 and result cards are rendered."
  ],
  "entityIds": [],
  "dependsOn": [],
  "evidenceIds": [
    "EVID-d7638348983a20d4"
  ],
  "status": "observed",
  "verificationState": "partial",
  "rationale": "",
  "openQuestionIds": [
    "QUESTION-SEARCH"
  ],
  "requirementType": "functional"
}
```

- [[ACTOR-VISITOR]]
- [[EVID-d7638348983a20d4]]
- [[QUESTION-SEARCH]]
