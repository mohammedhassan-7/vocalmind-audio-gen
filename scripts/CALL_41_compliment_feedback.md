# CALL_41 — Positive Feedback Call + Light Upsell

```yaml
call_id: CALL_41_compliment_feedback
duration_estimate: 4m 00s
turns: 32
sop_primary: SOP-02 (General Service)
policy_refs: [CS-RULE-001, CS-RULE-002, CS-RULE-003, CS-RULE-004, CS-RULE-018, CS-RULE-019, CS-RULE-020, CS-RULE-021]
kb_refs: [Section 3.4 - Plan Catalog]
customer_profile:
  name: "Carlos Mendez"
  account_number: "7781-3340-22"
  voice_hint: "male, 40s, warm Texan accent, upbeat and genuinely appreciative"
agent_profile:
  name: "Priya"
  voice_hint: "female, 30s, neutral US accent, warm and measured"
emotional_arc: "happy -> happy -> engaged -> satisfied"
expected_outcome: "Customer calls specifically to give positive feedback about a technician who went above and beyond on an install. Priya receives the compliment graciously, logs it as a recognition note for the tech, and — reading genuine satisfaction — offers a light, no-pressure mention of a loyalty perk the customer qualifies for (a free speed-boost trial). Customer accepts. PASS — exemplary handling of a happy-path call; happy-emotion ground-truth balance. Short call."
```

## Coverage

| Element | Where | Notes |
|---|---|---|
| Greeting | T01 | CS-RULE-001 verbatim — PASS |
| Recording notice | T02 | CS-RULE-002 — PASS |
| Acknowledge reason for call | T05 | CS-RULE-003 — PASS |
| 3-of-5 verification (light, for account note) | T05–T11 | CS-RULE-004 — PASS |
| Receives compliment graciously + logs recognition | T13, T17, T19 | service quality — PASS |
| Reads satisfaction, light no-pressure upsell | T21 | CS-RULE-018 spirit — PASS |
| Resolution summary | T27 | CS-RULE-019 — PASS |
| Anything else + case ref + survey | T29, T31 | CS-RULE-020, CS-RULE-021 — PASS |

---

## Dialog

```
[T01] AGENT | professional:3 | normal | mid | normal
"Thank you for calling NexaLink Telecommunications Broadband and Support. My name is Priya. Who do I have the pleasure of speaking with today?"
```

```
[T02] AGENT | professional:3 | normal | mid | normal
"And just so you know, this call may be recorded for quality assurance and training purposes."
```

```
[T03] CUSTOMER | happy:3 | normal | mid | normal
"Hi Priya! This is Carlos Mendez. Don't worry — nothing's wrong. I actually called to say something good for once."
```

```
[T04] AGENT | warm:4 | normal | mid | normal
"Oh, I love hearing that, Mr. Mendez! Those are my favourite calls. What's the good news?"
```

```
[T05] AGENT | professional:3 | normal | mid | normal
"And I understand you're calling to share some feedback — I'd genuinely love to capture it. Let me just quickly verify the account so I can log it properly. Could you give me your account number?"
```

```
[T06] CUSTOMER | cooperative:3 | normal | mid | normal
"Sure thing. Seven-seven-eight-one, three-three-four-zero, two-two."
```

```
[T07] AGENT | professional:3 | normal | mid | normal | (typing)
"Thank you. And the last four of the payment method on file?"
```

```
[T08] CUSTOMER | cooperative:3 | normal | mid | normal
"Five-five-one-two."
```

```
[T09] AGENT | professional:3 | normal | mid | normal
"And your full name?"
```

```
[T10] CUSTOMER | cooperative:3 | normal | mid | normal
"Carlos Antonio Mendez."
```

```
[T11] AGENT | reassuring:3 | normal | mid | normal
"Perfect, you're verified. Okay — tell me everything."
```

```
[T12] CUSTOMER | happy:4 | normal | mid | normal
"So I had a tech come out Tuesday for a fiber install — fella named Devon. My install was the last of his day, ran late, and it was pouring rain. He could've rushed it. Instead he stayed an extra hour, ran the cable cleaner than I'd ever have asked, showed my mom how to use the new remote, and didn't leave till everything worked. I just wanted somebody to know."
```

```
[T13] AGENT | warm:4 | normal | mid | normal
"Oh, that is wonderful to hear — and honestly it just made my afternoon. That's exactly the kind of thing we hope for but don't always hear about. Devon stayed late, in the rain, and took care of your mom on top of it."
```

```
[T14] CUSTOMER | happy:3 | normal | mid | normal
"Exactly. My mom's eighty-one and not great with tech. He was so patient with her."
```

```
[T15] AGENT | warm:4 | normal | mid | normal
"That patience matters more than almost anything. I want to make sure this lands where it should."
```

```
[T16] CUSTOMER | curious:3 | normal | mid | normal
"Can you actually do something with it? Or does it just disappear?"
```

```
[T17] AGENT | reassuring:3 | normal | mid | normal
"It absolutely does not disappear. I'm logging a formal recognition note on Devon's record right now, tied to your install work order, and it routes to his field-service manager. Those notes count toward quarterly recognition awards. So Devon's manager will see this with your name on it."
```

```
[T18] CUSTOMER | satisfied:4 | normal | mid | normal
"That's great. He earned it."
```

```
[T19] AGENT | professional:3 | normal | mid | normal | (typing)
"Recognition note logged — commending technician Devon for staying late in poor weather, exceptional cable work, and going out of his way to help your mother with the equipment. That's on his record now."
```

```
[T20] CUSTOMER | grateful:3 | normal | mid | normal
"Perfect. Thank you for taking the time."
```

```
[T21] AGENT | warm:3 | normal | mid | normal
"My pleasure. And since I have you — and only because you're clearly happy with the fiber, no pressure at all — I can see your account qualifies for a complimentary thirty-day speed-boost trial, double your current speed, free. If you like it you keep it at a small add-on; if not, it reverts automatically with nothing owed. Want me to switch it on?"
```

```
[T22] CUSTOMER | happy:3 | normal | mid | normal
"Free for thirty days and it just reverts if I don't want it? Sure, why not. Turn it on."
```

```
[T23] AGENT | professional:3 | normal | mid | normal | (typing)
"Done — speed boost is active now, doubles your download for thirty days. You'll get a reminder a few days before it ends so there are no surprises, and it reverts on its own unless you choose to keep it."
```

```
[T24] CUSTOMER | satisfied:3 | normal | mid | normal
"Love it. No surprises is how I like it."
```

```
[T25] AGENT | warm:3 | normal | mid | normal
"That's exactly how we like to do it too."
```

```
[T26] CUSTOMER | happy:3 | normal | mid | normal
"You all are batting a thousand this week."
```

```
[T27] AGENT | reassuring:3 | normal | mid | normal
"To recap: I logged a formal recognition note for Devon that goes to his manager with your commendation, and I switched on a free thirty-day speed-boost trial that reverts automatically with nothing owed if you don't keep it."
```

```
[T28] CUSTOMER | satisfied:3 | normal | mid | normal
"Perfect. That's everything."
```

```
[T29] AGENT | warm:3 | normal | mid | normal
"Is there anything else I can help you with today, Mr. Mendez?"
```

```
[T30] CUSTOMER | happy:3 | normal | mid | normal
"Nope. Y'all keep it up. Tell Devon thanks again."
```

```
[T31] AGENT | warm:4 | normal | mid | normal
"I will make sure of it. Your case reference number is N-X-L dash four-one-three-three-four-zero-two. You'll get a brief survey after we hang up — and I have a feeling I know how that one's going to go."
```

```
[T32] AGENT | warm:3 | normal | mid | normal
"Thank you for being such a great customer, Mr. Mendez, and for taking the time to say something kind. Have a wonderful day."
```
