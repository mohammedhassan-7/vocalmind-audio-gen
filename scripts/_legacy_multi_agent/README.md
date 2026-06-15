# Legacy Multi-Agent Scripts (Archived)

These three scripts were authored against an **older NexaLink policy
set** that included Tier 2 / Tier 3 escalation, warm transfers, and
per-tier authority limits.  They contain `T2_AGENT` / `T3_AGENT`
speakers and dialog flows that demonstrate behaviors which are no
longer permitted under the **flat single-tier policies** introduced on
2026-05-19.

| Script | Demonstrated (deprecated) behavior |
|---|---|
| `CALL_02_billing_dispute_escalation.md` | Tier 1 → Tier 2 transfer when dispute > $200 |
| `CALL_04_access_recovery_fraud.md` | Tier 1 → Tier 2 transfer on suspected unauthorized access (SEC-RULE-008) |
| `CALL_05_retention_abuse.md` | Tier 1 → Tier 3 transfer for cancellation processing AND on Strike 3 of the 3-Strike Protocol |

## Why archived, not deleted

* The dialog content (customer scenarios, agent tone, emotional arcs)
  is high-quality and serves as a reference when authoring the new
  2-agent replacements.
* They are NOT included in the active script set:
  - `parse_scripts.py` and `generate_audio.py` only scan
    `scripts/CALL_*.md` at depth 1, so files under
    `scripts/_legacy_multi_agent/` are ignored.
  - `build_ground_truth.py` therefore does not emit GT for them.
* If you ever need to read them, treat them as **scenario inspiration**
  only — do not copy the multi-agent transfer flows verbatim.

## Replacement plan

The next batch of scripts (written in the follow-up chat) will produce
fresh 2-agent versions covering the same scenarios:

| Old call | New 2-agent replacement scenario |
|---|---|
| CALL_02 | Billing dispute — Daniel resolves end-to-end, opens **Manager Approval ticket** if > $200 cap |
| CALL_04 | Access recovery + suspected fraud — Aisha handles in-call, opens **Data Compliance ticket** for SEC-RULE-008 |
| CALL_05 | Retention + abusive customer — Hannah handles, applies 3-Strike → **terminates** (no transfer) |
