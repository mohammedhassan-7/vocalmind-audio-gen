"""verify.py — One-command corpus audit for the TTS audio generator.

Verifies that every script in scripts/CALL_*.md has:
  - a matching declared turn count in YAML
  - the same number of [Tnn] dialog blocks in the body
  - the same number of per-turn WAVs on disk in data/output/<call>/turns/
  - a merged WAV at data/output/<call>/<merged>.wav
  - a ground-truth JSON at data/ground_truth/<call_id>.json

Also scans data/output/generation.log (if present) for the historical retry-failed
error pattern.

Exit code:
  0 — all calls clean
  1 — one or more calls have a turn or file gap
  2 — environment problem (missing scripts/ directory)

Usage:
  python src/verify.py                  # audit every script in scripts/
  python src/verify.py CALL_03 CALL_36  # audit just the named calls
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

_TURN_RE     = re.compile(r"\[T(\d+)\]")
_DECLARED_RE = re.compile(r"^turns:\s*(\d+)", re.MULTILINE)
_WAV_TURN_RE = re.compile(r"^T(\d+)")


def audit_call(script: Path) -> dict:
    """Return one row of audit data for a single script."""
    cid = script.stem
    text = script.read_text(encoding="utf-8", errors="ignore")

    m = _DECLARED_RE.search(text)
    declared = int(m.group(1)) if m else None

    body_ids = sorted({int(t) for t in _TURN_RE.findall(text)})
    in_body = len(body_ids)

    turns_dir = ROOT / "data" / "output" / cid / "turns"
    on_disk = sorted(
        int(_WAV_TURN_RE.match(p.name).group(1))
        for p in turns_dir.glob("T*.wav")
        if _WAV_TURN_RE.match(p.name)
    )

    merged = [
        p for p in (ROOT / "data" / "output" / cid).glob("*.wav")
        if "turns" not in str(p)
    ]
    has_merged = bool(merged)

    gt = ROOT / "data" / "ground_truth" / f"{cid}.json"
    has_gt = gt.exists()

    missing_turns = [t for t in body_ids if t not in on_disk]
    extra_turns   = [t for t in on_disk if t not in body_ids]

    ok = (
        declared is not None
        and declared == in_body
        and declared == len(on_disk)
        and has_merged
        and has_gt
        and not missing_turns
        and not extra_turns
    )

    return {
        "cid": cid,
        "declared": declared,
        "in_body": in_body,
        "on_disk": len(on_disk),
        "has_merged": has_merged,
        "has_gt": has_gt,
        "missing_turns": missing_turns,
        "extra_turns": extra_turns,
        "ok": ok,
    }


def fmt_row(r: dict) -> str:
    flags = []
    if r["declared"] is None:
        flags.append("[no `turns:` in YAML]")
    if r["declared"] is not None and r["declared"] != r["in_body"]:
        flags.append(f"[body!=declared {r['in_body']}/{r['declared']}]")
    if r["declared"] is not None and r["declared"] != r["on_disk"]:
        flags.append(f"[wavs!=declared {r['on_disk']}/{r['declared']}]")
    if not r["has_merged"]:
        flags.append("[NO MERGED]")
    if not r["has_gt"]:
        flags.append("[NO GT JSON]")
    if r["missing_turns"]:
        flags.append(f"[missing T{r['missing_turns']}]")
    if r["extra_turns"]:
        flags.append(f"[extra T{r['extra_turns']}]")
    flag_str = " " + " ".join(flags) if flags else ""
    return (
        f"  {r['cid']:50s} declared={r['declared'] if r['declared'] is not None else '?':>3}  "
        f"body={r['in_body']:>3}  WAVs={r['on_disk']:>3}  "
        f"merged={'Y' if r['has_merged'] else 'N'}  gt={'Y' if r['has_gt'] else 'N'}"
        f"{flag_str}"
    )


def scan_log() -> int:
    """Print the count of historical retry-failed entries in data/output/generation.log."""
    log = ROOT / "data" / "output" / "generation.log"
    if not log.exists():
        print("  (no data/output/generation.log; nothing to scan)")
        return 0
    text = log.read_text(encoding="utf-8", errors="ignore")
    n = text.count("skipped (all retries failed)")
    print(f"  skipped (retries failed) entries: {n}")
    if n:
        print("  These are HISTORICAL events; check that the affected turn WAVs")
        print("  are present on disk above. A recovered turn shows as a normal row.")
    return n


def main() -> int:
    scripts_dir = ROOT / "scripts"
    if not scripts_dir.exists():
        print(f"ERROR: {scripts_dir} not found", file=sys.stderr)
        return 2

    selected = set(sys.argv[1:])
    scripts = sorted(scripts_dir.glob("CALL_*.md"))
    if selected:
        scripts = [s for s in scripts if any(sel in s.stem for sel in selected)]

    print(f"=== Auditing {len(scripts)} script(s) ===")
    rows = []
    for s in scripts:
        r = audit_call(s)
        print(fmt_row(r))
        rows.append(r)

    bad = [r for r in rows if not r["ok"]]
    print("---")
    print(f"TOTAL: {len(rows)}  OK: {len(rows) - len(bad)}  ISSUES: {len(bad)}")

    print()
    print("=== Generation log scan ===")
    scan_log()

    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
