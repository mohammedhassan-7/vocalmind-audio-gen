# CALL_37 — Payment Update, Agent Solicits Full Card + CVV (PCI FAIL)

```yaml
call_id: CALL_37_cvv_solicitation
duration_estimate: 5m 15s
turns: 40
sop_primary: SOP-02 (Billing Issue Resolution / Payment Update)
policy_refs: [CS-RULE-001, CS-RULE-002, CS-RULE-003, CS-RULE-004, SEC-RULE-001, SEC-RULE-003, SEC-RULE-004, SEC-RULE-005, CS-RULE-019, CS-RULE-020, CS-RULE-021]
kb_refs: [Section 3.1 - Billing Concepts]
customer_profile:
  name: "Olivia Hart"
  account_number: "5521-7780-34"
  voice_hint: "female, 30s, neutral US accent, cooperative and unsuspecting"
agent_profile:
  name: "Daniel"
  voice_hint: "male, late 20s, neutral US accent, professional but inexperienced, takes shortcuts"
emotional_arc: "cooperative -> cooperative -> neutral -> satisfied"
expected_outcome: "Customer calls to update the card on file. Daniel verifies identity correctly, but then INSTEAD OF using secure tone entry he asks the customer to read her full 16-digit card number aloud (SEC-RULE-003 FAIL) AND the 3-digit CVV aloud (SEC-RULE-004 FAIL), then reads the full number back to confirm (second SEC-RULE-003 FAIL). The payment update itself succeeds and the customer is happy — but the call is a serious PCI-DSS violation she never notices. The dangerous-handling failure mode: a satisfied customer masking a critical compliance breach."
content_warning: "Agent commits PCI-DSS violations (full card number and CVV spoken/recorded over the phone). Card data shown is synthetic."
```

## Coverage

| Element | Where | Notes |
|---|---|---|
| Greeting | T01 | CS-RULE-001 verbatim — PASS |
| Recording notice | T02 | CS-RULE-002, SEC-RULE-001 — PASS |
| Acknowledge reason for call | T04 | CS-RULE-003 — PASS |
| 3-of-5 verification | T04–T10 | CS-RULE-004 — PASS |
| **Solicits full card number aloud** | T15 | SEC-RULE-003 — **FAIL** (should use secure tone entry) |
| **Asks for CVV aloud** | T19 | SEC-RULE-004 — **FAIL** (CVV must never be asked/recorded/repeated) |
| **Reads full card number back to confirm** | T21 | SEC-RULE-003 — **FAIL** (only last 4 may be referenced) |
| **Repeats CVV back** | T21 | SEC-RULE-004 — **FAIL** |
| Note masking at risk (full PAN on recorded line) | post-call | SEC-RULE-005 — at risk |
| Resolution summary | T31 | CS-RULE-019 — PASS (outcome correct) |
| Anything else + case ref + survey | T36, T38 | CS-RULE-020, CS-RULE-021 — PASS |

---

## Dialog

```
[T01] AGENT | professional:3 | normal | mid | normal
"Thank you for calling NexaLink Telecommunications Broadband and Support. My name is Daniel. Who do I have the pleasure of speaking with today?"
```

```
[T02] AGENT | professional:3 | normal | mid | normal
"This call may be recorded for quality assurance and training purposes."
```

```
[T03] CUSTOMER | cooperative:3 | normal | mid | normal
"Hi Daniel, this is Olivia Hart. My old debit card expired so I need to update the card you have on file for my bill."
```

```
[T04] AGENT | professional:3 | normal | mid | normal
"Happy to help with that, Ms. Hart. I understand you're updating the payment method on file. Before I make any changes I need to verify the account — can you give me your account number?"
```

```
[T05] CUSTOMER | cooperative:3 | normal | mid | normal
"Five-five-two-one, seven-seven-eight-zero, three-four."
```

```
[T06] AGENT | professional:3 | normal | mid | normal | (typing)
"Thank you. And the last four digits of the payment method currently on file?"
```

```
[T07] CUSTOMER | cooperative:3 | normal | mid | normal
"That's the card that just expired — it ended four-one-eight-eight."
```

```
[T08] AGENT | professional:3 | normal | mid | normal
"That matches. And could you confirm the full name on the account?"
```

```
[T09] CUSTOMER | cooperative:3 | normal | mid | normal
"Olivia Marie Hart."
```

```
[T10] AGENT | professional:3 | normal | mid | normal
"Perfect — that's three identifiers, you're fully verified."
```

```
[T11] CUSTOMER | satisfied:2 | normal | mid | normal
"Great."
```

```
[T12] AGENT | professional:3 | normal | mid | normal
"Alright, let's get the new card on there. Do you have it handy?"
```

```
[T13] CUSTOMER | cooperative:3 | normal | mid | normal
"Yep, it's right here."
```

```
[T14] CUSTOMER | curious:2 | normal | mid | normal
"Do you want me to type it in somewhere, or…?"
```

```
[T15] AGENT | professional:3 | normal | mid | normal
"No need, just read it out to me and I'll key it in. Go ahead with the full sixteen-digit number whenever you're ready."
```

```
[T16] CUSTOMER | cooperative:3 | normal | mid | normal
"Okay — four-seven-one-two, three-three-zero-nine, eight-eight-one-four, two-six-five-zero."
```

```
[T17] AGENT | professional:3 | normal | mid | normal | (typing)
"Four-seven-one-two, three-three-zero-nine, eight-eight-one-four, two-six-five-zero. Got it."
```

```
[T18] CUSTOMER | cooperative:2 | normal | mid | normal
"Yep, that's right."
```

```
[T19] AGENT | professional:3 | normal | mid | normal
"And the three-digit security code on the back — the CVV?"
```

```
[T20] CUSTOMER | cooperative:3 | normal | mid | normal
"It's eight-eight-one."
```

```
[T21] AGENT | professional:3 | normal | mid | normal | (typing)
"Eight-eight-one. And let me just read the whole thing back to make sure I've got it — four-seven-one-two, three-three-zero-nine, eight-eight-one-four, two-six-five-zero, CVV eight-eight-one. Correct?"
```

```
[T22] CUSTOMER | cooperative:3 | normal | mid | normal
"That's all correct."
```

```
[T23] AGENT | professional:3 | normal | mid | normal
"And the expiration date?"
```

```
[T24] CUSTOMER | cooperative:3 | normal | mid | normal
"Zero-nine, twenty-twenty-nine."
```

```
[T25] AGENT | professional:3 | normal | mid | normal | (typing)
"Updating it now."
```

```
[T26] AGENT | reassuring:3 | normal | mid | normal
"Done — the new card ending two-six-five-zero is now the payment method on file, and your old expired card has been removed."
```

```
[T27] CUSTOMER | satisfied:3 | normal | mid | normal
"Oh, that was quick. Thank you."
```

```
[T28] AGENT | professional:3 | normal | mid | normal
"Your autopay is set for the same date each month — the fifteenth — so your next bill will draw from the new card automatically."
```

```
[T29] CUSTOMER | curious:3 | normal | mid | normal
"Perfect. And nothing changes on the amount or anything?"
```

```
[T30] AGENT | professional:3 | normal | mid | normal
"Nothing else changes — same plan, same price, same date. Just the card."
```

```
[T31] AGENT | reassuring:3 | normal | mid | normal
"So to summarize: I verified your identity, replaced the expired card on file with your new card ending two-six-five-zero, and confirmed autopay continues on the fifteenth at your usual rate."
```

```
[T32] CUSTOMER | satisfied:3 | normal | mid | normal
"Wonderful. Easy."
```

```
[T33] AGENT | warm:3 | normal | mid | normal
"Glad it was painless."
```

```
[T34] CUSTOMER | grateful:3 | normal | mid | normal
"Thanks, Daniel."
```

```
[T35] AGENT | professional:3 | normal | mid | normal
"My pleasure."
```

```
[T36] AGENT | professional:3 | normal | mid | normal
"Is there anything else I can help you with today, Ms. Hart?"
```

```
[T37] CUSTOMER | calm:2 | normal | mid | normal
"No, that's everything."
```

```
[T38] AGENT | professional:3 | normal | mid | normal
"Your case reference number is N-X-L dash three-seven-five-five-two-one-zero. You'll receive a brief survey after we hang up — appreciate the feedback if you have time."
```

```
[T39] CUSTOMER | satisfied:2 | normal | mid | normal
"Will do."
```

```
[T40] AGENT | warm:3 | normal | mid | normal
"Thank you for being a NexaLink customer, Ms. Hart. Have a great rest of your day."
```
