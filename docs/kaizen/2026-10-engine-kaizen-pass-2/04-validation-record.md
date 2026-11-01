# Validation record, pass 2 (2026-10-31)

Every command was run from the repository root after the last code or content edit of the pass, as `python3 -B -X utf8 ...` (the registered commands name `python`). Logs are in [`logs/`](logs/). Routing figures are lexical-fixture measures, not live routing. The source gate fails by design while five records stay quarantined.

## Registered release checks

| Command | Exit | Baseline (31 Oct) | Final | Log |
|---|---:|---|---|---|
| `scripts/validate_skill_engine.py --baseline quality-baseline.json` | 0 | 112 compliant, 0 failures | 112 compliant, 0 failures, median 121 | [`final-validate.txt`](logs/final-validate.txt) |
| `scripts/routing_smoke_test.py --lint-fixtures` | 0 | 396/396; p@1 377/396 (95.2%); owned negatives 123/123 | 400/400; top-3 1.000; p@1 381/400 (95.2%); owned negatives 125/125; lint 0 | [`final-routing.txt`](logs/final-routing.txt) |
| `scripts/check_source_freshness.py` | **1** | 11 findings (10 quarantined, 1 overdue) | **5 findings, all quarantined and `NOT_ASSESSED`** | [`final-freshness.txt`](logs/final-freshness.txt) |
| `scripts/check_skill_aliases.py` | 0 | 83 routes, 0 findings | 83 routes, 0 findings, 112 active, cap 120 | [`final-aliases.txt`](logs/final-aliases.txt) |
| `scripts/check_package_integrity.py` | 0 | checkout 1,164, package 921 | checkout 1,338, package 958, limit 5,000, 0 findings | [`final-package.txt`](logs/final-package.txt) |
| `scripts/check_machine_paths.py` (new) | 0 | would fail: 4 router lines, 1 active line | PASS; router 3 of 3 allowed | [`final-machine-paths.txt`](logs/final-machine-paths.txt) |
| `-m unittest discover -s tests -p 'test_*.py'` | 0 | 92 tests | 116 tests pass | [`final-unittest.txt`](logs/final-unittest.txt) |

The package count rose with the new evidence files and references; the 5,000-entry ceiling is unaffected.

## New automated checks (guard against recurrence)

| Check | Guards against | Evidence |
|---|---|---|
| Released-quarantine rule in `check_source_freshness.py`, 4 new tests | Clearing a source by changing a date | [`test-released-quarantine.txt`](logs/test-released-quarantine.txt); red before, green after |
| `tests/test_legal_claim_guard.py`, 4 tests | Reintroducing "s.7 is an offence" | [`test-legal-claim-guard.txt`](logs/test-legal-claim-guard.txt); negative control matched the old text |
| Platform-spec gate in `validate_media_plan_provenance.py`, 11 new tests | A quarantined or overdue spec shown as current | [`test-platform-spec-gate-live.txt`](logs/test-platform-spec-gate-live.txt) (live pass and negative control) |
| `scripts/check_machine_paths.py` plus 5 tests | New host-specific paths in active content | [`test-machine-paths.txt`](logs/test-machine-paths.txt) |
| Audit-date test follows the register `as_of` | A hand-edited date test breaking each cycle | `tests/test_engine_quality.py`; suite green |

## Independent cross-checks

[`independent-crosschecks.txt`](logs/independent-crosschecks.txt): 400 fixture lines by `grep`, 112 `SKILL.md` and 83 `ALIAS.md` by `find`, 5 quarantined and 179 total register records by a separate script, and a `grep` for host paths that finds only the router and the checker's own pattern. [`clause-screen-text-checks.txt`](logs/clause-screen-text-checks.txt): 16 quoted clause or statute phrases located in the extracted primary texts; seven digital-media terms occur 0 times in the UCC text.

## Re-measured tasks

The three practitioner outputs were re-produced after the changes: [calendar and copy](tasks/task1-launch-calendar.md), [media plan](tasks/task2-media-plan.md) (arithmetic recomputed, specification states gated against the register) and [outage sequence](tasks/task3-outage-sequence.md) (derived from the new engine reference). Synthetic, review-only artefacts.

## NOT_ASSESSED and blockers

- Source freshness exits 1: `UG-DPPR-2021`, `UG-COPYRIGHT-2026`, `KE-DP-GENERAL-2021`, `RW-DPP-2021`, `ITU-INTERNET-USAGE` have no readable primary text yet (ULII, ITU DataHub and Kenya Law block automated access; ODPC link dead; Rwanda articles not read).
- Amendments after December 2023 to the Uganda Act, and any revision of the UCC standard, are not proven absent.
- Tier 3 behavioural runs and every paid model call (none made); live routing; live accounts, forecasts, deduplicated reach, platform specification values (not read in this pass).
- Rendered accessibility, worked-example depth sample, dangling cross-engine skill names.
- Model comparison (quality, latency, cost, account availability) for the newer OpenAI releases: not run; pins unchanged.
- No `pwsh` or `pytest` on this host; nothing in this engine's registered checks needed either.
