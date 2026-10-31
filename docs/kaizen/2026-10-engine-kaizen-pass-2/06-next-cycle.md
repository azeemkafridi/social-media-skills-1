# Next-cycle handoff (from pass 2, 2026-10-31)

## Open findings

1. **Five quarantined records** (the only freshness failures): `UG-DPPR-2021` and `UG-COPYRIGHT-2026` (ULII blocks automated HTML access; find a ULII media PDF for each or the PDPO and Parliament copies), `KE-DP-GENERAL-2021` (registered ODPC URL returns 404; find the current ODPC or Kenya Law copy), `RW-DPP-2021` (read Articles 29 to 36 and the direct-marketing articles; confirm the law number and gazette date), `ITU-INTERNET-USAGE` (no skill uses it; read the indicator through an accessible ITU route or retire the record). Details: [03-currentness.md](03-currentness.md).
2. **Amendment chain after December 2023** for the Uganda Act, and any UCC revision: search the Uganda Gazette and UCC notices, then lift the `partial` limits.
3. **Short-window launch calendar (D7):** `11-content-calendar` fixes a 13-week grid. Add a four-week launch variant (objective per week, per-platform measure with denominator, claim-evidence file) and link the existing four-week pilot example in `06-digital-marketing-strategy/references/channel-creative-and-service-lab.md`.
4. **Media-maths class thresholds (D8):** primary, secondary and tertiary overlap and leave 20% to 30% open. Add a stated tie-break without altering the book-attributed numbers.
5. **LinkedIn page-field limits:** 120-character tagline and 2,000-character overview are supported only by LinkedIn Learning tutorials; find a LinkedIn Help Centre source or mark them in the reference.
6. **Pass-1 carry-over:** broader 179-record claim audit; worked-example depth sample; routing coverage toward 56 of 112 (now 9); raise the p@1 floor from 92 to 93 with the portfolio ratchet (measured 95.2%); Tier 3 behavioural runs need Peter's spend approval.
7. **Platform specification values:** `META-CREATIVE-SPECS-2026` and similar records are `verified` in the register but were not opened in this pass; the new gate proves record state, not values. Read the live pages at each build date.

## Cross-engine and portfolio mismatches (not edited; exact files)

| Mismatch | This engine | Other side |
|---|---|---|
| Host-specific paths in portfolio-shared router blocks | `AGENTS.md` lines 47 (a Windows checkout path to the research engine), 60 (a Windows path to the dev engine's control-plane document) and 443 (a Windows path to the craft standard in `chwezi-engine-agents`) | These blocks are portfolio-shared text (the currentness gate, the control-plane pointer and the craft contract), so they were not edited here. The research engine's own `AGENTS.md` already words the equivalent pointers as "resolve via the active engine-routing table"; adopt that wording in the shared source, then lower `PORTFOLIO_OWNED_ROUTER_LINES` in `scripts/check_machine_paths.py` to 0. |
| Dated pointers to the research engine's registers | `skills/meta-utility/kaizen-improvement-system/SKILL.md` links the portfolio standard by a GitHub URL under the repository name `digital-research-skills`, which may be the pre-rename name | Research engine repository was renamed upstream; confirm the live URL in the research cycle. |
| UCC standard handoffs | New clause screen in `skills/content-writing/references/uganda-advertising-standards-check.md` | `proposal-skills` (communications and visibility plans) and `website-skills` (shared AI-search learning) carry their own advertising claims; offer them the screen and the `NOT_ASSESSED` wording. Brand assets stay with the design engine. |

## One small experiment for next time

Run the new platform-spec gate against two real, client-supplied media plans (permission first) and measure how many specifications arrive without a register record. Where a platform has no record (LinkedIn ad formats, TikTok paid placements), register one only after its official page has been opened and read, then count how many `NOT_ASSESSED` specs convert to `partial`. Stop if the gate blocks an organic-only plan or if a record is added without a read.

## Re-audit

Proposed date: **2026-11-30**, or earlier once the five quarantined records are read. Re-run all registered checks and the three practitioner tasks, and have the scores graded by someone who did not make the changes.
