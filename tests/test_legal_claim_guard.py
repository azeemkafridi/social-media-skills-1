"""Regression guard for legal claims that were checked against primary text and found overstated.

Each guard records the finding (what the primary text says) so a later edit cannot
reintroduce the overstated wording. Scope is narrow on purpose: these are claims a
practitioner would act on, verified by reading the instrument, not general legal review.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

# id, forbidden pattern, finding. Patterns are applied to every active skill and reference file.
GUARDS = [
    (
        "UG-DPPA-S7-NO-OFFENCE",
        re.compile(r"(?:\(s\.7\)|section 7|s\.7)[^.\n]{0,120}\b(?:is|are) an offence", re.IGNORECASE),
        "Uganda Data Protection and Privacy Act, Cap. 97 (Act 9 of 2019), read 2026-10-31 on the ULII "
        "PDF: s.7 states a consent rule and its exceptions with no penalty; the offences are ss.35 to 37.",
    ),
]

REQUIRED = [
    (
        "skills/business-development/biz-dev-lawful-prospecting-outreach/references/data-protection-checks-for-outreach.md",
        "ss.35 to 37",
        "the corrected statement of where the Act's offences sit",
    ),
]


def active_markdown() -> list[Path]:
    return [p for p in SKILLS.rglob("*.md") if p.name != "ALIAS.md"]


class LegalClaimGuardTests(unittest.TestCase):
    def test_overstated_claims_do_not_reappear(self):
        findings = []
        for path in active_markdown():
            text = path.read_text(encoding="utf-8")
            for guard_id, pattern, why in GUARDS:
                match = pattern.search(text)
                if match:
                    findings.append(f"{guard_id}: {path.relative_to(ROOT).as_posix()}: {match.group(0)!r} ({why})")
        self.assertEqual(findings, [])

    def test_corrected_statements_are_present(self):
        for rel, needle, meaning in REQUIRED:
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertIn(needle, text, f"{rel} lost {meaning}")

    def test_guard_catches_the_original_wording(self):
        original = "- Processing personal data without prior consent (s.7) is an offence; collecting a list therefore needs consent."
        self.assertTrue(GUARDS[0][1].search(original))

    def test_guard_allows_the_corrected_wording(self):
        corrected = "Section 7 carries no penalty of its own: the Act's offences are ss.35 to 37."
        self.assertIsNone(GUARDS[0][1].search(corrected))


if __name__ == "__main__":
    unittest.main()
