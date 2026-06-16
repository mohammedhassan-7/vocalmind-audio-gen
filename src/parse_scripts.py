"""parse_scripts.py — Parse NexaLink call scripts into structured objects.

Each script .md file contains three machine-readable regions:

  1. A YAML front-matter block at the top (in a ```yaml … ``` fence).
     Provides call-level metadata: call_id, agent_profile.name,
     customer_profile.name, sop_primary, policy_refs, kb_refs,
     expected_outcome, emotional_arc, content_warning.

  2. A Markdown "Coverage" table mapping policy elements to turn ranges.

  3. A sequence of turn blocks, each formatted as:
       [Tnn] SPEAKER | emotion:intensity | pace | pitch | volume [| (para)]
       "utterance text"
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Turn:
    turn_id: str       # "T01", "T02", …
    speaker: str       # "AGENT", "CUSTOMER", "IVR", "T2_AGENT", "T3_AGENT"
    emotion: str       # e.g. "frustrated"
    intensity: int     # 1–5
    pace: str          # slow | normal | fast | rushed
    pitch: str         # low | mid | high
    volume: str        # quiet | normal | loud
    paralinguistics: list = field(default_factory=list)  # ["sigh", "pause", …]
    text: str = ""
    call_id: str = ""


@dataclass
class CoverageItem:
    element: str
    where:   str
    notes:   str = ""


@dataclass
class ScriptMetadata:
    """Call-level metadata pulled from the YAML front-matter."""
    call_id: str = ""
    duration_estimate: str = ""
    turns_declared: int = 0
    sop_primary: str = ""
    policy_refs: str = ""
    kb_refs: str = ""
    agent_name: str = ""
    agent_voice_hint: str = ""
    customer_name: str = ""
    customer_voice_hint: str = ""
    expected_outcome: str = ""
    emotional_arc: str = ""
    content_warning: str = ""


# ── Header regex (turn dialog lines) ─────────────────────────────────────────

# [T01] SPEAKER | emotion:N | pace | pitch | volume [| (para)]
_HEADER = re.compile(
    r'\[(?P<id>T\d+)\]\s+(?P<speaker>\S+)\s*\|'
    r'\s*(?P<emotion>[a-z_]+):(?P<intensity>\d)\s*\|'
    r'\s*(?P<pace>\w+)\s*\|'
    r'\s*(?P<pitch>\w+)\s*\|'
    r'\s*(?P<volume>\w+)'
    r'(?:\s*\|\s*(?P<para>[^\n]+))?'
)

_TEXT = re.compile(r'"([^"]+)"', re.DOTALL)

# ── YAML front-matter regexes ────────────────────────────────────────────────

_YAML_BLOCK = re.compile(r'```yaml\s*\n(.*?)\n```', re.DOTALL)

# matches:    name: "Priya"   under  agent_profile:
_AGENT_NAME = re.compile(
    r'agent_profile\s*:\s*\n\s*name\s*:\s*"(?P<name>[^"\n]+)"',
    re.MULTILINE,
)
_CUSTOMER_NAME = re.compile(
    r'customer_profile\s*:\s*\n\s*name\s*:\s*"(?P<name>[^"\n]+)"',
    re.MULTILINE,
)

# top-level YAML scalars: e.g.  sop_primary: "SOP-01 (...)"
def _yaml_scalar(yaml_text: str, key: str) -> str:
    pat = re.compile(rf'^{re.escape(key)}\s*:\s*"?(?P<val>[^"\n]+?)"?\s*$', re.MULTILINE)
    m = pat.search(yaml_text)
    return m.group("val").strip() if m else ""


def _yaml_block_field(yaml_text: str, block_key: str, field: str) -> str:
    """Return the value of `field` nested under `block_key:` in the YAML text.

    Walks indented lines after `block_key:` until indentation drops back to
    column zero, looking for a `field: "value"` row. Safer than a single
    multi-line regex because it cannot leak into a sibling block.

    Example:
      customer_profile:
        name: "Rachel Thornton"
        voice_hint: "female, 30s, neutral US accent"
      agent_profile:
        ...

    _yaml_block_field(text, "customer_profile", "voice_hint")
        → "female, 30s, neutral US accent"
    """
    header = re.search(rf'^{re.escape(block_key)}\s*:\s*$', yaml_text, re.MULTILINE)
    if not header:
        return ""
    rest = yaml_text[header.end():]
    for raw_line in rest.splitlines():
        if not raw_line.strip():
            continue
        stripped = raw_line.lstrip()
        if stripped == raw_line:  # un-indented → next top-level block
            break
        m = re.match(rf'{re.escape(field)}\s*:\s*"([^"\n]+)"', stripped)
        if m:
            return m.group(1).strip()
    return ""


# ── Coverage-table regex ─────────────────────────────────────────────────────

# Looks for a Markdown pipe table whose header row contains "Element" + "Where"
_COVERAGE_HEADER = re.compile(
    r'^\|\s*Element\s*\|\s*Where\s*\|\s*Notes\s*\|\s*$',
    re.MULTILINE | re.IGNORECASE,
)


# ── Public helpers ───────────────────────────────────────────────────────────

def parse_agent_name(md_path: Path) -> str | None:
    """Lowercase, ASCII-safe first-name token from agent_profile.name."""
    raw = md_path.read_text(encoding="utf-8")
    m = _AGENT_NAME.search(raw)
    if not m:
        return None
    name = m.group("name").strip()
    first = re.sub(r"[^a-zA-Z]", "", name.split()[0]) if name else ""
    return first.lower() or None


def parse_metadata(md_path: Path) -> ScriptMetadata:
    """Extract call-level metadata from the YAML front-matter."""
    raw = md_path.read_text(encoding="utf-8")
    meta = ScriptMetadata(call_id=md_path.stem)

    yaml_match = _YAML_BLOCK.search(raw)
    yaml_text = yaml_match.group(1) if yaml_match else raw  # fall back to full doc

    meta.duration_estimate = _yaml_scalar(yaml_text, "duration_estimate")
    try:
        meta.turns_declared = int(_yaml_scalar(yaml_text, "turns") or 0)
    except ValueError:
        meta.turns_declared = 0
    meta.sop_primary      = _yaml_scalar(yaml_text, "sop_primary")
    meta.policy_refs      = _yaml_scalar(yaml_text, "policy_refs")
    meta.kb_refs          = _yaml_scalar(yaml_text, "kb_refs")
    meta.expected_outcome = _yaml_scalar(yaml_text, "expected_outcome")
    meta.emotional_arc    = _yaml_scalar(yaml_text, "emotional_arc")
    meta.content_warning  = _yaml_scalar(yaml_text, "content_warning")

    agent_m = _AGENT_NAME.search(yaml_text)
    if agent_m:
        meta.agent_name = agent_m.group("name").strip()
    cust_m = _CUSTOMER_NAME.search(yaml_text)
    if cust_m:
        meta.customer_name = cust_m.group("name").strip()

    meta.agent_voice_hint    = _yaml_block_field(yaml_text, "agent_profile",    "voice_hint")
    meta.customer_voice_hint = _yaml_block_field(yaml_text, "customer_profile", "voice_hint")

    return meta


def parse_coverage(md_path: Path) -> list[CoverageItem]:
    """Extract the Coverage table rows. Returns [] if no table is found."""
    raw = md_path.read_text(encoding="utf-8")
    header = _COVERAGE_HEADER.search(raw)
    if not header:
        return []

    # Scan rows directly after the header until we hit a non-pipe line
    items: list[CoverageItem] = []
    rest = raw[header.end():]
    for line in rest.splitlines():
        line = line.strip()
        if not line:
            if items:
                break  # blank line ends the table
            else:
                continue
        if not line.startswith("|"):
            break
        if re.match(r'^\|[\s\-:|]+\|$', line):  # alignment separator row
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        element = cells[0]
        where   = cells[1]
        notes   = cells[2] if len(cells) > 2 else ""
        if not element or element.lower() == "element":
            continue
        items.append(CoverageItem(element=element, where=where, notes=notes))

    return items


def parse_script(md_path: Path) -> list[Turn]:
    """Parse every dialog turn from the script."""
    raw = md_path.read_text(encoding="utf-8")
    call_id = md_path.stem

    # Strip markdown code-fence markers so the regex works on plain content.
    raw = re.sub(r'```\s*\n?', '', raw)

    turns: list[Turn] = []
    pos = 0

    while pos < len(raw):
        hm = _HEADER.search(raw, pos)
        if not hm:
            break

        tm = _TEXT.search(raw, hm.end())
        if not tm:
            break

        para_raw = hm.group("para") or ""
        para_list = [p.strip() for p in re.findall(r'\(([^)]+)\)', para_raw)]

        turns.append(Turn(
            turn_id=hm.group("id"),
            speaker=hm.group("speaker"),
            emotion=hm.group("emotion"),
            intensity=int(hm.group("intensity")),
            pace=hm.group("pace"),
            pitch=hm.group("pitch"),
            volume=hm.group("volume"),
            paralinguistics=para_list,
            text=tm.group(1).strip(),
            call_id=call_id,
        ))

        pos = tm.end()

    return turns
