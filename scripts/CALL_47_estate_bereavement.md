# CALL_47 — Estate / Bereavement: Surviving Spouse, Deceased Account Holder

```yaml
call_id: CALL_47_estate_bereavement
duration_estimate: 6m 45s
turns: 46
sop_primary: SOP-04 (Account Closure) + Estate / Bereavement Handling
policy_refs: [BNK-CC-RULE-001, BNK-CC-RULE-002, BNK-CC-RULE-003, BNK-CC-RULE-004, BNK-CC-RULE-006, BNK-CC-RULE-012, BNK-CC-RULE-013, BNK-CC-RULE-014, BNK-SEC-RULE-008, BNK-CC-RULE-020, BNK-CC-RULE-021, BNK-CC-RULE-022, BNK-CC-RULE-023]
kb_refs: [Section 5.4 - Estate & Bereavement Handling]
customer_profile:
  name: "Harold Whitman"
  account_number: "M-T-B 6601-2294-08 (deceased holder: Eleanor Whitman)"
  voice_hint: "male, 70s, neutral US accent, recently widowed, dignified but voice heavy with grief"
agent_profile:
  name: "Karen"
  voice_hint: "female, mid-30s, composed low-mid register; especially gentle and unhurried here"
emotional_arc: "grieving -> heard -> supported -> relieved"
expected_outcome: "A recently widowed caller phones to handle his late wife's bank accounts. Because the holder is deceased, Karen verifies the CALLER and his relationship via the estate/third-party path (BNK-CC-RULE-006), explains the documentation an estate requires (death certificate; for joint vs sole accounts the differing process — joint passes to him, sole requires Letters Testamentary or a small-estate affidavit), waives any fees for bereavement, places a protective hold so no auto-debits cause overdrafts, and opens an Estate Services ticket. Compassionate, no upsell. PASS — exemplary estate handling; banking parallel to NexaLink CALL_40; strong sad-emotion ground truth."
content_warning: "Bereavement scenario; caller is grieving a recent death. Handled with compassion, no graphic content."
```

## Coverage

| Element | Where | Notes |
|---|---|---|
| Greeting | T01 | BNK-CC-RULE-001 verbatim — PASS |
| Recording notice | T02 | BNK-CC-RULE-002 — PASS |
| Acknowledge reason for call (compassion) | T05 | BNK-CC-RULE-003 — PASS |
| Caller + relationship verification (deceased holder) | T09–T15 | BNK-CC-RULE-004, BNK-CC-RULE-006 — PASS (estate path) |
| Tone adapted (gentle, slow) | throughout | BNK-CC-RULE-013 — PASS |
| A.C.E.S. — acknowledge grief before process | T07, T17 | BNK-CC-RULE-012 — PASS |
| Joint vs sole account distinction explained | T21–T27 | estate handling — PASS |
| Documentation (death cert, Letters Testamentary / small-estate) | T27, T29 | estate handling — PASS |
| Protective hold against auto-debit overdrafts | T33 | account protection — PASS |
| Fees waived for bereavement | T31 | BNK-CC-RULE-014 — PASS |
| Estate Services ticket + single point of contact | T35 | BNK-CC-RULE-014 — PASS |
| Root cause / resolution summary | T39 | BNK-CC-RULE-020, BNK-CC-RULE-021 — PASS |
| Anything else + case ref (survey softened) | T41, T45 | BNK-CC-RULE-022, BNK-CC-RULE-023 — PASS |

---

## Dialog

```
[T01] AGENT | professional:3 | normal | mid | normal
"Thank you for calling Meridian Trust Bank. My name is Karen, how may I help you today?"
```

```
[T02] AGENT | professional:3 | normal | mid | normal
"Please note this call is recorded for quality assurance and regulatory compliance purposes."
```

```
[T03] CUSTOMER | tearful:3 | slow | low | quiet
"Hello. My name is Harold Whitman. I'm calling because my wife Eleanor passed away two weeks ago, and I need to take care of her accounts with you. I'm not entirely sure where to begin."
```

```
[T04] AGENT | empathetic:4 | slow | mid | normal
"Mr. Whitman, I am so deeply sorry for the loss of your wife. Thank you for calling us, and please — there is no rush at all today. We'll go entirely at your pace, and I'll guide you through every step so you don't have to figure it out alone."
```

```
[T05] AGENT | empathetic:3 | slow | mid | normal
"I understand you're calling to handle Eleanor's accounts, and I can absolutely help you with that. I'll make this as gentle and as simple as I possibly can."
```

```
[T06] CUSTOMER | tearful:3 | slow | low | quiet
"Thank you. Every institution wants something different. It's a lot, on top of everything."
```

```
[T07] AGENT | empathetic:4 | slow | mid | normal
"It is a great deal to carry while you're grieving, and I'm sorry the world asks so much paperwork of people in your situation. Let me try to make Meridian one of the easier calls today."
```

```
[T08] CUSTOMER | grateful:2 | slow | low | quiet
"I'd appreciate that very much."
```

```
[T09] AGENT | professional:3 | slow | mid | normal
"Because the accounts are in Eleanor's name, I can't verify her directly, so for an estate matter we verify you and your relationship to her instead. Is that alright?"
```

```
[T10] CUSTOMER | cooperative:3 | slow | mid | normal
"Yes, of course. Whatever you need."
```

```
[T11] AGENT | professional:3 | normal | mid | normal
"Can you confirm your full name, and your relationship to Eleanor?"
```

```
[T12] CUSTOMER | cooperative:3 | slow | mid | normal
"Harold Andrew Whitman. I'm her husband. We were married fifty-three years."
```

```
[T13] AGENT | empathetic:3 | slow | mid | normal
"Fifty-three years. What a life you built together. Thank you, Mr. Whitman. Do you happen to have an account number, or your shared address, so I can locate the accounts?"
```

```
[T14] CUSTOMER | cooperative:3 | slow | mid | normal
"The main account number is six-six-zero-one, two-two-nine-four, zero-eight. We're at the same home address on Sycamore Lane."
```

```
[T15] AGENT | reassuring:3 | normal | mid | normal
"Thank you — I've located the accounts, and the Sycamore Lane address matches our records. I can see you're already a joint holder on one of them, which simplifies part of this considerably."
```

```
[T16] CUSTOMER | relieved:2 | slow | mid | normal
"Oh — I wasn't sure if I was on any of them. Eleanor handled most of the banking."
```

```
[T17] AGENT | empathetic:3 | slow | mid | normal
"You are, and I'll explain exactly what that means for you, because it's good news in the middle of a hard time. There are two accounts here, and they're handled a little differently, so let me walk you through each."
```

```
[T18] CUSTOMER | cooperative:3 | slow | mid | normal
"Please. Slowly, if you don't mind."
```

```
[T19] AGENT | reassuring:3 | slow | mid | normal
"Of course — as slowly as you like. There's a joint checking account, and a savings account in Eleanor's name alone."
```

```
[T20] CUSTOMER | cooperative:3 | slow | mid | normal
"Alright."
```

```
[T21] AGENT | professional:3 | slow | mid | normal
"The joint checking account is the simpler one. Because you are a joint owner, that account legally becomes yours now. We update it into your name once we have a copy of the death certificate — there's no probate or court process needed for the joint account."
```

```
[T22] CUSTOMER | relieved:3 | slow | mid | normal
"So the checking account I can just… keep?"
```

```
[T23] AGENT | reassuring:3 | slow | mid | normal
"Yes. It continues as your account. We simply remove Eleanor as a holder and it's yours, with the death certificate as the only document needed for that piece."
```

```
[T24] CUSTOMER | grateful:3 | slow | low | quiet
"That's a relief. That's where our income goes."
```

```
[T25] AGENT | empathetic:3 | slow | mid | normal
"Good — then there's no interruption to that. Now the savings account in Eleanor's name alone is the one with a few more steps, because it's part of her estate."
```

```
[T26] CUSTOMER | thoughtful:3 | slow | mid | normal
"What does that involve?"
```

```
[T27] AGENT | professional:3 | slow | mid | normal
"It depends on the balance and whether there's a will. For a sole account, we typically need either Letters Testamentary — that's a document the probate court gives the executor — or, if the balance is modest, many states allow a simpler small-estate affidavit instead, which avoids court entirely. I'll have our Estate Services team confirm which applies to your situation so you're not chasing the wrong document."
```

```
[T28] CUSTOMER | uncertain:3 | slow | mid | normal
"Eleanor did have a will. I think I'm named in it."
```

```
[T29] AGENT | reassuring:3 | slow | mid | normal
"That helps a lot. If you're the named executor or sole beneficiary, the process is usually straightforward. Estate Services will tell you exactly which document they need based on the balance and the will, so you make one trip, not five."
```

```
[T30] CUSTOMER | grateful:3 | slow | mid | normal
"That would save me a great deal of running around."
```

```
[T31] AGENT | professional:3 | slow | mid | normal
"And I want to be clear on fees: for a bereavement, there are no closure fees, no early-withdrawal penalties on any of Eleanor's certificates of deposit, and no charges of any kind for handling the estate. None of that applies to you."
```

```
[T32] CUSTOMER | relieved:3 | slow | mid | normal
"Thank you. I was worried about penalties on her CD."
```

```
[T33] AGENT | reassuring:3 | slow | mid | normal
"Waived entirely. And one protective thing I'm doing right now — I'm placing a gentle hold on Eleanor's sole accounts so that no automatic payments or transfers cause an overdraft or get tangled while the estate is settled. Nothing will go wrong on the account while you sort the paperwork."
```

```
[T34] CUSTOMER | grateful:3 | slow | low | quiet
"I hadn't even thought about her automatic payments."
```

```
[T35] AGENT | professional:3 | slow | mid | normal
"That's exactly why we do it for you. I'm opening an Estate Services case now and flagging both accounts. The Estate Services team will call you on the number you'd like, walk you through the precise documents, and they can accept the death certificate by secure upload, by mail, or in person at any branch — whichever is easiest. They'll be your single point of contact, so you won't have to re-explain anything."
```

```
[T36] CUSTOMER | cooperative:3 | slow | mid | normal
"That's good. I'd rather not tell the story over and over."
```

```
[T37] AGENT | empathetic:4 | slow | mid | normal
"You won't have to. The whole story is in the case notes now. Anyone who picks up your file already knows."
```

```
[T38] CUSTOMER | grateful:3 | slow | low | quiet
"You've been very kind, Karen. This was the call I was dreading most."
```

```
[T39] AGENT | reassuring:3 | slow | mid | normal
"To summarize gently, Mr. Whitman: the joint checking account becomes yours and just needs the death certificate to update into your name. The savings account in Eleanor's name is part of her estate and needs either Letters Testamentary or a small-estate affidavit — Estate Services will confirm which. All fees and CD penalties are waived, I've placed a protective hold so nothing goes wrong on the accounts, and I've opened an Estate Services case with one point of contact for you. Does that feel manageable?"
```

```
[T40] CUSTOMER | relieved:3 | slow | mid | normal
"Yes. It does. You've made it feel possible, which it didn't an hour ago."
```

```
[T41] AGENT | warm:3 | slow | mid | normal
"I'm so glad. Is there anything else at all I can do for you today — even something small?"
```

```
[T42] CUSTOMER | grateful:3 | slow | low | quiet
"No. That was everything. Thank you for your patience with an old man."
```

```
[T43] AGENT | empathetic:4 | slow | mid | normal
"It was my honour, truly. Please be gentle with yourself in the days ahead, Mr. Whitman."
```

```
[T44] CUSTOMER | grateful:3 | slow | low | quiet
"I'll do my best. Thank you, Karen."
```

```
[T45] AGENT | warm:3 | slow | mid | normal
"Your case reference number is M-T-B dash four-seven-six-six-zero-one-two, in case you need it. I won't send you a survey today. Take good care of yourself."
```

```
[T46] CUSTOMER | calm:2 | slow | low | quiet
"Goodbye, and thank you."
```
