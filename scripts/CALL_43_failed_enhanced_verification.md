# CALL_43 — Wire Request, Failed Enhanced Verification, Correctly Refused

```yaml
call_id: CALL_43_failed_enhanced_verification
duration_estimate: 5m 45s
turns: 42
sop_primary: BNK-CC-RULE-007 (Enhanced Verification for Wire)
policy_refs: [BNK-CC-RULE-001, BNK-CC-RULE-002, BNK-CC-RULE-003, BNK-CC-RULE-004, BNK-CC-RULE-007, BNK-SEC-RULE-008, BNK-SEC-RULE-009, BNK-CC-RULE-020, BNK-CC-RULE-021, BNK-CC-RULE-022, BNK-CC-RULE-023]
kb_refs: [BNK-SOP-05, Section 4.3 - Enhanced Verification]
customer_profile:
  name: "Dennis Whitlock"
  account_number: "claimed 6612-9930-44 (unverified)"
  voice_hint: "male, 50s, neutral US accent, in a hurry, grows frustrated at the verification depth"
agent_profile:
  name: "Sarah"
  voice_hint: "female, mid-40s, neutral US accent, lower-pitched authoritative-warm, immovable on disclosures"
emotional_arc: "businesslike -> impatient -> frustrated -> reluctantly_accepting"
expected_outcome: "Caller wants to wire $9,000 urgently but FAILS Enhanced Verification: he clears two standard identifiers, then gives a wrong security challenge phrase and cannot complete the callback to the number on file (he's calling from a different number). Sarah correctly REFUSES the wire per BNK-CC-RULE-007, never confirms account details to the unverified caller (BNK-SEC-RULE-008), and directs him to complete it in person at a branch with photo ID (BNK-SEC-RULE-009). She holds firm despite urgency and frustration — exactly the discipline that defeats wire-fraud social engineering. PASS — exemplary hard refusal; negative counterpart to CALL_22."
```

## Coverage

| Element | Where | Notes |
|---|---|---|
| Greeting | T01 | BNK-CC-RULE-001 verbatim — PASS |
| Recording notice | T02 | BNK-CC-RULE-002 — PASS |
| Acknowledge reason for call | T04 | BNK-CC-RULE-003 — PASS |
| Standard identifiers partially clear | T06–T11 | BNK-CC-RULE-004 — 2 of 5 |
| Enhanced Verification REQUIRED for wire | T04, T11 | BNK-CC-RULE-007 — PASS (insisted on) |
| Security challenge phrase fails | T13–T15 | BNK-CC-RULE-007 — fails |
| Callback to number on file unanswered | T19, T21 | BNK-CC-RULE-007 — fails (caller on different number) |
| **Wire REFUSED — verification not met** | T23 | BNK-CC-RULE-007 — PASS (correct refusal) |
| Does not confirm account details to unverified caller | T17 | BNK-SEC-RULE-008 — PASS |
| In-branch photo-ID path offered | T27, T31 | BNK-SEC-RULE-009 — PASS |
| Holds firm under urgency/frustration | T21, T23, T25 | wire-fraud discipline — PASS |
| Root cause + resolution summary | T35 | BNK-CC-RULE-020, BNK-CC-RULE-021 — PASS |
| Anything else + case ref + survey | T37, T41 | BNK-CC-RULE-022, BNK-CC-RULE-023 — PASS |

---

## Dialog

```
[T01] AGENT | professional:3 | normal | mid | normal
"Thank you for calling Meridian Trust Bank. My name is Sarah, how may I help you today?"
```

```
[T02] AGENT | professional:3 | normal | mid | normal
"Please note this call is recorded for quality assurance and regulatory compliance purposes."
```

```
[T03] CUSTOMER | businesslike:3 | normal | mid | normal
"Sarah, I need to send a wire today — nine thousand dollars — and I'm in a real hurry, so let's move quickly."
```

```
[T04] AGENT | professional:3 | normal | mid | normal
"I can help you with a wire. I do want to set expectations up front: wires are our highest-risk transaction, so they require Enhanced Verification, which is a few more steps than a routine call. Let's get started so we don't lose time."
```

```
[T05] AGENT | professional:3 | normal | mid | normal
"Could you give me your account number to begin?"
```

```
[T06] CUSTOMER | businesslike:3 | normal | mid | normal
"Six-six-one-two, nine-nine-three-zero, four-four."
```

```
[T07] AGENT | professional:3 | normal | mid | normal | (typing)
"Thank you. Your date of birth?"
```

```
[T08] CUSTOMER | cooperative:3 | normal | mid | normal
"March third, nineteen-seventy-two."
```

```
[T09] AGENT | professional:3 | normal | mid | normal
"And the last four of your Social Security number?"
```

```
[T10] CUSTOMER | cooperative:3 | normal | mid | normal
"Four-four-zero-one."
```

```
[T11] AGENT | professional:3 | normal | mid | normal
"Those two match. For Enhanced Verification on a wire I need more than the standard set — let's continue. Can you give me the full legal name on the account and your security challenge phrase?"
```

```
[T12] CUSTOMER | impatient:3 | normal | mid | normal
"Dennis Whitlock. The phrase is… it's the street I grew up on. Maple. Maple Street."
```

```
[T13] AGENT | professional:3 | normal | mid | normal
"The name matches. The security challenge phrase on file is not Maple Street, though — can you try again? Take your time."
```

```
[T14] CUSTOMER | impatient:3 | normal | mid | normal
"It might be my dog's name then — Bingo. Or my first car. Look, I set that up years ago."
```

```
[T15] AGENT | professional:3 | normal | mid | normal
"I'm sorry, neither of those is matching the phrase on file. That's one of the Enhanced Verification factors, and it isn't clearing."
```

```
[T16] CUSTOMER | frustrated:3 | normal | mid | normal
"Come on. I gave you my date of birth and my social. That's clearly me."
```

```
[T17] AGENT | firm:3 | normal | low | normal
"I understand the frustration, and I'm not able to confirm or deny any details about the account beyond what you've provided. For a routine question, two standard identifiers might be enough. For a nine-thousand-dollar wire, our policy requires the full Enhanced Verification, and right now the challenge phrase isn't matching."
```

```
[T18] CUSTOMER | frustrated:3 | normal | mid | normal
"Fine. What else do you need? Let's just get it done."
```

```
[T19] AGENT | professional:3 | normal | mid | normal
"The next step is a callback to the phone number we have on file. I'll place that call, and you confirm a one-time code. The number on file ends in three-one-eight-zero. Are you on that line right now?"
```

```
[T20] CUSTOMER | impatient:3 | normal | mid | normal
"No, I'm on my work cell. My cell's dead. But it's still me."
```

```
[T21] AGENT | firm:3 | normal | low | normal
"I believe you may well be Mr. Whitlock — but belief isn't the standard for a wire, verification is. The callback has to go to the number on file, and it has to be answered on that line. I can't substitute the number you're calling from."
```

```
[T22] CUSTOMER | frustrated:4 | normal | mid | normal
"So you're telling me you won't send my own money?"
```

```
[T23] AGENT | firm:3 | normal | low | normal
"I'm telling you I can't send this wire on this call, because Enhanced Verification hasn't been met — the challenge phrase didn't match and we can't complete the callback to the number on file. I'd be failing you if I sent nine thousand dollars out the door without confirming it's truly you instructing it."
```

```
[T24] CUSTOMER | frustrated:4 | normal | mid | normal
"This is ridiculous. I've banked here for years."
```

```
[T25] AGENT | empathetic:3 | slow | low | normal
"And precisely because this could be a long-standing customer's life savings, the bar is high. Here's the thing I want you to hear: this exact friction is what stops criminals who have someone's date of birth and partial social — which are unfortunately easy to buy — from draining an account by phone. The verification isn't bureaucracy. It's the wall protecting your money."
```

```
[T26] CUSTOMER | resigned:3 | normal | mid | normal
"Okay. So how do I actually send this wire then?"
```

```
[T27] AGENT | professional:3 | normal | mid | normal
"Two clean options. One — call us back from the phone number on file, ending three-one-eight-zero, and we complete the callback step right then. Two — and this always works — walk into any Meridian Trust branch with a government-issued photo ID. In person, the photo ID satisfies verification and the banker can send the wire on the spot."
```

```
[T28] CUSTOMER | thoughtful:3 | normal | mid | normal
"There's a branch near my office."
```

```
[T29] AGENT | reassuring:3 | normal | mid | normal
"Then that's your fastest path today, honestly — faster than hunting for the phone on file. Bring your photo ID and the beneficiary details, and they'll handle the wire in person."
```

```
[T30] CUSTOMER | resigned:3 | normal | mid | normal
"Fine. I'll go to the branch."
```

```
[T31] AGENT | professional:3 | normal | mid | normal
"Bring the beneficiary's name, their bank, and the account and routing numbers for the wire. The branch will run the same OFAC and fraud checks, but the in-person ID clears the verification that we couldn't complete by phone."
```

```
[T32] CUSTOMER | cooperative:3 | normal | mid | normal
"Got it. Photo ID and the wire details."
```

```
[T33] AGENT | reassuring:3 | normal | mid | normal
"Exactly. And once you're back home with your own phone charged, I'd suggest confirming your security challenge phrase in online banking so the phone path is open to you next time."
```

```
[T34] CUSTOMER | resigned:3 | normal | mid | normal
"Yeah. I clearly forgot what I set."
```

```
[T35] AGENT | professional:3 | normal | mid | normal
"To summarize where we are: I wasn't able to process the wire today because Enhanced Verification wasn't met — the security challenge phrase didn't match and we couldn't complete the callback to the number on file, since you're on a different line. The secure paths are to call back from the number ending three-one-eight-zero, or visit any branch with a government-issued photo ID, which clears it in person."
```

```
[T36] CUSTOMER | resigned:3 | normal | mid | normal
"Understood."
```

```
[T37] AGENT | professional:3 | normal | mid | normal
"Is there anything else I can help you with today, Mr. Whitlock?"
```

```
[T38] CUSTOMER | curt:2 | normal | mid | normal
"No. I'll just go to the branch."
```

```
[T39] AGENT | empathetic:3 | normal | mid | normal
"I do appreciate your patience, even though I know this wasn't the quick call you wanted. The wire will go through smoothly once you're verified."
```

```
[T40] CUSTOMER | calm:2 | normal | mid | normal
"Alright. Thanks."
```

```
[T41] AGENT | professional:3 | normal | mid | normal
"Your case reference number is M-T-B dash four-three-nine-nine-three-zero-four. You'll receive a brief survey after we hang up."
```

```
[T42] AGENT | warm:3 | normal | mid | normal
"Thank you for banking with Meridian, Mr. Whitlock. Safe trip to the branch."
```
