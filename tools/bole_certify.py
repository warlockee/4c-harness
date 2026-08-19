#!/usr/bin/env python3
"""Decide whether 4C has earned the public Bole claim.

The gate is intentionally conservative and prospective. Discovery cohorts and
post-hoc case studies never enter certification.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
COHORT_DIR = ROOT / "docs" / "scouts" / "cohorts"
STATUS_PATH = ROOT / "docs" / "scouts" / "bole-status.json"
README_PATH = ROOT / "README.md"
BASELINES = ("popularity", "feature_coverage", "random")
HITS = {"task_hit", "breakout_hit", "adoption_hit"}
THRESHOLDS = {
    "minimum_cohorts": 3,
    "minimum_terrains": 3,
    "minimum_resolved_calls": 20,
    "minimum_shadow_calls": 5,
    "minimum_hit_rate": 0.80,
    "minimum_hit_rate_wilson_lower_95": 0.60,
    "maximum_shadow_winner_rate": 0.20,
}


def wilson(successes: int, trials: int, z: float = 1.959963984540054) -> tuple[float, float]:
    if trials == 0:
        return (0.0, 1.0)
    rate = successes / trials
    denominator = 1 + z * z / trials
    center = (rate + z * z / (2 * trials)) / denominator
    margin = z * math.sqrt(rate * (1 - rate) / trials + z * z / (4 * trials**2)) / denominator
    return (max(0.0, center - margin), min(1.0, center + margin))


def load_records() -> list[dict[str, Any]]:
    return [json.loads(path.read_text()) for path in sorted(COHORT_DIR.glob("*.json"))]


def evaluate(records: list[dict[str, Any]]) -> dict[str, Any]:
    cohorts: set[str] = set()
    terrains: set[str] = set()
    calls = hits = shadow_calls = shadow_hits = 0
    baseline_totals = {name: {"hits": 0, "trials": 0} for name in BASELINES}
    invalid: list[str] = []

    for record in records:
        if record.get("status") != "resolved" or record.get("included_in_hit_rate") is not True:
            continue
        cohort_id = record.get("cohort_id", "<unknown>")
        if record.get("prospective") is not True:
            invalid.append(f"{cohort_id}: resolved counted cohort is not prospective")
            continue
        if not record.get("public_lock_url") or not record.get("first_trial_at"):
            invalid.append(f"{cohort_id}: missing public pre-run lock evidence")
            continue
        if record.get("decision_owner") == record.get("outcome_adjudicator"):
            invalid.append(f"{cohort_id}: outcome adjudication is not independent")
            continue
        terrain = record.get("terrain_id")
        if not isinstance(terrain, str) or not terrain.strip():
            invalid.append(f"{cohort_id}: missing terrain_id")
            continue
        candidates = record.get("candidates", [])
        if any(candidate.get("resolution") == "censored" for candidate in candidates):
            invalid.append(f"{cohort_id}: censored calls cannot support certification")
            continue

        selected = [candidate for candidate in candidates if candidate.get("lane") != "shadow"]
        shadows = [candidate for candidate in candidates if candidate.get("lane") == "shadow"]
        if not selected:
            invalid.append(f"{cohort_id}: no resolved selected candidates")
            continue

        baseline_results = record.get("selection_baseline_results", {})
        if set(baseline_results) != set(BASELINES):
            invalid.append(f"{cohort_id}: needs popularity, feature_coverage and random baselines")
            continue
        malformed_baseline = False
        for name in BASELINES:
            result = baseline_results[name]
            if not isinstance(result, dict):
                invalid.append(f"{cohort_id}: {name} baseline result must be an object")
                malformed_baseline = True
                continue
            result_hits = result.get("hits")
            result_trials = result.get("trials")
            valid_counts = type(result_hits) is int and type(result_trials) is int
            if not valid_counts or result_trials != len(selected) or not 0 <= result_hits <= result_trials:
                invalid.append(f"{cohort_id}: {name} must use the same {len(selected)}-call budget")
                malformed_baseline = True
        if malformed_baseline:
            continue

        cohorts.add(cohort_id)
        terrains.add(terrain.strip())
        calls += len(selected)
        hits += sum(candidate.get("resolution") in HITS for candidate in selected)
        shadow_calls += len(shadows)
        shadow_hits += sum(candidate.get("resolution") in HITS for candidate in shadows)
        for name in BASELINES:
            baseline_totals[name]["hits"] += baseline_results[name]["hits"]
            baseline_totals[name]["trials"] += baseline_results[name]["trials"]

    hit_rate = hits / calls if calls else 0.0
    hit_low, hit_high = wilson(hits, calls)
    shadow_rate = shadow_hits / shadow_calls if shadow_calls else 1.0
    baselines: dict[str, Any] = {}
    for name, totals in baseline_totals.items():
        low, high = wilson(totals["hits"], totals["trials"])
        baselines[name] = {**totals, "rate": totals["hits"] / totals["trials"] if totals["trials"] else 0.0,
                           "wilson_lower_95": low, "wilson_upper_95": high}

    gates = {
        "valid_prospective_data": not invalid,
        "enough_cohorts": len(cohorts) >= THRESHOLDS["minimum_cohorts"],
        "enough_terrains": len(terrains) >= THRESHOLDS["minimum_terrains"],
        "enough_calls": calls >= THRESHOLDS["minimum_resolved_calls"],
        "enough_shadow_calls": shadow_calls >= THRESHOLDS["minimum_shadow_calls"],
        "hit_rate": hit_rate >= THRESHOLDS["minimum_hit_rate"],
        "hit_rate_lower_bound": hit_low >= THRESHOLDS["minimum_hit_rate_wilson_lower_95"],
        "shadow_winner_rate": shadow_rate <= THRESHOLDS["maximum_shadow_winner_rate"],
        "beats_all_baselines": calls > 0 and all(hit_low > result["wilson_upper_95"] for result in baselines.values()),
    }
    return {
        "schema_version": 1,
        "status": "CERTIFIED" if all(gates.values()) else "UNPROVEN",
        "thresholds": THRESHOLDS,
        "observed": {
            "cohorts": len(cohorts), "terrains": len(terrains), "resolved_calls": calls,
            "hits": hits, "hit_rate": hit_rate, "hit_rate_wilson_95": [hit_low, hit_high],
            "shadow_calls": shadow_calls, "shadow_hits": shadow_hits,
            "shadow_winner_rate": shadow_rate if shadow_calls else None,
            "baselines": baselines,
        },
        "gates": gates,
        "invalid_records": invalid,
    }


def status_line(result: dict[str, Any]) -> str:
    observed = result["observed"]
    thresholds = result["thresholds"]
    return (
        f"> **Bole status: {result['status']}** — "
        f"{observed['resolved_calls']}/{thresholds['minimum_resolved_calls']} "
        f"prospective calls resolved, {observed['hits']} hits; "
        f"{observed['shadow_calls']}/{thresholds['minimum_shadow_calls']} shadow calls."
    )


def main() -> int:
    result = evaluate(load_records())
    if "--json" in sys.argv:
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    expected = json.loads(STATUS_PATH.read_text())
    if result != expected:
        print("FAIL bole-status.json is stale; run tools/bole_certify.py --json", file=sys.stderr)
        return 1
    expected_line = status_line(result)
    if expected_line not in README_PATH.read_text():
        print(f"FAIL README Bole status is stale; expected:\n{expected_line}", file=sys.stderr)
        return 1
    print(f"PASS Bole status: {result['status']} ({result['observed']['hits']}/{result['observed']['resolved_calls']} hits)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
