# Task 2 re-run: media plan with budget, reach and frequency

Routed through `advertising-strategy-and-budget`, `media-planning` (with `media-maths-and-selection`) and `playbook-paid-social-advertising`. Fictional client and synthetic inputs, as in pass 1: the numbers below are labelled assumptions, not market rates or platform forecasts. The input file is [`media-plan-pass2.json`](media-plan-pass2.json); its provenance and platform-specification states are checked by `scripts/validate_media_plan_provenance.py` against the source register.

## Arithmetic (each line recomputed independently)

Formulae from the skill: impressions = spend ÷ CPM × 1,000; implied reach at the assumed average frequency = impressions ÷ frequency.

| Channel | Spend (UGX) | CPM (UGX) | Impressions | Frequency | Implied reach | Independent check |
|---|---:|---:|---:|---:|---:|---|
| LinkedIn | 4,000,000 | 25,000 | 160,000 | 2.5 | 64,000 | 4,000,000 ÷ 25 = 160,000; 160,000 ÷ 2.5 = 64,000 |
| Instagram / Meta | 5,000,000 | 10,000 | 500,000 | 3.0 | 166,666.67 | 5,000,000 ÷ 10 = 500,000; 500,000 ÷ 3 = 166,666.67 |
| TikTok | 3,000,000 | 8,000 | 375,000 | 3.0 | 125,000 | 3,000,000 ÷ 8 = 375,000; 375,000 ÷ 3 = 125,000 |
| **Total** | **12,000,000** | | **1,035,000** | | **355,666.67 (sum, not unique people)** | 160,000 + 500,000 + 375,000 = 1,035,000 |

The pass-1 script (`../../2026-10-engine-kaizen/tasks/media-plan-check.py`) was re-run on 2026-10-31 and reproduces these figures; its output file is unchanged. The sum of platform reach is not deduplicated reach: unique people across the three platforms are `NOT_ASSESSED`, and the plan must not state a combined reach figure to the client.

Worked comparison in the skill (daily paper and trade magazine) was also recomputed: CPM 75,000 and CPIM 375,000; CPM 240,000 and CPIM 300,000. Both match the text.

## Platform specifications against the register

| Platform and specification | Register record | State in the plan | Why |
|---|---|---|---|
| Meta image and video creative specifications | `META-CREATIVE-SPECS-2026` (register status `verified`, next review 2027-03-23) | `partial` | The record is in window, but the page was not opened in this pass, so no dimension or length is carried into the plan; read the live Ads Guide at the build date |
| Meta advertising policy categories | `META-AD-STANDARDS` (released from quarantine 2026-10-31 as `partial`, structure only) | `partial` | Supports the list of policy headings only; the relevant category must be read in the ad account |
| LinkedIn single-image ad file and text limits | none in the register | `NOT_ASSESSED` | An official page exists (opened in pass 1) but is not registered; no value is carried |
| TikTok paid-placement video limits | none in the register | `NOT_ASSESSED` | Only commercial-content disclosure is registered (`TIKTOK-BRANDED-CONTENT`, `partial`) |

Gate output ([`../logs/test-platform-spec-gate-live.txt`](../logs/test-platform-spec-gate-live.txt)): the plan passes (exit 0, four specifications checked). A negative control that cites the quarantined `UG-DPPR-2021` as `verified`, and a `NOT_ASSESSED` specification carrying a value, fails with exit 1 and two findings. That is the behaviour the pass-1 next-cycle experiment asked for.

## What approval still needs

A client-approved budget and floor, an account-level reach and frequency forecast from each platform, placement previews, frequency controls, a deduplication method, conversion definitions, a landing page, a consent basis for any retargeting, and written client authority before any spend. None is supplied; the plan authorises nothing.
