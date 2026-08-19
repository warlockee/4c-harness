#!/usr/bin/env python3
"""Validate Harness Scout cohort records.

Discovery cohorts may contain incomplete trial contracts, but they must be
excluded from hit-rate accounting. Locked, running and resolved cohorts must
contain the preregistered fields that make hindsight-resistant evaluation
possible.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
COHORT_DIR = ROOT / "docs" / "scouts" / "cohorts"
VALID_STATUSES = {"draft", "discovery", "locked", "running", "resolved"}
VALID_LANES = {"exploit", "explore", "shadow"}
VALID_RESOLUTIONS = {
    "task_hit",
    "breakout_hit",
    "adoption_hit",
    "miss",
    "censored",
}

COHORT_FIELDS = (
    "cohort_id",
    "schema_version",
    "status",
    "information_cutoff",
    "decision_owner",
    "terrain_contract",
    "eligible_candidates",
    "baseline",
    "selection_baselines",
    "lane_allocation",
    "candidates",
    "outcome_adjudicator",
    "included_in_hit_rate",
)

CANDIDATE_FIELDS = (
    "name",
    "exact_commit",
    "lane",
    "evidence_tripod",
    "activated_4c",
    "boundary_obligations",
    "primary_causal_prediction",
    "primary_metric",
    "minimum_uplift",
    "external_postcondition",
    "falsifier",
    "repetitions",
    "trial_budget",
    "deadline",
    "early_stop_rule",
    "pre_run_probability",
)


def present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return True


def missing_fields(obj: dict[str, Any], fields: tuple[str, ...]) -> list[str]:
    return [field for field in fields if not present(obj.get(field))]


def validate_record(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        record = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path.relative_to(ROOT)}: cannot read JSON: {exc}"]

    prefix = str(path.relative_to(ROOT))
    status = record.get("status")
    if status not in VALID_STATUSES:
        errors.append(f"{prefix}: invalid status {status!r}")

    if path.stem != record.get("cohort_id"):
        errors.append(f"{prefix}: filename must equal cohort_id")

    if status == "discovery":
        if record.get("included_in_hit_rate") is not False:
            errors.append(f"{prefix}: discovery cohort must be excluded from hit rate")
        if not present(record.get("exclusion_reason")):
            errors.append(f"{prefix}: discovery cohort needs exclusion_reason")
        return errors

    if status == "draft":
        if record.get("included_in_hit_rate") is True:
            errors.append(f"{prefix}: draft cohort cannot enter hit rate")
        return errors

    missing = missing_fields(record, COHORT_FIELDS)
    if missing:
        errors.append(f"{prefix}: counted cohort missing {', '.join(missing)}")
        return errors

    if record["included_in_hit_rate"] is not True:
        errors.append(f"{prefix}: {status} cohort must enter hit-rate accounting")

    allocation = record["lane_allocation"]
    if set(allocation) != VALID_LANES:
        errors.append(f"{prefix}: lane_allocation must contain exploit/explore/shadow")
    elif sum(allocation.values()) != 100:
        errors.append(f"{prefix}: lane_allocation percentages must sum to 100")

    for index, candidate in enumerate(record["candidates"]):
        candidate_prefix = f"{prefix}: candidate[{index}]"
        missing = missing_fields(candidate, CANDIDATE_FIELDS)
        if missing:
            errors.append(f"{candidate_prefix} missing {', '.join(missing)}")
            continue
        if candidate["lane"] not in VALID_LANES:
            errors.append(f"{candidate_prefix} has invalid lane {candidate['lane']!r}")
        tripod = candidate["evidence_tripod"]
        tripod_missing = missing_fields(
            tripod, ("implementation", "executable_invariant", "shipped_reachability")
        )
        if tripod_missing:
            errors.append(
                f"{candidate_prefix} evidence_tripod missing {', '.join(tripod_missing)}"
            )

        if status == "resolved":
            resolution = candidate.get("resolution")
            if resolution not in VALID_RESOLUTIONS:
                errors.append(f"{candidate_prefix} has invalid resolution {resolution!r}")
            if not present(candidate.get("resolution_evidence")):
                errors.append(f"{candidate_prefix} missing resolution_evidence")
            if not present(candidate.get("adjudicator")):
                errors.append(f"{candidate_prefix} missing adjudicator")

    return errors


def main() -> int:
    paths = sorted(COHORT_DIR.glob("*.json"))
    if not paths:
        print("FAIL no scout cohort records found", file=sys.stderr)
        return 1

    errors = [error for path in paths for error in validate_record(path)]
    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1

    print(f"PASS scout cohorts: {len(paths)} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
