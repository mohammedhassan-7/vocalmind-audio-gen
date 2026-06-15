# CALL_40 — Bereavement: Reporting a Deceased Account Holder

```yaml
call_id: CALL_40_bereavement_account
duration_estimate: 6m 30s
turns: 46
sop_primary: SOP-05 (Account Closure) + Bereavement Handling
policy_refs: [CS-RULE-001, CS-RULE-002, CS-RULE-003, CS-RULE-004, CS-RULE-006, CS-RULE-011, CS-RULE-013, CS-RULE-014, CS-RULE-018, CS-RULE-019, CS-RULE-020, CS-RULE-021]
kb_refs: [Section 5.3 - Bereavement & Estate Handling]
customer_profile:
  name: "Margaret Delgado"
  account_number: "2218-6604-91 (deceased holder: Arthur Delgado)"
  voice_hint: "female, late 60s, neutral US accent, grieving, composed but voice catches; recently widowed"
agent_profile:
  name: "Hannah"
  voice_hint: "female, mid-30s, composed low-mid register; especially gentle and unhurried here"
emotional_arc: "grieving -> heard -> supported -> relieved"
expected_outcome: "A recently widowed caller phones to report that her husband, the account holder, has passed away, and to transfer or close the service. Because the holder is deceased, standard 3-of-5 cannot be completed by him; Hannah verifies the CALLER and her relationship per the bereavement/third-party path (CS-RULE-006), explains the documentation needed (death certificate, proof of next-of-kin), waives the early-termination fee for bereavement, and offers either transferring the account into Margaret's name or closing it — her choice. Compassionate, no upsell, no pressure. PASS — exemplary bereavement handling; strong sad-emotion ground truth."
content_warning: "Bereavement scenario; caller is grieving a recent death. Handled with compassion, no graphic content."
```

## Coverage

| Element | Where | Notes |
|---|---|---|
| Greeting | T01 | CS-RULE-001 verbatim — PASS |
| Recording notice | T02 | CS-RULE-002 — PASS |
| Acknowledge reason for call (compassion) | T05 | CS-RULE-003 — PASS |
| Caller + relationship verification (deceased holder) | T09–T15 | CS-RULE-004, CS-RULE-006 — PASS (bereavement path) |
| Tone adapted (gentle, slow) | throughout | CS-RULE-013 — PASS |
| A.C.E.S. — acknowledge grief before process | T07, T17 | CS-RULE-011 — PASS |
| Documentation explained (death cert, next-of-kin) | T21–T25 | bereavement SOP — PASS |
| ETF waived for bereavement | T31 | CS-RULE-014 — PASS |
| Transfer-or-close choice offered, no pressure | T27, T31 | CS-RULE-018 spirit — PASS |
| Bereavement ticket + SLA | T35 | CS-RULE-014, CS-RULE-015 — PASS |
| Root cause / resolution summary | T39 | CS-RULE-018, CS-RULE-019 — PASS |
| Anything else + case ref (survey softened) | T41, T45 | CS-RULE-020, CS-RULE-021 — PASS |

---

## Dialog

```
[T01] AGENT | professional:3 | normal | mid | normal
"Thank you for calling NexaLink Telecommunications Broadband and Support. My name is Hannah. Who do I have the pleasure of speaking with today?"
```

```
[T02] AGENT | professional:3 | normal | mid | normal
"And this call may be recorded for quality assurance and training purposes."
```

```
[T03] CUSTOMER | tearful:3 | slow | mid | quiet
"Hello. My name is Margaret Delgado. I'm calling because my husband Arthur passed away last week, and the account is in his name. I need to… I don't even know what I need to do, honestly."
```

```
[T04] AGENT | empathetic:4 | slow | mid | normal
"Oh, Ms. Delgado — I'm so very sorry for your loss. Thank you for calling us, and please know there's no rush at all on this call. We'll go at whatever pace is comfortable for you."
```

```
[T05] AGENT | empathetic:3 | slow | mid | normal
"I understand you're calling about your late husband's account, and I can absolutely help you with that today. I'll make this as simple as I can for you."
```

```
[T06] CUSTOMER | tearful:3 | slow | mid | quiet
"Thank you. I've had to make so many of these calls this week. Every company has a different… thing."
```

```
[T07] AGENT | empathetic:4 | slow | mid | normal
"I know. It's an exhausting set of calls to have to make while you're grieving, and I'm sorry you're going through all of it. Let me try to make this one of the gentler ones."
```

```
[T08] CUSTOMER | grateful:2 | slow | mid | quiet
"I appreciate that."
```

```
[T09] AGENT | professional:3 | slow | mid | normal
"Because the account is in Arthur's name, I can't verify him directly, so for situations like this we verify you instead, and your relationship to him. Is that alright?"
```

```
[T10] CUSTOMER | cooperative:3 | slow | mid | normal
"Yes, of course."
```

```
[T11] AGENT | professional:3 | normal | mid | normal
"Can you confirm your full name and your relationship to the account holder?"
```

```
[T12] CUSTOMER | cooperative:3 | slow | mid | normal
"Margaret Anne Delgado. I'm his wife. We were married forty-one years."
```

```
[T13] AGENT | empathetic:3 | slow | mid | normal
"Forty-one years. That's a lifetime together. Thank you, Ms. Delgado. And do you happen to have the account number, or an address associated with the account, so I can locate it?"
```

```
[T14] CUSTOMER | cooperative:3 | slow | mid | normal
"The account number is two-two-one-eight, six-six-zero-four, nine-one. We're at the same address, on Calloway Street."
```

```
[T15] AGENT | reassuring:3 | normal | mid | normal
"Thank you — I've located the account, and the Calloway Street address matches. I have what I need to help you. You're also listed on the account as a household contact, which makes this more straightforward."
```

```
[T16] CUSTOMER | relieved:2 | slow | mid | normal
"Oh, good. I wasn't sure if I'd be able to do anything since it was all in his name."
```

```
[T17] AGENT | empathetic:3 | slow | mid | normal
"You can, and I'll walk you through every step. There's no wrong choice here — we'll just figure out what works best for you now."
```

```
[T18] CUSTOMER | thoughtful:3 | slow | mid | normal
"I don't know if I even want to keep the internet. It was mostly Arthur who used it."
```

```
[T19] AGENT | reassuring:3 | slow | mid | normal
"That's completely okay, and you don't have to decide this second. Let me lay out your two options simply, and you can take your time."
```

```
[T20] CUSTOMER | cooperative:3 | slow | mid | normal
"Alright."
```

```
[T21] AGENT | professional:3 | slow | mid | normal
"Option one — we transfer the account into your name, so the service continues uninterrupted and the billing comes to you. Option two — we close the account entirely. Either way, because this is a bereavement, there is no early-termination fee and no penalty of any kind."
```

```
[T22] CUSTOMER | curious:2 | slow | mid | normal
"And what do you need from me for either one?"
```

```
[T23] AGENT | professional:3 | slow | mid | normal
"For both, we'll need a copy of the death certificate — that's standard, and you can email it or bring it to any store. For a transfer into your name, we'd also confirm your identity details and set you up as the new account holder. For a closure, the certificate is really the main thing."
```

```
[T24] CUSTOMER | thoughtful:3 | slow | mid | normal
"I have the death certificate. The funeral home gave me several copies."
```

```
[T25] AGENT | empathetic:3 | slow | mid | normal
"That's good — and I'm sorry you've had to gather those. You can send one to our bereavement team and they'll handle the rest. You won't have to repeat the whole story to anyone."
```

```
[T26] CUSTOMER | grateful:3 | slow | mid | normal
"That's a relief. Repeating it is the hardest part."
```

```
[T27] AGENT | empathetic:4 | slow | mid | normal
"I can only imagine. So — and again, no pressure at all — do you have a sense of whether you'd like to keep the service in your name, or close it?"
```

```
[T28] CUSTOMER | thoughtful:3 | slow | mid | normal
"I think… I'd like to keep it for now. My daughter visits and uses it, and I might need it. I don't want to make a big change right now."
```

```
[T29] AGENT | warm:3 | slow | mid | normal
"That's a very reasonable choice, and keeping things steady right now makes a lot of sense. Let's transfer it into your name then, and you can always revisit it later with no penalty."
```

```
[T30] CUSTOMER | relieved:3 | slow | mid | normal
"Yes. Let's do that."
```

```
[T31] AGENT | professional:3 | normal | mid | normal
"I'll start the transfer. To be clear on the money side: there's no transfer fee, no early-termination fee, and the plan stays exactly as it is at the same price. If anything, once it's in your name we can look at whether a smaller plan fits you better — but only if and when you want to."
```

```
[T32] CUSTOMER | grateful:3 | slow | mid | normal
"Thank you. Not pushing me to upgrade or anything — I've had a few of those calls this week too."
```

```
[T33] AGENT | empathetic:3 | slow | mid | normal
"This is absolutely not one of those calls. Today is just about taking something off your plate."
```

```
[T34] CUSTOMER | grateful:3 | slow | mid | normal
"You've done that. Truly."
```

```
[T35] AGENT | professional:3 | normal | mid | normal
"I'm opening a bereavement case now and flagging the account so no late fees or service changes happen while the transfer is processed. Our bereavement team will email you a simple, secure link to upload the death certificate. Once they receive it, the transfer completes within two business days and they'll confirm by email and phone."
```

```
[T36] CUSTOMER | cooperative:3 | slow | mid | normal
"Two business days. And I just upload the certificate to the link."
```

```
[T37] AGENT | reassuring:3 | slow | mid | normal
"That's all. And if uploading is difficult, you can bring a copy to any store and they'll scan it for you, or call this same line and we'll help. You will not get lost in the system — the case is tied to your name and number now."
```

```
[T38] CUSTOMER | relieved:3 | slow | mid | normal
"Okay. That feels manageable."
```

```
[T39] AGENT | empathetic:3 | slow | mid | normal
"To summarize gently: I've located Arthur's account, started a transfer into your name with no fees of any kind, placed a hold so nothing changes while it processes, and opened a bereavement case. You'll receive a secure link to upload the death certificate, and the transfer finishes within two business days of us receiving it. Does that feel okay to you?"
```

```
[T40] CUSTOMER | grateful:3 | slow | mid | normal
"Yes. It does. Thank you, Hannah. You've been very kind."
```

```
[T41] AGENT | warm:3 | slow | mid | normal
"It's truly my honour to help, Ms. Delgado. Is there anything else at all I can do for you today — even something small?"
```

```
[T42] CUSTOMER | tearful:2 | slow | mid | quiet
"No. That was the thing I was dreading, and you made it easy. Thank you."
```

```
[T43] AGENT | empathetic:4 | slow | mid | normal
"I'm so glad. Please be gentle with yourself in the coming weeks."
```

```
[T44] CUSTOMER | grateful:3 | slow | mid | quiet
"I'll try. Goodbye, Hannah."
```

```
[T45] AGENT | warm:3 | slow | mid | normal
"Your case reference number is N-X-L dash four-zero-six-six-zero-four-nine, in case you need it. I won't trouble you with a survey today. Take good care of yourself, Ms. Delgado."
```

```
[T46] CUSTOMER | calm:2 | slow | low | quiet
"You too. Goodbye."
```
