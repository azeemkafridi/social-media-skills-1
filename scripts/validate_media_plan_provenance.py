#!/usr/bin/env python3
"""Validate the evidence origin of numeric media-plan inputs and the source state of platform specifications."""

from __future__ import annotations

import argparse
import json
import math
from datetime import date
from pathlib import Path


NUMERIC_FIELDS = ("budget_ugx", "cpm_ugx", "frequency")
ALLOWED_ORIGINS = {"observed", "client_input", "synthetic_assumption"}
SPEC_STATES = ("verified", "partial", "NOT_ASSESSED")
PARTIAL_OK_STATUSES = {"verified", "partial", "context-bound"}
DEFAULT_REGISTER = Path(__file__).resolve().parents[1] / "docs" / "source-registers" / "source-register.json"


def validate_rows(rows: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(rows, list) or not rows:
        return ["rows must be a non-empty array"]
    for index, row in enumerate(rows, 1):
        label = row.get("channel", f"row {index}") if isinstance(row, dict) else f"row {index}"
        if not isinstance(row, dict):
            errors.append(f"{label}: row must be an object")
            continue
        if not isinstance(row.get("channel"), str) or not row["channel"].strip():
            errors.append(f"row {index}: non-empty channel is required")
        for field in NUMERIC_FIELDS:
            record = row.get(field)
            if not isinstance(record, dict):
                errors.append(f"{label}: {field} must include value, origin and source")
                continue
            value = record.get("value")
            if (isinstance(value, bool) or not isinstance(value, (int, float))
                    or not math.isfinite(value) or value <= 0):
                errors.append(f"{label}: {field}.value must be a finite positive number")
            origin = record.get("origin")
            if origin not in ALLOWED_ORIGINS:
                errors.append(f"{label}: {field}.origin must be observed, client_input or synthetic_assumption")
            source = record.get("source")
            if not isinstance(source, str) or not source.strip():
                errors.append(f"{label}: {field}.source must identify its evidence or assumption")
    return errors


def load_register(path: Path) -> dict[str, dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {r["id"]: r for r in payload["records"] if isinstance(r, dict) and "id" in r}


def validate_platform_specs(specs: object, register: dict[str, dict], as_of: date) -> list[str]:
    """A platform specification cannot appear as current unless its register record is in window and not quarantined.

    `platform_specs` is optional: a plan that cites no specification is not affected.
    """
    if specs is None:
        return []
    if not isinstance(specs, list) or not specs:
        return ["platform_specs must be a non-empty array when present"]
    errors: list[str] = []
    for index, spec in enumerate(specs, 1):
        label = f"platform spec {index}"
        if not isinstance(spec, dict):
            errors.append(f"{label}: must be an object")
            continue
        for field in ("platform", "spec"):
            if not isinstance(spec.get(field), str) or not spec[field].strip():
                errors.append(f"{label}: non-empty {field} is required")
        label = f"{spec.get('platform', index)} / {spec.get('spec', 'spec')}"
        state = spec.get("state")
        if state not in SPEC_STATES:
            errors.append(f"{label}: state must be verified, partial or NOT_ASSESSED")
            continue
        if state == "NOT_ASSESSED":
            if "value" in spec:
                errors.append(f"{label}: a NOT_ASSESSED spec must not carry a value into the plan")
            continue
        source_id = spec.get("source_id")
        if not isinstance(source_id, str) or not source_id.strip():
            errors.append(f"{label}: a {state} spec needs a source_id")
            continue
        record = register.get(source_id)
        if record is None:
            errors.append(f"{label}: source_id {source_id} is not in the source register")
            continue
        if record.get("quarantined") is True:
            errors.append(f"{label}: cannot appear as {state}: register record {source_id} is quarantined")
            continue
        try:
            overdue = date.fromisoformat(record["next_review"]) < as_of
        except (KeyError, TypeError, ValueError):
            errors.append(f"{label}: register record {source_id} has no readable next_review date")
            continue
        if overdue:
            errors.append(f"{label}: cannot appear as {state}: register record {source_id} is overdue since {record['next_review']}")
            continue
        status = str(record.get("support_status", "")).lower()
        if state == "verified" and status != "verified":
            errors.append(f"{label}: verified requires register support_status verified; {source_id} is {record.get('support_status', 'unset')}")
        elif state == "partial" and status not in PARTIAL_OK_STATUSES:
            errors.append(f"{label}: partial requires a partial, context-bound or verified record; {source_id} is {record.get('support_status', 'unset')}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--as-of", type=date.fromisoformat, default=date.today())
    options = parser.parse_args()
    try:
        payload = json.loads(options.input.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"media-plan provenance: FAIL; cannot read input: {exc}")
        return 1
    errors = validate_rows(payload.get("rows") if isinstance(payload, dict) else None)
    if isinstance(payload, dict) and "platform_specs" in payload:
        try:
            register = load_register(options.register)
        except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
            print(f"media-plan provenance: FAIL; cannot read source register: {exc}")
            return 1
        errors += validate_platform_specs(payload["platform_specs"], register, options.as_of)
    if errors:
        print(f"media-plan provenance: FAIL ({len(errors)} finding(s))")
        for error in errors:
            print(f"- {error}")
        return 1
    specs = len(payload.get("platform_specs") or [])
    print(f"media-plan provenance: PASS ({len(payload['rows'])} rows; numeric origins and references present; {specs} platform spec(s) checked against the register)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
