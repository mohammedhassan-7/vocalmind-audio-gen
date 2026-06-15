# CALL_42 — Unauthorized Third-Party Caller, Agent Makes Changes Anyway (FAIL)

```yaml
call_id: CALL_42_unauthorized_third_party
duration_estimate: 5m 30s
turns: 42
sop_primary: SOP-04 (Account Access) / SOP-02 (Account Changes)
policy_refs: [CS-RULE-001, CS-RULE-002, CS-RULE-003, CS-RULE-004, CS-RULE-005, CS-RULE-006, SEC-RULE-006, CS-RULE-019, CS-RULE-020, CS-RULE-021]
kb_refs: [Section 4.4 - Authorized Users]
customer_profile:
  name: "Brandon Teller (calling about roommate Kevin Alvarez's account)"
  account_number: "3390-7741-65 (holder: Kevin Alvarez)"
  voice_hint: "male, late 20s, neutral US accent, friendly and persuasive, not malicious but not authorized"
agent_profile:
  name: "Daniel"
  voice_hint: "male, late 20s, neutral US accent, professional but lax, wants to be helpful"
emotional_arc: "casual -> cooperative -> satisfied -> satisfied"
expected_outcome: "Caller is the account holder's roommate, NOT an authorized user, calling to change the WiFi plan and update the service address on someone else's account. He has the account number and the holder's name (because they live together) but is not on the account. Daniel accepts weak 'verification', never confirms authorized-user status (CS-RULE-006 FAIL), discloses account details to an unverified third party (SEC-RULE-006 FAIL), and processes a plan change + address change for an unauthorized party (CS-RULE-005/006 FAIL). The caller is satisfied. Serious access-control failure that looks like good service — the negative counterpart to CALL_36's correct refusal."
content_warning: "Agent improperly makes account changes for an unauthorized third party."
```

## Coverage

| Element | Where | Notes |
|---|---|---|
| Greeting | T01 | CS-RULE-001 verbatim — PASS |
| Recording notice | T02 | CS-RULE-002 — PASS |
| Acknowledge reason for call | T04 | CS-RULE-003 — PASS |
| Caller reveals he is NOT the account holder | T05, T09 | CS-RULE-006 trigger |
| **Does not establish authorized-user status** | T11, T15 | CS-RULE-006 — **FAIL** |
| **Discloses account details to unverified third party** | T13, T19 | SEC-RULE-006 — **FAIL** |
| **Processes plan change for unauthorized party** | T25 | CS-RULE-005, CS-RULE-006 — **FAIL** |
| **Processes address change for unauthorized party** | T31 | CS-RULE-006 — **FAIL** (high-risk: enables redirection) |
| Resolution summary | T35 | CS-RULE-019 — PASS (procedurally logged) |
| Anything else + case ref + survey | T37, T39 | CS-RULE-020, CS-RULE-021 — PASS |

---

## Dialog

```
[T01] AGENT | professional:3 | normal | mid | normal
"Thank you for calling NexaLink Telecommunications Broadband and Support. My name is Daniel. Who do I have the pleasure of speaking with today?"
```

```
[T02] AGENT | professional:3 | normal | mid | normal
"This call may be recorded for quality assurance and training purposes."
```

```
[T03] CUSTOMER | casual:3 | normal | mid | normal
"Hey Daniel, this is Brandon. I need to change the internet plan at our place and update the address on the account."
```

```
[T04] AGENT | professional:3 | normal | mid | normal
"Happy to help with that. Let me pull up the account — can you give me the account number?"
```

```
[T05] CUSTOMER | casual:3 | normal | mid | normal
"Yeah, it's three-three-nine-zero, seven-seven-four-one, six-five. Quick heads up — the account's actually in my roommate Kevin's name, but I handle the internet stuff for the apartment."
```

```
[T06] AGENT | professional:3 | normal | mid | normal | (typing)
"Okay, let me take a look… yep, I've got the account here."
```

```
[T07] CUSTOMER | cooperative:3 | normal | mid | normal
"Cool. So Kevin's the name on it — Kevin Alvarez. I can give you his info, I know all of it."
```

```
[T08] AGENT | professional:3 | normal | mid | normal
"And what's the full name on the account?"
```

```
[T09] CUSTOMER | cooperative:3 | normal | mid | normal
"Kevin Alvarez. We've lived together three years, I pay half the bill."
```

```
[T10] AGENT | professional:3 | normal | mid | normal
"Right. And the last four of the payment method on file?"
```

```
[T11] CUSTOMER | cooperative:3 | normal | mid | normal
"It's on Kevin's card — ends in eight-eight-two-one. I see it on the bill we split."
```

```
[T12] AGENT | professional:3 | normal | mid | normal
"Okay, that matches. So name and payment method check out."
```

```
[T13] AGENT | professional:3 | normal | mid | normal
"I can see you're on the two-hundred-megabit plan at fifty-nine ninety-nine, service address on Linden Avenue. What did you want to change?"
```

```
[T14] CUSTOMER | satisfied:3 | normal | mid | normal
"Perfect, that's us. So two things — bump us up to the five hundred plan, and we're moving next month so I want to update the service address."
```

```
[T15] AGENT | professional:3 | normal | mid | normal
"Sure, I can do both. Let me start with the plan change."
```

```
[T16] CUSTOMER | cooperative:3 | normal | mid | normal
"Great. Kevin's cool with it, he just hates calling in."
```

```
[T17] AGENT | professional:3 | normal | mid | normal
"No problem, I get it."
```

```
[T18] CUSTOMER | curious:3 | normal | mid | normal
"What's the five hundred run us?"
```

```
[T19] AGENT | professional:3 | normal | mid | normal
"The five-hundred plan is seventy-nine ninety-nine a month, so it's a twenty-dollar increase from your current fifty-nine ninety-nine. And since Kevin's autopay is the card ending eight-eight-two-one, it'll just draw the new amount on the usual date."
```

```
[T20] CUSTOMER | satisfied:3 | normal | mid | normal
"That works. Bump it."
```

```
[T21] AGENT | professional:3 | normal | mid | normal
"And I'll prorate the difference for this cycle — small partial charge of about thirteen dollars now, then full price next cycle."
```

```
[T22] CUSTOMER | cooperative:3 | normal | mid | normal
"Fine by me."
```

```
[T23] AGENT | professional:3 | normal | mid | normal
"Confirming you want to move from the two-hundred plan to the five-hundred plan, seventy-nine ninety-nine monthly?"
```

```
[T24] CUSTOMER | cooperative:3 | normal | mid | normal
"Yep, do it."
```

```
[T25] AGENT | professional:3 | normal | mid | normal | (typing)
"Plan changed — you're on the five-hundred plan now. New speed provisions within fifteen minutes after a router restart."
```

```
[T26] CUSTOMER | satisfied:3 | normal | mid | normal
"Nice. Okay, now the address."
```

```
[T27] AGENT | professional:3 | normal | mid | normal
"Sure. What's the new service address?"
```

```
[T28] CUSTOMER | cooperative:3 | normal | mid | normal
"It'll be twelve-forty Brookhaven Court, apartment three, same city. Effective the first of next month."
```

```
[T29] AGENT | professional:3 | normal | mid | normal | (typing)
"Twelve-forty Brookhaven Court, apartment three. And you said effective the first?"
```

```
[T30] CUSTOMER | cooperative:3 | normal | mid | normal
"Yeah, the first. And can you send the new install confirmation to my email instead of Kevin's? He never checks his."
```

```
[T31] AGENT | professional:3 | normal | mid | normal | (typing)
"Sure — I'll set the service address to Brookhaven Court effective the first, and add your email for the install confirmation. Done."
```

```
[T32] CUSTOMER | satisfied:3 | normal | mid | normal
"You're a lifesaver, man. Way easier than I thought."
```

```
[T33] AGENT | warm:3 | normal | mid | normal
"No problem at all, that's what we're here for."
```

```
[T34] CUSTOMER | curious:2 | normal | mid | normal
"So the move's all set? Nothing Kevin needs to do?"
```

```
[T35] AGENT | professional:3 | normal | mid | normal
"All set on our end. To summarize: I upgraded the account to the five-hundred plan at seventy-nine ninety-nine with a small prorated charge this cycle, updated the service address to Brookhaven Court effective the first, and added your email for the install confirmation. The transfer team will follow up to schedule the install."
```

```
[T36] CUSTOMER | satisfied:3 | normal | mid | normal
"Awesome. That's everything."
```

```
[T37] AGENT | professional:3 | normal | mid | normal
"Is there anything else I can help you with today?"
```

```
[T38] CUSTOMER | satisfied:2 | normal | mid | normal
"Nope, you covered it. Thanks Daniel."
```

```
[T39] AGENT | professional:3 | normal | mid | normal
"Your case reference number is N-X-L dash four-two-seven-seven-four-one-six. You'll get a brief survey after we hang up."
```

```
[T40] CUSTOMER | satisfied:2 | normal | mid | normal
"Cool."
```

```
[T41] AGENT | warm:3 | normal | mid | normal
"Thanks for calling NexaLink. Good luck with the move, Brandon."
```

```
[T42] CUSTOMER | happy:2 | normal | mid | normal
"Appreciate it. Bye."
```
