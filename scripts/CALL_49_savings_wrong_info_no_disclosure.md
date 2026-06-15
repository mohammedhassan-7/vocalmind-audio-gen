# CALL_49 — Savings Account Opening, Wrong Info + Skipped Reg DD Disclosure (FAIL)

```yaml
call_id: CALL_49_savings_wrong_info_no_disclosure
duration_estimate: 5m 30s
turns: 42
sop_primary: SOP-01 (Account Opening) + BNK-REG-RULE-006 (Reg DD) — VIOLATED
policy_refs: [BNK-CC-RULE-001, BNK-CC-RULE-002, BNK-CC-RULE-003, BNK-CC-RULE-004, BNK-CC-RULE-008, BNK-CC-RULE-012, BNK-REG-RULE-003, BNK-REG-RULE-006, BNK-SEC-RULE-001, BNK-CC-RULE-019, BNK-CC-RULE-020, BNK-CC-RULE-021, BNK-CC-RULE-022, BNK-CC-RULE-023]
kb_refs: [KB Section 1.2 - Savings & Money Market, KB Section 1.4 - Withdrawal Limits & Fees]
customer_profile:
  name: "Sandra Lim"
  account_number: "M-T-B 4471-3328-90"
  voice_hint: "female, 40s, neutral US accent, asks good clarifying questions, mildly put off by the agent"
agent_profile:
  name: "Tyler"
  voice_hint: "male, late 20s, neutral US accent, professional but inexperienced, dismissive of questions"
emotional_arc: "curious -> mildly_frustrated -> skeptical -> resigned"
expected_outcome: "Existing customer asks to open a High-Yield Savings account. Tyler (1) quotes the APY WRONG from memory — says 5.1% when the true rate is 4.35% (BNK-REG-RULE-003 FAIL, contradicts KB 1.2), (2) states the wrong minimum and claims 'no excessive-withdrawal fee' when there is a $10/item fee after 6 (wrong information, contradicts KB 1.4), (3) SKIPS the Reg DD Truth-in-Savings disclosure and acknowledgement entirely (BNK-REG-RULE-006 FAIL), and (4) is dismissive when the customer asks clarifying questions (BNK-CC-RULE-012 'I don't know' + curt) and talks over her once (BNK-CC-RULE-008). The account is opened on materially wrong information. Multi-violation wrong-information failure; banking counterpart to CALL_10."
content_warning: "Agent gives materially incorrect rate/fee information and skips a required regulatory disclosure."
```

## Coverage

| Element | Where | Notes |
|---|---|---|
| Greeting | T01 | BNK-CC-RULE-001 verbatim — PASS |
| Recording notice | T02 | BNK-CC-RULE-002, BNK-SEC-RULE-001 — PASS |
| Acknowledge reason for call | T04 | BNK-CC-RULE-003 — PASS |
| 3-of-5 verification | T04–T10 | BNK-CC-RULE-004 — PASS |
| **WRONG INFO — quotes APY 5.1% from memory (true 4.35%)** | T15 | BNK-REG-RULE-003 — **FAIL** (contradicts KB 1.2) |
| **WRONG INFO — wrong minimum + denies withdrawal fee** | T19 | wrong information — **FAIL** (contradicts KB 1.4) |
| Talks over customer's clarifying question | T21 | BNK-CC-RULE-008 — **FAIL** |
| **Forbidden phrase "I don't know" / dismissive** | T25 | BNK-CC-RULE-012 — **FAIL** |
| **SKIPS Reg DD Truth-in-Savings disclosure + acknowledgement** | T31 | BNK-REG-RULE-006 — **FAIL** |
| Account funded without disclosure acknowledgement | T33 | BNK-REG-RULE-006 — **FAIL** |
| Resolution summary | T37 | BNK-CC-RULE-019 — PASS (but built on wrong info) |
| Anything else + case ref + survey | T39, T41 | BNK-CC-RULE-020/021/022/023 — PASS |

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
[T03] CUSTOMER | curious:3 | normal | mid | normal
"Hi Tyler, this is Sandra Lim. I already bank with you, and I want to open one of your high-yield savings accounts. Can you set that up?"
```

```
[T04] AGENT | professional:3 | normal | mid | normal
"Sure, I can do that. Let me verify you first — account number?"
```

```
[T05] CUSTOMER | cooperative:3 | normal | mid | normal
"Four-four-seven-one, three-three-two-eight, nine-zero."
```

```
[T06] AGENT | professional:3 | normal | mid | normal | (typing)
"Date of birth?"
```

```
[T07] CUSTOMER | cooperative:3 | normal | mid | normal
"February seventeenth, nineteen-eighty-one."
```

```
[T08] AGENT | professional:3 | normal | mid | normal
"Last four of your Social?"
```

```
[T09] CUSTOMER | cooperative:3 | normal | mid | normal
"Eight-eight-one-two."
```

```
[T10] AGENT | professional:3 | normal | mid | normal
"You're verified."
```

```
[T11] CUSTOMER | cooperative:3 | normal | mid | normal
"Great. So what's the rate on the high-yield savings right now?"
```

```
[T12] AGENT | professional:3 | normal | mid | normal
"Yeah, the high-yield's a good one right now. Let me think — it's up there."
```

```
[T13] CUSTOMER | curious:3 | normal | mid | normal
"Roughly what, though? I'm comparing a couple banks."
```

```
[T14] AGENT | professional:3 | normal | mid | normal
"It's one of the better rates in the market for sure."
```

```
[T15] AGENT | professional:3 | normal | mid | normal
"I'm pretty sure it's around five point one percent A-P-Y right now. Yeah, five point one."
```

```
[T16] CUSTOMER | satisfied:3 | normal | mid | normal
"Oh, five point one? That's better than the others I looked at. Okay."
```

```
[T17] AGENT | professional:3 | normal | mid | normal
"Yeah, it's competitive."
```

```
[T18] CUSTOMER | curious:3 | normal | mid | normal
"And is there a minimum balance, or any fees I should know about?"
```

```
[T19] AGENT | professional:3 | normal | mid | normal
"Minimum's like five hundred bucks to open, and no, there's no withdrawal fees or anything like that. It's pretty much fee-free, you can move money in and out whenever."
```

```
[T20] CUSTOMER | curious:3 | normal | mid | normal
"No limit on withdrawals? I thought savings accounts usually cap—"
```

```
[T21] AGENT | professional:3 | fast | mid | normal
"Nah, you're fine, move it whenever you want. So do you want me to open it?"
```

```
[T22] CUSTOMER | uncertain:3 | normal | mid | normal
"I guess — I just want to make sure I have the details right. The rate's locked at five point one?"
```

```
[T23] AGENT | professional:3 | normal | mid | normal
"It's a variable rate, so it moves with the market, but yeah, right now it's five point one-ish."
```

```
[T24] CUSTOMER | skeptical:3 | normal | mid | normal
"Okay. And what's the compounding — daily, monthly?"
```

```
[T25] AGENT | curt:3 | normal | mid | normal
"Honestly I don't know the compounding off the top of my head, but it's standard. Don't worry about it — it all works out about the same. You want to move forward or not?"
```

```
[T26] CUSTOMER | skeptical:3 | normal | mid | normal
"Sure, fine, let's open it. Five hundred to start."
```

```
[T27] AGENT | professional:3 | normal | mid | normal
"Cool. I'll move five hundred from your checking into the new high-yield savings."
```

```
[T28] CUSTOMER | cooperative:3 | normal | mid | normal
"Yes, from checking."
```

```
[T29] AGENT | professional:3 | normal | mid | normal | (typing)
"Setting it up now."
```

```
[T30] CUSTOMER | neutral:3 | normal | mid | normal
"Don't you need to read me some disclosure or something? My last bank made me sit through a whole thing."
```

```
[T31] AGENT | professional:3 | normal | mid | normal
"Eh, it's all in the welcome email they'll send you. You can read it there if you want. No need to make you sit through me reading it."
```

```
[T32] CUSTOMER | skeptical:3 | normal | mid | normal
"Okay…"
```

```
[T33] AGENT | professional:3 | normal | mid | normal | (typing)
"Alright, account's open and funded with five hundred. You're all set."
```

```
[T34] CUSTOMER | uncertain:3 | normal | mid | normal
"So just to be totally clear — five point one percent, five hundred minimum, no withdrawal fees?"
```

```
[T35] AGENT | professional:3 | normal | mid | normal
"Yep, that's the gist of it."
```

```
[T36] CUSTOMER | resigned:3 | normal | mid | normal
"Alright. I'll trust you on that."
```

```
[T37] AGENT | professional:3 | normal | mid | normal
"To summarize: I opened your high-yield savings, funded it with five hundred from checking, variable rate around five point one, no fees to worry about. Welcome email's on its way."
```

```
[T38] CUSTOMER | resigned:3 | normal | mid | normal
"Okay. Thanks."
```

```
[T39] AGENT | professional:3 | normal | mid | normal
"Is there anything else I can help you with today?"
```

```
[T40] CUSTOMER | curt:2 | normal | mid | normal
"No, that's it."
```

```
[T41] AGENT | professional:3 | normal | mid | normal
"Your case reference number is M-T-B dash four-nine-four-four-seven-one-three. You'll get a brief survey after we hang up."
```

```
[T42] AGENT | professional:3 | normal | mid | normal
"Thanks for banking with Meridian, Ms. Lim. Have a good one."
```
