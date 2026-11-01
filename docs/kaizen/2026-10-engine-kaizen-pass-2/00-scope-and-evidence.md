# Social Media Skills Engine: scope and evidence, pass 2

**As of:** 2026-10-31. **Branch:** `kaizen/2026-10-pass2`, created from `main` at `f5e1ab1`. **Pass 1:** 2026-10-29, evidence in [`../2026-10-engine-kaizen/`](../2026-10-engine-kaizen/). No paid model call, account access, posting, spend or publication occurred in this pass.

## Preconditions (Step 0)

| Check | Result |
|---|---|
| Starting branch and HEAD | `main`, `f5e1ab1740e4538024ea4428a772a3d65e0295f3` |
| `git status --porcelain` at start | empty (0 lines); no uncommitted or foreign files to preserve |
| Pass-1 branch | `kaizen/2026-10` still exists locally; `main` is one commit ahead of it (`f5e1ab1`, the experiment-log commit). Pass 2 continues from `main`. |
| Standard and currentness gate | Read in full: portfolio Kaizen Standard (2026-08) and `kaizen-currentness-gate.md` from the research engine |
| Router and kaizen skill | `AGENTS.md`; `skills/meta-utility/kaizen-improvement-system/SKILL.md` |
| Earlier evidence read | Pass-1 `05-final-report.md`, `06-next-cycle.md`, `01-baseline-scorecard.md`, `02-improvement-backlog.md`, `03-currentness.md`, `03-experiment-log.md`, `04-validation-record.md`; the 2026-09-06 audit; the 2026-09-29 consolidation record, scorecard, decisions and snapshot diff |
| Toolchain | `python3` 3.14, `node` 22. No `pwsh`, no `pytest`. The registered commands are run as `python3 -B -X utf8 ...`; `unittest` discovery replaces pytest. No package was installed. |

Registered validator commands, run once before any change (logs in [`logs/`](logs/)):

| Command | Exit | Result |
|---|---:|---|
| `python3 -B -X utf8 scripts/validate_skill_engine.py --baseline quality-baseline.json` | 0 | 112 skills, 112 compliant, 0 failures, median 121 lines |
| `python3 -B -X utf8 scripts/routing_smoke_test.py --lint-fixtures` | 0 | 396/396; top-3 1.000; p@1 377/396 (95.2%); owned negatives 123/123; fixture lint 0 |
| `python3 -B -X utf8 scripts/check_source_freshness.py` | 1 | 11 findings: 10 quarantined (overdue since 2026-10-11 and 2026-10-19) plus `UG-FACEBOOK-ACCESS-2026` overdue since 2026-10-29 |
| `python3 -B -X utf8 scripts/check_skill_aliases.py` | 0 | 83 routes, 0 findings, 112 active, cap 120 |
| `python3 -B -X utf8 scripts/check_package_integrity.py` | 0 | checkout 1,164 entries, package 921, limit 5,000, 0 findings |
| `python3 -B -X utf8 -m unittest discover -s tests -p 'test_*.py'` | 0 | 92 tests pass |

## Pass-1 backlog confirmed as still open (Step 0 item 4)

| Open item | State on 2026-10-31 |
|---|---|
| Ten quarantined source records (pass-1 `06-next-cycle.md` item 1) | **Open.** All ten still quarantined; one further record (`UG-FACEBOOK-ACCESS-2026`) lapsed on 2026-10-29. Worked in item SM2-01. |
| Claim-level support audit of the 2026-09-06 "17 records" (P1) | **Open** for the register as a whole. This pass adds claim-level checks against primary text for the Uganda Act, the UCC standard and the Tanzanian Act (SM2-01, SM2-02, SM2-03). |
| Permission-safe campaign fixtures with failure states and measurement provenance (P2) | **Partly closed** by pass 1 (`5a2f371`). Pass 2 extends it to platform-specification source state (SM2-05). |
| Pass-1 "one small experiment": structured source-state gate in the platform-format check | **Open.** Implemented in SM2-05. |
| 2026-09-29 snapshot: N2 (routing coverage 7/112 vs target 56), N3 (raise p@1 floor 92 to 93), N6/N7 (citations and THIN rows), N8 (legacy short labels) | N2 open at 7/112; N3 open (measured 95.2%; floor not changed here because a floor is registered portfolio-wide); N6-N8 not selected. Moved to `06-next-cycle.md`. |
| Worked-example depth, machine-specific links, cross-engine references | Pass 1 left these `NOT_ASSESSED`. Machine-specific paths and broken relative links are now measured (below). |

## Step 1: the three practitioner tasks, observed through the router

The engine was used as a practitioner would use it: by reading `AGENTS.md`, choosing skills from the router, and then reading the chosen skills and their references to see what they actually supply. The fictional product "Kite Ledger" (invoice-record software for small Ugandan organisations) is retained from pass 1 so results are comparable; it has no customers, results, pricing or live account. The finished practitioner outputs are produced twice: the baseline reading is recorded here (what the engine supplied before any change), and the re-measured outputs are in [`tasks/`](tasks/) after the changes.

### Task 1: four-week launch calendar and first-week copy, three platforms

| Item | Finding |
|---|---|
| Router choice | `pipeline/11-content-calendar` (calendar), `pipeline/10-content-pillars` (inputs), `platforms/platform-linkedin`, `platform-instagram`, `platform-whatsapp`, `meta-analytics-ops/measurement-tracking-plan` (measures), `ai-marketing/anti-ai-slop` (ship gate). Facebook was excluded on engine evidence: `platform-facebook` states access in Uganda is unstable (register `UG-FACEBOOK-ACCESS-2026`). |
| Was the route right? | Mostly. The calendar skill fits only partly: its workflow fixes a 13-week grid on approved pillars (`pipeline/11-content-calendar/SKILL.md`, Workflow step 2) and stops without pillars. A four-week launch is a short window with one objective per week; the skill has no short-window variant. The nearest example is a four-week pilot in `pipeline/06-digital-marketing-strategy/references/channel-creative-and-service-lab.md:127`, which the calendar skill does not link to. |
| Defect (minor, guidance gap) | No short-window launch calendar method in `11-content-calendar`; a practitioner must improvise objective-by-week and per-platform measures. Not fixed this pass (structural; `06-next-cycle.md`). |
| Defect (minor, currency) | `platforms/platform-linkedin/references/company-pages-showcase-and-events.md:51-52` states 120-character tagline and 2,000-character overview limits flagged "legacy; verify current values". A web search found no LinkedIn Help Centre page; the only LinkedIn-owned sources found were LinkedIn Learning tutorials supporting 120 and 2,000, while third-party guides give 1,500 for the overview. Left `NOT_ASSESSED`; not registered. |
| Disclosure check | Owned-product content, no paid creator: influencer disclosure is not triggered. The UCC testimonial and recognition-of-advertising clauses were not available to the practitioner at all (see D3). |

### Task 2: media plan with budget, reach and frequency, checked against the register

| Item | Finding |
|---|---|
| Router choice | `advertising/advertising-strategy-and-budget`, `advertising/media-planning` (and its `media-maths-and-selection.md`), `playbooks/playbook-paid-social-advertising`. Correct. |
| Arithmetic check | The skill's worked comparison recomputes exactly: half-page UGX 4.5m over 60,000 copies gives CPM 75,000 and, at 20% in-target (12,000), CPIM 375,000; magazine UGX 1.2m over 5,000 copies gives CPM 240,000 and, at 80% (4,000), CPIM 300,000. Pass-1's synthetic plan arithmetic (`../2026-10-engine-kaizen/tasks/media-plan-check.py`) was re-run and unchanged. |
| Defect (minor, internal inconsistency) | `media-maths-and-selection.md` section 2: "Secondary: about 30% or more" overlaps "Primary: above about 50%", and no class covers 20% to 30%. A medium at 25% in-target cannot be classified from the text. Thresholds are attributed to a book that is not held in the repository, so the numbers are not changed; a tie-break rule is the safe repair (deferred to `06-next-cycle.md`). |
| Defect (major, tooling) | The media-plan validator checks origin and source on budget, CPM and frequency but nothing about platform specifications. A plan can cite a placement specification whose register record is quarantined or overdue and still pass (pass-1 next-cycle experiment). Fixed in SM2-05. |
| Platform specifications against the register | LinkedIn, Google, TikTok records were scoped `partial` in pass 1 and are inside their windows (to 2026-11-28). `META-AD-STANDARDS` was quarantined with a stale URL. Worked in SM2-01. |

### Task 3: crisis sequence for a paid-service outage

| Item | Finding |
|---|---|
| Router choice | `playbooks/playbook-crisis-communications` (correct), with `policies/policy-ai-content-ethics` and the direct-marketing ethics filter for claims. |
| Defect (major, guidance missing) | The crisis skill and its three references contain no guidance for the client's own service outage or a personal-data incident. A search of `SKILL.md` and `references/` for personal data, breach, outage, downtime, status page and regulator returns only a deepfake reference, a profanity-filter menu path, and the internet-shutdown note (which concerns a state shutdown, not a client outage). Pass 1 therefore wrote its outage sequence by improvisation, not from the engine. |
| Defect (major, legal accuracy gap) | Uganda's Data Protection and Privacy Act s.23 requires a controller to "immediately notify the Authority" of unauthorised access to or acquisition of personal data and lets the Authority decide whether data subjects are told (primary text read this pass). No skill states it. The pass-1 sequence said only "assess notice obligations with counsel". Fixed in SM2-04. |
| Disclosure and tone | No influencer or paid-promotion context. Refund, credit or compensation wording has no engine rule; the source register holds no Uganda consumer-protection instrument that was verified, so the new reference tells the practitioner to take such commitments only from the client's contract and approved policy. |

## Defect register (Step 1 output)

| ID | Severity | File and line | Description |
|---|---|---|---|
| D1 | Major (legal accuracy) | `skills/business-development/biz-dev-lawful-prospecting-outreach/references/data-protection-checks-for-outreach.md:8` | States that processing personal data without prior consent (s.7) "is an offence". The Act's offence provisions are ss.35 to 37 (unlawful obtaining or disclosure, unlawful destruction or alteration, sale of personal data); s.7 states a prohibition and the exceptions, with no penalty. Verified against the ULII PDF of the Act (Chapter 97, as at 3 May 2019). |
| D2 | Major (guidance missing) | `skills/playbooks/playbook-crisis-communications/SKILL.md` and `references/` | No client service-outage or personal-data-incident guidance; s.23 duty absent. |
| D3 | Major (claim without carrier) | `README.md:5` versus `skills/` | README says advertising claims are checked against the UCC Advertising Standards 2019. No skill carries a clause-level check; the standard appears only in the README bibliography and the register. |
| D4 | Minor (unconfirmed claim now confirmable) | `skills/pipeline/08-influencer-marketing-strategy/references/influencer-term-sheet-and-disclosure.md:43` | Says the UCC Advertising Standards cover electronic marketing "(UG-03, reported, not confirmed)". The standard's text was opened: it has testimonial (Section 6 cl.10; Annex 4 cl.43-44) and recognition-of-advertising (Annex 5) clauses, and names neither the internet, social media nor influencers. |
| D5 | Major (currentness blocker) | `docs/source-registers/source-register.json` | 11 overdue records. Three register URLs are dead or mismatched: `TZ-PDPA` and `TZ-PDPR-2023` (host `www.pdpc.go.tz` fails certificate validation; the site is served at `pdpc.go.tz`), `KE-DP-GENERAL-2021` (ODPC PDF returns 404), `META-AD-STANDARDS` (redirects to `transparency.meta.com`). |
| D6 | Minor (hygiene) | `skills/meta-utility/skill-writing/SKILL.md:13`; `AGENTS.md:47,60,232,440` | Host-specific absolute paths in active content. Lines 47, 60 and 440 sit in portfolio-shared router blocks (cross-engine; recorded, not edited). Line 232 and the skill-writing stub are engine-local. |
| D7 | Minor (guidance gap) | `skills/pipeline/11-content-calendar/SKILL.md` Workflow step 2 | No short-window launch calendar (see Task 1). |
| D8 | Minor (internal inconsistency) | `skills/advertising/media-planning/references/media-maths-and-selection.md` section 2 | Class thresholds overlap and leave 20% to 30% unassigned. |
| D9 | Major (tooling) | `scripts/validate_media_plan_provenance.py` | No platform-specification source-state check. |

No safety, privacy or release defect beyond the standing currentness blocker was found. D1 is a legal-accuracy overstatement in a screening checklist, and is treated as a blocker for any real outreach use until corrected.

## Measured inputs added this pass

| Input | Baseline | Source |
|---|---|---|
| Machine-specific paths, active content | 1 line (skill-writing stub) | [`logs/baseline-hygiene-scan.txt`](logs/baseline-hygiene-scan.txt) |
| Machine-specific paths, router | 4 lines (`AGENTS.md`) | same |
| Machine-specific paths, dated history under `docs/` (excluding this evidence) | 27 lines in 18 files; not changed (historical records) | same |
| Broken relative links in README, AGENTS, CONTRIBUTING, rules, prompts, docs | 0 | same |
| Routing coverage at 3 positives plus 2 owned negatives | 7 of 112 (6.25%) | [`logs/baseline-routing-coverage.txt`](logs/baseline-routing-coverage.txt) |
| Dangling cross-engine skill names | `NOT_ASSESSED` (no cross-engine inventory run) | n/a |
| Worked-example depth | `NOT_ASSESSED` (no independent sample) | n/a |
