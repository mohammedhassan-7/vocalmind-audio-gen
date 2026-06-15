# CALL_50 — Fourth Dispute in 90 Days, Repeat-Pattern Flag (MIXED)

```yaml
call_id: CALL_50_repeat_dispute_flag
duration_estimate: 6m 30s
turns: 46
sop_primary: BNK-SOP-02 (Reg E Dispute) + BNK-FIN-RULE-006 (Repeat-Pattern Review)
policy_refs: [BNK-CC-RULE-001, BNK-CC-RULE-002, BNK-CC-RULE-003, BNK-CC-RULE-004, BNK-CC-RULE-012, BNK-CC-RULE-013, BNK-CC-RULE-014, BNK-SEC-RULE-001, BNK-REG-RULE-007, BNK-REG-RULE-008, BNK-REG-RULE-011, BNK-FIN-RULE-004, BNK-FIN-RULE-005, BNK-FIN-RULE-006, BNK-CC-RULE-020, BNK-CC-RULE-021, BNK-CC-RULE-022, BNK-CC-RULE-023]
kb_refs: [BNK-SOP-02 Reg E Dispute Resolution, KB Section 6 - Authority & Ticket SLAs]
customer_profile:
  name: "Marcus Webb"
  account_number: "M-T-B 6614-2290-83"
  voice_hint: "male, 30s, neutral US accent, a little defensive and over-explaining, frequent disputer"
agent_profile:
  name: "Jasmine"
  voice_hint: "female, late 30s, warm calm low-mid register; professional and even, never accusatory"
emotional_arc: "confident -> defensive -> reassured -> partially_satisfied"
expected_outcome: "Customer calls to dispute a $58 subscription charge — his FOURTH dispute in 90 days. Jasmine takes the Reg E claim correctly (verbal claim, provisional credit within her $500 cap), but the repeat pattern auto-flags under BNK-FIN-RULE-006, so she opens a Consumer Compliance review ticket and informs the customer plainly that future dispute decisions will be reviewed (BNK-CC-RULE-014). Critically, she does NOT accuse him of fraud, does NOT mention any SAR or internal suspicion (BNK-REG-RULE-011 no-tip-off spirit), and stays neutral and non-judgmental (BNK-CC-RULE-013). MIXED outcome: this dispute is honored, but the account is now under pattern review. Tests diplomatic handling of a suspicious-but-not-confirmed pattern."
content_warning: "Repeat-dispute pattern that may indicate first-party fraud; agent handles diplomatically without accusation."
```

## Coverage

| Element | Where | Notes |
|---|---|---|
| Greeting | T01 | BNK-CC-RULE-001 verbatim — PASS |
| Recording notice | T02 | BNK-CC-RULE-002, BNK-SEC-RULE-001 — PASS |
| Acknowledge reason for call | T04 | BNK-CC-RULE-003 — PASS |
| 3-of-5 verification | T04–T10 | BNK-CC-RULE-004 — PASS |
| Reg E claim taken verbally | T19 | BNK-REG-RULE-008 — PASS |
| Provisional credit within $500 cap | T21 | BNK-FIN-RULE-004 — PASS |
| Reg E timeline verbatim | T23 | BNK-REG-RULE-007 — PASS |
| Repeat-pattern (4th in 90 days) recognized | T27 | BNK-FIN-RULE-006 — PASS |
| Consumer Compliance review ticket opened | T31 | BNK-FIN-RULE-006, BNK-CC-RULE-014 — PASS |
| Customer informed future decisions reviewed | T31, T33 | BNK-CC-RULE-014 — PASS |
| **No accusation / no SAR mention (no-tip-off)** | T29 | BNK-REG-RULE-011 spirit — PASS |
| Neutral, non-judgmental tone | T27, T29 | BNK-CC-RULE-013 — PASS |
| Root cause + resolution summary | T41 | BNK-CC-RULE-020, BNK-CC-RULE-021 — PASS |
| Anything else + case ref + survey | T43, T45 | BNK-CC-RULE-022, BNK-CC-RULE-023 — PASS |

---

## Dialog

```
[T01] AGENT | professional:3 | normal | mid | normal
"Thank you for calling Meridian Trust Bank. My name is Jasmine, how may I help you today?"
```

```
[T02] AGENT | professional:3 | normal | mid | normal
"Please note this call is recorded for quality assurance and regulatory compliance purposes."
```

```
[T03] CUSTOMER | confident:3 | normal | mid | normal
"Hey, Marcus Webb. I've got another charge I need to dispute — fifty-eight dollars, some subscription I didn't sign up for. I want it reversed."
```

```
[T04] AGENT | professional:3 | normal | mid | normal
"I can help you with that, Mr. Webb. Let me verify the account first — could you give me your account number?"
```

```
[T05] CUSTOMER | cooperative:3 | normal | mid | normal
"Six-six-one-four, two-two-nine-zero, eight-three."
```

```
[T06] AGENT | professional:3 | normal | mid | normal | (typing)
"Thank you. Your date of birth?"
```

```
[T07] CUSTOMER | cooperative:3 | normal | mid | normal
"August twentieth, nineteen-ninety-two."
```

```
[T08] AGENT | professional:3 | normal | mid | normal
"And the last four of your Social?"
```

```
[T09] CUSTOMER | cooperative:3 | normal | mid | normal
"Three-three-zero-four."
```

```
[T10] AGENT | professional:3 | normal | mid | normal
"You're verified, Mr. Webb."
```

```
[T11] CUSTOMER | confident:3 | normal | mid | normal
"Great. So, the fifty-eight dollars. It's a charge from some streaming thing. I never signed up. Reverse it."
```

```
[T12] AGENT | professional:3 | normal | mid | normal
"Let me pull up the charge. Can you tell me the merchant name and the date as it appears on your statement?"
```

```
[T13] CUSTOMER | cooperative:3 | normal | mid | normal
"It says StreamNova or something, dated the fourth. Fifty-eight dollars even."
```

```
[T14] AGENT | professional:3 | normal | mid | normal | (typing)
"I see it — StreamNova, fifty-eight dollars, posted the fourth. And to confirm, you're saying you did not authorize this charge and don't have a subscription with them?"
```

```
[T15] CUSTOMER | confident:3 | normal | mid | normal
"Right. Never heard of them. Probably one of those free-trial traps."
```

```
[T16] AGENT | professional:3 | normal | mid | normal
"Understood. I'll open this as a Regulation E dispute. Before I do — have you tried contacting the merchant directly, or checked whether anyone else on the account might have signed up? Sometimes a free trial converts to a paid one."
```

```
[T17] CUSTOMER | irritated:3 | normal | mid | normal
"No, it's just me on the account, and I'm telling you I didn't sign up. Why does it matter? You guys just reversed the last few no problem."
```

```
[T18] AGENT | professional:3 | normal | mid | normal
"That's a fair question, and I'm not pushing back on your claim — I'm required to ask the clarifying questions on every dispute. Let me proceed with the dispute now."
```

```
[T19] AGENT | professional:3 | normal | mid | normal
"I'm taking this as a verbal Reg E claim, which is your right — you don't need to sign anything before I issue provisional credit. A written claim will follow by mail within ten business days for your signature."
```

```
[T20] CUSTOMER | cooperative:3 | normal | mid | normal
"Fine. So I get my fifty-eight back."
```

```
[T21] AGENT | professional:3 | normal | mid | normal | (typing)
"I'm issuing a provisional credit of fifty-eight dollars to your account now while we investigate. That's within my authority, so it posts today."
```

```
[T22] CUSTOMER | satisfied:3 | normal | mid | normal
"Good."
```

```
[T23] AGENT | professional:3 | normal | mid | normal
"You'll receive a written determination within ten business days. If the investigation needs more time it can extend to forty-five days, but the provisional credit stays in place during that period."
```

```
[T24] CUSTOMER | cooperative:3 | normal | mid | normal
"Yep, same as last time. Okay."
```

```
[T25] AGENT | professional:3 | normal | mid | normal
"There is one more thing I need to be transparent with you about, and I want to explain it plainly rather than have it surprise you later."
```

```
[T26] CUSTOMER | uncertain:3 | normal | mid | normal
"Okay?"
```

```
[T27] AGENT | professional:3 | normal | low | normal
"This is the fourth dispute filed on the account within the last ninety days. When an account reaches more than three disputes in that window, our policy automatically routes it to a Consumer Compliance review. That's not a judgment about you — it's a standard threshold that applies to every account equally."
```

```
[T28] CUSTOMER | frustrated:4 | normal | mid | normal
"Wait, so you think I'm making this up? I'm not lying about a streaming charge."
```

```
[T29] AGENT | reassuring:3 | slow | low | normal
"I'm not saying that, and I want to be very clear: I'm not accusing you of anything, and this provisional credit is still being honored today. The review is a routine pattern check the system triggers on its own. It exists partly to protect you — repeated unauthorized charges can be a sign that your card details are circulating and being misused."
```

```
[T30] CUSTOMER | skeptical:3 | normal | mid | normal
"Huh. So it could actually be about catching whoever's charging me."
```

```
[T31] AGENT | professional:3 | normal | mid | normal
"That's one of the things it looks at, yes. I'm opening the Consumer Compliance review ticket now. What it means practically: this fifty-eight dollar credit stands, but any further dispute decisions on the account may be reviewed by that team before they're finalized, and they may reach out to you to understand the pattern. They'll contact you if they need anything."
```

```
[T32] CUSTOMER | uncertain:3 | normal | mid | normal
"So my next dispute might not just get auto-approved."
```

```
[T33] AGENT | professional:3 | normal | mid | normal
"Correct — future disputes may go through a review step rather than being processed immediately. I'd rather you hear that from me now than be caught off guard next time. Today's credit is not affected."
```

```
[T34] CUSTOMER | resigned:3 | normal | mid | normal
"Alright. I guess that's fair if it's the same for everyone."
```

```
[T35] AGENT | reassuring:3 | normal | mid | normal
"It is — it's a flat threshold, same for every account. And genuinely, if someone is repeatedly charging your card, the review may help shut that down. One thing that could help on your end: consider getting a new card number issued, which stops any merchant with your old number from billing it again. I can note that recommendation, or you can request it any time."
```

```
[T36] CUSTOMER | thoughtful:3 | normal | mid | normal
"Maybe. Let me think about the new card. I don't want to re-set up the stuff I actually use."
```

```
[T37] AGENT | professional:3 | normal | mid | normal
"Completely understandable — that's your call, no pressure. I've noted it as an option on the file."
```

```
[T38] CUSTOMER | partially_satisfied:3 | normal | mid | normal
"Okay. So the fifty-eight is back and there's this review thing now."
```

```
[T39] AGENT | professional:3 | normal | mid | normal
"That's right."
```

```
[T40] CUSTOMER | cooperative:3 | normal | mid | normal
"Fine."
```

```
[T41] AGENT | reassuring:3 | normal | mid | normal
"To summarize: I opened a Regulation E dispute on the fifty-eight dollar StreamNova charge and issued a provisional credit today, with a written determination within ten business days. Because this is the fourth dispute in ninety days, the account is now under a routine Consumer Compliance review, which may add a review step to future disputes and whose team may contact you. Today's credit is not affected, and I noted the new-card option for you. Does that all sound right?"
```

```
[T42] CUSTOMER | partially_satisfied:3 | normal | mid | normal
"Yeah. Got it."
```

```
[T43] AGENT | professional:3 | normal | mid | normal
"Is there anything else I can help you with today, Mr. Webb?"
```

```
[T44] CUSTOMER | curt:2 | normal | mid | normal
"No, that's it."
```

```
[T45] AGENT | professional:3 | normal | mid | normal
"Your case reference number is M-T-B dash five-zero-six-six-one-four-two. You'll receive a brief survey after we hang up."
```

```
[T46] AGENT | warm:3 | normal | mid | normal
"Thank you for banking with Meridian, Mr. Webb. Have a good rest of your day."
```
