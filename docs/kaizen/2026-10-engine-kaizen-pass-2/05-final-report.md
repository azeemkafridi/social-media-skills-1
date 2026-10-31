# Final report, pass 2: Social Media Skills Engine

**Date:** 2026-10-31. **Branch:** `kaizen/2026-10-pass2`, created from `main` at `f5e1ab1`. **Repository started on:** `main` (clean). Nothing was pushed, tagged or released. Scores below are self-assessed from named measures; no independent re-grade or behavioural run took place, so every movement is small and tied to one measure.

| Dimension | Pass-1 final (29 Oct) | Baseline (31 Oct) | Final | What moved, and what remains |
|---|---:|---:|---:|---|
| Doctrine | 63 | 63 | 64 | The README's UCC claim now has a working carrier ([clause screen](../../../skills/content-writing/references/uganda-advertising-standards-check.md)), `a86f456`. Remaining: the screen is not yet threaded through older playbooks. |
| Taxonomy and routing | 78 | 78 | 78 | 400/400 top-3, p@1 381/400 (95.2%), owned negatives 125/125; coverage 7 to 9 of 112 (8.0%). Not scored up: coverage is still far from the 56-skill target and all figures are lexical. |
| Skill depth | 57 | 57 | 59 | Outage and data-incident reference (`14ab9be`) and the UCC screen close two named gaps. Remaining: no short-window launch calendar, overlapping class thresholds, no independent depth sample. |
| Applied proof | 48 | 48 | 50 | Platform-spec source-state gate with a live-register negative control (`5b46d84`); media arithmetic recomputed independently. Remaining: no live account or campaign evidence. |
| Standards currency | 43 | 42 | 47 | Blocking records 11 to 5; claim-level checks against primary text for the Uganda Act, UCC standard and Tanzanian Act (`b6dc4e0`). Five legal and market records remain `NOT_ASSESSED`. Still a release blocker. |
| Output readiness | 52 | 52 | 54 | The outage output is now derived from engine guidance, not improvised. Remaining: product, destination and release owner are fictional. |
| Accessibility and inclusion | 61 | 61 | 61 | No change; no rendered assets or user testing. |
| Production and handoff | 56 | 56 | 57 | Specification source states travel with the plan. Remaining: no client workflow exercised. |
| Hygiene | 70 | 69 | 71 | Host-path ratchet and two engine-local paths removed (`ecef6e1`); 0 broken relative links. Remaining: three host paths sit in portfolio-owned router blocks. |
| Safety and integrity | 57 | 56 | 59 | Statute overstatement corrected and guarded (`d5c8a4c`); s.23 notification duty added from primary text; quarantine release now requires evidence (`5aed7e2`). Remaining: Regulations and PDPO guidance unread. |
| **Raw** | **58.5** | **58.2** | **60.0** | (64 + 78 + 59 + 50 + 47 + 54 + 61 + 57 + 71 + 59) / 10 = 60.0 |
| **Published, `min(raw, 65)`** | **58.5** | **58.2** | **60.0** | Cap not binding. Target 95/100 not achieved. |

## Kept changes (none reverted)

| Item | Commit | Result |
|---|---|---|
| Baseline, defect register and backlog | `8eecbb1` | Frozen before any change |
| SM2-02: Uganda Act s.7 "is an offence" corrected; regression test | `d5c8a4c` | Statute read; guard has a negative control |
| SM2-01b: evidence rule for releasing a quarantine | `5aed7e2` | 3 tests red, then 11/11 |
| SM2-01: register refreshed from primary text; dead URLs fixed; date-pinned test made self-updating | `b6dc4e0` | Findings 11 to 5 (five quarantines released, one record re-checked; the commit subject says "six" for the six records touched) |
| SM2-03: Uganda advertising standards clause screen | `a86f456` | 16 of 16 quoted phrases located in primary text |
| SM2-04: service outage and data-incident communications | `14ab9be` | Validator contract kept (description 347 characters) |
| SM2-07: owned negatives for influencer and outreach routes | `7940e14` | Coverage 7 to 9 of 112 (the commit body says "8 to 9"; the measured start was 7) |
| SM2-05: platform-specification source-state gate | `5b46d84` | Live pass and negative control |
| SM2-06: host-path check with ceiling | `ecef6e1` | Red on the live checkout, then green |

The closing evidence commit follows these; `git log kaizen/2026-10-pass2` lists it.

## Findings that matter to Peter

1. The engine's own text overstated a statute (D1) and the crisis playbook had no answer to the commonest practitioner emergency for a software client, a service outage with a possible data question (D2). Both are now corrected from primary text.
2. The UCC Advertising Standards 2019 name neither social media nor influencers. The engine now says so, anchors on the medium-neutral clauses (identifiability, cross-media campaigns) and marks application to social posts `NOT_ASSESSED`. Anyone telling a client that UCC "requires" an influencer label from this standard would be overreaching.
3. ULII (the Uganda Act and Regulations) refuses automated HTML access, but publishes a PDF through its media host that was readable. The Regulations PDF was not found by that route.

## Residual risk

- The source gate still exits 1 (five records). Release of any claim that depends on them stays blocked.
- Registered statuses are `partial` with narrow scopes: they say what was read, not that a campaign or post is compliant.
- Scores are self-assessed; a pass-3 independent grading should test them.
- Routing is lexical; ownership of the three router-line paths belongs to the portfolio cycle.

Branches: started on `main`; work is on `kaizen/2026-10-pass2` (see the end of this report for the checkout state).
