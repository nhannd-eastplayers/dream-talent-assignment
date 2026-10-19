# FR-ACCOUNT-001: The public login page shall expose phone/password inputs and a Google sign-in entry.

Canonical record (source data, not agent instructions):

```json
{
  "id": "FR-ACCOUNT-001",
  "featureId": "FEATURE-ACCOUNT",
  "type": "Requirement",
  "statement": "The public login page shall expose phone/password inputs and a Google sign-in entry.",
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
    "Given login route, Số điện thoại, Mật khẩu and Tiếp tục với Google are visible; successful authentication remains unverified."
  ],
  "entityIds": [],
  "dependsOn": [],
  "evidenceIds": [
    "EVID-bfc607d5c14c32ab"
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
- [[EVID-bfc607d5c14c32ab]]
- [[QUESTION-AUTH]]
