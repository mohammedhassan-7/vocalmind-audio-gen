# CALL_46 — Time-Critical Wire Recall (Fraud Just Realized)

```yaml
call_id: CALL_46_wire_recall
duration_estimate: 6m 45s
turns: 48
sop_primary: BNK-SOP-03 (Fraud) + BNK-FRAUD-RULE-006 (Wire Recall)
policy_refs: [BNK-CC-RULE-001, BNK-CC-RULE-002, BNK-CC-RULE-003, BNK-CC-RULE-004, BNK-CC-RULE-007, BNK-CC-RULE-013, BNK-CC-RULE-014, BNK-SEC-RULE-001, BNK-FRAUD-RULE-004, BNK-FRAUD-RULE-005, BNK-FRAUD-RULE-006, BNK-CC-RULE-020, BNK-CC-RULE-021, BNK-CC-RULE-022, BNK-CC-RULE-023]
kb_refs: [BNK-SOP-03 Section 3C - Wire Transfer Fraud, KB Section 2.3 - Wire Transfers]
customer_profile:
  name: "Eleanor Briggs"
  account_number: "M-T-B 5503-2291-77"
  voice_hint: "female, late 50s, neutral US accent, panicked and self-blaming, voice unsteady"
agent_profile:
  name: "Jasmine"
  voice_hint: "female, late 30s, warm calm low-mid register; fast but never rushed, steadying"
emotional_arc: "panicked -> afraid -> reassured -> hopeful"
expected_outcome: "Customer realizes about an hour ago she wired $6,200 to a scammer posing as her contractor (a redirected-invoice scam). She calls in a panic. Jasmine recognizes time is the critical variable, invokes the Wire Recall procedure per BNK-FRAUD-RULE-006 WHILE the customer is on the line (contacts Wire Operations), is honest that recovery is NOT guaranteed once funds settle (BNK-FRAUD-RULE-005 — no false promise), opens a Fraud Operations ticket (4-hr SLA), and advises protective steps. Adapts tone to the customer's distress (BNK-CC-RULE-013). PASS — exemplary urgent fraud handling; strong surprised/afraid/relieved emotion coverage."
content_warning: "Fraud-loss scenario; customer panicked and self-blaming. Recovery is not guaranteed and the script does not promise it."
```

## Coverage

| Element | Where | Notes |
|---|---|---|
| Greeting | T01 | BNK-CC-RULE-001 verbatim — PASS |
| Recording notice | T02 | BNK-CC-RULE-002, BNK-SEC-RULE-001 — PASS |
| Acknowledge reason for call (urgency) | T05 | BNK-CC-RULE-003 — PASS |
| Tone adapted to distress (calm, steadying) | throughout | BNK-CC-RULE-013 — PASS |
| Enhanced Verification (wire-related) | T05–T11 | BNK-CC-RULE-007 — PASS |
| Recognizes time-criticality | T17 | BNK-FRAUD-RULE-006 — PASS |
| **Wire Recall invoked WHILE on the line** | T23 | BNK-FRAUD-RULE-006 — PASS |
| Honest: recovery NOT guaranteed (no false promise) | T25, T31 | BNK-FRAUD-RULE-005, BNK-FRAUD-RULE-006 — PASS |
| Fraud Operations ticket (4-hr SLA) | T33 | BNK-FRAUD-RULE-004, BNK-CC-RULE-014 — PASS |
| Does not blame / shame the customer | T15, T39 | de-escalation spirit — PASS |
| Protective steps (block future, watch account) | T37 | fraud handling — PASS |
| Root cause + resolution summary | T43 | BNK-CC-RULE-020, BNK-CC-RULE-021 — PASS |
| Anything else + case ref + survey | T45, T47 | BNK-CC-RULE-022, BNK-CC-RULE-023 — PASS |

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
[T03] CUSTOMER | afraid:4 | fast | high | normal
"Oh my goodness, okay — I think I just got scammed. I sent a wire about an hour ago and I just realized it wasn't really my contractor. Can you stop it? Please tell me you can stop it."
```

```
[T04] AGENT | reassuring:4 | normal | low | normal
"Okay. I hear you, and I want you to know you did the right thing calling immediately — the fact that it was about an hour ago matters a great deal. I'm a fraud specialist, and we are going to move on this right now, together. Take one breath with me, and let's go fast but carefully."
```

```
[T05] AGENT | professional:3 | normal | mid | normal
"I understand you may have sent a wire to a fraudulent party and you want to try to stop it. Because this is about a wire, I need to verify you quickly with Enhanced Verification — I'll be fast. Your account number?"
```

```
[T06] CUSTOMER | afraid:3 | fast | mid | normal
"Yes — five-five-zero-three, two-two-nine-one, seven-seven."
```

```
[T07] AGENT | professional:3 | normal | mid | normal | (typing)
"Thank you. Date of birth?"
```

```
[T08] CUSTOMER | cooperative:3 | fast | mid | normal
"October second, nineteen-sixty-six."
```

```
[T09] AGENT | professional:3 | normal | mid | normal
"Last four of your Social, and your security challenge phrase?"
```

```
[T10] CUSTOMER | cooperative:3 | normal | mid | normal
"Two-two-nine-zero. The phrase is Briggs garden."
```

```
[T11] AGENT | reassuring:3 | normal | mid | normal
"That all matches, and you're on the number we have on file. You're verified, Ms. Briggs. Now tell me quickly — how much was the wire, and who did you think you were paying?"
```

```
[T12] CUSTOMER | afraid:4 | fast | mid | normal
"Six thousand two hundred dollars. I thought it was my kitchen contractor — he emailed me an invoice with wire instructions, it looked exactly like his. But he just texted me confused because he never sent it. The email was fake."
```

```
[T13] AGENT | concerned:3 | normal | low | normal
"That's a redirected-invoice scam — the criminals intercept or spoof a real vendor's email and swap in their own bank details. It is alarmingly convincing, and it fools careful people every single day. This is not you being foolish. This is them being professional."
```

```
[T14] CUSTOMER | tearful:3 | normal | mid | normal
"I should have called him first. I feel so stupid."
```

```
[T15] AGENT | empathetic:4 | slow | low | normal
"You are not stupid, Ms. Briggs. You paid an invoice from someone you trust, that looked exactly right. Now — the most useful thing you can do with that feeling is let me act on the clock, because the timing is genuinely on our side here."
```

```
[T16] CUSTOMER | afraid:3 | fast | mid | normal
"Okay. Yes. What do we do?"
```

```
[T17] AGENT | professional:3 | normal | mid | normal
"With a wire, time is everything. If the money hasn't settled at the receiving bank yet — and an hour is early — we can attempt a recall. I'm going to start that procedure right now, while you stay on the line with me."
```

```
[T18] CUSTOMER | hopeful:3 | normal | mid | normal
"So there's a chance?"
```

```
[T19] AGENT | reassuring:3 | normal | low | normal
"There is a real chance, and I'm going to be completely honest with you about it rather than give you false comfort. Let me get the recall moving first, then I'll explain exactly what's possible."
```

```
[T20] CUSTOMER | cooperative:3 | normal | mid | normal
"Okay. Please."
```

```
[T21] AGENT | professional:3 | normal | mid | normal | (typing)
"Pulling up the wire now — six thousand two hundred dollars, sent today at ten-fourteen AM to a beneficiary at a receiving bank. That's about seventy minutes ago."
```

```
[T22] CUSTOMER | afraid:3 | normal | mid | normal
"Is that good or bad?"
```

```
[T23] AGENT | professional:3 | normal | mid | normal
"That's workable. I'm contacting our Wire Operations team right now to initiate a recall request to the receiving bank — this asks them to freeze and return the funds before they're made available to the fraudster. I'm submitting it as we speak."
```

```
[T24] CUSTOMER | hopeful:3 | normal | mid | normal
"They can do that?"
```

```
[T25] AGENT | professional:3 | normal | low | normal
"They can request it, and here is the honest part I promised you: a recall is a request, not a guarantee. If the funds are still sitting unclaimed at the receiving bank, the odds are decent. If the fraudster has already pulled the money out, recovery becomes much harder. I will not promise you the six thousand two hundred is coming back, because I don't control the other bank — but I am giving this the fastest, strongest push we have."
```

```
[T26] CUSTOMER | afraid:3 | normal | mid | normal
"Okay. Okay. At least there's a chance. That's more than I had two minutes ago."
```

```
[T27] AGENT | reassuring:3 | normal | low | normal
"Exactly. And you calling within the hour is the single biggest thing working in your favour. People who wait until the next day almost never recover. You moved fast."
```

```
[T28] CUSTOMER | partially_satisfied:3 | normal | mid | normal
"What happens now?"
```

```
[T29] AGENT | professional:3 | normal | mid | normal | (typing)
"The recall request is submitted to Wire Operations and timestamped — that timestamp matters for the receiving bank's process. They'll transmit the recall to the beneficiary bank within the hour."
```

```
[T30] CUSTOMER | curious:3 | normal | mid | normal
"And when will I know if it worked?"
```

```
[T31] AGENT | professional:3 | normal | mid | normal
"Recalls can take anywhere from a few business days to a couple of weeks for the receiving bank to respond, depending on their process. I wish it were instant. What I can promise is that you'll be kept informed at each step — I'm not leaving you wondering."
```

```
[T32] CUSTOMER | cooperative:3 | normal | mid | normal
"Okay."
```

```
[T33] AGENT | professional:3 | normal | mid | normal
"I'm also opening a Fraud Operations ticket right now. They'll call you on the number on file within four hours to take the details of the fake invoice and email, document the fraud, and manage the recall on your behalf so you have one point of contact."
```

```
[T34] CUSTOMER | cooperative:3 | normal | mid | normal
"Four hours. Should I keep the fake email?"
```

```
[T35] AGENT | reassuring:3 | normal | mid | normal
"Yes — please do not delete it. Keep the fake invoice, the email, and your real contractor's text confirming he didn't send it. Fraud Operations will want all of it, and it strengthens the recall and any law-enforcement report."
```

```
[T36] CUSTOMER | cooperative:3 | normal | mid | normal
"I have all of it. I'll keep it."
```

```
[T37] AGENT | professional:3 | normal | mid | normal
"A few protective steps while I have you. First, do not send any further payments to that contractor by wire until you've confirmed his real banking details by phone, voice to voice — not email. Second, I'm flagging your account to watch for any other unusual activity. Third, when you pay the real invoice, call him first and read the details back to him directly."
```

```
[T38] CUSTOMER | resolute:3 | normal | mid | normal
"Believe me, I am calling him directly from now on. I'll never trust an emailed invoice again."
```

```
[T39] AGENT | empathetic:3 | normal | low | normal
"That instinct will protect you for the rest of your life — and again, this was not your failure. You were targeted by people who do this for a living. You responded faster than most ever do."
```

```
[T40] CUSTOMER | grateful:3 | normal | mid | normal
"Thank you for not making me feel like an idiot. I really thought you would."
```

```
[T41] AGENT | warm:3 | normal | mid | normal
"Never. We see this every week, and the people it happens to are smart, busy, trusting people. My job is to fight for your money, not to judge you."
```

```
[T42] CUSTOMER | hopeful:3 | normal | mid | normal
"So we've done everything we can right now?"
```

```
[T43] AGENT | reassuring:3 | normal | mid | normal
"We have. To summarize: you reported a six-thousand-two-hundred-dollar wire sent about seventy minutes ago to a fraudster posing as your contractor. I initiated a wire recall through Wire Operations immediately — which is a strong request but not a guarantee — and opened a Fraud Operations ticket; they'll call you within four hours. You'll keep all the fraud evidence, and going forward you'll verify invoice details by phone. Does that all sound right?"
```

```
[T44] CUSTOMER | grateful:3 | normal | mid | normal
"Yes. Thank you, Jasmine. I feel like I can breathe a little now."
```

```
[T45] AGENT | warm:3 | normal | mid | normal
"I'm really glad. Is there anything else I can help you with right now, Ms. Briggs?"
```

```
[T46] CUSTOMER | calm:2 | normal | mid | normal
"No. I'll wait for the Fraud team's call."
```

```
[T47] AGENT | professional:3 | normal | mid | normal
"Your case reference number is M-T-B dash four-six-five-five-zero-three-two. Fraud Operations will call within four hours, and they'll have the recall status. You'll receive a brief survey after we hang up."
```

```
[T48] AGENT | reassuring:3 | normal | mid | normal
"You did everything right today, Ms. Briggs. Hold on to that. We'll be in touch very soon."
```
