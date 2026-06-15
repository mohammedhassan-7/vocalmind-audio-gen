# CALL_48 — Unexpected Balance Jump, CD Maturity (Positive Surprise)

```yaml
call_id: CALL_48_cd_maturity_surprise
duration_estimate: 4m 15s
turns: 32
sop_primary: SOP-02 (General Service / Account Inquiry)
policy_refs: [BNK-CC-RULE-001, BNK-CC-RULE-002, BNK-CC-RULE-003, BNK-CC-RULE-004, BNK-CC-RULE-019, BNK-CC-RULE-020, BNK-CC-RULE-021, BNK-CC-RULE-022, BNK-CC-RULE-023]
kb_refs: [KB Section 1.3 - Certificates of Deposit]
customer_profile:
  name: "Vincent Russo"
  account_number: "M-T-B 3340-7781-55"
  voice_hint: "male, 60s, neutral US accent, started worried then delighted; expressive"
agent_profile:
  name: "Sarah"
  voice_hint: "female, mid-40s, neutral US accent, lower-pitched authoritative-warm"
emotional_arc: "worried -> surprised -> happy -> grateful"
expected_outcome: "Customer calls worried that several thousand dollars 'appeared' in his savings overnight, afraid it's a bank error he'll be liable for. Sarah verifies him, then happily explains it's legitimate: a 12-month CD he opened last year matured and the principal plus interest auto-deposited to his savings, plus a small loyalty-rate bonus. The customer is pleasantly surprised and relieved. Sarah offers (no pressure) to roll it into a new CD at the current rate or leave it. PASS — clean positive-surprise call; strong surprised + happy emotion ground truth. Short call."
```

## Coverage

| Element | Where | Notes |
|---|---|---|
| Greeting | T01 | BNK-CC-RULE-001 verbatim — PASS |
| Recording notice | T02 | BNK-CC-RULE-002 — PASS |
| Acknowledge reason for call | T05 | BNK-CC-RULE-003 — PASS |
| 3-of-5 verification | T05–T11 | BNK-CC-RULE-004 — PASS |
| Explains the balance change accurately (CD maturity) | T15–T19 | account inquiry — PASS |
| Positive surprise landed | T18, T20 | surprised/happy emotion — PASS |
| No-pressure renewal option offered | T25 | BNK-CC-RULE-018 spirit — PASS |
| Resolution summary | T27 | BNK-CC-RULE-019 — PASS |
| Anything else + case ref + survey | T29, T31 | BNK-CC-RULE-020/021/022/023 — PASS |

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
[T03] CUSTOMER | worried:3 | fast | mid | normal
"Hi, yes, Vincent Russo. Something strange happened — I logged in this morning and there's like eight thousand dollars more in my savings than there should be. I didn't put it there. Is this a mistake? Am I going to get in trouble for it?"
```

```
[T04] AGENT | reassuring:3 | normal | mid | normal
"Hello, Mr. Russo — let's get to the bottom of it, and I think you're going to like the answer. Money appearing is a lot less alarming than money disappearing, but I understand why an unexplained jump is unsettling. Let me verify the account and take a look."
```

```
[T05] AGENT | professional:3 | normal | mid | normal
"I understand you're calling about an unexpected increase in your savings balance. Could you give me your account number to start?"
```

```
[T06] CUSTOMER | cooperative:3 | normal | mid | normal
"Three-three-four-zero, seven-seven-eight-one, five-five."
```

```
[T07] AGENT | professional:3 | normal | mid | normal | (typing)
"Thank you. Your date of birth?"
```

```
[T08] CUSTOMER | cooperative:3 | normal | mid | normal
"January fourth, nineteen-sixty-one."
```

```
[T09] AGENT | professional:3 | normal | mid | normal
"And the last four of your Social Security number?"
```

```
[T10] CUSTOMER | cooperative:3 | normal | mid | normal
"Five-five-zero-one."
```

```
[T11] AGENT | reassuring:3 | normal | mid | normal
"Perfect — you're verified, Mr. Russo. Let me look at the recent activity."
```

```
[T12] CUSTOMER | worried:3 | normal | mid | normal
"I really didn't transfer anything. I swear."
```

```
[T13] AGENT | warm:3 | normal | mid | normal
"I believe you — and you didn't need to. I can already see exactly what happened, and it's entirely legitimate. Good news, in fact."
```

```
[T14] CUSTOMER | curious:3 | normal | mid | normal
"Okay…?"
```

```
[T15] AGENT | professional:3 | normal | mid | normal
"About a year ago you opened a twelve-month certificate of deposit — a CD — for seventy-five hundred dollars. That CD reached its maturity date yesterday."
```

```
[T16] CUSTOMER | thoughtful:3 | normal | mid | normal
"Oh… the CD. Right, I'd completely forgotten about that."
```

```
[T17] AGENT | warm:3 | normal | mid | normal
"Most people do — that's the beauty of them. When it matured, your principal plus the interest it earned over the year automatically deposited into your linked savings account. That's the eight thousand or so you're seeing."
```

```
[T18] CUSTOMER | surprised:4 | normal | high | normal
"Wait — so it's actually mine? All of it? It's not a glitch?"
```

```
[T19] AGENT | warm:4 | normal | mid | normal
"All of it is yours. Seventy-five hundred in principal, plus about four hundred and twenty in interest at the rate you locked in, plus there was a small loyalty bonus applied because you've held savings with us for over five years. So just over eight thousand, and every cent of it is yours to keep."
```

```
[T20] CUSTOMER | surprised:4 | normal | high | normal
"Oh, that's wonderful! I genuinely thought I was about to get a lecture about a banking error. This is the opposite!"
```

```
[T21] AGENT | warm:4 | normal | mid | normal
"The exact opposite — it's a little thank-you-for-saving from your past self. I love getting to deliver this kind of call."
```

```
[T22] CUSTOMER | happy:4 | normal | mid | normal
"I was bracing myself the whole way through verification!"
```

```
[T23] AGENT | warm:3 | normal | mid | normal
"You can unclench now — it's all good news today."
```

```
[T24] CUSTOMER | curious:3 | normal | mid | normal
"So is it just sitting in savings now? Should I do anything with it?"
```

```
[T25] AGENT | professional:3 | normal | mid | normal
"It's sitting safely in your savings earning the standard savings rate. You don't have to do anything at all. If you'd like it to keep earning the higher CD rate, I can roll it into a new CD at today's rate — but there's zero pressure, and leaving it in savings is perfectly fine. Entirely your call, now or later."
```

```
[T26] CUSTOMER | thoughtful:3 | normal | mid | normal
"Let me think about it and maybe call back. I want to enjoy the surprise for a day first."
```

```
[T27] AGENT | warm:3 | normal | mid | normal
"That's a perfectly good plan. To summarize: the eight-thousand-dollar increase is your matured twelve-month CD — principal, interest, and a loyalty bonus — deposited automatically into your savings. It's all yours, it's safe, and you can roll it into a new CD any time you like or simply leave it."
```

```
[T28] CUSTOMER | grateful:3 | normal | mid | normal
"Thank you so much, Sarah. You turned my whole morning around."
```

```
[T29] AGENT | warm:3 | normal | mid | normal
"That's the best thing I'll hear all day. Is there anything else I can help you with, Mr. Russo?"
```

```
[T30] CUSTOMER | happy:3 | normal | mid | normal
"No, that's it. I'm going to go tell my wife we found eight thousand dollars."
```

```
[T31] AGENT | warm:4 | normal | mid | normal
"Enjoy that conversation! Your case reference number is M-T-B dash four-eight-three-three-four-zero-seven. You'll receive a brief survey after we hang up."
```

```
[T32] AGENT | warm:3 | normal | mid | normal
"Thank you for banking with Meridian, Mr. Russo. Congratulations on the CD, and have a wonderful day."
```
