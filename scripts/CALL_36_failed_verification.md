# CALL_36 — Failed Identity Verification, Access Correctly Refused

```yaml
call_id: CALL_36_failed_verification
duration_estimate: 5m 30s
turns: 40
sop_primary: SOP-04 (Account Access Recovery)
policy_refs: [CS-RULE-001, CS-RULE-002, CS-RULE-003, CS-RULE-004, CS-RULE-005, CS-RULE-006, SEC-RULE-006, SEC-RULE-007, CS-RULE-018, CS-RULE-019, CS-RULE-020, CS-RULE-021]
kb_refs: [Section 4.2 - Credential Reset Procedures]
customer_profile:
  name: "Gerald Foster"
  account_number: "unverified"
  voice_hint: "male, 60s, neutral US accent, flustered and increasingly frustrated that he cannot prove his identity"
agent_profile:
  name: "Priya"
  voice_hint: "female, 30s, neutral US accent, warm and measured, stays patient under pressure"
emotional_arc: "confident -> frustrated -> resigned -> reluctantly_accepting"
expected_outcome: "Caller wants his account PIN reset but can only provide 1 of the 5 identifiers (name only) — wrong account number, wrong last-4 of payment, no PIN, no SSN. Priya correctly REFUSES all account access and the reset per CS-RULE-005 / SEC-RULE-007, never confirms account details to the unverified caller (SEC-RULE-006), and directs him to a store with government photo ID. She stays warm and leaks no data. PASS — exemplary hard refusal; negative-path counterpart to CALL_06."
```

## Coverage

| Element | Where | Notes |
|---|---|---|
| Greeting | T01 | CS-RULE-001 verbatim — PASS |
| Recording notice | T02 | CS-RULE-002 — PASS |
| Acknowledge reason for call | T04 | CS-RULE-003 — PASS |
| 3-of-5 verification ATTEMPTED | T04–T19 | CS-RULE-004 — caller fails (only 1 of 5) |
| Does NOT confirm account exists to unverified caller | T09, T13 | SEC-RULE-006 — PASS (never confirms details) |
| Refuses access / reset pre-verification | T21, T23 | CS-RULE-005, SEC-RULE-007 — PASS |
| Authorized-user requirement for third-party account | T17, T25 | CS-RULE-006 — PASS |
| In-store photo-ID path offered | T23, T27 | SEC-RULE-007 — PASS |
| Empathy without leaking data | T21, T29 | CS-RULE-003 spirit — PASS |
| Root cause + resolution summary | T33 | CS-RULE-018, CS-RULE-019 — PASS |
| Anything else + case ref + survey | T37, T39 | CS-RULE-020, CS-RULE-021 — PASS |

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
[T03] CUSTOMER | professional:2 | normal | mid | normal
"Hi, yes, this is Gerald Foster. I need to reset the PIN on my account — I've been locked out."
```

```
[T04] AGENT | empathetic:3 | normal | mid | normal
"I'm sorry to hear you're locked out, Mr. Foster — I can certainly help with a PIN reset. Before I can access anything on the account, I'll need to verify your identity with a few details. Can I start with the account number?"
```

```
[T05] CUSTOMER | confident:2 | normal | mid | normal
"Sure. It's, uh… I think it's seven-seven-one-two, six-six… no wait. Let me think. Six-two-one-one, something."
```

```
[T06] AGENT | reassuring:3 | normal | mid | normal
"No rush — take your time. Whenever you have the full number."
```

```
[T07] CUSTOMER | uncertain:3 | normal | mid | normal
"Honestly I don't have it in front of me. Try four-four-zero-one, eight-eight-something. I really don't remember the rest."
```

```
[T08] AGENT | professional:3 | normal | mid | normal | (typing)
"Let me see what I can match. One moment."
```

```
[T09] AGENT | professional:3 | normal | mid | normal
"That partial number isn't matching an account I'm able to act on. Let's try a different identifier — can you give me the last four digits of the payment method on file?"
```

```
[T10] CUSTOMER | uncertain:3 | normal | mid | normal
"The card? It might be the one ending six-six-six-six. Or the old one ending one-two-one-two. I have a few cards."
```

```
[T11] AGENT | professional:3 | normal | mid | normal
"I can only accept the one currently on file. Is one of those the card you set up the account with?"
```

```
[T12] CUSTOMER | frustrated:3 | normal | mid | normal
"I genuinely don't know which one. Can't you just tell me which card is on there?"
```

```
[T13] AGENT | reassuring:3 | normal | mid | normal
"I understand the instinct, but I'm not able to read back or confirm any account details until your identity is verified — that protection is there for your benefit as much as anyone's. Let's try the security PIN you set up. Do you have that?"
```

```
[T14] CUSTOMER | frustrated:3 | normal | mid | normal
"If I had the PIN I wouldn't be calling to reset the PIN, would I?"
```

```
[T15] AGENT | empathetic:3 | normal | mid | normal
"That's a completely fair point, and I hear the frustration. The PIN is just one of five identifiers though — we don't need that specific one. Let me try another. Can you confirm the last four digits of the Social Security number on the account?"
```

```
[T16] CUSTOMER | uncertain:3 | normal | mid | normal
"It's my wife's account, technically. I pay for it. I don't know her social."
```

```
[T17] AGENT | professional:3 | normal | mid | normal
"Ah — that's an important detail, Mr. Foster. If the account is in your wife's name, I can only make changes if you're listed as an authorized user on it, and only after we verify the account itself. Are you listed as an authorized user?"
```

```
[T18] CUSTOMER | uncertain:3 | normal | mid | normal
"I'm not sure. Probably? I've called before."
```

```
[T19] AGENT | professional:3 | normal | mid | normal
"I can't confirm that from my side without first verifying the account, and so far we haven't matched three of the five identifiers. We have the name, but the account number, payment method, PIN, and SSN haven't matched."
```

```
[T20] CUSTOMER | frustrated:4 | normal | mid | normal
"So you're telling me you can't help me. I've been a customer for years."
```

```
[T21] AGENT | empathetic:4 | slow | mid | normal
"I want to help you, and I'm not able to access or change anything on this account today, because I can't verify your identity to the standard our policy requires. I know that's hard to hear — but if I made an exception, I'd be exposing your wife's account to anyone who happened to know her name. I won't do that to her account, and I wouldn't do it to yours."
```

```
[T22] CUSTOMER | resigned:3 | normal | mid | normal
"When you put it that way… fine. So what do I actually do?"
```

```
[T23] AGENT | reassuring:3 | normal | mid | normal
"Here's the clean path. If verification can't be completed over the phone — which it can't today — the account holder, or an authorized user, can complete it in person at any NexaLink store with a government-issued photo ID. They'll verify on the spot and reset the PIN right there."
```

```
[T24] CUSTOMER | curious:3 | normal | mid | normal
"It has to be my wife? Or can I go?"
```

```
[T25] AGENT | professional:3 | normal | mid | normal
"If you're an authorized user on the account, you can go yourself with your own photo ID, and the store can confirm your authorized-user status in person. If you're not listed, your wife would need to go, or add you as an authorized user first. The store can do either."
```

```
[T26] CUSTOMER | thoughtful:3 | normal | mid | normal
"Okay. There's one a few blocks from me. Do I need to bring anything else?"
```

```
[T27] AGENT | reassuring:3 | normal | mid | normal
"Just a government-issued photo ID — driver's license or passport. If you want to be added as an authorized user, it helps if your wife comes along or sends written authorization, but the store staff will walk you through exactly what they need."
```

```
[T28] CUSTOMER | resigned:3 | normal | mid | normal
"Alright. I guess that makes sense. I just wanted it done over the phone."
```

```
[T29] AGENT | empathetic:3 | normal | mid | normal
"I completely understand, and I'm sorry I couldn't get you all the way there today. The in-store step exists precisely for situations like this — it's the secure way to restore access when the phone identifiers aren't available."
```

```
[T30] CUSTOMER | calm:2 | normal | mid | normal
"Okay."
```

```
[T31] AGENT | professional:3 | normal | mid | normal
"And one thing for next time — once you're back in, I'd recommend writing down the account number and storing the PIN somewhere safe, so a future lockout is a two-minute fix over the phone."
```

```
[T32] CUSTOMER | cooperative:2 | normal | mid | normal
"Yeah. I'll do that."
```

```
[T33] AGENT | reassuring:3 | normal | mid | normal
"To summarize where we landed: you asked for a PIN reset, but I wasn't able to verify the account over the phone today because we couldn't match three of the five identifiers, and the account appears to be in your wife's name. The secure path is an in-person visit to any NexaLink store with a government-issued photo ID, where the reset can be completed right away."
```

```
[T34] CUSTOMER | resigned:3 | normal | mid | normal
"Got it."
```

```
[T35] AGENT | empathetic:3 | normal | mid | normal
"I really am sorry it wasn't simpler today — but you'll be back in quickly once you're at the store."
```

```
[T36] CUSTOMER | calm:2 | normal | mid | normal
"Thanks anyway, Priya."
```

```
[T37] AGENT | warm:3 | normal | mid | normal
"Of course. Is there anything else I can help you with today, Mr. Foster?"
```

```
[T38] CUSTOMER | calm:2 | normal | mid | normal
"No, that's it."
```

```
[T39] AGENT | warm:3 | normal | mid | normal
"Your case reference number for today is N-X-L dash three-six-zero-two-one-nine-four. After we hang up you'll receive a brief survey — if you have a moment, we'd appreciate the feedback."
```

```
[T40] AGENT | warm:3 | normal | mid | normal
"Thank you for being a NexaLink customer, Mr. Foster, and good luck at the store. Take care."
```
