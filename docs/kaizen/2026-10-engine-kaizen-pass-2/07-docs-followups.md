# Documentation-wave follow-ups (31 October 2026)

The documentation wave changed only documents. These items need a skill, script or mode change, or a decision in another repository, so they were recorded and not edited. Each names the exact file and line as of the commit that closes the wave.

## Skills and references (not edited)

| File and line | Finding | Suggested change |
|---|---|---|
| `skills/meta-utility/kaizen-improvement-system/SKILL.md` line 60 | Names the Digital Research engine as `digital-research-engine`, a name that no longer exists | Use `digital-research-skills` (catalogue id) and resolve through the engine-routing table |
| `skills/content-writing/blog-writer/SKILL.md` line 44 | "the digital-research-engine's three-wave SEO/SERP study" | Same rename |
| `skills/advertising/creative-brief-and-big-idea/SKILL.md` line 36 | "`digital-research-engine`" as an evidence route | Same rename |
| `skills/language/language-standards/references/english-collocations-and-lexical-precision-2026-09-02.md` line 3 | "Canonical study: `digital-research-engine`" | Same rename |
| `skills/meta-utility/kaizen-improvement-system/SKILL.md` line 117 | GitHub URL already uses `digital-research-skills`, so the same file now holds both names | Fixed by the rename on line 60 |

`AGENTS.md` and `rules/common/core.md` already use the current name; the skills above are the remaining mismatch.

## Scripts and file modes (not edited)

| File | Finding | Suggested change |
|---|---|---|
| `scripts/check_machine_paths.py` line 26 | `PORTFOLIO_OWNED_ROUTER_LINES = 3`; `AGENTS.md` now holds 0 of 3 after the portfolio renderer ran (commit `830f154`) | Lower the ceiling to 0, as pass 2 `06-next-cycle.md` intended. `tests/test_machine_paths.py` line 47 reads the constant, so the test follows |
| `install.sh`, `install.ps1`, `scripts/*.js`, `hooks/*.js` | Every file is mode 100644 in the git index, so `./install.sh` fails with "Permission denied" on a fresh Linux clone; the README now says `bash install.sh` | `git update-index --chmod=+x install.sh` (and any script meant to be run directly), then drop the workaround from the README |
| `tests/agent-integration/test_social_media_agent_contract.py` line 24 | Finds the coordination catalogue at `ROOT.parent / "chwezi-engine-agents"`, a fixed sibling name | Read a configurable root (`CHWEZI_ENGINES_ROOT`) first, then fall back to the sibling folder |
| `scripts/generate-plugin-manifest.js` lines 12 and 28 | Header comment uses `digital-research-engine` as the example engine folder | Rename in the comment |
| `.skills-engine/engine-manifest.yaml` (validation list) | Declares four checks. CI also runs `check_package_integrity.py` and the unittest suite, a second workflow runs `source_ingestion_guardrail.py`, and `check_machine_paths.py` runs in neither; none of the four is declared. The routing entry omits `--min-rank1 92` | Decide whether the manifest should list them. The catalogue entry in `chwezi-engine-agents` repeats the same four, so change both together |

## Gate documents (not edited)

`docs/quality-gates/legal-market-release-gate.md` lines 89 (Uganda direct marketing, `UG-DPPR-2021`), 90 (Kenya direct marketing, `KE-DP-GENERAL-2021`) and 98 (Kenya bulk SMS, `KE-DP-GENERAL-2021`) state checks that rest on records that are quarantined and `NOT_ASSESSED`. The gate's own stop condition covers an unavailable source, so the rows are not wrong to cite them, but a reader cannot see the state from the table. Add a status mark to those rows when the five records are read or kept quarantined.

## Cross-engine mismatches (not edited; the other repositories are out of scope)

- `chwezi-engine-agents/catalog/engines.yaml` pins `released_commit: "724970f"` for `social-media-skills`; that commit exists here but is a September commit (`docs: design-system-skills trigger block v2`). The portfolio pin-refresh step in that repository's `06-next-cycle.md` is the owner.
- The `AGENTS.md` blocks between `<!-- chwezi-design-engine:trigger v4 -->` markers are portfolio-shared text and were left as they are.

## Not verified in this wave

- `install.ps1` and the Windows route: no PowerShell is installed on this workstation.
- Non-dry-run `install.sh` and `uninstall` in user scope: they write to `~/.claude`; only `--dry-run`, `doctor` and a project-scope dry run in a scratch folder were run.
- Any claim in the README's reference lists, which were not re-read; the wave checked counts, commands, links and cross-engine names only.
