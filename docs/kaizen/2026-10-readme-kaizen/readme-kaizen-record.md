# README kaizen record, 2026-10-31

Scope: the `README.md` of the Social Media Skills Engine (repository `social-media-skills`). This is a scoped micro-cycle that follows the Portfolio Kaizen steps (Observe, Baseline, Select, Experiment, Check, Standardise, Teach, Re-measure). It publishes no score: the engine's published score is unchanged at 60.0 (pass 2 final report). No skill body, script or test was edited.

Branch `kaizen/2026-10-readme-kaizen`, created from `main` at `bfe839b` with a clean working tree (`git status --porcelain` printed 0 lines). Nothing was pushed, tagged or merged. A branch named `kaizen/2026-10-readme-improvements` already existed; it was not touched.

## Observe

The README held 11,393 words in 6 H2 sections. One section, References, held 6,019 words. There was no contents list. The first fenced command was at line 15, but a reader reached the install route only after two paragraphs of 1,205 and 1,783 characters. The October kaizen section held 1,887 words in 17 paragraph-length items. The catalogue (112 rows) and the retired-route table (83 rows) sit in the README because `tests/test_engine_quality.py` reads them from it.

Baseline, measured with `readme-metrics.py` on `main` before any edit, and the result after the last README edit:

| Metric | Baseline | After | Target | Met |
|---|---:|---:|---|---|
| `words` | 11,393 | 5,732 | at most +5%, aim -10% | yes (-49.7%) |
| `h2` | 6 | 18 | none | n/a |
| `toc` | 0 | 1 | 1 | yes |
| `first_cmd` (line) | 15 | 24 | 40 or less | yes (later than before: the at-a-glance list now comes first) |
| `longest_sec` (words) | 6,019 | 833 | 1,500 or less, 1,200 preferred | yes |
| `long_lines` (over 300 characters) | 39 | 12 | at most half (19) | yes (-69%) |
| `max_line` (characters) | 1,783 | 542 | 700 or less | yes |
| `sent_len` (words) | 20.7 | 11.3 | 16.5 or less | yes |
| `fre` (reading ease) | 31 | 58 | no lower than baseline, aim +5 | yes (+27) |

Two cautions about these numbers. First, `words` fell mainly because text moved, not because facts were deleted: 6,019 words went to `docs/references.md` and about 1,900 words of the kaizen section went to a detail record. Second, `readme-metrics.py` leaves bullets and table rows out of `sent_len` and `fre`. A separate count that includes bullets gives mean sentence length 19.6 words before and 11.8 after (386 and 243 sentences). Further checks: no paragraph or list item is over 90 words (longest 69), and no table cell is over 35 words (none before either).

Twelve lines are still over 300 characters. Two are the legal-source statements, which are kept in their original wording. Ten are kaizen items whose link targets add to the line length.

## Select

| Item | Decision | Reason |
|---|---|---|
| R1 Front door | Applied | Purpose in three sentences, audience, six measured facts, three numbered steps with commands, all within the first 39 lines. The freshness exit 1 is the fifth fact. |
| R2 Contents | Applied | 17 in-page links, all resolve (preservation check). |
| R3 Structure | Applied | Largest section is now 833 words. The kaizen section became two H2 sections. The 112-row catalogue became two H2 sections of 56 rows each. |
| R4 Find the right skill | Applied | 12 rows. Every skill path was checked with `test -f`. Tasks paraphrase prompts from `tests/routing-fixtures.json`. |
| R5 No walls of text | Applied | See the cautions above. |
| R6 Plain English | Applied | Short sentences, bullets for lists, terms defined at first use. No word from the anti-slop vocabulary list appears except inside skill names; no em dash; no banned typeface. |
| R7 Say it once | Applied | Plugin commands appear once (Start here). Process narrative sits in the linked records. The kaizen section is kept and tightened. |
| R8 Relocate bulk | Applied to two blocks | References (470 lines) and the unabridged kaizen text. No script, test, manifest or router reads either block (`grep` for the README path and heading text, then the full validator set). |
| R8 for the catalogue and retired routes | Skipped | `tests/test_engine_quality.py` (`count_surface_findings`) reads both tables from `README.md`. Moving them needs a test change, which this cycle may not make. |
| R8 for the date-gate calendar | Skipped | Eight short rows that the "date gates" part of the quality section needs; kept, tightened. |

## Experiment

One commit per theme, explicit `git add` paths only.

| Commit | Theme | Change |
|---|---|---|
| `9bc7877` | Relocation | The References section moved unchanged to `docs/references.md` (197 books, 5 repositories, 81 standards, 122 register sources, 22 websites). Index row added to `docs/README.md`. |
| `ca3bfe2` | Structure and front door | At a glance, Start here, Contents, When to use it, Find the right skill, How it works, Standards the engine checks against, What is inside, Contributing, author and licence. Catalogue split in two. Two H3 sections promoted to H2. |
| `7a4fcf3` | Plain English | Installation, Validation and Quality sections rewritten as short sentences and bullets. Quality split into latest score, open findings and date-triggered gates. |
| `2ede77a` | Relocation | Kaizen section tightened; unabridged text moved to `docs/kaizen/2026-10-readme-kaizen/october-2026-kaizen-detail.md` with links re-based. |
| `1205342` | Plain English | Long lines split, items shortened, kaizen section split into a summary and a list of the 17 changes. |
| `ee4341d` | Correction | The release-block sentence ("Do not release a claim that depends on any of them, including the Ugandan and Kenyan direct-marketing rows ...") restored to its original wording after the plain-English pass had split it. |

### Mandated statements

These were checked as exact strings (whitespace normalised) against `main:README.md` and the new README: the legal-source clauses (Uganda Data Protection and Privacy Act 2019, the 2021 Regulations and the Kenyan, Rwandan and Tanzanian laws, the 179-record register, the quarantine sentence, the UCC clause screen and ICC Code, FTC and ASA/CAP, platform policy pages, WCAG 2.2), the four approval-boundary lines, the retired-route rule, the Digital Research currentness sentence, the release-block sentence, and the CI sentence. All 17 strings are present. The legal clauses are bullets now. Where the original used a semicolon list with an elided verb ("advertising claims against ..."), the bullet restores the verb ("Advertising claims are checked against ...") and keeps every other word.

### Deliberate corrections

1. Item 12 said the package check "now exits 0 with 1,431 and 971 entries". The count was 1,439 at this cycle's baseline and 1,469 after it, because the checkout count includes `.git`. The figure was removed; the README says only that the check enforces a 5,000-entry ceiling.
2. "It already fails today" became "As of 2026-10-31 it already fails".
3. The inline `bash install.sh` in kaizen item 17 now appears only in the detail record. The Validation section still says to call `install.sh` through `bash`.
4. Headings: "Capabilities" became "What is inside" plus two "Skill catalogue" sections; "References" became "Sources and references". Nothing links to `#capabilities` or `#references`. The two anchors that other files use, `#validation` and `#what-the-october-2026-kaizen-improved`, are unchanged.

## Check

Validators on this host (Fedora 44, Python 3.14, Node 22), run on `main` before the first edit and on the branch after the last README edit. Exit codes are identical.

| Command | Before | After |
|---|---|---|
| `python3 -X utf8 scripts/validate_skill_engine.py --baseline quality-baseline.json` | 0 | 0 |
| `python3 -X utf8 scripts/check_package_integrity.py` | 0 | 0 |
| `python3 -X utf8 scripts/check_machine_paths.py` | 0 | 0 |
| `python3 -X utf8 scripts/check_skill_aliases.py` | 0 | 0 |
| `python3 -X utf8 scripts/routing_smoke_test.py --min-rank1 92 --lint-fixtures` | 0 | 0 |
| `python3 -X utf8 scripts/check_source_freshness.py` | 1 (five quarantined records) | 1 (the same five) |
| `python3 -X utf8 scripts/source_ingestion_guardrail.py` | 0 | 0 |
| `python3 -X utf8 -m unittest discover -s tests -p "test_*.py"` | 0 (116 tests) | 0 (116 tests) |
| `python3 -X utf8 tests/agent-integration/test_social_media_agent_contract.py` | 0 | 0 |
| `node hooks/test-destructive-bash-gate.js` | 0 | 0 |
| `node hooks/test-plugin-hook-config.js` | 0 | 0 |
| `node scripts/generate-plugin-manifest.js --engine . --check` | 0 | 0 |
| `quick_validate.py` on one skill folder | not run | 0 for `playbook-crisis-communications` and `blog-writer` |

The freshness gate exits 1 by design and the README says so in At a glance, Validation and Quality and improvement. The `quick_validate.py` check has no baseline run, but the branch changes no skill folder (`git diff --stat main..HEAD` lists only `README.md`, `docs/README.md`, `docs/references.md` and the detail record).

Preservation check, `readme-preserve-check.py . main kaizen/2026-10-readme-kaizen`, after the last README edit:

```text
links: old README 236 targets; new README 32; moved to docs 212; LOST 0
commands: old README 25; kept in README 24; moved to docs 1; LOST 0
anchors: 2 README.md#<anchor> links in tracked files; BROKEN 0
in-page links: 17 anchors used; BROKEN 0
RESULT: OK
```

The anchors line is shown with `<anchor>` in place of the word the checker prints, because the checker would otherwise read that literal text in this file as a link. The first run after this record was added reported 3 anchor links and 1 broken for that reason; it was a false finding caused by the pasted output, not a missing heading. The one command reported as moved is `bash install.sh` (correction 3). Nothing was replaced or removed beyond the four corrections above.

Independent counts used for the figures in At a glance (not taken from the generator that wrote them): `find skills -name SKILL.md` gives 112; `find skills -name ALIAS.md` gives 83; `ls -d skills/*/` gives 16 folders, 15 with active skills; the register parsed with `json` gives 179 records and 5 with `quarantined: true`; the fixture file gives 400 fixtures; the routing and unittest logs give 381 of 400, 125 of 125 and 116 tests.

Not verified: the live status of the URLs in `docs/references.md` (moved unchanged, not re-fetched); rendering of the anchors on GitHub (the checker uses its own slug rule, which matches GitHub's for these headings); `install.ps1` (no PowerShell on this host).

## Standardise

Conventions for the next README editor:

1. Order: title and purpose; At a glance with Start here (first command by line 40); Contents; When to use it; Find the right skill; How it works; standards; approval boundaries; what is inside; Installation; Validation; Quality and improvement; reference tables; sources; Contributing, author and licence.
2. Limits: no H2 section over 1,200 words; no paragraph over 90 words; no table cell over 35 words; mean sentence length 16 words or less; lines over 300 characters only for a mandated statement or a line that carries link targets.
3. Keep these because other files depend on them: the sentence "112 active `SKILL.md` files" style counts, the category table with its total row, the catalogue rows and the retired-route rows (read by `tests/test_engine_quality.py`), and the anchors `#validation` and `#what-the-october-2026-kaizen-improved` (linked from `CONTRIBUTING.md`, `docs/README.md` and `CHANGELOG.md`). The headings "Validation" and "Quality and improvement" are also named in `AGENTS.md`.
4. Put a number in At a glance only after measuring it. Date the block ("Figures as of ...").
5. Long lists go to `docs/`. Leave a short summary and a link in the README, then run the preservation check.

## Teach

1. Measure first with `readme-metrics.py`, then move bulk before you rewrite prose: relocation gave most of the gain, and it is the safest edit.
2. Before moving a table, grep the tests: the 112-row catalogue looks like bulk but `tests/test_engine_quality.py` reads it.
3. After a plain-English pass, re-check every mandated sentence as an exact string. One was split in two and had to be restored.

## Re-measure and next cycle

Re-measured after the last README edit: the table in Observe. The engine score is not re-scored in this cycle.

Open for a later cycle:

- Move the catalogue and retired-route tables (about 1,700 words, 195 rows) to a generated page by changing `tests/test_engine_quality.py` to read it. This cycle may not edit tests.
- The At a glance figures are hand-written. Only the count of 112 is guarded by a test. A small test that compares the fixture, test and register counts with the README would stop them drifting.
- Re-measure the figures at the next audit (proposed 2026-11-30) or when the five quarantined records are read, whichever comes first.
- Add the README metrics (`longest_sec`, `long_lines`, `toc`) to a check, so a future edit that regrows a section is caught.

Cross-engine mismatches found: none. No other repository was edited.
