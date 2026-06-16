"""build_ground_truth.py — Emit VocalMind-compatible ground-truth files.

For each script in ./scripts/CALL_*.md this script produces:

  * One per-call JSON  →  data/ground_truth/<call_id>.json
  * One manifest.json  →  data/ground_truth/manifest.json

The JSON schema matches what VocalMind already consumes in
`storage/audio/<org>/evaluation/`.  Each turn carries its TTS emotion
tag AND the VocalMind canonical label (`emotion_gt`) — projection via
`emotion_map.to_vocalmind_emotion`.

Run AFTER writing or editing a script.  Safe to re-run; outputs are
overwritten.

  python build_ground_truth.py                              # all scripts
  python build_ground_truth.py --call CALL_01_refund_outage # single call
  python build_ground_truth.py --check                      # validate only

If `--check` flags any TTS emotion as `unknown` it means a new tag was
introduced without updating `emotion_map.TTS_TO_VOCALMIND_EMOTION` —
fix the map before generating audio.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from collections import Counter
from dataclasses import asdict
from pathlib import Path
from typing import Iterable

from emotion_map import is_canonical_label, to_vocalmind_emotion
from parse_scripts import (
    CoverageItem,
    ScriptMetadata,
    Turn,
    parse_coverage,
    parse_metadata,
    parse_script,
)

# ── Paths ─────────────────────────────────────────────────────────────────────

_PIPELINE   = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = _PIPELINE / "scripts"
GT_DIR      = _PIPELINE / "data" / "ground_truth"


# ── Helpers ───────────────────────────────────────────────────────────────────

def _vm_audio_filename(call_id: str, agent_token: str) -> str:
    """Build the VocalMind-watcher merged-wav filename.

    Must stay in sync with generate_audio.py::_vm_merged_filename — the
    two helpers produce the same string.
    """
    parts = call_id.split("_", 2)
    if len(parts) >= 3:
        return f"{parts[0]}_{parts[1]}_{agent_token}_{parts[2]}.wav"
    return f"{call_id}_{agent_token}.wav"


def _turn_to_dict(t: Turn, primary_agent: str) -> dict:
    """Serialize a Turn for the GT JSON. Includes both rich TTS tag and
    the VocalMind canonical label."""
    agent_name = primary_agent if t.speaker.upper() == "AGENT" else None
    return {
        "turn_id":         t.turn_id,
        "speaker":         t.speaker,
        "agent_name":      agent_name,
        "text":            t.text,
        # Rich TTS metadata (useful for re-synthesis and detailed analysis)
        "emotion":         t.emotion,
        "intensity":       t.intensity,
        "pace":            t.pace,
        "pitch":           t.pitch,
        "volume":          t.volume,
        "paralinguistics": t.paralinguistics,
        # VocalMind canonical ground truth for the emotion evaluator
        "emotion_gt":      to_vocalmind_emotion(t.emotion),
    }


def _coverage_to_dict(items: Iterable[CoverageItem]) -> list[dict]:
    return [{"element": c.element, "where": c.where, "notes": c.notes} for c in items]


def _validate_emotions(turns: list[Turn], call_id: str) -> list[str]:
    """Return list of WARNING strings for emotions that project to 'unknown'."""
    warnings: list[str] = []
    for t in turns:
        if not is_canonical_label(to_vocalmind_emotion(t.emotion)):
            warnings.append(
                f"  {call_id} {t.turn_id}: TTS emotion '{t.emotion}' "
                f"is not in emotion_map.TTS_TO_VOCALMIND_EMOTION"
            )
    return warnings


# ── Per-call build ────────────────────────────────────────────────────────────

def build_call_ground_truth(md_path: Path) -> dict:
    """Construct the GT dict for one script."""
    meta     = parse_metadata(md_path)
    turns    = parse_script(md_path)
    coverage = parse_coverage(md_path)

    primary_agent = meta.agent_name or "Agent"
    agent_token   = primary_agent.split()[0].lower() if primary_agent else "agent"

    # Distribution of VocalMind-canonical emotions (handy for quick stats)
    vm_emotion_counts = Counter(
        to_vocalmind_emotion(t.emotion) for t in turns
    )

    # Speakers that appear in this script beyond AGENT and CUSTOMER (e.g.
    # legacy T2_AGENT/T3_AGENT in CALL_02/04/05).  Listed for traceability.
    extra_speakers = sorted({
        t.speaker for t in turns
        if t.speaker.upper() not in {"AGENT", "CUSTOMER"}
    })

    return {
        "call_id":           meta.call_id,
        "audio_file":        _vm_audio_filename(meta.call_id, agent_token),
        "script_file":       f"scripts/{md_path.name}",
        "primary_agent":     primary_agent,
        "agent_token":       agent_token,
        "extra_speakers":    extra_speakers,
        "customer_profile":  meta.customer_name,
        "sop_primary":       meta.sop_primary,
        "policy_refs":       meta.policy_refs,
        "kb_refs":           meta.kb_refs,
        "expected_outcome":  meta.expected_outcome,
        "emotional_arc":     meta.emotional_arc,
        "content_warning":   meta.content_warning,
        "turn_count":        len(turns),
        "duration_estimate": meta.duration_estimate,
        "emotion_distribution": dict(vm_emotion_counts),
        "coverage":          _coverage_to_dict(coverage),
        "turns":             [_turn_to_dict(t, primary_agent) for t in turns],
    }


# ── Manifest ──────────────────────────────────────────────────────────────────

_MANIFEST_HEADER = {
    "organization":     "nexalink",
    "audio_format":     "wav",
    "source":           "tts-audio-generator (Gemini TTS via Vertex AI)",
    "filename_pattern": "CALL_<NN>_<agent>_<scenario>.wav",
    "evaluation_targets": {
        "stt": {
            "metric":     "word_error_rate",
            "target_max": 0.15,
            "uses":       "turns[].text",
        },
        "speaker_diarization": {
            "metric":     "speaker_role_accuracy",
            "target_min": 0.9,
            "uses":       "turns[].speaker (collapsed: agent | customer)",
        },
        "emotion": {
            "metric":     "utterance_emotion_accuracy",
            "target_min": 0.7,
            "uses":       "turns[].emotion_gt (VocalMind canonical 7-label)",
        },
        "rag_compliance": {
            "metric":     "required_trigger_recall",
            "target_min": 0.8,
            "uses":       "coverage + policy_refs",
        },
        "agent_assignment": {
            "metric":     "interaction_agent_name_match",
            "target_min": 1.0,
            "uses":       "primary_agent (from agent_profile.name)",
        },
    },
    "vocalmind_emotion_vocabulary": [
        "happy", "angry", "sad", "frustrated",
        "surprised", "neutral", "unknown",
    ],
}


def build_manifest(call_records: list[dict]) -> dict:
    summary = []
    for rec in call_records:
        summary.append({
            "call_id":          rec["call_id"],
            "audio_file":       rec["audio_file"],
            "script_file":      rec["script_file"],
            "ground_truth_file": f"data/ground_truth/{rec['call_id']}.json",
            "primary_agent":    rec["primary_agent"],
            "turn_count":       rec["turn_count"],
            "expected_outcome": rec["expected_outcome"],
        })

    return {**_MANIFEST_HEADER, "calls": summary}


# ── CLI ───────────────────────────────────────────────────────────────────────

def _select_scripts(call_filter: str | None) -> list[Path]:
    if call_filter:
        path = SCRIPTS_DIR / f"{call_filter}.md"
        if not path.exists():
            logging.error("Not found: %s", path)
            sys.exit(1)
        return [path]
    return sorted(SCRIPTS_DIR.glob("CALL_*.md"))


def main() -> None:
    ap = argparse.ArgumentParser(description="Build VocalMind ground-truth JSON.")
    ap.add_argument("--call", help="Build for one call only (e.g. CALL_01_refund_outage)")
    ap.add_argument("--check", action="store_true",
                    help="Validate only — do not write any files.")
    args = ap.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    scripts = _select_scripts(args.call)
    if not scripts:
        logging.error("No CALL_*.md scripts found in %s", SCRIPTS_DIR)
        sys.exit(1)

    if not args.check:
        GT_DIR.mkdir(parents=True, exist_ok=True)

    all_warnings: list[str] = []
    records: list[dict] = []

    for md in scripts:
        logging.info("Building ground truth: %s", md.stem)
        record = build_call_ground_truth(md)
        records.append(record)

        warnings = _validate_emotions(parse_script(md), md.stem)
        all_warnings.extend(warnings)

        if not args.check:
            out = GT_DIR / f"{md.stem}.json"
            out.write_text(json.dumps(record, indent=2, ensure_ascii=False),
                           encoding="utf-8")
            logging.info("  -> %s  (%d turns, emotions=%s)",
                         out.name, record["turn_count"], record["emotion_distribution"])

    if not args.check and not args.call:
        # Only refresh manifest when running over all scripts
        manifest = build_manifest(records)
        manifest_path = GT_DIR / "manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False),
                                 encoding="utf-8")
        logging.info("manifest -> %s  (%d calls)", manifest_path.name, len(records))

    if all_warnings:
        logging.warning("UNMAPPED TTS EMOTIONS — extend emotion_map.py:")
        for w in all_warnings:
            logging.warning(w)
        if args.check:
            sys.exit(2)

    logging.info("Done.")


if __name__ == "__main__":
    main()
