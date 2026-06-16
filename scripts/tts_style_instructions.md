# VocalMind — Google TTS Style Instructions

Companion guide to the call scripts in `/scripts/`. This file gives the natural-language prompts to feed Google's controllable TTS (Gemini-TTS / Chirp 3 HD / equivalent) so that emotion tags in the scripts translate into believable audio.

The principle: the script tag (`emotion:INTENSITY | pace | pitch | volume | paralinguistics`) is **structured metadata**. The TTS API wants **natural-language style prompts**. This file is the lookup table that converts one to the other.

---

## 1. Voice Selection Per Speaker

Pin one Google voice ID per character so every utterance from that character sounds like the same person across the whole call.

### Recommended Google voices (Chirp 3 HD / Gemini-TTS)

| Character | Script(s) | Voice ID | Backup | Why |
|---|---|---|---|---|
| **AGENT — Priya** | CALL_01 | `en-US-Chirp3-HD-Aoede` | `en-US-Neural2-F` | Warm, mid-pitch female; carries empathy without sounding scripted. |
| **AGENT — Daniel** | CALL_02 | `en-US-Chirp3-HD-Charon` | `en-US-Neural2-D` | Professional male, slightly younger timbre; under-pressure feel. |
| **T2_AGENT — Sarah Chen** | CALL_02 | `en-US-Chirp3-HD-Kore` | `en-US-Neural2-C` | Lower-pitched female, authoritative-warm. |
| **AGENT — Marcus** | CALL_03 | `en-US-Chirp3-HD-Puck` | `en-US-Neural2-J` | Friendly mid-30s male, methodical cadence. |
| **CUSTOMER — Sofia Reyes** | CALL_03 | `en-US-Chirp3-HD-Leda` + light Spanish accent prompt | `es-US-Neural2-A` (in English) | ESL fluent; need slightly slower default cadence. |
| **AGENT — Aisha** | CALL_04 | `en-US-Chirp3-HD-Despina` | `en-US-Neural2-H` | Warm low-mid female; natural deliberate-reassurance register. |
| **T2_AGENT — James** | CALL_04 | `en-US-Chirp3-HD-Orus` | `en-US-Neural2-A` | Calm authoritative male, 40s. |
| **CUSTOMER — Margaret Holloway** | CALL_04 | `en-US-Chirp3-HD-Achird` (older female) | `en-US-Neural2-G` | Late 60s; deliberately soft, slightly tremulous baseline. |
| **AGENT — Hannah** | CALL_05 | `en-US-Chirp3-HD-Erinome` | `en-US-Neural2-F` | Composed female; must hold register under abuse. |
| **T3_AGENT — Robert** | CALL_05 | `en-US-Chirp3-HD-Iapetus` | `en-US-Studio-Q` | Older male, low pitch, very calm authority. |
| **CUSTOMER — Marcus Whitfield** | CALL_01 | `en-US-Chirp3-HD-Algieba` | `en-US-Neural2-D` | Mid-40s male, mild Midwest, weary baseline. |
| **CUSTOMER — Linda Park** | CALL_02 | `en-US-Chirp3-HD-Pulcherrima` | `en-US-Neural2-E` | 50s female, sharp articulation. |
| **CUSTOMER — Brett Donovan** | CALL_05 | `en-US-Chirp3-HD-Sadachbia` | `en-US-Neural2-J` | 30s male, must escalate volume cleanly. |
| **IVR** | All | `en-US-Studio-O` | `en-US-Neural2-F` | Studio voice = the flat broadcast register IVRs actually use. |

**Tip:** if your TTS endpoint doesn't support all Chirp 3 HD names, the Neural2 backups produce the same character mapping with about 80% of the expressiveness.

---

## 2. The Style Prompt Template

For Gemini-TTS / Chirp 3 HD, you pass a natural-language style prompt alongside the text. Use this template:

```
[base_voice_persona] + [emotion_clause] + [intensity_clause] + [prosody_clause] + [paralinguistic_clause if present]

Then say: "<utterance text>"
```

### Worked example — turn `[T29]` from CALL_01

Tag line:
```
[T29] CUSTOMER | frustrated:4 | fast | mid | loud
"Wait — two dollars? For two days with no internet? Are you serious?"
```

Generated style prompt:
```
You are Marcus Whitfield, a 40-year-old man from the US Midwest with a slight regional accent and a weary baseline. You feel sharply frustrated — almost insulted — by what you just heard. The frustration is high but not yet shouting (intensity 4 of 5). Speak faster than your normal pace, with mid pitch but raised volume. The first word "Wait" is an interruption, almost cutting off. Pause briefly after the em-dash before "two dollars". Let "Are you serious?" rise at the end with disbelief, not yet anger.

Then say: "Wait — two dollars? For two days with no internet? Are you serious?"
```

That's the unit you generate per turn.

---

## 3. Emotion → Style Prompt Lookup

Drop these clauses into the template above. They are written for Google's controllable TTS, which responds well to embodied, sensory cues ("breathe in slightly", "voice tightens") rather than abstract labels alone.

### 3.1 Calm / Professional / Neutral register

| Tag | Style clause |
|---|---|
| `neutral:1-2` | Speak in your normal conversational baseline. Even tone, neither warm nor cold. No emphasis. |
| `calm:2-3` | Voice settled, breath unhurried. Slightly lower pitch than baseline. Warmth optional. |
| `professional:3` | Confident, clear articulation. Mid pitch, measured pace. Like a clerk reading information they know well. |
| `cooperative:2-3` | Open, willing tone. Slight upward intonation at the end of phrases to signal engagement. |
| `uncertain:2-3` | Slight upward pitch on statements; voice softens on the uncertain word. A small pause or "um" quality before the key answer, even without explicit filler. |
| `thoughtful:2-3` | Slightly slower pace; micro-pause before responding. Pitch mid-to-low. The listener hears someone choosing words carefully, not hesitating nervously. |
| `concentrating:2` | Very quiet, almost self-directed delivery. Volume slightly under baseline. Pace slow. Each word has deliberate spacing, as if narrating an action in progress. No emotional colour. |
| `surprised:3` | Start with a slight breath-catch. Pitch rises sharply on the first stressed word, then levels. Mid volume. |

### 3.2 Warm / Empathetic register

| Tag | Style clause |
|---|---|
| `warm:3-4` | Voice opens up. Slightly slower pace, gentle smile audible in tone. Pitch slightly raised mid-phrase, lowered at sentence end. |
| `empathetic:3-4` | Softer voice, slower pace, slight breathiness on the first word. Pitch drops on the comforting verbs ("I hear you", "I understand"). |
| `reassuring:3-4` | Lower pitch, deliberate pace, weight on the verbs that carry the reassurance. Pause briefly before key promises. |
| `apologetic:3-4` | Softer volume, head-down delivery. Slight downward pitch contour. Lengthen the apology word ("I'm so sorry"). |
| `grateful:3` | Slight smile in voice, warm release of breath on "thank you". Slight pitch rise on "thank", drop on "you". |
| `satisfied:3-4` | Settled, resolved tone. Slightly lower pitch than baseline. No smile-in-voice (that is warm), but a quiet fullness — the feeling of completion. Volume normal to quiet. |
| `partially_satisfied:3` | The voice carries two signals at once: mild relief (that something was offered) and mild residual doubt. Slight uplift at end of phrases, but the breath doesn't fully release. |
| `hopeful:3` | Slightly softer volume, pitch gently lifted. The voice opens upward — tentative warmth. Not yet grateful; still conditional. |

### 3.3 Stress / Negative-affect register

| Tag | Style clause |
|---|---|
| `tired:3` | Slow pace. Slight breath out at the start. Pitch slightly low. Energy noticeably below baseline. |
| `confused:3` | Pitch rises at end of statements as if they were questions. Slight hesitation between phrases. |
| `worried:3-4` | Voice tightens slightly. Faster breath. Pitch creeping upward as the sentence progresses. |
| `anxious:3-4` | Audible tension. Voice slightly compressed. Pace fluctuates — rushes, then catches, then rushes again. |
| `afraid:4-5` | Voice thins. Volume drops involuntarily. Slight tremor on vowels. Pitch elevated. Words may trail or break. |
| `frustrated:3-4` | Pace quickens. Volume up. Stress on the operative verbs. Sharper consonants. Pitch rises on emphasis. |
| `angry:4-5` | Loud, sharp consonants, fast pace, pitch elevated. Bite on the noun the anger is directed at. Avoid yelling distortion — keep it clean. |
| `hostile:4-5` | Edged delivery. Loud but controlled. Words land like punches. Sneering quality on insults. |
| `abusive:5` | Volume peaks. Pace fast. Words hit hard, no softening. Slight scoff or laugh of contempt allowed. (Sanitized — never include slurs in audio.) |
| `resigned:3` | Pace slows. Pitch flattens to monotone. Volume drops. Audible exhale. |
| `impatient:3-4` | Slightly faster pace than baseline. Clipped syllables; the speaker is not finishing sentences the way they would if they had time. Pitch rises slightly on the operative verb. Volume up at intensity 4. |
| `curt:3` | Short sentences, reduced prosody range. No warmth, no harshness — just efficiency. Pitch flat, pace business-like. The voice does the minimum to communicate. |
| `irritated:3` | Like frustrated but lower volume and more controlled. Sharpness lives in consonants, not loudness. Pace slightly faster than baseline. Pitch slightly elevated. |
| `distressed:4` | Voice thinner than afraid but less tremor. Breath audibly shorter. Pitch elevated, pace irregular — rushing then catching. The voice wants to hold together but can't quite. |
| `tearful:3-4` | Voice catches on vowels. Slight wet quality. Pitch trembles. Volume lower. Pace slower with micro-pauses. |
| `concerned:4` | Pitch lower than worried. Slower than anxious. The weight of recognition rather than panic. |
| `shocked:4` | Brief pause before the response. Pitch jump on the first word. Volume drops mid-sentence as belief sets in. |
| `relieved:3-4` | Audible exhale on the first word. Voice opens up. Pitch drops then rises into a smile. |
| `vindicated:3` | "I knew it" tone. Slight rise on the operative word. Mild self-satisfaction. |
| `skeptical:3` | Pitch flat-with-edge. Slight pause before the response. Inflection of "I don't believe you yet". |
| `suspicious:3-4` | Lower pitch, slower pace, narrowed delivery. Words feel weighed. |

### 3.4 Authority / Firmness register

| Tag | Style clause |
|---|---|
| `firm:3-4` | Lower pitch, slower pace, no hedging. Each sentence is a complete unit with a hard period. |
| `cautious:3-4` | Measured pace. Slight pause before sensitive words. Lower volume to invite attention. |
| `curious:3` | Slight upward pitch contour. Engaged tone. Pace neutral. |
| `resolute:3-4` | Firm pitch, slower pace. The voice has made a decision and is not revisiting it. Slightly lower than baseline. Each word lands with quiet finality. No aggression — just settled certainty. |

### 3.6 Compound / Blended Tags

These are used where two emotions are genuinely simultaneous. Weight the first word first, then blend in the second.

| Tag | Style clause |
|---|---|
| `vindicated_angry:4` | Open with the brief satisfaction of being proven right — a half-beat of "I knew it" — then let anger take over within the same sentence. Pace fast, pitch high, volume loud. The bitterness of being right about something bad. |
| `resolute_afraid:4` | The voice is afraid (slight pitch elevation, thinning) but is holding itself still and forceful on the key words. Do not let the fear win. The listener should hear both. |
| `grateful_afraid:4` | Relief and residual fear co-present. Warm and breathy on "thank you" phrases; voice catches slightly when referring to the frightening thing. Gratitude in the melody, fear in the breath. |

---

### 3.5 Specialty (children, elderly, ESL)

| Tag | Style clause |
|---|---|
| ESL fluent (Sofia Reyes) | Add to base persona: "speak with a mild Latin American Spanish accent. Slightly slower pace as a default. Occasional micro-hesitations between English clauses. Pronounce vowels with Spanish purity — 'i' as /i/, 'e' as /e/." |
| Elderly soft (Margaret Holloway) | Add to base persona: "voice has a soft baseline tremor that increases with stress. Slower pace by default. Slight breath audibility at sentence starts. Pitch lower than a younger woman's." |

---

## 4. Intensity Calibration

Intensity is a multiplier on the emotion clause, not a separate emotion. Same emotion at intensity 2 vs 5 should sound clearly different but recognizably the same affect.

| Level | Description | Practical effect on TTS prompt |
|---|---|---|
| 1 | Trace amount, almost neutral | "barely perceptible — only the shape, not the energy" |
| 2 | Subtle | "lightly audible, easy to miss" |
| 3 | Clearly present (default audible baseline) | no qualifier needed |
| 4 | Strong, dominates the line | "strongly — this emotion is the main thing the listener should hear" |
| 5 | Extreme, near boundary | "at full intensity, but never breaking voice quality (no distortion or yelling-into-mic)" |

**Rule of thumb:** if a single call reaches intensity 5 more than twice, redistribute. Audiences habituate fast, and the data needs ground-truth variance to teach an emotion model the gradient.

---

## 5. Pace / Pitch / Volume — Prompt Phrasing

Plain words work better than SSML for Chirp 3 HD. Use these.

| Tag | Phrase to add to prompt |
|---|---|
| `pace: slow` | "speak more slowly than your baseline, with a small pause between clauses" |
| `pace: normal` | (omit) |
| `pace: fast` | "speak faster than baseline, words running together at clause boundaries" |
| `pace: rushed` | "speak rushed, words tumbling out, not waiting for natural breath" |
| `pitch: low` | "lower your pitch slightly below your baseline" |
| `pitch: mid` | (omit) |
| `pitch: high` | "raise your pitch noticeably; voice sits in the upper part of your range" |
| `volume: quiet` | "quieter than baseline, as if speaking close to the microphone" |
| `volume: normal` | (omit) |
| `volume: loud` | "louder than baseline; voice projects but does not distort" |

---

## 6. Paralinguistics

Add these only when explicitly tagged in a turn. Do not sprinkle automatically — the script tags choose where they belong.

| Tag | TTS prompt clause |
|---|---|
| `(sigh)` | "begin with a soft audible exhale before the first word" |
| `(pause)` | "include a one-second pause where the dash or ellipsis appears in the text" |
| `(throat-clear)` | "begin with a brief throat clear, then the first word" |
| `(typing)` | (do not vocalize — add ambient typing sound in post; agent voice continues normally) |
| `(overlap)` | "begin while the previous speaker is still finishing — start mid-word energy" — handle overlap in mixing, not synthesis |
| `(trails-off)` | "let the final words fade in volume and pitch, ending unfinished" |
| `(self-correct)` | "include a brief stutter or restart on the corrected word" |
| `(laugh-soft)` | "include a brief soft exhale-laugh before or within the line" |
| `(interrupting)` | (mixing layer — generate the line normally; in post, cut the previous turn ~0.4s short) |

---

## 7. Per-Script Direction Notes

### CALL_01 — Refund Outage (the "clean happy path")

Overall emotional shape: customer enters mildly frustrated, gets validated, ends grateful. Agent stays warm and steady throughout. Dynamic range: low. This is the calibration baseline — if STT and emotion models can't get this one right, nothing else will land.

Direction:
- Keep agent volume **flat** across the whole call. The warmth is in pitch contour and pace, not loudness.
- Customer's frustration peaks at T29 (intensity 4). That is the only loud moment. Everything before is intensity 2-3. After T30, customer steadily releases — by T46 he's intensity 3 grateful.
- Long pause ambience cues (T20, T28) should include light typing/keystroke ambient in post-mix.

### CALL_02 — Billing Dispute Escalation

Overall shape: customer arrives frustrated, escalates through anger as new charges are revealed, transfers, settles. Agent under pressure but composed. Tier 2 enters with a noticeably lower, slower, more authoritative voice — that contrast is the audible signal of the warm transfer.

Direction:
- T22, T28, T30, T32 are the angry peaks. Intensity 4-5. Use them sparingly elsewhere — these need to feel earned.
- Critical: agent Daniel's voice should show a small audible tightness between T31 and T37 — under pressure but holding form. A subtle prompt addition like "voice slightly tighter, breath shorter" works.
- Tier 2 (Sarah) enters at T43. Mark a clear voice change: lower pitch, slower pace, more pause. The listener should hear "different person" in two seconds.
- Customer's de-escalation between T46 and T56 is the most subtle modeling target. Linda transitions from anger → tired → cooperative. Each step should be one notch down in volume + one notch slower in pace.

### CALL_03 — Slow Internet (ESL customer)

Overall shape: low-affect call. The emotion target is the contrast between Sofia's tired baseline and her relieved peak at T48. Most of the call sits at intensity 2.

Direction:
- Pin Sofia's accent prompt at the top of every utterance. Do not let the TTS drift to pure American English mid-call.
- Agent Marcus pace is intentionally **methodical** — slightly slower than CALL_01's Priya. Each instruction step gets its own breath.
- T48 ("Oh! Two hundred and twelve Mbps! It's working!") is the emotional payoff. Push pitch up, volume up, smile audible. This is the one moment in the call that should be intensity 4.
- Re-engagement turns (T20-T21 in CALL_01, T32 in CALL_03) — keep agent voice **identical** to baseline. The whole point of the rule is that the customer hears the agent is still there, not anxious.

### CALL_04 — Access Recovery / Suspected Fraud

Overall shape: the most complex call emotionally. Margaret moves through worried → afraid → tearful → relieved. Two agents, both calibrated to her vulnerability.

Direction:
- Margaret's tremor should grow with intensity. At intensity 3 it's barely there; at intensity 5 (T25, T31, T49) the tremor is audible. Do not overdo it — she is frightened, not breaking.
- Aisha (Tier 1 agent) speaks slower than every other agent in the corpus. Her pace prompt should explicitly say "slower than your baseline, with deliberate space between sentences". Margaret needs that space.
- T39 (Aisha's off-line briefing to James) should sound mechanically different — shift voice characteristics slightly to suggest she's now talking to a colleague, not the customer. Slightly faster, slightly lower pitch, less warmth, more clinical.
- James (T2) enters at T42 with an even lower-pitched, even slower delivery than Aisha. He's the rock-solid presence Margaret needs.
- T55 (Margaret's final "I was — I was so frightened") is the emotional high point of the entire corpus. It should land. Tearful intensity 4, with a real sigh on the final phrase.

### CALL_05 — Retention with Abuse

Overall shape: agent must hold composure while customer escalates. The dramatic question is whether the agent's voice quality changes. **It should not.** Hannah's intensity stays at 3 the entire call. That contrast is the most important signal in the audio.

Direction:
- Brett's voice escalates: T03 (volume loud, intensity 4) → T15 (intensity 5, pitch high) → T23 (intensity 5, near-yelling). Push volume but **never distort**. If your TTS clips at high volume, drop intensity to 4 and let the consonants do the work.
- Hannah's voice is the through-line. Keep her: pitch low, pace slow, volume normal. Every single turn. The only register change Hannah is allowed is at T16, T22, T24 where `firm` replaces `calm` — slightly more weight on the verbs, but still no volume increase.
- Robert (T3) enters at T27. He should be even lower-pitched and slower than Hannah. His T29 boundary-setting line is the most important non-customer line in the call. Land it firm but never escalated.
- The 3-strike protocol turns (T16, T22, T24) are the closest thing to ground truth for "policy-trigger detection" models. Make them sound naturally embedded in conversation — not robotic citations of policy. The phrase "Strike One" should be delivered as quietly serious, not announced.

---

## 8. Background Ambience (Mixing Layer)

For realism — add these in post-mix, not in the TTS prompt itself.

| Source | Ambience | Level |
|---|---|---|
| Agent side (all calls) | Soft call-center murmur, distant headset chatter, quiet HVAC | -32 dB to -28 dB |
| Customer side — CALL_01 | Quiet home office, distant traffic | -36 dB |
| Customer side — CALL_02 | Quiet home, occasional dish/cup sound | -36 dB |
| Customer side — CALL_03 | Domestic background, possible TV bleed | -34 dB |
| Customer side — CALL_04 | Very quiet home, occasional grandfather clock | -38 dB |
| Customer side — CALL_05 | Mild road noise (suggests calling from car or driveway) | -32 dB |
| Codec | G.711 μ-law narrowband emulation across the whole call | full mix |
| Tier transfer (CALL_02, 04, 05) | Brief hold-music snippet on customer side, none on agent side | -24 dB during hold turns only |

The narrowband codec pass at the end is what makes synthetic calls actually sound like phone calls and not podcast clips. Don't skip it.

---

## 9. Generation Pipeline (Practical)

Pseudocode for batch generation:

```python
for script in scripts:
    voices = load_voice_pins(script.metadata)
    for turn in script.turns:
        emotion_clause = EMOTION_LOOKUP[turn.emotion][turn.intensity]
        prosody_clause = build_prosody(turn.pace, turn.pitch, turn.volume)
        paralang_clause = PARA_LOOKUP.get(turn.paralinguistic, "")

        style_prompt = f"""
        You are {turn.speaker_persona}.
        {emotion_clause}
        {prosody_clause}
        {paralang_clause}
        Then say: "{turn.text}"
        """

        audio = google_tts.synthesize(
            voice=voices[turn.speaker],
            style_prompt=style_prompt,
            text=turn.text,
        )
        save(f"{script.id}/{turn.id}.wav", audio)

    # post-processing
    mix_with_ambience(script.id)
    apply_narrowband_codec(script.id)
    if script.has_overlap:
        apply_overlap_offsets(script.id)
```

---

## 10. Known Limits & Workarounds

- **Chirp 3 HD struggles with sustained anger past intensity 4.** If T30 in CALL_02 sounds shouty-distorted, fall back to Neural2 for that single turn and rejoin Chirp for the next.
- **ESL accent drift.** Re-prompt the accent at every Sofia turn — it does not persist reliably across requests.
- **Tremor on elderly voices** is best added as a light vibrato in post (LFO at ~5 Hz, depth ±15 cents) on Margaret's high-intensity turns. Don't rely on the TTS prompt alone.
- **Crying/tearful** rarely renders cleanly in any current TTS. Get a clean delivery, then add a single soft sniff sample in post on the marked turns.
- **Overlap** — generate each turn in isolation, then in the mixer cut the earlier turn 300-500 ms before its end and crossfade the new turn in. Do not try to make the TTS produce an overlap; it will sound wrong.

---

## 11. VocalMind Ground-Truth Emotion Mapping

VocalMind's emotion classifier (acoustic + text fusion) outputs exactly **seven canonical labels**, defined in `backend/app/core/inference_contracts.py::normalize_emotion_label`:

```
happy | angry | sad | frustrated | surprised | neutral | unknown
```

The rich TTS vocabulary used in scripts (~50 fine-grained tags) is collapsed onto these 7 labels by `emotion_map.py::TTS_TO_VOCALMIND_EMOTION`. The mapping is canonical — when writing new scripts, **only use TTS tags that already have a projection** (otherwise the ground-truth file flags the turn as `unknown`).

| VocalMind label | TTS tags that project to it |
|---|---|
| `neutral` | neutral, calm, professional, cooperative, uncertain, thoughtful, concentrating, curious, cautious, firm, resolute, apologetic |
| `happy` | warm, empathetic, reassuring, grateful, satisfied, partially_satisfied, hopeful, vindicated, relieved, grateful_afraid |
| `angry` | angry, hostile, abusive, vindicated_angry |
| `sad` | tired, distressed, resigned, tearful |
| `frustrated` | worried, anxious, afraid, frustrated, impatient, irritated, curt, suspicious, skeptical, concerned, confused, resolute_afraid |
| `surprised` | surprised, shocked |

If you genuinely need a new TTS emotion shade, add it to **both** `src/generate_audio.py::EMOTION_STYLE` (with a natural-language clause) **and** `src/emotion_map.py::TTS_TO_VOCALMIND_EMOTION` (with its canonical projection) in the same change.

After writing or editing a script:
```bash
python src/build_ground_truth.py --check       # validate emotion coverage
python src/build_ground_truth.py               # emit ground_truth/*.json
```
