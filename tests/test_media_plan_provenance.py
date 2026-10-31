import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_media_plan_provenance.py"
spec = importlib.util.spec_from_file_location("media_provenance", SCRIPT)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def valid_row():
    return {"channel": "Example", **{
        key: {"value": value, "origin": "synthetic_assumption", "source": "fixture assumption"}
        for key, value in (("budget_ugx", 1000), ("cpm_ugx", 25), ("frequency", 2))
    }}


class MediaPlanProvenanceTests(unittest.TestCase):
    def test_workflow_numbering_remains_sequential(self):
        workflow = (ROOT / "skills/advertising/media-planning/SKILL.md").read_text(encoding="utf-8").split("## Workflow", 1)[1].split("## ", 1)[0]
        numbers = [int(line.split(".", 1)[0]) for line in workflow.splitlines()
                   if line[:1].isdigit() and ". " in line]
        self.assertEqual(list(range(1, 11)), numbers)

    def test_valid_numeric_origins_and_sources_pass(self):
        self.assertEqual(module.validate_rows([valid_row()]), [])

    def test_missing_origin_fails(self):
        row = valid_row()
        del row["budget_ugx"]["origin"]
        self.assertTrue(any("budget_ugx.origin" in item for item in module.validate_rows([row])))

    def test_unknown_origin_fails(self):
        row = valid_row()
        row["cpm_ugx"]["origin"] = "estimated"
        self.assertTrue(any("cpm_ugx.origin" in item for item in module.validate_rows([row])))

    def test_missing_source_fails(self):
        row = valid_row()
        row["frequency"]["source"] = "  "
        self.assertTrue(any("frequency.source" in item for item in module.validate_rows([row])))

    def test_zero_or_nonfinite_frequency_fails(self):
        for value in (0, float("inf")):
            with self.subTest(value=value):
                row = valid_row()
                row["frequency"]["value"] = value
                self.assertTrue(any("frequency.value" in item for item in module.validate_rows([row])))

    def test_invalid_json_input_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "invalid.json"
            path.write_text(json.dumps({"rows": [valid_row() | {"budget_ugx": 1000}]}), encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("FAIL", result.stdout)


class PlatformSpecGateTests(unittest.TestCase):
    AS_OF = date(2026, 10, 31)

    def record(self, **overrides):
        base = {"id": "SPEC-SRC", "support_status": "verified", "next_review": "2026-12-01"}
        base.update(overrides)
        return base

    def register(self, *records):
        return {r["id"]: r for r in records}

    def spec(self, **overrides):
        base = {"platform": "LinkedIn", "spec": "single image ad file size", "source_id": "SPEC-SRC", "state": "verified"}
        base.update(overrides)
        return base

    def check(self, specs, *records):
        return module.validate_platform_specs(specs, self.register(*records), self.AS_OF)

    def test_plan_without_platform_specs_is_unaffected(self):
        self.assertEqual(module.validate_platform_specs(None, {}, self.AS_OF), [])

    def test_verified_spec_with_verified_in_window_record_passes(self):
        self.assertEqual(self.check([self.spec()], self.record()), [])

    def test_partial_spec_accepts_partial_or_context_bound_record(self):
        for status in ("partial", "context-bound", "verified"):
            self.assertEqual(self.check([self.spec(state="partial")], self.record(support_status=status)), [])

    def test_verified_spec_needs_a_verified_record(self):
        errors = self.check([self.spec()], self.record(support_status="partial"))
        self.assertTrue(any("verified requires" in e for e in errors), errors)

    def test_quarantined_record_cannot_support_a_current_spec(self):
        for state in ("verified", "partial"):
            errors = self.check([self.spec(state=state)], self.record(quarantined=True, support_status="NOT_ASSESSED"))
            self.assertTrue(any("quarantined" in e for e in errors), (state, errors))

    def test_overdue_record_cannot_support_a_current_spec(self):
        errors = self.check([self.spec()], self.record(next_review="2026-10-30"))
        self.assertTrue(any("overdue" in e for e in errors), errors)

    def test_unknown_source_id_is_refused(self):
        errors = self.check([self.spec(source_id="MISSING")], self.record())
        self.assertTrue(any("not in the source register" in e for e in errors), errors)

    def test_current_spec_requires_a_source_id(self):
        spec = self.spec()
        del spec["source_id"]
        self.assertTrue(any("source_id" in e for e in self.check([spec], self.record())))

    def test_unknown_state_and_missing_fields_are_refused(self):
        self.assertTrue(any("state" in e for e in self.check([self.spec(state="current")], self.record())))
        self.assertTrue(any("platform" in e for e in self.check([self.spec(platform=" ")], self.record())))
        self.assertTrue(any("non-empty array" in e or "array" in e for e in module.validate_platform_specs({}, {}, self.AS_OF)))

    def test_not_assessed_spec_may_omit_source_but_must_not_carry_a_value(self):
        spec = {"platform": "Meta", "spec": "Reels creative limits", "state": "NOT_ASSESSED"}
        self.assertEqual(self.check([spec]), [])
        errors = self.check([{**spec, "value": "90 seconds"}])
        self.assertTrue(any("must not carry a value" in e for e in errors), errors)

    def test_cli_blocks_a_quarantined_source_and_passes_organic_plans(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            register = {"records": [self.record(id="OK-SRC"), self.record(id="Q-SRC", quarantined=True, support_status="NOT_ASSESSED")]}
            (tmp / "register.json").write_text(json.dumps(register), encoding="utf-8")
            plan = {"rows": [valid_row()], "platform_specs": [self.spec(source_id="Q-SRC")]}
            (tmp / "bad.json").write_text(json.dumps(plan), encoding="utf-8")
            organic = {"rows": [valid_row()]}
            (tmp / "organic.json").write_text(json.dumps(organic), encoding="utf-8")
            good = {"rows": [valid_row()], "platform_specs": [self.spec(source_id="OK-SRC")]}
            (tmp / "good.json").write_text(json.dumps(good), encoding="utf-8")
            def run(name):
                return subprocess.run([sys.executable, "-B", "-X", "utf8", str(SCRIPT), str(tmp / name),
                                       "--register", str(tmp / "register.json"), "--as-of", "2026-10-31"],
                                      capture_output=True, text=True)
            self.assertEqual(run("bad.json").returncode, 1)
            self.assertIn("quarantined", run("bad.json").stdout)
            self.assertEqual(run("organic.json").returncode, 0)
            self.assertEqual(run("good.json").returncode, 0)


if __name__ == "__main__":
    unittest.main()
