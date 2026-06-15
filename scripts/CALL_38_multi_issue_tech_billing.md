# CALL_38 — Multi-Issue Call: Intermittent Drops + Billing Question

```yaml
call_id: CALL_38_multi_issue_tech_billing
duration_estimate: 7m 00s
turns: 48
sop_primary: SOP-03 (Technical Support Troubleshooting) + SOP-02 (Billing)
policy_refs: [CS-RULE-001, CS-RULE-002, CS-RULE-003, CS-RULE-004, CS-RULE-009, CS-RULE-010, CS-RULE-011, CS-RULE-018, CS-RULE-019, CS-RULE-020, CS-RULE-021]
kb_refs: [Section 2.2 - Router & WiFi Facts, Section 3.1 - Billing Concepts]
customer_profile:
  name: "Nathan Brooks"
  account_number: "6690-2218-77"
  voice_hint: "male, 40s, neutral US accent, organized, has two separate things on a list"
agent_profile:
  name: "Marcus"
  voice_hint: "male, mid-30s, friendly neutral US accent, methodical instructional cadence"
emotional_arc: "businesslike -> engaged -> reassured -> satisfied"
expected_outcome: "Customer raises TWO unrelated issues in one call: (1) intermittent connection drops every evening, and (2) a $7 line-item on his bill he doesn't recognize. Marcus handles both cleanly: diagnoses the drops as 2.4GHz channel congestion and queues a firmware push + channel change (SOP-03), then explains the $7 charge is a regional sports surcharge he opted into and removes it going forward (SOP-02). Re-engages during the line scan (CS-RULE-009). PASS — exemplary multi-issue handling, both threads resolved and summarized separately."
```

## Coverage

| Element | Where | Notes |
|---|---|---|
| Greeting | T01 | CS-RULE-001 verbatim — PASS |
| Recording notice | T02 | CS-RULE-002 — PASS |
| Acknowledge both stated reasons | T05 | CS-RULE-003 — PASS (captures both issues up front) |
| 3-of-5 verification | T05–T11 | CS-RULE-004 — PASS |
| Issue 1: technical diagnosis (SOP-03) | T13–T28 | process adherence — PASS |
| Re-engagement during line scan | T21, T23 | CS-RULE-009 — PASS |
| Talk-ratio managed across both topics | T15–T26 | CS-RULE-010 — PASS |
| Issue 2: billing line-item explained (SOP-02) | T31–T39 | process adherence — PASS |
| A.C.E.S. light on the surprise charge | T33 | CS-RULE-011 — PASS |
| Root cause for BOTH issues | T41 | CS-RULE-018 — PASS |
| Two-part resolution summary | T43 | CS-RULE-019 — PASS |
| Anything else + case ref + survey | T45, T47 | CS-RULE-020, CS-RULE-021 — PASS |

---

## Dialog

```
[T01] AGENT | professional:3 | normal | mid | normal
"Thank you for calling NexaLink Telecommunications Broadband and Support. My name is Marcus. Who do I have the pleasure of speaking with today?"
```

```
[T02] AGENT | professional:3 | normal | mid | normal
"And this call may be recorded for quality assurance and training purposes."
```

```
[T03] CUSTOMER | cooperative:3 | normal | mid | normal
"Hi Marcus, Nathan Brooks. I've actually got two separate things — my internet keeps dropping in the evenings, and there's a charge on my bill I don't recognize. Figured I'd do both in one call."
```

```
[T04] AGENT | warm:3 | normal | mid | normal
"Smart — let's knock out both. I appreciate you batching them."
```

```
[T05] AGENT | professional:3 | normal | mid | normal
"So I've got two items: an intermittent connection drop in the evenings, and a billing line you don't recognize. I'll take the connection issue first since that's usually the bigger headache, then we'll sort the bill. Before I pull anything up, let me verify the account — your account number?"
```

```
[T06] CUSTOMER | cooperative:3 | normal | mid | normal
"Six-six-nine-zero, two-two-one-eight, seven-seven."
```

```
[T07] AGENT | professional:3 | normal | mid | normal | (typing)
"Thank you. Last four of the payment method on file?"
```

```
[T08] CUSTOMER | cooperative:3 | normal | mid | normal
"Three-three-zero-one."
```

```
[T09] AGENT | professional:3 | normal | mid | normal
"And the full name on the account?"
```

```
[T10] CUSTOMER | cooperative:3 | normal | mid | normal
"Nathan James Brooks."
```

```
[T11] AGENT | reassuring:3 | normal | mid | normal
"Perfect, you're fully verified, Mr. Brooks."
```

```
[T12] CUSTOMER | satisfied:2 | normal | mid | normal
"Great."
```

```
[T13] AGENT | professional:3 | normal | mid | normal
"Let's start with the drops. When you say evenings — roughly what time, and does everything drop at once or just some devices?"
```

```
[T14] CUSTOMER | thoughtful:3 | normal | mid | normal
"Around eight, nine PM. It's everything on WiFi — phones, the TV. The drop lasts a minute or two then comes back. Wired stuff seems fine."
```

```
[T15] AGENT | professional:3 | normal | mid | normal
"That last detail is the key one — wired is fine, only WiFi drops, and it clusters in the evening. That pattern is almost always channel congestion on the 2.4 gigahertz band, when all your neighbours' networks get busy at the same time."
```

```
[T16] CUSTOMER | curious:3 | normal | mid | normal
"Huh. So it's not my equipment failing?"
```

```
[T17] AGENT | reassuring:3 | normal | mid | normal
"Doesn't look like it. The 2.4 band has only a few non-overlapping channels, and in dense areas they get crowded at peak hours. Two things fix it: pushing your router to auto-select a cleaner channel, and nudging your newer devices onto the 5 gigahertz band, which is far less congested. Let me run a quick line scan from my side first to confirm signal levels are healthy."
```

```
[T18] CUSTOMER | cooperative:3 | normal | mid | normal
"Go for it."
```

```
[T19] AGENT | professional:3 | normal | mid | normal | (typing)
"Starting the scan now."
```

```
[T20] CUSTOMER | neutral:2 | normal | mid | normal
"How long's it take?"
```

```
[T21] AGENT | warm:3 | normal | mid | normal
"About thirty seconds. I'm still here with you, Mr. Brooks — the scan is running. Thank you for your patience."
```

```
[T22] CUSTOMER | calm:2 | normal | mid | normal
"No problem."
```

```
[T23] AGENT | professional:3 | normal | mid | normal | (pause)
"Still going on my side — just gathering the channel data for your area."
```

```
[T24] AGENT | reassuring:3 | normal | mid | normal
"Okay, scan's done. Your downstream signal and noise levels are clean — confirms the line itself is healthy. And sure enough, your 2.4 band is sitting on channel six, which in your area is the single most congested channel."
```

```
[T25] CUSTOMER | satisfied:3 | normal | mid | normal
"That tracks. Channel six, of course."
```

```
[T26] AGENT | professional:3 | normal | mid | normal
"I'm going to do two things. First, I'll push a firmware update tonight that switches your router to automatic channel selection, so it'll move off congested channels on its own. Second, I'd suggest renaming your 5 gigahertz network to something obvious so you can connect your phone and TV to it directly — that band rarely congests."
```

```
[T27] CUSTOMER | cooperative:3 | normal | mid | normal
"Can you push the firmware now or does it have to be tonight?"
```

```
[T28] AGENT | professional:3 | normal | mid | normal
"It queues for tonight around 3 AM so it doesn't interrupt you — the router reboots once during the push. By tomorrow morning you'll be on auto channel selection. If the evening drops continue past a couple of days, call back and we'll look at a band-steering config or a mesh node."
```

```
[T29] CUSTOMER | satisfied:3 | normal | mid | normal
"Great. That's issue one. Want to do the bill?"
```

```
[T30] AGENT | warm:3 | normal | mid | normal
"Let's do it. What's the line item that caught your eye?"
```

```
[T31] CUSTOMER | curious:3 | normal | mid | normal
"There's a seven-dollar charge labelled R-S-N surcharge. I have no idea what that is."
```

```
[T32] AGENT | professional:3 | normal | mid | normal | (typing)
"Let me pull the bill. R-S-N stands for Regional Sports Network — it's a surcharge that comes bundled when a TV package includes regional sports channels."
```

```
[T33] AGENT | empathetic:3 | normal | mid | normal
"I can see how that's confusing if you didn't knowingly sign up for it. Let me check how it got on there before we assume anything."
```

```
[T34] CUSTOMER | neutral:3 | normal | mid | normal
"Please."
```

```
[T35] AGENT | professional:3 | normal | mid | normal
"Okay — it was added when you took the Sports Plus add-on back in March. It's a real opt-in on the account, not an error, but it is optional. If you're not watching the regional sports channels, we can remove the add-on and the seven-dollar surcharge goes with it."
```

```
[T36] CUSTOMER | thoughtful:3 | normal | mid | normal
"Honestly I forgot I even added that. I don't watch it. Take it off."
```

```
[T37] AGENT | professional:3 | normal | mid | normal | (typing)
"Removing Sports Plus and the R-S-N surcharge now. That's a seven-dollar reduction starting your next billing cycle."
```

```
[T38] CUSTOMER | satisfied:3 | normal | mid | normal
"Good. I'd rather keep the seven bucks."
```

```
[T39] AGENT | reassuring:3 | normal | mid | normal
"Done — it's off. Just so it's clear: this isn't a refund of a wrongful charge, since it was a real opt-in. It's a removal going forward. From next cycle, it's gone."
```

```
[T40] CUSTOMER | cooperative:3 | normal | mid | normal
"That's fair. I did have it, I just didn't use it. Going forward is fine."
```

```
[T41] AGENT | warm:3 | normal | mid | normal
"Exactly right. So to give you the full picture on both — the evening drops are channel congestion on 2.4 gigahertz, not a fault, and the surcharge was a real but forgotten add-on."
```

```
[T42] CUSTOMER | satisfied:3 | normal | mid | normal
"Makes sense on both counts."
```

```
[T43] AGENT | reassuring:3 | normal | mid | normal
"To summarize the two items: One — for the evening WiFi drops, I confirmed the line is healthy, queued a firmware push tonight to enable automatic channel selection, and recommended moving your devices to the 5 gigahertz band. Two — for the bill, I removed the Sports Plus add-on and its seven-dollar regional sports surcharge effective next cycle. Does that all sound right?"
```

```
[T44] CUSTOMER | grateful:3 | normal | mid | normal
"Perfect. Two for two. Thanks, Marcus."
```

```
[T45] AGENT | warm:3 | normal | mid | normal
"My pleasure. Is there anything else I can help you with today, Mr. Brooks?"
```

```
[T46] CUSTOMER | calm:2 | normal | mid | normal
"Nope, you covered it."
```

```
[T47] AGENT | warm:3 | normal | mid | normal
"Your case reference number is N-X-L dash three-eight-zero-six-six-two-one. You'll receive a brief survey after we hang up — if you have a moment, we'd really appreciate the feedback."
```

```
[T48] AGENT | warm:3 | normal | mid | normal
"Thank you for being a NexaLink customer, Mr. Brooks. Have a great rest of your evening."
```
