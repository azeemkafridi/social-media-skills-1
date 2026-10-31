# Contributing

Create and revise skills under `skills/<category>/<skill-name>/`. Read [the authoring standard](docs/standards/skill-authoring-standard.md) and copy [the skill template](docs/templates/SKILL.template.md); do not create an active skill directly under `skills/`.

Preserve the skill's domain knowledge. Frontmatter and marker repairs may be mechanical, but inputs, decisions, examples, evidence, degraded behaviour, safety boundaries, and acceptance conditions require domain judgement. Keep `SKILL.md` at or below 300 lines (the lean template, D-SK-06) and link extracted references back to the parent entrypoint.

Before opening or merging a change, run (see the README's [Validation](README.md#validation) section for dependencies and the result of each check):

```sh
python3 -X utf8 scripts/validate_skill_engine.py --baseline quality-baseline.json
python3 -X utf8 scripts/check_package_integrity.py
python3 -X utf8 scripts/check_machine_paths.py
python3 -X utf8 scripts/check_skill_aliases.py
python3 -X utf8 scripts/routing_smoke_test.py --min-rank1 92 --lint-fixtures
python3 -X utf8 scripts/check_source_freshness.py
python3 -X utf8 -m unittest discover -s tests -p "test_*.py"
```

`check_source_freshness.py` currently exits 1 because five quarantined source records are overdue; a change must not add to that list. Run `python3 -X utf8 skills/meta-utility/skill-writing/scripts/quick_validate.py <skill-dir>` for each changed skill directory. Finish with `git diff --check`. Update routing fixtures when a trigger or neighbour boundary changes. The expected skill must remain in the top three for every fixture, with a 100% release threshold.

Do not add findings to `quality-baseline.json`; its empty `failure_counts` object is the release invariant. A new finding must be fixed before merge.
