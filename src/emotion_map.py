"""emotion_map.py — Map rich TTS emotion tags to VocalMind canonical labels.

VocalMind's emotion classifier (acoustic + text fusion) outputs exactly
ONE of these 7 canonical labels per turn, per
`backend/app/core/inference_contracts.py::normalize_emotion_label`:

    happy | angry | sad | frustrated | surprised | neutral | unknown

The TTS pipeline uses a much richer vocabulary (~50 fine-grained emotion
tags) to give Gemini TTS the nuance it needs.  Ground-truth evaluation
must collapse those rich tags onto VocalMind's 7-label space.

If you add a new TTS tag in `generate_audio.py::EMOTION_STYLE`, add it
here too — otherwise it falls back to `unknown` and the GT comparison
will mark the turn as unrecognized.
"""

from __future__ import annotations

# ── TTS tag → VocalMind canonical GT label ────────────────────────────────────

TTS_TO_VOCALMIND_EMOTION: dict[str, str] = {
    # Neutral / professional register → neutral
    "neutral":       "neutral",
    "calm":          "neutral",
    "professional":  "neutral",
    "cooperative":   "neutral",
    "uncertain":     "neutral",
    "thoughtful":    "neutral",
    "concentrating": "neutral",
    "curious":       "neutral",
    "cautious":      "neutral",
    "firm":          "neutral",
    "resolute":      "neutral",
    "apologetic":    "neutral",   # downward, even tone — not perceived as happy

    # Warm / empathetic register → happy
    "warm":                "happy",
    "empathetic":          "happy",
    "reassuring":          "happy",
    "grateful":            "happy",
    "satisfied":           "happy",
    "partially_satisfied": "happy",
    "hopeful":             "happy",
    "vindicated":          "happy",
    "relieved":            "happy",

    # Sadness register → sad
    "tired":     "sad",
    "distressed": "sad",
    "resigned":  "sad",
    "tearful":   "sad",

    # Frustration / anxiety register → frustrated
    # (VocalMind folds fear/disgust/anxiety into "frustrated")
    "worried":     "frustrated",
    "anxious":     "frustrated",
    "afraid":      "frustrated",
    "frustrated":  "frustrated",
    "impatient":   "frustrated",
    "irritated":   "frustrated",
    "curt":        "frustrated",
    "suspicious":  "frustrated",
    "skeptical":   "frustrated",
    "concerned":   "frustrated",   # agent-side concern about a situation
    "confused":    "frustrated",

    # Anger register → angry
    "angry":   "angry",
    "hostile": "angry",
    "abusive": "angry",

    # Surprise register → surprised
    "surprised": "surprised",
    "shocked":   "surprised",

    # Compound tags — pick the dominant VocalMind label
    "vindicated_angry": "angry",       # anger dominates
    "resolute_afraid":  "frustrated",  # fear+resolve → frustrated
    "grateful_afraid":  "happy",       # relief dominates
}


# ── Valid VocalMind labels (the closed set the classifier outputs) ────────────

VOCALMIND_LABELS: frozenset[str] = frozenset({
    "happy",
    "angry",
    "sad",
    "frustrated",
    "surprised",
    "neutral",
    "unknown",
})


def to_vocalmind_emotion(tts_emotion: str) -> str:
    """Project a TTS emotion tag onto VocalMind's 7-label space.

    Falls back to 'unknown' for tags not in the map — call sites should
    treat this as a bug to fix (extend the map) rather than ignore.
    """
    return TTS_TO_VOCALMIND_EMOTION.get(tts_emotion.strip().lower(), "unknown")


def is_canonical_label(label: str) -> bool:
    """Whether `label` is one of VocalMind's 7 canonical emotion labels."""
    return label in VOCALMIND_LABELS
