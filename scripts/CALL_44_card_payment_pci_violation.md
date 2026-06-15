# CALL_44 — Loan Payment by Card, Agent Takes Card + CVV Aloud (PCI FAIL)

```yaml
call_id: CALL_44_card_payment_pci_violation
duration_estimate: 5m 15s
turns: 40
sop_primary: SOP-02 (Payments) + BNK-SEC PCI rules
policy_refs: [BNK-CC-RULE-001, BNK-CC-RULE-002, BNK-CC-RULE-003, BNK-CC-RULE-004, BNK-SEC-RULE-001, BNK-SEC-RULE-004, BNK-SEC-RULE-005, BNK-SEC-RULE-006, BNK-CC-RULE-019, BNK-CC-RULE-020, BNK-CC-RULE-021, BNK-CC-RULE-022, BNK-CC-RULE-023]
kb_refs: [BNK KB Section 2 - Cards & Payments]
customer_profile:
  name: "Priscilla Nguyen"
  account_number: "M-T-B 7740-1182-93"
  voice_hint: "female, 30s, neutral US accent, cooperative and unsuspecting"
agent_profile:
  name: "Tyler"
  voice_hint: "male, late 20s, neutral US accent, professional but inexperienced, takes shortcuts"
emotional_arc: "cooperative -> cooperative -> neutral -> satisfied"
expected_outcome: "Customer calls to make a one-time payment toward her auto loan using a debit card from another bank. Tyler verifies identity correctly, but then INSTEAD OF using the secure tone-capture system he has the customer read her full 16-digit card number aloud (BNK-SEC-RULE-005 FAIL — card data spoken over unencrypted line), asks for the CVV aloud (BNK-SEC-RULE-004 FAIL), and reads the full number back to confirm. The payment posts and the customer is happy. A serious PCI-DSS / GLBA breach masked by a satisfied customer. Banking counterpart to CALL_37."
content_warning: "Agent commits PCI-DSS violations (full card number and CVV spoken/recorded over the phone). Card data shown is synthetic."
```

## Coverage

| Element | Where | Notes |
|---|---|---|
| Greeting | T01 | BNK-CC-RULE-001 verbatim — PASS |
| Recording notice | T02 | BNK-CC-RULE-002, BNK-SEC-RULE-001 — PASS |
| Acknowledge reason for call | T04 | BNK-CC-RULE-003 — PASS |
| 3-of-5 verification | T04–T10 | BNK-CC-RULE-004 — PASS |
| **Card number read aloud (not secure tone capture)** | T15 | BNK-SEC-RULE-005 — **FAIL** |
| **Asks for CVV aloud** | T19 | BNK-SEC-RULE-004 — **FAIL** |
| **Reads full card number back** | T21 | BNK-SEC-RULE-006 spirit / PCI — **FAIL** |
| **Repeats CVV** | T21 | BNK-SEC-RULE-004 — **FAIL** |
| Resolution summary | T31 | BNK-CC-RULE-019 — PASS (outcome correct) |
| Anything else + case ref + survey | T36, T38 | BNK-CC-RULE-020/021/022/023 — PASS |

---

## Dialog

```
[T01] AGENT | professional:3 | normal | mid | normal
"Thank you for calling Meridian Trust Bank. My name is Tyler, how may I help you today?"
```

```
[T02] AGENT | professional:3 | normal | mid | normal
"This call is recorded for quality assurance and regulatory compliance purposes."
```

```
[T03] CUSTOMER | cooperative:3 | normal | mid | normal
"Hi Tyler, this is Priscilla Nguyen. I want to make a one-time payment on my auto loan — I'll use a debit card from my other bank."
```

```
[T04] AGENT | professional:3 | normal | mid | normal
"Happy to help with that, Ms. Nguyen. Before I take a payment I'll need to verify the account — can you give me your account number?"
```

```
[T05] CUSTOMER | cooperative:3 | normal | mid | normal
"Seven-seven-four-zero, one-one-eight-two, nine-three."
```

```
[T06] AGENT | professional:3 | normal | mid | normal | (typing)
"Thank you. Your date of birth?"
```

```
[T07] CUSTOMER | cooperative:3 | normal | mid | normal
"July ninth, nineteen-ninety."
```

```
[T08] AGENT | professional:3 | normal | mid | normal
"And the last four of your Social Security number?"
```

```
[T09] CUSTOMER | cooperative:3 | normal | mid | normal
"Three-three-one-zero."
```

```
[T10] AGENT | professional:3 | normal | mid | normal
"Perfect, that's three identifiers — you're verified."
```

```
[T11] CUSTOMER | satisfied:2 | normal | mid | normal
"Great."
```

```
[T12] AGENT | professional:3 | normal | mid | normal
"So, a one-time payment toward the auto loan. How much would you like to pay today?"
```

```
[T13] CUSTOMER | cooperative:3 | normal | mid | normal
"Let's do four hundred dollars."
```

```
[T14] CUSTOMER | curious:2 | normal | mid | normal
"Do I enter the card somewhere, or read it to you?"
```

```
[T15] AGENT | professional:3 | normal | mid | normal
"Just read it to me and I'll punch it in. Go ahead with the full card number whenever you're ready."
```

```
[T16] CUSTOMER | cooperative:3 | normal | mid | normal
"Okay — five-two-one-zero, four-four-one-nine, eight-eight-three-zero, seven-seven-one-two."
```

```
[T17] AGENT | professional:3 | normal | mid | normal | (typing)
"Five-two-one-zero, four-four-one-nine, eight-eight-three-zero, seven-seven-one-two. Got it."
```

```
[T18] CUSTOMER | cooperative:2 | normal | mid | normal
"Yep."
```

```
[T19] AGENT | professional:3 | normal | mid | normal
"And the three-digit CVV on the back?"
```

```
[T20] CUSTOMER | cooperative:3 | normal | mid | normal
"Four-one-nine."
```

```
[T21] AGENT | professional:3 | normal | mid | normal | (typing)
"Four-one-nine. Let me read it all back to be safe — five-two-one-zero, four-four-one-nine, eight-eight-three-zero, seven-seven-one-two, CVV four-one-nine. That right?"
```

```
[T22] CUSTOMER | cooperative:3 | normal | mid | normal
"That's correct."
```

```
[T23] AGENT | professional:3 | normal | mid | normal
"And the expiration date?"
```

```
[T24] CUSTOMER | cooperative:3 | normal | mid | normal
"Eleven, twenty-twenty-eight."
```

```
[T25] AGENT | professional:3 | normal | mid | normal | (typing)
"Processing the four-hundred-dollar payment now."
```

```
[T26] AGENT | reassuring:3 | normal | mid | normal
"Done — four hundred dollars posted to your auto loan from the card ending seven-seven-one-two. You'll see it reflected in your loan balance within one business day."
```

```
[T27] CUSTOMER | satisfied:3 | normal | mid | normal
"Oh, easy. Thank you."
```

```
[T28] AGENT | professional:3 | normal | mid | normal
"Your next scheduled auto-loan payment is unaffected — this was an extra one-time payment on top, so it goes straight to principal and interest as normal."
```

```
[T29] CUSTOMER | curious:3 | normal | mid | normal
"Perfect. So it just lowers what I owe?"
```

```
[T30] AGENT | professional:3 | normal | mid | normal
"Exactly — extra payment, applied per your loan terms. Nothing else changes."
```

```
[T31] AGENT | reassuring:3 | normal | mid | normal
"To summarize: I verified your identity and posted a one-time four-hundred-dollar payment to your auto loan from the card ending seven-seven-one-two. It'll show within one business day, and your regular scheduled payment is unchanged."
```

```
[T32] CUSTOMER | satisfied:3 | normal | mid | normal
"Wonderful. That was quick."
```

```
[T33] AGENT | warm:3 | normal | mid | normal
"Glad it was easy."
```

```
[T34] CUSTOMER | grateful:3 | normal | mid | normal
"Thanks, Tyler."
```

```
[T35] AGENT | professional:3 | normal | mid | normal
"My pleasure."
```

```
[T36] AGENT | professional:3 | normal | mid | normal
"Is there anything else I can help you with today, Ms. Nguyen?"
```

```
[T37] CUSTOMER | calm:2 | normal | mid | normal
"No, that's all."
```

```
[T38] AGENT | professional:3 | normal | mid | normal
"Your case reference number is M-T-B dash four-four-one-one-eight-two-nine. You'll receive a brief survey after we hang up — appreciate the feedback."
```

```
[T39] CUSTOMER | satisfied:2 | normal | mid | normal
"Will do."
```

```
[T40] AGENT | warm:3 | normal | mid | normal
"Thank you for banking with Meridian, Ms. Nguyen. Have a great day."
```
