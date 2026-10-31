"""Host-specific paths must not enter active engine content (Kaizen pass 2, SM2-06)."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_machine_paths.py"
spec = importlib.util.spec_from_file_location("check_machine_paths", SCRIPT)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def tree(files: dict[str, str]) -> Path:
    base = Path(tempfile.mkdtemp())
    for rel, text in files.items():
        path = base / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return base


class MachinePathTests(unittest.TestCase):
    def test_live_checkout_is_clean_within_the_portfolio_allowance(self):
        self.assertEqual(module.findings(ROOT), [])

    def test_windows_unix_and_mac_host_paths_are_found_in_a_skill(self):
        for text in ("see C:\\wamp64\\www\\other\\x.md", "see C:/Users/someone/file.md",
                     "see /home/someone/repo/file.md", "see /Users/someone/repo", "the wamp64 folder"):
            root = tree({"skills/g/s/SKILL.md": text})
            self.assertTrue(module.findings(root), text)

    def test_ordinary_relative_paths_and_urls_are_not_flagged(self):
        root = tree({"skills/g/s/SKILL.md": "see references/a.md and https://example.com/home/page and /home alone"})
        self.assertEqual(module.findings(root), [])

    def test_history_and_hooks_are_out_of_scope(self):
        root = tree({"docs/audits/old.md": "C:\\wamp64\\www\\x", "hooks/t.js": "C:\\wamp64\\www\\x", "tests/t.py": "/home/a/b/c"})
        self.assertEqual(module.findings(root), [])

    def test_router_allowance_is_a_ceiling(self):
        allowed = "\n".join("C:\\wamp64\\www\\x" for _ in range(module.PORTFOLIO_OWNED_ROUTER_LINES))
        self.assertEqual(module.findings(tree({"AGENTS.md": allowed})), [])
        over = allowed + "\nC:\\wamp64\\www\\y"
        self.assertTrue(any("AGENTS.md" in f for f in module.findings(tree({"AGENTS.md": over}))))


if __name__ == "__main__":
    unittest.main()
