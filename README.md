# TTS Audio Generator

Generates realistic customer-service call audio from structured Markdown
scripts using Google **Gemini TTS** via **Vertex AI**.  Each call script
becomes a single merged `.wav` file whose filename matches the
[VocalMind](https://github.com/galalqassas/VocalMind) auto-ingest
watcher pattern, so the audio can be dropped straight into VocalMind's
storage folder and processed automatically.

---

## What it does

1. Parses a Markdown call script (`scripts/CALL_*.md`) into structured turns
   — each turn has a speaker, emotion, intensity, pace, pitch, volume,
   paralinguistic cues, and an utterance.
2. Builds a compact natural-language style prompt for every turn.
3. Synthesises each turn with Gemini TTS using a pinned per-speaker voice.
4. Merges turns with realistic silence gaps (`pause`, `overlap`, on-hold).
5. Writes the merged WAV with the filename pattern VocalMind's watcher
   expects:

   ```
   CALL_<NN>_<agent>_<scenario>.wav
   e.g. CALL_01_priya_refund_outage.wav
   ```

---

## Quick start

```bash
# 1. Install dependencies
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt

# 2. Confirm credentials are in ./keys/
#    Option A (recommended): service-account JSON for Vertex AI
#      -> uses your $300 GCP free-trial credits
#    Option B: api_key.txt with a Generative Language API key
#      -> billed via AI Studio prepayment
#
#    Override location with: set TTS_KEY_DIR=<absolute path>

# 3. Generate
python generate_audio.py                                    # all calls
python generate_audio.py --call CALL_01_refund_outage       # one call
python generate_audio.py --dry-run                          # parse only
```

The merged WAVs land in `output/<call_id>/`.  Copy them into your
VocalMind `storage/audio/<org_slug>/` folder; the watcher will pick them
up automatically (default scan interval: 15 s).

---

## Repository layout

```
tts-audio-generator/
├── generate_audio.py       # Main synthesis pipeline
├── parse_scripts.py        # Markdown → Turn / Coverage / Metadata parser
├── emotion_map.py          # TTS emotion → VocalMind canonical 7-label map
├── build_ground_truth.py   # Emit per-call GT JSON + manifest.json
├── requirements.txt
├── .gitignore
├── README.md               # This file
├── scripts/                # Call scripts (Markdown)
│   ├── README.md
│   ├── tts_style_instructions.md
│   └── CALL_*.md           # One script per call
├── ground_truth/           # Per-call evaluation JSON + manifest (regenerable)
│   └── *.json
```


---

## Ground-truth generation (for VocalMind evaluation)

After writing or editing a script, regenerate the ground-truth JSON:

```bash
python build_ground_truth.py                                # all scripts
python build_ground_truth.py --call CALL_06_priya_password  # one script
python build_ground_truth.py --check                        # validate only
```

This produces:

* `ground_truth/<call_id>.json` — call-level metadata + Coverage table +
  every turn with both the rich TTS emotion tag and the VocalMind
  canonical label (`emotion_gt`).
* `ground_truth/manifest.json` — VocalMind-compatible index of all calls
  with evaluation targets (STT WER, speaker diarization, emotion
  accuracy, RAG compliance, agent assignment).

### VocalMind emotion vocabulary

VocalMind's emotion classifier outputs exactly **7 canonical labels**
(defined in `VocalMind/backend/app/core/inference_contracts.py`):

| Label | TTS tags that project to it |
|-------|-----------------------------|
| `happy` | empathetic, reassuring, warm, grateful, satisfied, hopeful, relieved, vindicated, … |
| `angry` | angry, hostile, abusive, vindicated_angry |
| `sad` | tired, distressed, resigned, tearful |
| `frustrated` | worried, anxious, afraid, frustrated, impatient, irritated, curt, suspicious, skeptical, concerned, confused, resolute_afraid |
| `surprised` | surprised, shocked |
| `neutral` | neutral, calm, professional, cooperative, uncertain, thoughtful, concentrating, curious, cautious, firm, resolute, apologetic |
| `unknown` | anything not in `emotion_map.TTS_TO_VOCALMIND_EMOTION` |

If `build_ground_truth.py --check` reports an `unknown` label, **fix
`emotion_map.py` rather than ignoring** — it means a new TTS tag was
introduced without a canonical projection.

---

## Script format

Each call script is a Markdown file with one fenced block per turn:

````md
[T02] AGENT | professional:3 | normal | mid | normal
"Thank you for calling NexaLink. How can I help you today?"
````

Format: `[TID] SPEAKER | emotion:intensity | pace | pitch | volume [| (para)]`

* **TID**: `T01`, `T02`, …
* **SPEAKER**: `AGENT`, `CUSTOMER` (future scripts must use these two only).
* **emotion**: see `scripts/tts_style_instructions.md` for valid labels.
* **intensity**: 1–5.
* **pace**: `slow` | `normal` | `fast` | `rushed`.
* **pitch**: `low` | `mid` | `high`.
* **volume**: `quiet` | `normal` | `loud`.
* **para** (optional): parenthesised cues like `(sigh)`, `(pause)`,
  `(trails-off)`, `(typing)`, `(overlap)`.

---

## VocalMind integration

VocalMind's `audio_folder_watcher` (in `backend/app/core/audio_folder_watcher.py`)
scans `storage/audio/<org>/` every 15 s and parses filenames with the regex:

```
^CALL_\d{2}_(?P<agent>[a-zA-Z]+)_
```

It uses the `agent` token (lowercase first name) to look up the matching
agent user in the org and assigns the resulting Interaction to them.

The agent token is **read automatically from each script's YAML
front-matter** — specifically the `agent_profile.name` field.  Add new
scripts (including multiple calls per agent) without touching any code:

```yaml
# Top of every script
agent_profile:
  name: "Priya"          # → filename token "priya"
  voice_hint: "..."
```

Current scripts resolve to:

| Script | Token |
|--------|-------|
| CALL_01_refund_outage              | priya  |
| CALL_02_billing_dispute_escalation | daniel |
| CALL_03_tech_support_slow_internet | marcus |
| CALL_04_access_recovery_fraud      | aisha  |
| CALL_05_retention_abuse            | hannah |

A single agent can own multiple calls (`CALL_06_priya_password_reset`,
`CALL_07_priya_complaint`, …) — the watcher routes them all to the same
agent user.

> **Going forward, all new scripts use exactly two speakers (CUSTOMER and
> AGENT) — no Tier-2/Tier-3 escalation.**  The watcher assigns one file
> to one agent, so multi-agent calls leave portions of the audio
> "credited" to the wrong agent.  Existing CALL_02, CALL_04, CALL_05 are
> legacy and stay as-is; new calls will be 2-agent.

---

## Credentials

Two paths are supported, in priority order:

1. **Vertex AI (recommended — uses $300 GCP free-trial credits)**
   Drop a service-account JSON file into `keys/`.  The service account
   needs the `Vertex AI User` role on a GCP project where the
   `Generative AI API` is enabled.

2. **Google AI / AI Studio (separate prepayment billing)**
   Save your API key to `keys/api_key.txt` (a plain text file with just
   the key string).  Falls back to this only if no service-account JSON
   is found.

Set `TTS_KEY_DIR=<absolute path>` to keep credentials entirely outside
the repo.

---

## Rate limits

`gemini-2.5-flash-preview-tts` is currently capped at **10 RPM** even on
paid tiers.  `generate_audio.py` sleeps 6 s between turns and retries
429 responses up to 4 times with exponential delay parsed from the API
response.  Expect ~6–10 s per turn end-to-end.

---

## License

TBD.
