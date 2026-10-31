#!/usr/bin/env python3
"""Fail when host-specific absolute paths appear in active engine content.

Active content is what an agent loads: skills, rules, prompts, scripts, the README,
the router and the quality-gate, template, standard and source-register documents.
Dated history under docs/, hooks and tests are out of scope.

`AGENTS.md` may keep a small number of lines that sit in router blocks shared across
the portfolio and owned by the coordination package. That allowance is a ceiling:
lower it when those blocks are rewritten; never raise it.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r"(?:[A-Za-z]:[\\/](?:wamp64|Users|Windows|Program Files)|/home/[a-z][\w.-]*/|/Users/[\w.-]+/|\bwamp64\b)")
ACTIVE = ("skills", "rules", "prompts", "scripts", "README.md", "CONTRIBUTING.md", "install.sh", "install.ps1",
          "AGENTS.md", "CLAUDE.md", "docs/quality-gates", "docs/templates", "docs/standards", "docs/source-registers")
SKIP_NAMES = {"check_machine_paths.py"}
SKIP_PARTS = {".git", "__pycache__", "node_modules"}
ROUTER = "AGENTS.md"
PORTFOLIO_OWNED_ROUTER_LINES = 3


def hits(root: Path) -> dict[str, list[int]]:
    found: dict[str, list[int]] = {}
    for item in ACTIVE:
        base = root / item
        if base.is_file():
            files = [base]
        elif base.is_dir():
            files = [p for p in base.rglob("*") if p.is_file()]
        else:
            continue
        for path in files:
            if path.name in SKIP_NAMES or SKIP_PARTS & set(path.parts) or path.suffix in {".pyc", ".pdf", ".png", ".jpg"}:
                continue
            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except (OSError, UnicodeError):
                continue
            numbers = [i for i, line in enumerate(lines, 1) if PATTERN.search(line)]
            if numbers:
                found[path.relative_to(root).as_posix()] = numbers
    return found


def findings(root: Path = ROOT) -> list[str]:
    errors = []
    for rel, numbers in sorted(hits(root).items()):
        if rel == ROUTER:
            if len(numbers) > PORTFOLIO_OWNED_ROUTER_LINES:
                errors.append(f"{rel}: {len(numbers)} host-specific path lines (allowance {PORTFOLIO_OWNED_ROUTER_LINES}); lines {numbers}")
        else:
            errors.append(f"{rel}: host-specific path on line(s) {numbers}")
    return errors


def main() -> int:
    errors = findings()
    if errors:
        print("machine paths: FAIL")
        print("\n".join(f"- {e}" for e in errors))
        return 1
    router = len(hits(ROOT).get(ROUTER, []))
    print(f"machine paths: PASS (active content clean; {ROUTER} holds {router} of {PORTFOLIO_OWNED_ROUTER_LINES} allowed portfolio-owned lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
