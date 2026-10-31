# Social Media Skills Engine: frozen baseline, pass 2

Frozen on 2026-10-31 at `f5e1ab1`, before any change in this pass. The measurements were taken fresh (commands and logs in [`logs/`](logs/)); the 29 October pass-1 final scores are shown beside them. Each dimension is equally weighted; raw is the arithmetic mean; the Portfolio Standard publishes `min(raw, 65)`. A score moves only where a named measure or defect moved.

| Dimension | Pass-1 final (29 Oct) | Baseline (31 Oct) | Evidence and one-line deficiency |
|---|---:|---:|---|
| Doctrine | 63 | 63 | `AGENTS.md` carries market defaults, authority limits, currentness gate and the anti-slop gate. **Deficiency:** the README states that advertising is checked against the UCC Advertising Standards 2019, but no skill carries a clause-level check (D3). |
| Taxonomy and routing | 78 | 78 | Lexical routing: 396/396 top-3, p@1 377/396 (95.2%), owned negatives 123/123, fixture lint 0 ([log](logs/baseline-routing.txt)). **Deficiency:** only 7 of 112 skills meet three positives and two owned negatives ([log](logs/baseline-routing-coverage.txt)); the figures are a lexical proxy, not live routing. |
| Skill depth | 57 | 57 | The three practitioner routes were read to their references. **Deficiency:** no short-window launch calendar (D7), no client service-outage or data-incident guidance (D2), overlapping class thresholds in media maths (D8); no independent worked-example sample. |
| Applied proof | 48 | 48 | Media arithmetic recomputes; provenance of numeric inputs is enforced since pass 1. **Deficiency:** platform specifications have no source-state check (D9); no live account or campaign evidence. |
| Standards currency | 43 | 42 | 179 records; gate exits 1 with 11 findings: 10 quarantined and `UG-FACEBOOK-ACCESS-2026` overdue since 2026-10-29 ([log](logs/baseline-freshness.txt)). Three register URLs are dead or mismatched (D5). **Deficiency:** the Uganda Act, Regulations, UCC standard, Copyright Act, three other jurisdictions' data laws, Meta policy and the ITU indicator are not currently supported. One point lower than pass 1 for the newly lapsed record. |
| Output readiness | 52 | 52 | Three task outputs exist as synthetic review artefacts. **Deficiency:** the outage output was improvised, not derived from engine guidance (D2); product, destination and release owner remain fictional. |
| Accessibility and inclusion | 61 | 61 | Language and alt-text prompts present. **Deficiency:** no rendered assets or user testing; `NOT_ASSESSED`. |
| Production and handoff | 56 | 56 | Provenance fields validate; handoffs named. **Deficiency:** no client workflow or live account exercised. |
| Hygiene | 70 | 69 | Package check 1,164 / 921 entries under the 5,000 cap, 0 findings; 0 broken relative links in README, router, rules, prompts and docs ([scan](logs/baseline-hygiene-scan.txt)). **Deficiency:** host-specific paths now measured: 1 active-content line and 4 router lines (D6). One point lower because the defect is newly measured, not newly introduced. |
| Safety and integrity | 57 | 56 | No secrets; authority boundary intact. **Deficiency:** a screening checklist overstates the statute (D1, s.7 "is an offence"), and the s.23 breach-notification duty is absent from every skill (D2). |
| **Raw** | **58.5** | **58.2** | (63 + 78 + 57 + 48 + 42 + 52 + 61 + 56 + 69 + 56) / 10 = 58.2 |
| **Published** | **58.5** | **58.2** | `min(58.2, 65)` = 58.2 (cap not binding) |

Target: 95/100. Not achieved; the distance is stated in the backlog.

## Measured inputs

| Input | Result | Source and limit |
|---|---|---|
| Skill validator | `skills=112 compliant=112 failures=0 median_lines=121.0`, exit 0 | [`logs/baseline-validate.txt`](logs/baseline-validate.txt); static contract check |
| Routing smoke test | 396 fixtures; top-3 1.000; p@1 377/396 (95.2%); registered floor 92.0%; owned negatives 123/123; fixture lint 0, exit 0 | [`logs/baseline-routing.txt`](logs/baseline-routing.txt); lexical proxy |
| Owned negatives | 123 across 112 skills | routing coverage log |
| Fixture coverage (three positives plus two owned negatives) | 7 / 112 (6.25%) | [`logs/baseline-routing-coverage.txt`](logs/baseline-routing-coverage.txt) |
| Source freshness | exit 1; 11 findings (10 quarantined, 1 overdue) | [`logs/baseline-freshness.txt`](logs/baseline-freshness.txt) |
| Expired source records | 11 of 179 (6.1%) | same |
| Alias check | 83 routes, 0 findings, 112 active, cap 120, exit 0 | [`logs/baseline-aliases.txt`](logs/baseline-aliases.txt) |
| Package integrity | checkout 1,164, package 921, limit 5,000, 0 findings, exit 0 | [`logs/baseline-package.txt`](logs/baseline-package.txt) |
| Unit tests | 92 pass, exit 0 | [`logs/baseline-unittest.txt`](logs/baseline-unittest.txt) |
| Machine-specific paths | active content 1 line; router 4 lines; dated history 27 lines in 18 files (unchanged) | [`logs/baseline-hygiene-scan.txt`](logs/baseline-hygiene-scan.txt) |
| Broken relative links (README, AGENTS, CONTRIBUTING, rules, prompts, docs) | 0 | same |
| Dangling cross-engine skill names | `NOT_ASSESSED` (no cross-engine inventory run) | n/a |
| Worked-example depth | `NOT_ASSESSED` (no independent sample run) | n/a |
| Tier 3 behavioural evaluation | `NOT_ASSESSED` (no paid model calls) | n/a |

## Blockers (regardless of score)

1. Currentness: the freshness gate fails on 11 records. Quarantined records must not support any current legal or platform claim.
2. D1: until corrected, the outreach checklist overstates s.7 of the Uganda Act and must not be relied on for real outreach.
3. Any real use still needs verified product facts, destination, budget, permissions, privacy review, current platform checks and a named release owner; crisis text must not imply a security or privacy conclusion without a qualified incident owner and counsel.
