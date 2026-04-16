#!/usr/bin/env python3
"""Validate the standard OMI rubric family after the evidence_guide cutover."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPERIMENTS_DIR = ROOT / "experiments"
PROMPT_PATHS = [
    ROOT / "prompt-library" / "system-prompts" / "grading" / "grading-instructor.txt",
    ROOT / "experiments" / "AS92006" / "instruction-prompt.txt",
]
EXPECTED_TOP_LEVEL_KEYS = {
    "meta",
    "grade_descriptors",
    "key_terms",
    "omis",
    "aggregation_rules",
    "governance",
}
EXPECTED_OMI_KEYS = {
    "id",
    "description",
    "level",
    "weight",
    "evidence_guide",
    "success_examples",
    "source_ref",
}
EXPECTED_EVIDENCE_GUIDE_KEYS = {
    "positive_signals",
    "negative_signals",
    "common_confusion",
}
EXPECTED_LAST_VALIDATED = "2025-07-18"
EXCLUDED_RUBRIC_STEMS = {"AS93604"}


def discover_standard_rubric_paths() -> list[Path]:
    candidates = []
    for path in sorted(EXPERIMENTS_DIR.glob("AS*/*.json")) + sorted(
        EXPERIMENTS_DIR.glob("AS*/*/*.json")
    ):
        if not path.stem.startswith("AS"):
            continue
        if path.stem in EXCLUDED_RUBRIC_STEMS:
            continue
        candidates.append(path)
    return candidates


def validate_prompts(errors: list[str]) -> None:
    for prompt_path in PROMPT_PATHS:
        text = prompt_path.read_text()
        if "detection_hint" in text:
            errors.append(f"{prompt_path}: still references detection_hint")
    grading_prompt = PROMPT_PATHS[0].read_text()
    for needle in [
        "description",
        "positive_signals",
        "negative_signals",
        "common_confusion",
        "matched_positive_signals",
        "matched_negative_signals",
    ]:
        if needle not in grading_prompt:
            errors.append(
                f"{PROMPT_PATHS[0]}: missing required grading contract term '{needle}'"
            )


def validate_rubric(path: Path, errors: list[str]) -> None:
    try:
        data = json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{path}: invalid JSON ({exc})")
        return

    if not isinstance(data, dict):
        errors.append(f"{path}: top-level JSON must be an object")
        return

    missing_top_level = EXPECTED_TOP_LEVEL_KEYS - set(data.keys())
    if missing_top_level:
        errors.append(
            f"{path}: missing top-level keys {sorted(missing_top_level)}"
        )

    meta = data.get("meta")
    if not isinstance(meta, dict) or not str(meta.get("as_code", "")).startswith("AS"):
        errors.append(f"{path}: meta.as_code must start with 'AS'")

    governance = data.get("governance")
    if not isinstance(governance, dict):
        errors.append(f"{path}: governance must be an object")
    elif governance.get("last_validated") != EXPECTED_LAST_VALIDATED:
        errors.append(
            f"{path}: governance.last_validated must be {EXPECTED_LAST_VALIDATED}"
        )

    omis = data.get("omis")
    if not isinstance(omis, list) or not omis:
        errors.append(f"{path}: omis must be a non-empty array")
        return

    for index, omi in enumerate(omis, start=1):
        if not isinstance(omi, dict):
            errors.append(f"{path}: omi #{index} must be an object")
            continue

        if "detection_hint" in omi:
            errors.append(f"{path}: omi #{index} still contains detection_hint")

        omi_keys = set(omi.keys())
        missing_omi_keys = EXPECTED_OMI_KEYS - omi_keys
        extra_omi_keys = omi_keys - EXPECTED_OMI_KEYS
        if missing_omi_keys:
            errors.append(
                f"{path}: omi #{index} missing keys {sorted(missing_omi_keys)}"
            )
        if extra_omi_keys:
            errors.append(
                f"{path}: omi #{index} has unexpected keys {sorted(extra_omi_keys)}"
            )

        evidence_guide = omi.get("evidence_guide")
        if not isinstance(evidence_guide, dict):
            errors.append(f"{path}: omi #{index} evidence_guide must be an object")
            continue

        guide_keys = set(evidence_guide.keys())
        missing_guide_keys = EXPECTED_EVIDENCE_GUIDE_KEYS - guide_keys
        extra_guide_keys = guide_keys - EXPECTED_EVIDENCE_GUIDE_KEYS
        if missing_guide_keys:
            errors.append(
                f"{path}: omi #{index} evidence_guide missing keys {sorted(missing_guide_keys)}"
            )
        if extra_guide_keys:
            errors.append(
                f"{path}: omi #{index} evidence_guide has unexpected keys {sorted(extra_guide_keys)}"
            )

        for list_key in ("positive_signals", "negative_signals"):
            if not isinstance(evidence_guide.get(list_key), list):
                errors.append(
                    f"{path}: omi #{index} evidence_guide.{list_key} must be a list"
                )

        if not isinstance(evidence_guide.get("common_confusion"), str):
            errors.append(
                f"{path}: omi #{index} evidence_guide.common_confusion must be a string"
            )


def main() -> int:
    errors: list[str] = []

    validate_prompts(errors)
    for rubric_path in discover_standard_rubric_paths():
        validate_rubric(rubric_path, errors)

    if errors:
        print("STANDARD OMI VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("STANDARD OMI VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
