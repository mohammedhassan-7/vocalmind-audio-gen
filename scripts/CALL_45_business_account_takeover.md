# CALL_45 — Business Account Takeover, Full Freeze Procedure

```yaml
call_id: CALL_45_business_account_takeover
duration_estimate: 7m 00s
turns: 50
sop_primary: BNK-SOP-03 (Fraud) + BNK-SEC-RULE-010 (Account Takeover Freeze)
policy_refs: [BNK-CC-RULE-001, BNK-CC-RULE-002, BNK-CC-RULE-003, BNK-CC-RULE-004, BNK-CC-RULE-007, BNK-CC-RULE-014, BNK-SEC-RULE-001, BNK-SEC-RULE-008, BNK-SEC-RULE-010, BNK-FRAUD-RULE-004, BNK-FRAUD-RULE-009, BNK-FRAUD-RULE-010, BNK-CC-RULE-020, BNK-CC-RULE-021, BNK-CC-RULE-022, BNK-CC-RULE-023]
kb_refs: [BNK-SOP-03 Section 3D - Account Takeover, KB Section 8.2 - Identity Theft Support]
customer_profile:
  name: "Gloria Tan"
  account_number: "M-T-B-BIZ 8819-4471-20"
  voice_hint: "female, 40s, neutral US accent, alarmed business owner, composed but urgent"
agent_profile:
  name: "Andre"
  voice_hint: "male, mid-30s, neutral US accent, friendly methodical cadence, calm in a crisis"
emotional_arc: "alarmed -> reassured -> cooperative -> resolute"
expected_outcome: "Business owner discovers her company online banking shows a changed contact email and two pending outbound transfers she didn't initiate — a classic account takeover. Andre completes Enhanced Verification (control person), then executes BNK-SEC-RULE-010 in full: (1) freezes all account changes AND outbound transfers, (2) flags Security Review, (3) opens a Fraud Operations ticket (4-hr follow-up), (4) advises credential changes. He arranges the Identity Theft Affidavit mailed to the address ON FILE per BNK-FRAUD-RULE-009 (not any address given on the call), and advises the BNK-FRAUD-RULE-010 self-protection steps (credit bureaus, IdentityTheft.gov) without filing them himself. PASS — exemplary takeover handling; banking parallel to NexaLink CALL_16."
content_warning: "Account-takeover fraud scenario; customer alarmed. No graphic content."
```

## Coverage

| Element | Where | Notes |
|---|---|---|
| Greeting | T01 | BNK-CC-RULE-001 verbatim — PASS |
| Recording notice | T02 | BNK-CC-RULE-002, BNK-SEC-RULE-001 — PASS |
| Acknowledge reason for call | T04 | BNK-CC-RULE-003 — PASS |
| Enhanced Verification (control person) | T05–T13 | BNK-CC-RULE-007 — PASS |
| SEC-010 (1) freeze all changes + outbound transfers | T21–T23 | BNK-SEC-RULE-010 — PASS |
| Pending unauthorized transfers held | T23 | BNK-SEC-RULE-010 — PASS |
| SEC-010 (2) Security Review flag | T25 | BNK-SEC-RULE-010 — PASS |
| SEC-010 (3) Fraud Operations ticket (4-hr SLA) | T27 | BNK-SEC-RULE-010, BNK-FRAUD-RULE-004 — PASS |
| No further account changes beyond freeze | T29, T33 | BNK-SEC-RULE-010 — PASS |
| SEC-010 (4) advise credential changes | T35 | BNK-SEC-RULE-010 — PASS |
| Identity Theft Affidavit mailed to address ON FILE | T39 | BNK-FRAUD-RULE-009 — PASS |
| Self-protection steps advised, NOT filed for customer | T41 | BNK-FRAUD-RULE-010 — PASS |
| Root cause + resolution summary | T45 | BNK-CC-RULE-020, BNK-CC-RULE-021 — PASS |
| Anything else + case ref + survey | T47, T49 | BNK-CC-RULE-022, BNK-CC-RULE-023 — PASS |

---

## Dialog

```
[T01] AGENT | professional:3 | normal | mid | normal
"Thank you for calling Meridian Trust Bank. My name is Andre, how may I help you today?"
```

```
[T02] AGENT | professional:3 | normal | mid | normal
"Please note this call is recorded for quality assurance and regulatory compliance purposes."
```

```
[T03] CUSTOMER | worried:4 | fast | mid | normal
"Andre, this is Gloria Tan — I own Tan Design Studio. I just logged into our business banking and the contact email's been changed to something I don't recognize, and there are two transfers pending that I did not set up. I think someone's in our account."
```

```
[T04] AGENT | concerned:3 | normal | mid | normal
"Ms. Tan, thank you for calling the moment you saw this — that's exactly right, and we're going to act fast. I'm going to secure the account with you on this call. First I need to verify you as the control person, and because this is a fraud situation I'll use Enhanced Verification. Bear with me — it's a few quick steps."
```

```
[T05] AGENT | professional:3 | normal | mid | normal
"Can you give me the business account number?"
```

```
[T06] CUSTOMER | cooperative:3 | normal | mid | normal
"Eight-eight-one-nine, four-four-seven-one, two-zero."
```

```
[T07] AGENT | professional:3 | normal | mid | normal | (typing)
"Thank you. The full legal business name?"
```

```
[T08] CUSTOMER | cooperative:3 | normal | mid | normal
"Tan Design Studio LLC."
```

```
[T09] AGENT | professional:3 | normal | mid | normal
"Your full legal name and date of birth?"
```

```
[T10] CUSTOMER | cooperative:3 | normal | mid | normal
"Gloria Mei Tan. June twelfth, nineteen-eighty-three."
```

```
[T11] AGENT | professional:3 | normal | mid | normal
"Last four of your Social, and your security challenge phrase?"
```

```
[T12] CUSTOMER | cooperative:3 | normal | mid | normal
"Six-six-zero-two. The phrase is Wedgwood blue."
```

```
[T13] AGENT | reassuring:3 | normal | mid | normal
"That all matches — you're fully verified as the control person, Ms. Tan, and I can confirm you're on the number we have on file. Good."
```

```
[T14] CUSTOMER | worried:3 | normal | mid | normal
"Okay. Please, the transfers — can you stop them?"
```

```
[T15] AGENT | reassuring:3 | normal | mid | normal
"Yes. I want to walk you through exactly what I'm doing, in order, so you know the account is being locked down step by step. There are four parts and I'll narrate each one."
```

```
[T16] CUSTOMER | cooperative:3 | normal | mid | normal
"Go."
```

```
[T17] AGENT | professional:3 | normal | mid | normal
"First, tell me what you're seeing — the two pending transfers. Do you know the amounts or where they're going?"
```

```
[T18] CUSTOMER | worried:3 | normal | mid | normal
"One's for forty-eight hundred, one's for thirty-two hundred. Both to an account I've never seen. And they're dated to send tomorrow morning."
```

```
[T19] AGENT | concerned:3 | normal | mid | normal
"Dated for tomorrow — that's good news in one sense: they haven't gone yet, which means we can stop them. That changed email plus unauthorized pending transfers is a textbook account takeover, and you caught it in the window where we can prevent the loss."
```

```
[T20] CUSTOMER | partially_satisfied:3 | normal | mid | normal
"Okay. Okay, good."
```

```
[T21] AGENT | professional:3 | normal | mid | normal
"Step one — I'm freezing the account against all changes and all outbound transfers right now. That stops both pending transfers from executing and blocks anyone, including the intruder, from moving money or changing settings."
```

```
[T22] CUSTOMER | cooperative:3 | normal | mid | normal
"Please do that immediately."
```

```
[T23] AGENT | professional:3 | normal | mid | normal | (typing)
"Freeze applied. Both pending transfers — the forty-eight hundred and the thirty-two hundred — are now held and will not send. No outbound money can leave this account until the freeze is lifted by our Fraud team."
```

```
[T24] CUSTOMER | relieved:3 | normal | mid | normal
"Oh thank goodness."
```

```
[T25] AGENT | reassuring:3 | normal | mid | normal
"Step two — I'm flagging the account as Security Review. That tells every banker who touches this account that it's under active fraud investigation and no changes are permitted. Done."
```

```
[T26] CUSTOMER | cooperative:3 | normal | mid | normal
"Okay."
```

```
[T27] AGENT | professional:3 | normal | mid | normal
"Step three — I'm opening a Fraud Operations ticket right now with the details: changed contact email, two unauthorized pending transfers totalling eight thousand dollars, and the freeze. Fraud Operations will call you on the number on file within four hours to walk through the access history and reverse the email change."
```

```
[T28] CUSTOMER | curious:3 | normal | mid | normal
"Four hours. And they'll fix the email back?"
```

```
[T29] AGENT | professional:3 | normal | mid | normal
"They'll restore your legitimate contact details as part of the investigation — I'm intentionally not changing the email myself, because once an account is frozen for takeover I don't make further changes beyond the freeze. That's deliberate: it stops a bad actor from using a support call to undo the protection. Fraud Operations handles the restoration under verified conditions."
```

```
[T30] CUSTOMER | cooperative:3 | normal | mid | normal
"That makes sense. So you lock it, they unlock and fix it properly."
```

```
[T31] AGENT | reassuring:3 | normal | mid | normal
"Exactly. Ticket is open, four-hour follow-up. Now step four is on your side, and it's important."
```

```
[T32] CUSTOMER | cooperative:3 | normal | mid | normal
"Tell me."
```

```
[T33] AGENT | professional:3 | normal | mid | normal
"Because the account is frozen, I'm not making any other changes today — that's by design. What I need you to do is secure the credentials the intruder may have. Three things."
```

```
[T34] CUSTOMER | cooperative:3 | normal | mid | normal
"Okay, I'm writing this down."
```

```
[T35] AGENT | professional:3 | normal | mid | normal
"One — change your online banking password from a device you trust, and do not reuse an old one. Two — change the password on the email account tied to the business banking, because if that email was compromised, the attacker can reset everything else. Three — if you reuse that password anywhere, especially on anything financial, change those too."
```

```
[T36] CUSTOMER | resolute:3 | normal | mid | normal
"I'll do all three today. The email especially — I think I did reuse that password. That's probably how they got in."
```

```
[T37] AGENT | reassuring:3 | normal | mid | normal
"That's a very likely vector, and the fact that you spotted it means you're already ahead. Changing the email password is the single most important one."
```

```
[T38] CUSTOMER | cooperative:3 | normal | mid | normal
"Got it. Anything else?"
```

```
[T39] AGENT | professional:3 | normal | mid | normal
"Yes — we'll mail you an Identity Theft Affidavit packet to complete. It goes to the business address on file, the one in our records — not to any address given over the phone, including today. That protects you in case anyone tries to redirect your mail. It'll arrive in a few business days; Fraud Operations will reference it when they call."
```

```
[T40] CUSTOMER | cooperative:3 | normal | mid | normal
"Address on file is fine — it's the studio on Birch Street."
```

```
[T41] AGENT | professional:3 | normal | mid | normal
"Two more recommendations, though these are steps only you can take, not me. Place a fraud alert with the three credit bureaus, and file a report at IdentityTheft.gov. I can't file those on your behalf — they have to come from you — but they strengthen your protection and create a paper trail. Fraud Operations will remind you of both."
```

```
[T42] CUSTOMER | resolute:3 | normal | mid | normal
"Credit bureaus and IdentityTheft.gov. I'll handle those tonight."
```

```
[T43] AGENT | warm:3 | normal | mid | normal
"You're doing everything right, Ms. Tan. The money is safe — the transfers are stopped — and the account is locked until Fraud Operations restores it under verified conditions."
```

```
[T44] CUSTOMER | grateful:3 | normal | mid | normal
"I was so scared I'd lost eight thousand dollars on a Tuesday."
```

```
[T45] AGENT | reassuring:3 | normal | mid | normal
"To summarize what we did: you reported a changed contact email and two unauthorized pending transfers totalling eight thousand dollars. I froze the account against all changes and outbound transfers — which stopped both transfers — flagged it Security Review, and opened a Fraud Operations ticket with a four-hour follow-up. You'll change your online banking and email passwords today, place a credit-bureau fraud alert and an IdentityTheft.gov report, and an Identity Theft Affidavit is being mailed to your address on file. Does that all sound right?"
```

```
[T46] CUSTOMER | grateful:3 | normal | mid | normal
"Yes. Completely. Thank you, Andre — you were so calm about it, it helped."
```

```
[T47] AGENT | warm:3 | normal | mid | normal
"That's what we're here for. Is there anything else I can help you with today, Ms. Tan?"
```

```
[T48] CUSTOMER | resolute:3 | normal | mid | normal
"No — I'm going to go change those passwords right now."
```

```
[T49] AGENT | professional:3 | normal | mid | normal
"That's the perfect next move. Your case reference number is M-T-B dash four-five-eight-eight-one-nine-two. Fraud Operations will call within four hours. You'll receive a brief survey after we hang up."
```

```
[T50] AGENT | warm:3 | normal | mid | normal
"Thank you for catching this so quickly and banking with Meridian, Ms. Tan. Go secure those passwords — you've got this."
```
