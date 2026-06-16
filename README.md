# TTS Audio Generator

Generates realistic customer-service call audio from structured Markdown
scripts using Google **Gemini TTS** via **Vertex AI** (or Google AI Studio
as a fallback).  Each call script becomes a single merged `.wav` file whose
filename matches the [VocalMind](https://github.com/galalqassas/VocalMind)
auto-ingest watcher pattern, so the audio can be dropped straight into
VocalMind's storage folder and processed automatically.

The repo ships with **50 annotated scripts across two example orgs**
(NexaLink — telecom, 27 calls; Meridian Trust Bank — banking, 23 calls)
covering happy paths, policy violations, fraud handling, abuse termination,
and edge cases like failed verification and bereavement. You can use it
as-is to regenerate the audio, or as a template for your own scripts.

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

6. Hardlinks the merged WAV into `data/agents/<org>/<agent>/` so you can
   listen to one agent's full corpus without hunting through per-call
   folders. No bytes are duplicated where the filesystem supports
   hardlinks (NTFS, ext4, APFS).

---

## Quick start

```bash
# 1. Clone + create venv
git clone https://github.com/mohammedhassan-7/vocalmind-audio-gen.git
cd vocalmind-audio-gen
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt

# 2. Configure environment
cp .env.example .env            # macOS / Linux
copy .env.example .env          # Windows
#    Edit .env: set TTS_PROJECT_ID to your GCP project (for Vertex)
#    or leave defaults if you'll use a plain Gemini API key

# 3. Add credentials to ./keys/ (gitignored)
#    Option A (recommended): drop a Vertex AI service-account JSON in ./keys/
#    Option B: save a Gemini API key as ./keys/api_key.txt

# 4. Verify the repo is consistent (no audio generated yet)
python src/verify.py

# 5. Parse-check a single script without spending any API credits
python src/generate_audio.py --dry-run --call CALL_01_refund_outage

# 6. Generate one call as a smoke test (~5 minutes, ~50 API calls)
python src/generate_audio.py --call CALL_01_refund_outage

# 7. Generate everything else
python src/generate_audio.py                          # skips any call with a merged WAV
python src/build_ground_truth.py                      # emit per-call GT + manifest
```

The merged WAVs land in `data/output/<call_id>/` and are hardlinked into
`data/agents/<org>/<agent>/`.  Copy them into your VocalMind
`storage/audio/<org_slug>/` folder; the watcher will pick them up
automatically (default scan interval: 15 s).

---

## Environment configuration (`.env`)

`generate_audio.py` reads its configuration from environment variables,
loaded from a project-root `.env` file if `python-dotenv` is installed
(it's in `requirements.txt`). All variables are optional; defaults work
for the original VocalMind project.

| Variable | Default | What it controls |
|---|---|---|
| `TTS_KEY_DIR` | `./keys` | Directory containing your service-account JSON or `api_key.txt`. |
| `TTS_PROJECT_ID` | `vocalmind-487116` | GCP project ID (Vertex AI path only). **Override this.** |
| `TTS_LOCATION` | `us-central1` | GCP region the Gemini TTS model is deployed in. |

Copy `.env.example` to `.env` and edit. `.env` is gitignored —
**never commit it**.

Two credential paths are supported, in priority order:

1. **Vertex AI (recommended — uses $300 GCP free-trial credits)** — drop
   a service-account JSON file into your `TTS_KEY_DIR`. The service
   account needs the `Vertex AI User` role on the project named in
   `TTS_PROJECT_ID`, with the Generative AI API enabled.
2. **Google AI / AI Studio (separate prepayment billing)** — save your
   key string to `<TTS_KEY_DIR>/api_key.txt`. Used only if no
   service-account JSON is present.

---

## Verifying the corpus

`verify.py` audits every script and confirms the on-disk artefacts match.
Useful before and after generation, and in CI.

```bash
python src/verify.py                       # audit every script
python src/verify.py CALL_03 CALL_36       # audit just the listed call(s)
```

It checks, per script:

- The `turns:` value in YAML matches the number of `[Tnn]` blocks in the body.
- The number of per-turn WAVs in `data/output/<call>/turns/` matches `turns:`.
- A merged WAV exists at `data/output/<call>/`.
- A ground-truth JSON exists at `data/ground_truth/<call>.json`.

It also tells you how many entries in `data/output/generation.log` were
historical retry-failed errors (those are normally already recovered;
the per-call rows above will show any that aren't).

Exit code: `0` clean, `1` any gap found, `2` repo not found.

---

## Repository layout

```
tts-audio-generator/
├── src/                          # Python source (entry-point scripts)
│   ├── generate_audio.py         #   Main synthesis pipeline
│   ├── parse_scripts.py          #   Markdown → Turn / Coverage / Metadata parser
│   ├── emotion_map.py            #   TTS emotion → VocalMind canonical 7-label map
│   ├── build_ground_truth.py     #   Emit per-call GT JSON + manifest.json
│   └── verify.py                 #   One-command corpus audit
├── scripts/                      # 50 call scripts (tracked)
│   ├── README.md
│   ├── tts_style_instructions.md
│   ├── CALL_01_refund_outage.md
│   ├── CALL_02_billing_dispute.md
│   └── …
├── data/                         # Generated artifacts
│   ├── ground_truth/             #   Per-call GT JSON + manifest (tracked)
│   │   ├── manifest.json
│   │   ├── CALL_01_refund_outage.json
│   │   └── …
│   ├── output/                   #   Generated audio (gitignored — regenerable)
│   │   └── CALL_<id>/
│   │       ├── turns/T01_AGENT.wav, T02_CUSTOMER.wav, …
│   │       └── CALL_<NN>_<agent>_<scenario>.wav     ← merged
│   └── agents/                   #   Per-agent rollup (gitignored — hardlinked)
│       ├── nexalink/{priya,daniel,marcus,aisha,hannah}/*.wav
│       └── meridian/{sarah,tyler,andre,jasmine,karen}/*.wav
├── keys/                         # Credentials (gitignored)
│   ├── <service-account>.json    #   or
│   └── api_key.txt
├── requirements.txt
├── .env.example                  # Copy to .env; document your configuration
├── .gitignore
└── README.md
```

---

## Script format

Each call script is a Markdown file with YAML front-matter at the top,
a coverage table, and one fenced block per turn:

````md
[T02] AGENT | professional:3 | normal | mid | normal
"Thank you for calling NexaLink. How can I help you today?"
````

Header line format:
`[TID] SPEAKER | emotion:intensity | pace | pitch | volume [| (para)]`

* **TID**: `T01`, `T02`, …
* **SPEAKER**: `AGENT`, `CUSTOMER` (scripts must use these two only).
* **emotion**: see `scripts/tts_style_instructions.md` for valid labels.
* **intensity**: 1–5.
* **pace**: `slow` | `normal` | `fast` | `rushed`.
* **pitch**: `low` | `mid` | `high`.
* **volume**: `quiet` | `normal` | `loud`.
* **para** (optional): parenthesised cues like `(sigh)`, `(pause)`,
  `(trails-off)`, `(typing)`, `(overlap)`.

Each script's YAML front-matter declares the agent name and the customer
voice hint — see any `scripts/CALL_*.md` for a working example. Adding
a new script is as simple as dropping a new `.md` file in `scripts/` —
no code changes needed (unless you're also adding a new agent or org;
see below).

---

## Adding new content

### A new call for an existing agent

1. Copy any existing script in `scripts/` to `scripts/CALL_NN_<scenario>.md`
   (the next free `NN`).
2. Edit the YAML `agent_profile.name` to the existing agent's first
   name, and `customer_profile.voice_hint` to a clear description.
3. Write the dialog turns.
4. `python src/verify.py CALL_NN_<scenario>` confirms the script parses.
5. `python src/generate_audio.py --dry-run --call CALL_NN_<scenario>`
   confirms voices resolve.
6. `python src/generate_audio.py --call CALL_NN_<scenario>` generates it.
7. `python src/build_ground_truth.py --call CALL_NN_<scenario>` emits GT.

### A new agent

Add an entry to `AGENT_VOICE_BY_NAME` (Gemini voice ID) and
`AGENT_PERSONA_BY_NAME` (one-sentence persona prompt) at the top of
`generate_audio.py`, plus a row in `AGENT_ORG_BY_NAME` for the rollup.

### A new organization

Use any short slug (`nexalink`, `meridian`, …). Add each of its agents'
entries to `AGENT_ORG_BY_NAME` mapping to that slug. The rollup folders
under `data/agents/<org>/` are created automatically on first generation.

---

## Ground-truth generation (for VocalMind evaluation)

After writing or editing a script, regenerate the ground-truth JSON:

```bash
python src/build_ground_truth.py                                # all scripts
python src/build_ground_truth.py --call CALL_06_pin_reset       # one script
python src/build_ground_truth.py --check                        # validate only
```

This produces:

* `data/ground_truth/<call_id>.json` — call-level metadata + Coverage table +
  every turn with both the rich TTS emotion tag and the VocalMind
  canonical label (`emotion_gt`).
* `data/ground_truth/manifest.json` — VocalMind-compatible index of all calls
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

## VocalMind integration

VocalMind's `audio_folder_watcher` (in
`backend/app/core/audio_folder_watcher.py`) scans `storage/audio/<org>/`
every 15 s and parses filenames with the regex:

```
^CALL_\d{2}_(?P<agent>[a-zA-Z]+)_
```

It uses the `agent` token (lowercase first name) to look up the matching
agent user in the org and assigns the resulting Interaction to them.

The agent token is **read automatically from each script's YAML
front-matter** — specifically the `agent_profile.name` field — and
combined with the scenario slug at merge time:

```yaml
agent_profile:
  name: "Priya"          # → filename token "priya"
  voice_hint: "..."
```

A single agent can own multiple calls — the watcher routes them all to
the same agent user.

> **All 50 scripts use exactly two speakers** (CUSTOMER and AGENT) so
> credit attribution matches downstream analytics. Earlier
> Tier-2/Tier-3 escalation scripts have been retired; the corresponding
> call IDs (CALL_02, CALL_04, CALL_05) were re-authored as 2-agent
> versions with the same customer personas.

---

## Rate limits and retries

`gemini-2.5-flash-preview-tts` is currently capped at **10 RPM** even on
paid tiers. `generate_audio.py`:

- Sleeps 6 s between turns to stay under the limit.
- Retries `429 RESOURCE_EXHAUSTED` up to 4 times using the
  `retryDelay` value parsed from the API response.
- Retries transient errors (`499 CANCELLED`, `500 INTERNAL`, `502`,
  `503`, `504`, `UNAVAILABLE`, `DEADLINE_EXCEEDED`) with exponential
  local backoff (6 / 12 / 24 s).
- After 4 failed attempts on a single turn, the merged WAV gets a
  500 ms silence placeholder for that slot and the per-turn WAV is
  **not** cached — so re-running `generate_audio.py --call <id>`
  retries only the missing turn (cheap repair).

Expect ~6–10 s per turn end-to-end. A typical 50-turn call takes
about 5 minutes.

---

## Troubleshooting

| Symptom | Likely cause / fix |
|---|---|
| `ModuleNotFoundError: dotenv` | `pip install -r requirements.txt` (or just `pip install python-dotenv`). |
| `FileNotFoundError: No service-account JSON or api_key.txt found` | Drop credentials into `keys/`, or set `TTS_KEY_DIR` in `.env`. |
| `403 Permission denied` (Vertex) | Service account is missing `Vertex AI User` on `TTS_PROJECT_ID`, or the API isn't enabled. |
| `verify.py` shows `[missing T05]` | One turn never made it to disk (transient error). Re-run `generate_audio.py --call <id>` — only the missing turn hits the API. |
| Generation seems "stuck" | Normal 10-RPM throttle. Check the latest log line in `data/output/generation.log` — if it's still ticking, it's fine. |
| Voice sounds wrong gender | Check `AGENT_VOICE_BY_NAME` and the customer voice pool in `generate_audio.py`. |

---

## License

TBD.
