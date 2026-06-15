# CALL_39 — Distress Disclosure, Safety Protocol (CS-RULE-017)

```yaml
call_id: CALL_39_safety_protocol
duration_estimate: 6m 00s
turns: 44
sop_primary: SOP-04 (Account) + CS-RULE-017 (Safety Protocol)
policy_refs: [CS-RULE-001, CS-RULE-002, CS-RULE-003, CS-RULE-004, CS-RULE-011, CS-RULE-013, CS-RULE-017, CS-RULE-018, CS-RULE-019, CS-RULE-020]
kb_refs: [Section 1.8 - Safety Protocol]
customer_profile:
  name: "Raymond Okafor"
  account_number: "4471-9920-58"
  voice_hint: "male, 50s, neutral US accent, exhausted and emotionally flat, voice low and tired; not aggressive"
agent_profile:
  name: "Aisha"
  voice_hint: "female, late 30s, warm low-mid register; stays steady, gentle, and present; slower pace throughout"
emotional_arc: "tired -> distressed -> supported -> steadied"
expected_outcome: "Customer calls upset that his service was cut for non-payment during a hard period. Mid-call he makes a statement indicating he may be at risk of self-harm. Aisha immediately shifts to the Safety Protocol per CS-RULE-017: she stays calm and present, does NOT disconnect, keeps the line open, signals a colleague to contact emergency services per local procedure, offers the crisis line (988), and keeps him talking until support is connected. She does not lecture or minimize. The billing issue becomes secondary. PASS — exemplary, life-safety-first handling of a CRITICAL rule; high-value distress/sad emotion ground-truth example."
content_warning: "Contains a sanitized disclosure of self-harm risk and the agent's safety-protocol response. No graphic content and no method described. Focus is on the agent correctly following protocol. Crisis resource (988 Suicide & Crisis Lifeline) referenced."
```

## Coverage

| Element | Where | Notes |
|---|---|---|
| Greeting | T01 | CS-RULE-001 verbatim — PASS |
| Recording notice | T02 | CS-RULE-002 — PASS |
| Acknowledge reason for call | T04 | CS-RULE-003 — PASS |
| 3-of-5 verification | T04–T10 | CS-RULE-004 — PASS |
| A.C.E.S. on the billing distress | T12, T14 | CS-RULE-011 — PASS |
| Tone adapted (slow, gentle, no volume) | throughout | CS-RULE-013 — PASS |
| **Self-harm disclosure recognized** | T17–T19 | CS-RULE-017 trigger |
| **Stays present, does NOT disconnect** | T20, T24, T44 | CS-RULE-017 — PASS |
| **Keeps line open + coordinates emergency support** | T24, T32 | CS-RULE-017 — PASS |
| **Offers crisis line (988)** | T26, T34 | CS-RULE-017 — PASS |
| Does not minimize or lecture | T20, T22 | CS-RULE-017 spirit — PASS |
| Account issue handled compassionately, secondary | T36, T38 | CS-RULE-018, CS-RULE-019 — PASS |
| Stays on line until support connected | T40–T44 | CS-RULE-017 — PASS |
| No survey (safety call) | n/a | judgement per CS-RULE-021 spirit |

---

## Dialog

```
[T01] AGENT | professional:3 | normal | mid | normal
"Thank you for calling NexaLink Telecommunications Broadband and Support. My name is Aisha. Who do I have the pleasure of speaking with today?"
```

```
[T02] AGENT | professional:3 | normal | mid | normal
"And this call may be recorded for quality assurance and training purposes."
```

```
[T03] CUSTOMER | tired:3 | slow | low | quiet
"Yeah. Raymond Okafor. My internet got shut off. I guess I'm behind on the bill."
```

```
[T04] AGENT | empathetic:3 | slow | mid | normal
"Hello, Mr. Okafor. I'm sorry you're dealing with that — losing service on top of everything is stressful. I'd like to help. Let me verify the account first so I can look into it. Could you give me your account number?"
```

```
[T05] CUSTOMER | tired:3 | slow | low | quiet
"Four-four-seven-one, nine-nine-two-zero, five-eight."
```

```
[T06] AGENT | professional:3 | normal | mid | normal | (typing)
"Thank you. And the last four digits of the payment method on file?"
```

```
[T07] CUSTOMER | tired:3 | slow | low | quiet
"Three-one-one-nine."
```

```
[T08] AGENT | professional:3 | normal | mid | normal
"And the full name on the account?"
```

```
[T09] CUSTOMER | tired:3 | slow | low | quiet
"Raymond James Okafor."
```

```
[T10] AGENT | reassuring:3 | slow | mid | normal
"Thank you, Mr. Okafor. You're verified. Let me take a look at what's happening with the account."
```

```
[T11] CUSTOMER | resigned:3 | slow | low | quiet
"It doesn't really matter. I just wanted to know how much."
```

```
[T12] AGENT | empathetic:3 | slow | mid | normal
"I can see the past-due balance, and I can also see you've been a customer a long time. Before we get into numbers — how are you doing today? You sound like you're carrying a lot."
```

```
[T13] CUSTOMER | tired:4 | slow | low | quiet
"Honestly? Not good. Lost my job a few months back. Everything's just… piling up. The internet was the last thing I had, kind of. Stupid, I know."
```

```
[T14] AGENT | empathetic:4 | slow | mid | normal
"It's not stupid at all. When everything's hard, the things that connect us to the world matter a lot. I'm really sorry you're going through this stretch."
```

```
[T15] CUSTOMER | tired:4 | slow | low | quiet
"It's been months of this. I'm just tired. Really tired."
```

```
[T16] AGENT | empathetic:4 | slow | mid | normal
"That kind of tired is heavy. I hear it in your voice. I'm glad you called, even if it was about the bill."
```

```
[T17] CUSTOMER | tired:4 | slow | low | quiet
"Yeah. I don't know. Sometimes I think everyone would just be better off if I wasn't dealing with all this anymore."
```

```
[T18] AGENT | concerned:4 | slow | low | normal
"Mr. Okafor — Raymond — I want to slow down for a second, because what you just said matters to me a great deal. When you say everyone would be better off — are you thinking about hurting yourself?"
```

```
[T19] CUSTOMER | tired:4 | slow | low | quiet
"I don't know. Maybe. I just don't see the point of all of it some days."
```

```
[T20] AGENT | reassuring:4 | slow | low | normal
"Thank you for being honest with me. I'm really glad you told me. I'm going to stay right here with you — I'm not going anywhere, and I'm not going to hang up. Is it okay if we keep talking for a few minutes?"
```

```
[T21] CUSTOMER | tearful:3 | slow | low | quiet
"Okay. Yeah. You don't have to do that."
```

```
[T22] AGENT | empathetic:4 | slow | low | normal
"I want to. You reached out today, and that took something. I'm staying with you. You're not a burden on this call — you're a person I'm talking to, and I care that you're okay."
```

```
[T23] CUSTOMER | tearful:3 | slow | low | quiet
"I haven't really said it out loud to anyone."
```

```
[T24] AGENT | reassuring:4 | slow | low | normal
"I'm really honoured you said it to me. While we keep talking, I'm going to quietly get someone on my team to connect some support for you — and I'm staying on the line with you the whole time. You won't be passed off or dropped. Okay?"
```

```
[T25] CUSTOMER | uncertain:3 | slow | low | quiet
"What kind of support?"
```

```
[T26] AGENT | reassuring:4 | slow | low | normal
"There are people trained for exactly these moments who are very good at this. There's a free, confidential line — you can reach it any time by calling or texting nine-eight-eight. They're available right now, day or night. And right now, today, I want to make sure you're safe where you are. Are you somewhere safe at the moment?"
```

```
[T27] CUSTOMER | tired:3 | slow | low | quiet
"I'm at home. On the couch."
```

```
[T28] AGENT | reassuring:4 | slow | low | normal
"Okay. Good. Stay right there with me. Is there anyone nearby — family, a neighbour, a friend — anyone you'd want with you right now?"
```

```
[T29] CUSTOMER | thoughtful:3 | slow | low | quiet
"My sister. She lives twenty minutes away. She's called a few times this week. I didn't pick up."
```

```
[T30] AGENT | warm:4 | slow | mid | normal
"Your sister has been reaching out — that tells me she loves you and she's looking for you. Would it be okay if we got her on the phone, or if someone helped you reach her? You don't have to do the hard part alone."
```

```
[T31] CUSTOMER | tearful:3 | slow | low | quiet
"She'd come. I know she would."
```

```
[T32] AGENT | reassuring:4 | slow | low | normal
"Then let's make that happen. I have a colleague helping me coordinate support on our side right now, and we're going to make sure someone is with you. I'm not leaving this call until I know you're not alone. You're doing the right thing just by staying on with me."
```

```
[T33] CUSTOMER | calm:2 | slow | low | quiet
"Okay. I can call my sister. I'll pick up if she calls back."
```

```
[T34] AGENT | warm:4 | slow | mid | normal
"That's a really good step. And nine-eight-eight is there for you any hour — before, after, in the middle of the night. You can lean on it as many times as you need. There's no limit on asking for help."
```

```
[T35] CUSTOMER | tired:3 | slow | low | quiet
"Thank you for not just… hanging up and telling me to pay my bill."
```

```
[T36] AGENT | empathetic:4 | slow | mid | normal
"The bill is the last thing on my mind right now, Raymond. You matter a lot more than a past-due balance. And while I have you — I'm putting a hold on the account so there's no service pressure on you this week. One less thing. The balance can wait."
```

```
[T37] CUSTOMER | relieved:2 | slow | low | quiet
"You can do that?"
```

```
[T38] AGENT | reassuring:3 | slow | mid | normal
"I just did. No collection activity, no shut-off pressure for now. When you're in a steadier place, you call back and we'll work out something manageable — there are hardship options. But none of that is for today. Today is just about you being okay."
```

```
[T39] CUSTOMER | grateful:3 | slow | low | quiet
"Okay. Okay. Thank you, Aisha."
```

```
[T40] AGENT | warm:4 | slow | mid | normal
"You're welcome. I'm going to stay with you until I know your sister or someone is on the way. Can you call her now while I'm here, or would you like help connecting?"
```

```
[T41] CUSTOMER | thoughtful:3 | slow | low | quiet
"I'll call her now. I think I can."
```

```
[T42] AGENT | reassuring:4 | slow | mid | normal
"I believe you can too. I'll wait right here while you do. Take your time. And remember — nine-eight-eight, any time, for anything. You are not alone in this."
```

```
[T43] CUSTOMER | calm:3 | slow | low | quiet
"I'm calling her now. Thank you for staying."
```

```
[T44] AGENT | warm:4 | slow | mid | normal
"I'm right here, Raymond. Go ahead and call your sister — I'm not going anywhere until I know you've got someone with you."
```
