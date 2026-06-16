"""generate_audio.py — TTS Audio Generator (for VocalMind ingest)

Converts NexaLink-style call scripts to merged WAV audio using Gemini TTS
via Vertex AI.  Each script becomes a single merged WAV whose filename
matches the VocalMind auto-ingest watcher pattern:

    CALL_<NN>_<agent>_<scenario>.wav

The agent token is the lowercase first name of the primary (Tier-1) agent
in the call.  VocalMind's `audio_folder_watcher` parses this filename to
auto-assign the interaction to the matching agent user.

Output layout:
  output/
  └── CALL_01_refund_outage/
      ├── turns/
      │   ├── T02_AGENT.wav
      │   ├── T03_CUSTOMER.wav
      │   └── …
      └── CALL_01_priya_refund_outage.wav    ← copy this into VocalMind storage

Usage:
  pip install -r requirements.txt
  python generate_audio.py                               # all calls
  python generate_audio.py --call CALL_01_refund_outage  # single call
  python generate_audio.py --dry-run                     # parse only, no API calls
"""

import argparse
import logging
import os
import sys
import time
import wave
from pathlib import Path
from typing import Optional

from pydub import AudioSegment
from google import genai
from google.genai import types

from parse_scripts import Turn, parse_agent_name, parse_metadata, parse_script

# ── Optional .env loader ──────────────────────────────────────────────────────
# Load environment variables from a .env file at the repo root if one exists.
# python-dotenv is in requirements.txt but the load is best-effort so the
# pipeline still works in environments where it isn't installed.
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent / ".env")
except ImportError:
    pass

# ── Paths ─────────────────────────────────────────────────────────────────────

_PIPELINE   = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = _PIPELINE / "scripts"
OUTPUT_DIR  = _PIPELINE / "data" / "output"

# Per-agent rollup: a sibling of data/output/ where each agent has a folder
# containing every merged WAV they were the AGENT on. Hardlinked from
# data/output/ where the filesystem supports it (same bytes on disk, two
# paths), otherwise copied. Useful for listening to one agent's full corpus
# at a time without hunting through per-call folders.
AGENTS_DIR  = _PIPELINE / "data" / "agents"

# Credentials directory.  Looks for a service-account JSON or api_key.txt.
# Override with the TTS_KEY_DIR environment variable (or .env entry) if your
# keys live outside the repo (recommended for security).
KEY_DIR = Path(
    os.environ.get(
        "TTS_KEY_DIR",
        str(_PIPELINE / "keys"),
    )
).expanduser()

# Vertex AI project + location. Used only when a service-account JSON is
# present in KEY_DIR (Vertex path). Override per-environment via .env.
TTS_PROJECT_ID = os.environ.get("TTS_PROJECT_ID", "vocalmind-487116")
TTS_LOCATION   = os.environ.get("TTS_LOCATION",   "us-central1")

TTS_MODEL  = "gemini-2.5-flash-preview-tts"

# ── Audio settings ─────────────────────────────────────────────────────────────

SAMPLE_RATE = 24_000  # Hz — Gemini TTS native output

SILENCE_MS = {
    "normal":  500,
    "pause":  1_500,
    "overlap":   80,
    "hold":   8_000,
}

# ── VocalMind watcher filename mapping ────────────────────────────────────────

# The primary agent for each call is read from the script's YAML front-matter
# (`agent_profile.name`).  This lets you add new calls — including multiple
# calls per agent — without editing any code.  Just ensure every script
# declares its agent_profile.name and add a row to VOICE_MAP / PERSONA_MAP
# below for the (call_id, "AGENT") pair.
#
# Watcher contract (see VocalMind backend/app/core/audio_folder_watcher.py):
#   filename must match  ^CALL_\d{2}_(?P<agent>[a-zA-Z]+)_
#   agent token = lowercase first name of an active agent in the org.
#
# Going forward, all new scripts use exactly two speakers (CUSTOMER + AGENT).
# Existing CALL_02 / CALL_04 / CALL_05 are legacy multi-agent and are
# credited to their primary (Tier-1) agent via agent_profile.name.


def _vm_merged_filename(call_id: str, agent_token: str) -> str:
    """Build the VocalMind-watcher-compatible filename stem.

    'CALL_01_refund_outage' + 'priya' → 'CALL_01_priya_refund_outage'

    The agent token must sit between CALL_NN and the scenario slug.
    """
    parts = call_id.split("_", 2)  # ["CALL", "NN", "rest"]
    if len(parts) >= 3:
        return f"{parts[0]}_{parts[1]}_{agent_token}_{parts[2]}"
    return f"{call_id}_{agent_token}"


# ── Voice pins ─────────────────────────────────────────────────────────────────

# (call_id, speaker) → Gemini TTS voice name
VOICE_MAP: dict[tuple[str, str], str] = {
    ("CALL_01_refund_outage", "AGENT"):    "Aoede",
    ("CALL_01_refund_outage", "CUSTOMER"): "Algieba",

    ("CALL_02_billing_dispute_escalation", "AGENT"):    "Charon",
    ("CALL_02_billing_dispute_escalation", "CUSTOMER"): "Pulcherrima",
    ("CALL_02_billing_dispute_escalation", "T2_AGENT"): "Kore",

    ("CALL_03_tech_support_slow_internet", "AGENT"):    "Puck",
    ("CALL_03_tech_support_slow_internet", "CUSTOMER"): "Leda",

    ("CALL_04_access_recovery_fraud", "AGENT"):    "Despina",
    ("CALL_04_access_recovery_fraud", "CUSTOMER"): "Achird",
    ("CALL_04_access_recovery_fraud", "T2_AGENT"): "Orus",

    ("CALL_05_retention_abuse", "AGENT"):    "Erinome",
    ("CALL_05_retention_abuse", "CUSTOMER"): "Sadachbia",
    ("CALL_05_retention_abuse", "T3_AGENT"): "Iapetus",
}

# ── Speaker personas ──────────────────────────────────────────────────────────

PERSONA_MAP: dict[tuple[str, str], str] = {
    ("CALL_01_refund_outage", "AGENT"):    "Priya, a female customer service agent in her 30s with a warm, neutral US accent and an empathetic tone",
    ("CALL_01_refund_outage", "CUSTOMER"): "Marcus Whitfield, a male in his 40s with a mild Midwest US accent and a weary, tired baseline",

    ("CALL_02_billing_dispute_escalation", "AGENT"):    "Daniel, a male agent in his late 20s with a neutral US accent; professional but showing subtle pressure as the call escalates",
    ("CALL_02_billing_dispute_escalation", "CUSTOMER"): "Linda Park, a female in her 50s with sharp, articulate speech and escalating frustration",
    ("CALL_02_billing_dispute_escalation", "T2_AGENT"): "Sarah Chen, a female senior agent in her 40s with a lower-pitched, authoritative-warm voice",

    ("CALL_03_tech_support_slow_internet", "AGENT"):    "Marcus, a friendly male tech support agent in his mid-30s with a neutral US accent",
    ("CALL_03_tech_support_slow_internet", "CUSTOMER"): "Sofia Reyes, a female in her 30s who is fluent in English but speaks with a mild Latin American Spanish accent; vowels are pronounced with Spanish purity",

    ("CALL_04_access_recovery_fraud", "AGENT"):    "Aisha, a female agent in her 30s with a warm low-mid pitch and a reassuring manner",
    ("CALL_04_access_recovery_fraud", "CUSTOMER"): "Margaret Holloway, a woman in her late 60s with a soft voice that has a slight natural tremor; the tremor grows more audible with emotional stress",
    ("CALL_04_access_recovery_fraud", "T2_AGENT"): "James, a male senior agent in his 40s with a calm, authoritative voice and lower pitch",

    ("CALL_05_retention_abuse", "AGENT"):    "Hannah, a female agent in her 30s who maintains complete composure under verbal abuse; her pitch stays low and her volume never rises — even when struck",
    ("CALL_05_retention_abuse", "CUSTOMER"): "Brett Donovan, a male in his 30s who is hostile from the first word and escalates to verbal abuse; his volume increases with each turn",
    ("CALL_05_retention_abuse", "T3_AGENT"): "Robert, a male team lead in his 50s with a very low-pitched, firm voice; he is the calmest person in the call",
}


# ── Agent-keyed voice + persona (covers all of an agent's calls) ──────────────
#
# The legacy VOICE_MAP / PERSONA_MAP above are keyed by (call_id, speaker) and
# only cover CALL_01–05. Every new script just declares its agent via
# `agent_profile.name` in YAML — the lookups below are keyed by lowercase
# first-name token so adding a new call requires NO code edits.

AGENT_VOICE_BY_NAME: dict[str, str] = {
    # NexaLink (telecom)
    "priya":   "Aoede",     # female, warm, neutral US, 30s
    "daniel":  "Charon",    # male, late 20s, professional
    "marcus":  "Puck",      # male, mid-30s, friendly
    "aisha":   "Despina",   # female, late 30s, warm low-mid
    "hannah":  "Erinome",   # female, mid-30s, composed
    # Meridian Trust Bank
    "sarah":   "Kore",       # female, mid-40s, senior banker, authoritative-warm
    "tyler":   "Orus",       # male, late 20s, retail banker, professional-inexperienced
    "andre":   "Iapetus",    # male, mid-30s, business banking, methodical
    "jasmine": "Achernar",   # female, late 30s, fraud specialist, calm warm low-mid
    "karen":   "Achird",     # female, mid-30s, complaints/retention, composed
}

AGENT_PERSONA_BY_NAME: dict[str, str] = {
    # NexaLink
    "priya":  "Priya, a female customer service agent in her 30s with a warm, neutral US accent and an empathetic but professional cadence",
    "daniel": "Daniel, a male customer service agent in his late 20s with a neutral US accent, professional and businesslike",
    "marcus": "Marcus, a male customer service agent in his mid-30s with a friendly neutral US accent and a methodical instructional cadence",
    "aisha":  "Aisha, a female customer service agent in her late 30s with a warm low-mid register and a reassuring, deliberate manner",
    "hannah": "Hannah, a female customer service agent in her mid-30s with a composed low-mid register that stays steady even under pressure",
    # Meridian Trust Bank
    "sarah":   "Sarah Chen, a senior personal banker in her mid-40s with a neutral US accent, lower-pitched authoritative-warm register, confident and precise on disclosures",
    "tyler":   "Tyler Brennan, a retail banker in his late 20s with a neutral US accent, professional but inexperienced under pressure",
    "andre":   "Andre Williams, a business-banking specialist in his mid-30s with a neutral US accent, friendly methodical cadence",
    "jasmine": "Jasmine Patel, a fraud-prevention specialist in her late 30s with a warm calm low-mid register, deliberate and reassuring",
    "karen":   "Karen Vogel, a complaints and retention banker in her mid-30s with a composed low-mid register that holds steady under pressure",
}

# Agent → organization slug. Used to nest the agents/ rollup folder by org so
# the directory layout mirrors VocalMind's per-org storage convention. When
# you add a new organization, add its 5 agents here.
AGENT_ORG_BY_NAME: dict[str, str] = {
    # NexaLink (telecom)
    "priya":   "nexalink",
    "daniel":  "nexalink",
    "marcus":  "nexalink",
    "aisha":   "nexalink",
    "hannah":  "nexalink",
    # Meridian Trust Bank
    "sarah":   "meridian",
    "tyler":   "meridian",
    "andre":   "meridian",
    "jasmine": "meridian",
    "karen":   "meridian",
}

# Customer voice pool — picked deterministically by hash(call_id) so each call
# gets a distinct customer voice but the choice is stable across regenerations.
# Two pools (male / female) so the voice timbre matches the script's voice_hint.
CUSTOMER_VOICE_POOL_MALE: list[str] = [
    "Algenib", "Schedar", "Rasalgethi", "Sadaltager",
    "Enceladus", "Fenrir", "Umbriel", "Alnilam",
]
CUSTOMER_VOICE_POOL_FEMALE: list[str] = [
    "Autonoe", "Callirrhoe", "Vindemiatrix", "Zubenelgenubi",
    "Sulafat", "Zephyr", "Gacrux", "Laomedeia",
]


def _detect_gender(voice_hint: str) -> str:
    """Return 'male' / 'female' / 'unknown' from a free-form voice_hint string.

    First whole-word token wins. 'male' before 'female' would be wrong because
    'female' contains 'male' as a substring — check 'female' first.
    """
    h = voice_hint.lower()
    if "female" in h or "woman" in h:
        return "female"
    if "male" in h or " man" in h or h.startswith("man"):
        return "male"
    return "unknown"


def _pick_customer_voice(call_id: str, voice_hint: str) -> str:
    """Deterministically pick a customer voice from the gender-matched pool."""
    gender = _detect_gender(voice_hint)
    pool = (
        CUSTOMER_VOICE_POOL_FEMALE if gender == "female"
        else CUSTOMER_VOICE_POOL_MALE
    )
    # Stable, deterministic pick — hash(call_id) is process-randomised in
    # modern Python, so use a manual sum instead.
    seed = sum(ord(c) for c in call_id)
    return pool[seed % len(pool)]


# ── Per-call context cache (populated by generate_call) ──────────────────────

# Module-level cache so the per-turn helpers don't need to re-parse the script
# for the call's agent token and voice hints. Populated at the top of
# `generate_call` and read by `_get_voice` / `_build_style_prompt`.
_CALL_CTX: dict[str, dict[str, str]] = {}


# ── Emotion → style clause lookup ────────────────────────────────────────────

EMOTION_STYLE: dict[str, str] = {
    # NOTE: Pace is controlled EXCLUSIVELY by PACE_PHRASE (from the script's
    #       pace tag).  Emotion descriptions below must NOT mention speed/pace
    #       to avoid double-stacking that makes output unnaturally slow or fast.

    # Neutral / Professional register
    "neutral":       "Even tone, neither warm nor cold. No emphasis.",
    "calm":          "Voice settled, breath unhurried. Warmth optional.",
    "professional":  "Confident, clear articulation. Like someone reading information they know well.",
    "cooperative":   "Open, willing tone. Slight upward intonation at end of phrases.",
    "uncertain":     "Slight upward pitch on statements as if they were questions. Voice softens on the uncertain word.",
    "thoughtful":    "Pitch mid-to-low. The listener hears someone choosing words carefully, not hesitating nervously.",
    "concentrating": "Very quiet, almost self-directed delivery. Volume slightly under baseline. Deliberate spacing between words.",
    "surprised":     "Start with a slight breath-catch. Pitch rises sharply on the first stressed word, then levels.",
    "curious":       "Slight upward pitch contour. Engaged, interested tone.",
    "cautious":      "Slight pause before sensitive words. Lower volume to invite attention.",
    "firm":          "Lower pitch, no hedging. Each sentence is a complete unit with a hard period.",
    "resolute":      "Firm pitch. The voice has made a decision and is not revisiting it. Quiet finality — no aggression.",

    # Warm / Empathetic register
    "warm":               "Voice opens up. Gentle smile audible in tone. Pitch slightly raised mid-phrase, lowered at sentence end.",
    "empathetic":         "Softer voice, slight breathiness on the first word. Pitch drops on the comforting verbs.",
    "reassuring":         "Lower pitch, weight on the verbs that carry the reassurance. Pause briefly before key promises.",
    "apologetic":         "Softer volume, head-down delivery. Slight downward pitch contour. Lengthen the apology word.",
    "grateful":           "Slight smile in voice, warm release of breath on 'thank you'. Slight pitch rise on 'thank', drop on 'you'.",
    "satisfied":          "Settled, resolved tone. Slightly lower pitch than baseline. A quiet fullness — the feeling of completion.",
    "partially_satisfied": "Mild relief and mild residual doubt. Slight uplift at end of phrases, but the breath doesn't fully release.",
    "hopeful":            "Slightly softer volume, pitch gently lifted. Tentative warmth. Not yet grateful; still conditional.",
    "vindicated":         "'I knew it' tone. Slight rise on the operative word. Mild self-satisfaction.",

    # Stress / Negative-affect register
    "tired":       "Slight breath out at the start. Pitch slightly low. Energy noticeably below baseline.",
    "confused":    "Pitch rises at end of statements as if they were questions. Slight hesitation between phrases.",
    "worried":     "Voice tightens slightly. Pitch creeping upward as the sentence progresses.",
    "anxious":     "Audible tension. Voice slightly compressed. Breath catches between phrases.",
    "afraid":      "Voice thins. Volume drops involuntarily. Slight tremor on vowels. Pitch elevated. Words may trail or break.",
    "distressed":  "Voice thinner than afraid but less tremor. Breath audibly shorter. Pitch elevated. The voice wants to hold together but can't quite.",
    "frustrated":  "Volume up. Stress on the operative verbs. Sharper consonants. Pitch rises on emphasis.",
    "impatient":   "Clipped syllables; the speaker is not finishing sentences the way they would if they had time. Pitch rises slightly on the operative verb.",
    "irritated":   "Like frustrated but lower volume and more controlled. Sharpness lives in consonants, not loudness.",
    "curt":        "Reduced prosody range. No warmth, no harshness — just efficiency. Pitch flat. The voice does the minimum to communicate.",
    "angry":       "Loud, sharp consonants, pitch elevated. Bite on the noun the anger is directed at. No yelling distortion.",
    "hostile":     "Edged delivery. Loud but controlled. Words land like punches. Sneering quality on the key insults.",
    "abusive":     "Volume peaks. Words hit hard, no softening. Slight scoff or contemptuous laugh allowed. Never distort or clip.",
    "resigned":    "Pitch flattens to monotone. Volume drops. Audible exhale.",
    "tearful":     "Voice catches on vowels. Slight wet quality. Pitch trembles. Volume lower. Micro-pauses between phrases.",
    "concerned":   "Pitch lower than worried. The weight of recognition rather than panic.",
    "shocked":     "Brief pause before the response. Pitch jump on the first word. Volume drops mid-sentence as the reality sets in.",
    "skeptical":   "Pitch flat-with-edge. Slight pause before the response. Inflection of 'I don't believe you yet'.",
    "suspicious":  "Lower pitch, narrowed delivery. Words feel weighed.",
    "relieved":    "Audible exhale on the first word. Voice opens up. Pitch drops then rises into a smile.",

    # Compound tags
    "vindicated_angry":  "Open with the brief satisfaction of being proven right — then let anger take over. Pitch high, volume loud. The bitterness of being right about something bad.",
    "resolute_afraid":   "The voice is afraid — slight pitch elevation, thinning — but holding itself still and forceful on the key words. Both fear and determination.",
    "grateful_afraid":   "Relief and residual fear co-present. Warm and breathy on 'thank you' phrases; voice catches on the frightening thing. Gratitude in the melody, fear in the breath.",
}

# ── Intensity modifiers ───────────────────────────────────────────────────────

INTENSITY_MOD: dict[int, str] = {
    1: "barely perceptible — only the shape of the emotion, not the energy",
    2: "lightly audible, easy to miss",
    3: "",  # no qualifier at baseline
    4: "strongly — this emotion is the main thing the listener should hear",
    5: "at full intensity, but never breaking voice quality — no distortion or yelling-into-mic",
}

# ── Prosody → natural language phrases ───────────────────────────────────────

PACE_PHRASE: dict[str, str] = {
    # Keep these compact and gentle. The persona description (warm, methodical,
    # composed, etc.) already implies a certain cadence — the pace tag should
    # only nudge from that, not stack a second slowness instruction on top.
    "slow":   "a touch slower than normal conversational speed",
    "normal": "natural call-center conversational pace",
    "fast":   "noticeably faster than baseline, words flowing quickly",
    "rushed": "rushed, words tumbling out without natural breath",
}

PITCH_PHRASE: dict[str, str] = {
    "low":  "lower your pitch slightly below your baseline",
    "mid":  "",
    "high": "raise your pitch noticeably; voice sits in the upper part of your range",
}

VOLUME_PHRASE: dict[str, str] = {
    "quiet":  "quieter than baseline, as if speaking close to the microphone",
    "normal": "",
    "loud":   "louder than baseline; voice projects but does not distort",
}

# ── Paralinguistic → natural language phrases ─────────────────────────────────

PARA_PHRASE: dict[str, str] = {
    "sigh":         "begin with a soft audible exhale before the first word",
    "pause":        "include a natural pause where the em-dash or ellipsis appears in the text",
    "throat-clear": "begin with a brief throat clear, then the first word",
    "trails-off":   "let the final words fade in volume and pitch, ending unfinished",
    "self-correct": "include a brief stutter or restart on the corrected word",
    "laugh-soft":   "include a brief soft exhale-laugh before or within the line",
    "overlap":      "begin with the energy of someone who just cut in mid-conversation",
}

# ── Style prompt builder ──────────────────────────────────────────────────────

def _resolve_persona(call_id: str, speaker: str) -> str:
    """Resolve a natural-language persona string for (call_id, speaker), in order:

    1. Legacy PERSONA_MAP pin for (call_id, speaker)        — CALL_01–05 explicit
    2. AGENT_PERSONA_BY_NAME[agent_token]                   — agent-keyed
    3. Customer profile name + voice_hint from script YAML  — call-keyed
    4. Generic fallback
    """
    pinned = PERSONA_MAP.get((call_id, speaker))
    if pinned:
        return pinned

    ctx = _CALL_CTX.get(call_id, {})

    if speaker == "AGENT":
        persona = AGENT_PERSONA_BY_NAME.get(ctx.get("agent_token", ""))
        if persona:
            return persona

    if speaker == "CUSTOMER":
        name = ctx.get("customer_name", "")
        hint = ctx.get("customer_voice_hint", "")
        if name and hint:
            return f"{name} — {hint}"
        if hint:
            return hint

    return f"a {speaker.lower()} on a customer-support call"


def _build_style_prompt(turn: Turn) -> str:
    """Build a compact TTS style prompt.

    Format is a single direction line followed by the utterance text.
    Keeping the instruction short and ending with "Say exactly:" prevents
    Gemini TTS from repeating the text or vocalising the instructions.
    """
    persona = _resolve_persona(turn.call_id, turn.speaker)

    emotion_clause = EMOTION_STYLE.get(turn.emotion, f"{turn.emotion} affect")
    intensity_mod  = INTENSITY_MOD.get(turn.intensity, "")

    # Collect prosody modifiers (only non-empty)
    prosody_parts = [
        PACE_PHRASE.get(turn.pace, ""),
        PITCH_PHRASE.get(turn.pitch, ""),
        VOLUME_PHRASE.get(turn.volume, ""),
    ]
    prosody = ", ".join(p for p in prosody_parts if p)

    # Paralinguistic cues (sigh, pause, trails-off, etc.)
    para_parts = [
        PARA_PHRASE[p] for p in turn.paralinguistics
        if p in PARA_PHRASE and p != "typing"
    ]
    para = "; ".join(para_parts)

    # Build a single compact direction line
    direction = f"Speak as {persona}. {emotion_clause}"
    if intensity_mod:
        direction += f" Deliver this {intensity_mod}."
    if prosody:
        direction += f" {prosody.capitalize()}."
    if para:
        direction += f" {para.capitalize()}."

    return f"{direction}\nSay exactly: {turn.text}"


# ── TTS synthesis ─────────────────────────────────────────────────────────────

def _get_voice(call_id: str, speaker: str) -> str:
    """Resolve the Gemini voice for (call_id, speaker), in order:

    1. Legacy VOICE_MAP pin for (call_id, speaker)       — CALL_01–05 explicit
    2. AGENT_VOICE_BY_NAME[agent_token]                  — by script YAML
    3. Customer voice pool, gender-matched on voice_hint — by script YAML
    4. Hard fallback to Aoede
    """
    pinned = VOICE_MAP.get((call_id, speaker))
    if pinned:
        return pinned

    ctx = _CALL_CTX.get(call_id, {})

    if speaker == "AGENT":
        agent_token = ctx.get("agent_token", "")
        voice = AGENT_VOICE_BY_NAME.get(agent_token)
        if voice:
            return voice

    if speaker == "CUSTOMER":
        return _pick_customer_voice(call_id, ctx.get("customer_voice_hint", ""))

    return "Aoede"


def _parse_retry_delay(exc: Exception) -> float:
    """Extract retryDelay seconds from a 429 RESOURCE_EXHAUSTED exception body.

    Handles three formats the Gemini REST/gRPC API may return:
      JSON:        "retryDelay": "21s"
      Proto text:  retry_delay { seconds: 21 }
      Inline:      retryDelay: 21s

    Logs the first 400 chars of the exception at DEBUG level so the exact
    format is visible when debugging rate-limit issues.
    Falls back to 30 s if none of the patterns match.
    """
    import re
    text = str(exc)
    patterns = [
        r'"retryDelay"\s*:\s*"(\d+(?:\.\d+)?)s"',   # JSON: "retryDelay": "21s"
        r"retry_delay\s*\{\s*seconds\s*:\s*(\d+)",    # proto: retry_delay { seconds: 21 }
        r"retryDelay[^0-9]*(\d+(?:\.\d+)?)s",         # inline: retryDelay: 21s
    ]
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            return float(m.group(1)) + 2.0
    # No pattern matched — log so we can improve the regex next time
    logging.warning(f"  [retryDelay not parsed] error body: {text[:300]}")
    return 30.0


def synthesize_turn(client: genai.Client, turn: Turn) -> bytes:
    """Call the TTS API with up to 4 attempts, honouring retry-after delays.

    Raises the last exception if all attempts fail so the caller can decide
    whether to skip caching (do NOT write a silence placeholder to disk).
    """
    voice_name   = _get_voice(turn.call_id, turn.speaker)
    style_prompt = _build_style_prompt(turn)

    max_attempts = 4
    for attempt in range(1, max_attempts + 1):
        try:
            response = client.models.generate_content(
                model=TTS_MODEL,
                contents=style_prompt,
                config=types.GenerateContentConfig(
                    response_modalities=["AUDIO"],
                    speech_config=types.SpeechConfig(
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                voice_name=voice_name,
                            )
                        )
                    ),
                ),
            )
            return response.candidates[0].content.parts[0].inline_data.data

        except Exception as exc:
            exc_str = str(exc)
            # 429 → rate-limited, honour the API's retryDelay exactly.
            is_rate_limit = "429" in exc_str or "RESOURCE_EXHAUSTED" in exc_str
            # Transient server / network errors — same retry policy but with
            # an exponential local backoff since these don't carry a
            # retryDelay hint from the API.
            #   499 CANCELLED         — client/server cancelled, usually transient
            #   500 INTERNAL          — server-side blip
            #   502 / 503 / 504       — gateway / unavailable / gateway-timeout
            #   DEADLINE_EXCEEDED     — server timeout
            #   UNAVAILABLE           — overloaded backend
            transient_markers = (
                "499", "500", "502", "503", "504",
                "CANCELLED", "INTERNAL", "UNAVAILABLE", "DEADLINE_EXCEEDED",
            )
            is_transient = any(m in exc_str for m in transient_markers)

            if (is_rate_limit or is_transient) and attempt < max_attempts:
                if is_rate_limit:
                    delay = _parse_retry_delay(exc)
                    logging.warning(
                        f"  {turn.turn_id}: rate-limited (attempt {attempt}/{max_attempts})"
                        f" — waiting {delay:.0f}s then retrying…"
                    )
                else:
                    # Exponential backoff: 6s, 12s, 24s — small enough to keep
                    # the pipeline moving, large enough to clear most blips.
                    delay = 6.0 * (2 ** (attempt - 1))
                    logging.warning(
                        f"  {turn.turn_id}: transient error (attempt {attempt}/{max_attempts})"
                        f" — {exc_str[:140]} — waiting {delay:.0f}s then retrying…"
                    )
                time.sleep(delay)
                continue
            # Non-retryable error, or out of attempts — propagate so caller
            # does NOT write a silence WAV to disk.
            raise


# ── WAV writing ───────────────────────────────────────────────────────────────

def _raw_to_wav(raw_pcm: bytes, path: Path) -> None:
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)      # 16-bit
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(raw_pcm)


# ── Silence helpers ────────────────────────────────────────────────────────────

def _silence_segment(ms: int) -> AudioSegment:
    return AudioSegment.silent(duration=ms, frame_rate=SAMPLE_RATE)


def _silence_between(turn: Turn, next_turn: Optional[Turn]) -> AudioSegment:
    if next_turn and any("off-line" in p for p in next_turn.paralinguistics):
        return _silence_segment(SILENCE_MS["hold"])
    if "pause" in turn.paralinguistics:
        return _silence_segment(SILENCE_MS["pause"])
    if next_turn and "overlap" in next_turn.paralinguistics:
        return _silence_segment(SILENCE_MS["overlap"])
    return _silence_segment(SILENCE_MS["normal"])


# ── Per-call generation ────────────────────────────────────────────────────────

def generate_call(
    client: Optional[genai.Client],
    md_path: Path,
    dry_run: bool = False,
) -> None:
    call_id = md_path.stem
    turns   = parse_script(md_path)
    meta    = parse_metadata(md_path)

    agent_token = parse_agent_name(md_path)
    if not agent_token:
        logging.warning(
            "  %s: no agent_profile.name in script YAML — falling back to 'agent'. "
            "VocalMind watcher will use a deterministic fallback agent.",
            call_id,
        )
        agent_token = "agent"

    # Populate the per-call context so _get_voice / _resolve_persona can pick
    # the right agent voice and gender-matched customer voice without
    # re-parsing the script on every turn.
    _CALL_CTX[call_id] = {
        "agent_token":         agent_token,
        "agent_name":          meta.agent_name,
        "agent_voice_hint":    meta.agent_voice_hint,
        "customer_name":       meta.customer_name,
        "customer_voice_hint": meta.customer_voice_hint,
    }

    merged_stem = _vm_merged_filename(call_id, agent_token)
    turns_dir   = OUTPUT_DIR / call_id / "turns"
    merged_path = OUTPUT_DIR / call_id / f"{merged_stem}.wav"
    turns_dir.mkdir(parents=True, exist_ok=True)

    logging.info("")
    logging.info("=" * 60)
    logging.info(f"  {call_id}  ({len(turns)} turns)")
    logging.info("=" * 60)

    if not dry_run and merged_path.exists():
        logging.info(f"  Already generated — skipping. Delete {merged_path.name} to regenerate.")
        # Still mirror into agents/ in case the agent folder is out of sync
        # (e.g. agents/ was deleted, or output/ was populated from another machine).
        _copy_to_agent_folder(merged_path, agent_token)
        return

    if dry_run:
        for t in turns:
            logging.info(
                f"  {t.turn_id}  {t.speaker:<12}  {t.emotion}:{t.intensity}  "
                f"voice={_get_voice(t.call_id, t.speaker)}"
            )
        return

    segments: list[AudioSegment] = []

    for i, turn in enumerate(turns):
        out_wav = turns_dir / f"{turn.turn_id}_{turn.speaker}.wav"

        if out_wav.exists():
            logging.info(f"  {turn.turn_id} — cached")
            seg = AudioSegment.from_wav(str(out_wav))
        else:
            logging.info(
                f"  {turn.turn_id}  {turn.speaker:<12}  "
                f"{turn.emotion}:{turn.intensity}  "
                f"voice={_get_voice(turn.call_id, turn.speaker)}"
            )
            try:
                raw = synthesize_turn(client, turn)
                _raw_to_wav(raw, out_wav)   # write only on success
                seg = AudioSegment.from_wav(str(out_wav))
            except Exception as exc:
                logging.error(f"  {turn.turn_id}: skipped (all retries failed) — {exc}")
                seg = _silence_segment(500)  # placeholder in merged only; NOT cached
            time.sleep(6.0)  # 10 RPM limit → 1 request per 6 s minimum

        segments.append(seg)
        next_turn = turns[i + 1] if i + 1 < len(turns) else None
        segments.append(_silence_between(turn, next_turn))

    merged = segments[0]
    for s in segments[1:]:
        merged += s

    merged.export(str(merged_path), format="wav")
    logging.info(f"  → {merged_path.name}  ({len(merged) / 1000:.1f}s)")

    _copy_to_agent_folder(merged_path, agent_token)


def _copy_to_agent_folder(merged_path: Path, agent_token: str) -> None:
    """Mirror the merged WAV into agents/<org>/<agent_token>/ as a flat collection.

    Uses a hardlink when the filesystem supports it (same bytes on disk, two
    paths) and falls back to a full copy where hardlinks aren't possible
    (cross-filesystem, certain FAT/exFAT setups). Idempotent — replaces any
    existing entry so re-runs stay in sync with output/.

    The org is resolved from AGENT_ORG_BY_NAME; unknown agents fall through
    to a generic "unassigned" org so the file is not silently dropped.
    """
    import shutil
    if not merged_path.exists() or not agent_token:
        return
    org = AGENT_ORG_BY_NAME.get(agent_token, "unassigned")
    agent_dir = AGENTS_DIR / org / agent_token
    agent_dir.mkdir(parents=True, exist_ok=True)
    dst = agent_dir / merged_path.name
    # Always start fresh so a hardlink replaces any stale copy and vice versa.
    if dst.exists() or dst.is_symlink():
        try:
            dst.unlink()
        except OSError:
            pass
    try:
        os.link(merged_path, dst)
        link_kind = "link"
    except OSError:
        # Cross-volume, unsupported filesystem, or permission issue —
        # fall back to a full copy so the rollup still works.
        shutil.copy2(merged_path, dst)
        link_kind = "copy"
    logging.info(f"  → data/agents/{org}/{agent_token}/{merged_path.name}  ({link_kind})")


# ── Credentials & client ──────────────────────────────────────────────────────

def _resolve_api_key(key_dir: Path) -> str | None:
    """Look for an API key file (api_key.txt) in key_dir."""
    key_file = key_dir / "api_key.txt"
    if key_file.exists():
        key = key_file.read_text(encoding="utf-8").strip()
        if key:
            return key
    return None


def _build_client(key_dir: Path) -> genai.Client:
    """Build a Gemini client.

    Prefers a service-account JSON → Vertex AI (uses GCP $300 free-trial
    credits) over a plain API key (Google AI / AI Studio, which has its
    own prepayment billing).
    """
    # 1. Service-account JSON → Vertex AI  (uses GCP credits)
    matches = list(key_dir.glob("*.json"))
    if matches:
        creds_path = str(matches[0])
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = creds_path
        logging.info(
            "Using Vertex AI with service account: %s  (project=%s, location=%s)",
            Path(creds_path).name, TTS_PROJECT_ID, TTS_LOCATION,
        )
        return genai.Client(
            vertexai=True,
            project=TTS_PROJECT_ID,
            location=TTS_LOCATION,
        )

    # 2. Fallback: API key → Google AI / AI Studio
    api_key = _resolve_api_key(key_dir)
    if api_key:
        logging.info("Using Google AI API key (AI Studio billing)")
        return genai.Client(api_key=api_key)

    raise FileNotFoundError(
        f"No service-account JSON or api_key.txt found in {key_dir}\n"
        "Option 1 (recommended): Place a service-account JSON in {key_dir}\n"
        "Option 2: Save your AI Studio API key to {key_dir}/api_key.txt"
    )


# ── Entry point ────────────────────────────────────────────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser(description="VocalMind TTS pipeline — Gemini TTS")
    ap.add_argument("--call", help="Generate one call by stem name (e.g. CALL_01_refund_outage)")
    ap.add_argument("--dry-run", action="store_true", help="Parse scripts only — no API calls")
    args = ap.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(OUTPUT_DIR / "generation.log", encoding="utf-8"),
        ],
    )

    if args.call:
        script_files = [SCRIPTS_DIR / f"{args.call}.md"]
        if not script_files[0].exists():
            logging.error(f"Not found: {script_files[0]}")
            sys.exit(1)
    else:
        script_files = sorted(SCRIPTS_DIR.glob("CALL_*.md"))

    if not script_files:
        logging.error(f"No CALL_*.md scripts found in {SCRIPTS_DIR}")
        sys.exit(1)

    client = None
    if not args.dry_run:
        client = _build_client(KEY_DIR)

    for md_path in script_files:
        generate_call(client, md_path, dry_run=args.dry_run)

    logging.info("\nDone.")


if __name__ == "__main__":
    main()
