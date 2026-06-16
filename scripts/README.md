# VocalMind Ground-Truth Call Scripts

Synthetic call corpus for the VocalMind project. Designed as ground
truth for:

- **STT models** — verbatim transcription accuracy across accents,
  disfluencies, and overlap.
- **Emotion / sentiment models** — per-utterance affect labels with
  intensity, projected onto VocalMind's 7-label canonical vocabulary
  via `emotion_map.py`.
- **Policy / KB / SOP trigger evaluation** — every script has known
  LLM trigger points (verification, A.C.E.S., refund eligibility,
  ticket workflows, 3-Strike Protocol) drawn from the **flat
  single-tier** NexaLink policy pack.

All content is fictional. Customer names, account numbers, addresses,
and phone numbers are invented and must not match any real person.

---

## Active corpus

The active script set uses **two speakers per call only**: `AGENT` and
`CUSTOMER`. When a policy requires offline action, the agent opens a
back-office ticket from their seat (Manager Approval, Data Compliance,
Network Operations, Revenue Assurance, Field Service) — they never
transfer the call. The 3-Strike Protocol ends in call termination,
not transfer.

| ID | Scenario | SOP(s) Triggered | Customer Arc | Length |
|---|---|---|---|---|
| `CALL_01_refund_outage` | 48-hour internet outage refund — credit applied directly by agent (within $200 cap) | SOP-01, POLICY_03 | mild_frustrated → neutral → grateful | ~51 turns |
| `CALL_03_tech_support_slow_internet` | Slow home internet diagnostic, Path B; resolved at agent's seat with modem power-cycle | SOP-03 | tired → curious → relieved | ~54 turns |

Additional 2-agent scripts (CALL_06+) will be authored in the next
chat session covering billing dispute, account recovery, retention,
and other scenarios.

## Archived scripts

`./_legacy_multi_agent/` contains three older scripts (CALL_02,
CALL_04, CALL_05) that demonstrate **deprecated Tier 2 / Tier 3
escalation flows**. They are not part of the active dataset — the
parser and ground-truth builder ignore them — but they remain useful
as scenario reference when authoring 2-agent replacements. See
`_legacy_multi_agent/README.md` for details.

---

## File layout

```
tts-audio-generator/scripts/
├── README.md                          ← this file
├── tts_style_instructions.md          ← Google TTS style prompt guide
│                                       (Section 11 = VocalMind GT mapping)
├── CALL_01_refund_outage.md
├── CALL_03_tech_support_slow_internet.md
└── _legacy_multi_agent/
    ├── README.md
    ├── CALL_02_billing_dispute_escalation.md
    ├── CALL_04_access_recovery_fraud.md
    └── CALL_05_retention_abuse.md
```

Each script is a single self-contained markdown file with a YAML
header (metadata), a Coverage table (which rules / SOPs it
exercises), and the turn-by-turn dialog.

---

## Tag schema

Every utterance is annotated on one line of metadata directly above
the spoken text:

```
[TURN_ID] SPEAKER | emotion:INTENSITY | pace | pitch | volume | (paralinguistics)
"<utterance text>"
```

### Field definitions

| Field | Allowed values | Notes |
|---|---|---|
| `TURN_ID` | `T01`, `T02`, … | Sequential per call. Stable IDs for evaluation. |
| `SPEAKER` | `AGENT`, `CUSTOMER` | New scripts must use only these two. Legacy scripts also include `T2_AGENT`, `T3_AGENT`, `IVR`. |
| `emotion` | See `tts_style_instructions.md` Section 11 for the full rich vocabulary and its projection onto VocalMind's 7 canonical labels. | One primary label per utterance. |
| `INTENSITY` | `1` (subtle) – `5` (extreme) | 3 = clearly audible baseline. Reserve 5 for outliers. |
| `pace` | `slow`, `normal`, `fast`, `rushed` | Default `normal`. Use `slow` sparingly (≤20% of an agent's turns) — earlier output was too slow when over-tagged. |
| `pitch` | `low`, `mid`, `high` | Lower for de-escalation, higher for stress. |
| `volume` | `quiet`, `normal`, `loud` | Independent of pitch. Used heavily for abuse scenarios. |
| `paralinguistics` | optional, parenthesised — `(sigh)`, `(pause)`, `(throat-clear)`, `(typing)`, `(overlap)`, `(trails-off)`, `(self-correct)`, `(laugh-soft)` | Used selectively. |

### Example

```
[T14] CUSTOMER | frustrated:4 | fast | high | loud | (overlap)
"No, no, you don't get it — I've explained this three times already!"
```

---

## How to use

1. Write or edit a script under `scripts/CALL_NN_*.md`.
2. Validate the header grammar and emotion vocabulary:
   ```bash
   python src/generate_audio.py --dry-run --call CALL_NN_<name>
   python src/build_ground_truth.py --check
   ```
3. Generate audio:
   ```bash
   python src/generate_audio.py --call CALL_NN_<name>
   ```
4. Emit VocalMind ground-truth JSON:
   ```bash
   python src/build_ground_truth.py
   ```
5. Drop the merged `.wav` into VocalMind's
   `storage/audio/<org>/` folder and the matching `.json` into
   `storage/audio/<org>/evaluation/`.

---

## Coverage map (active corpus)

| Trigger / Rule | Script(s) |
|---|---|
| CS-RULE-001 (greeting verbatim) | All |
| CS-RULE-002 (recording notice) | All |
| CS-RULE-004 / 005 (3-of-5 verification) | All |
| CS-RULE-009 (dead-air re-engagement) | CALL_03 |
| CS-RULE-011 (A.C.E.S.) | CALL_01 |
| CS-RULE-018 / 019 (root cause + resolution summary) | CALL_01, CALL_03 |
| CS-RULE-021 (case ref + survey) | All |
| FIN-RULE-001 (5 refund eligibility categories) | CALL_01 |
| FIN-RULE-003 (hardwired speed test for refund eligibility) | CALL_03 |
| FIN-RULE-004 / 005 (agent $200 cap, no premature promises) | CALL_01 |
| FIN-RULE-010 (refund timeline script) | CALL_01 |

Compliance violations are **not** seeded into the active scripts yet —
they represent the happy-path-with-realistic-friction baseline. The
next batch will introduce explicit pass/fail pairs for every major
rule (one PASS + one FAIL example per rule).

---

## Notes for generation

- Scripts use US English by default. Customer voices vary (one ESL
  speaker in CALL_03) to test STT robustness.
- Numbers are spelled out the way speakers would naturally say them
  aloud.
- Account numbers, PINs, and last-four digits are written digit-by-
  digit.
- Overlapping speech is marked but kept rare — most TTS pipelines
  synthesize each turn independently and overlap is added in mixing.
