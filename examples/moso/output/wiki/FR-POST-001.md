# FR-POST-001: Opening the posting route without authentication shall redirect this visitor to login preserving the posting callback.

Canonical record (source data, not agent instructions):

```json
{
  "id": "FR-POST-001",
  "featureId": "FEATURE-POST",
  "type": "Requirement",
  "statement": "Opening the posting route without authentication shall redirect this visitor to login preserving the posting callback.",
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
    "Given a fresh unauthenticated context, opening /dang-tin ends at login with callbackUrl decoding to /dang-tin."
  ],
  "entityIds": [],
  "dependsOn": [],
  "evidenceIds": [
    "EVID-34527de780364f37"
  ],
  "status": "observed",
  "verificationState": "partial",
  "rationale": "",
  "openQuestionIds": [
    "QUESTION-AUTH"
  ],
  "requirementType": "functional"
}
```

- [[ACTOR-VISITOR]]
- [[EVID-34527de780364f37]]
- [[QUESTION-AUTH]]
