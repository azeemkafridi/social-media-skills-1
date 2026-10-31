# Changelog

Notable changes to the Social Media Skills Engine (repository `social-media-skills`). The repository has not kept a changelog before; the release of 1.2.0 (29 September 2026, `750982a`) was recorded only in the version fields of `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` and `.skills-engine/engine-manifest.yaml`. Evidence for each cycle is in [`docs/kaizen/`](docs/kaizen/); [`docs/README.md`](docs/README.md) is the index. The version field still reads 1.2.0: neither October cycle changed it.

## 2026-10-31: Kaizen pass 2 and documentation wave

The pass 2 commits were made on branch `kaizen/2026-10-pass2` and are on `main`. Scores are self-assessed: raw 60.0, published `min(raw, 65)` 60.0 (pass 1 closed at 58.5; pass 2 baseline 58.2). The source-freshness gate still exits 1 because five quarantined records remain overdue ([final report](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md)). The README section [What the October 2026 kaizen improved](README.md#what-the-october-2026-kaizen-improved) gives the before and after figures for both October cycles, with the basis of each figure.

### Safety and legal accuracy

- `d5c8a4c` corrects the claim that Uganda Data Protection and Privacy Act s.7 "is an offence" (the Act states the consent rule and exceptions with no penalty there) and adds a regression test with a negative control.
- `a86f456` adds the Uganda advertising standards clause screen (`skills/content-writing/references/uganda-advertising-standards-check.md`). The UCC Advertising Standards 2019 name neither social media nor influencers, so application to social posts is marked `NOT_ASSESSED`.
- `14ab9be` adds service-outage and data-incident communications to the crisis playbook, including the Act's s.23 notification duty read from primary text.

### Source currentness

- `5aed7e2` requires evidence (scope, release basis, same-day verification) to release a source quarantine.
- `b6dc4e0` refreshes the register from primary text: five quarantines released (Uganda Act, UCC standard, Tanzanian Act and Regulations, Meta advertising standards), one more record re-checked, three dead URLs corrected, and blocking findings fall from 11 to 5. The commit subject says "six sources"; the correct count is five released and one re-checked, six records touched.
- `5b46d84` gates platform specifications on the state of their register record in `scripts/validate_media_plan_provenance.py`, with a live pass and a negative control.

### Routing

- `7940e14` adds owned negatives for the influencer and outreach routes. Fixture coverage (three positives and two owned negatives) moves from 7 to 9 of 112 skills; the commit message says "8 of 112 to 9 of 112", but the measured start was 7. Routing at the close: 400 of 400 in the top three, precision at 1 of 381 of 400 (95.2%, lexical proxy), 125 owned negatives.

### Hygiene

- `ecef6e1` adds a host-specific path check with a ceiling (`scripts/check_machine_paths.py`).
- `8eecbb1`, `b04171e` and `df61a68` hold the frozen baseline, backlog and evidence for pass 2.

### Documentation wave

- `830f154` regenerates the three portfolio-managed router sentences in `AGENTS.md` with the shared renderer, so they no longer name workstation paths; a second run changed nothing.
- `5bfa956` adds [`docs/README.md`](docs/README.md), an index separating controlling documents from dated records.
- `2abddc7` rewrites the README's install and validation steps for Linux (`python3`, dependencies, a table of each check and its measured result, `bash install.sh` because the file is not executable, the installer also copies `rules/`) and adds the Quality and improvement section with the open findings and the calendar of date-triggered gates.
- `797a0ed` and `948d043` update `CONTRIBUTING.md` and the source-register guide in the same way.
- `57067dd` and `3075062` update `AGENTS.md` and `rules/common/core.md`: the Digital Research engine is named `digital-research-skills`, a pointer to a private, git-ignored project file is removed, and the release-gate command list now includes the alias, freshness, routing-lint and unittest checks.

Follow-ups that need a skill or script change are in [`07-docs-followups.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/07-docs-followups.md).

## 2026-10-29: Kaizen pass 1

Branch `kaizen/2026-10`. Raw and published score 58.5, unchanged from the baseline ([final report](docs/kaizen/2026-10-engine-kaizen/05-final-report.md)).

- `3664c85` quarantined ten overdue, unverified sources; `a80bc2e` makes a quarantined source fail the freshness gate whatever its review date; `b42b6ea` rejects malformed quarantine state.
- `177e2a0` enforces the 5,000-entry package ceiling and plugin identity; `15e73a8` rejects a symlinked plugin manifest directory.
- `5a2f371` requires an origin and source for every numeric media-plan input; `a4ef219` keeps the media-planning workflow numbering sequential.
- `ecc151a` exposes the editorial overlay checks (ME1 to ME7, AS1 to AS7) at the anti-slop entry skill.
- `f2fd463` and `40d6cd7` extend the calendar and crisis routing fixtures and align the currentness test.

## 1.2.0, 2026-09-29

`750982a` released version 1.2.0 after the Social Kaizen consolidation (191 to 112 active skills, 83 retired routes). See [`docs/kaizen/consolidation-2026-09-29/`](docs/kaizen/consolidation-2026-09-29/).
