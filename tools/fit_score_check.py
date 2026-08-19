#!/usr/bin/env python3
"""Validate machine-readable 4C Fit scorecards and recompute every score."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCORE_PATH = ROOT / "docs" / "scouts" / "fit-scores.json"
EVIDENCE_PATH = ROOT / "docs" / "scouts" / "fit-score-evidence.json"
COHORT_PATH = ROOT / "docs" / "scouts" / "cohorts" / "2026-08-19-source-sweep.json"
CS = {"Cost", "Compatibility", "Continuity", "Cognition"}
KNOWN_COMMITS = json.loads(COHORT_PATH.read_text())["exact_commits"]
EVIDENCE_CEILINGS = {
    "Documented": 1,
    "Mechanism-backed": 3,
    "Source-predicted": 4,
    "Trace-qualified": 4,
    "Task-proven": 5,
    "Frontier-proven": 5,
    "Adoptable": 5,
}
BOUNDARY_STATUSES = {"Pass", "Unknown", "Fail"}
CLAIM_TYPES = {"source-observed", "source-inferred", "runtime-observed"}
CLAIM_TYPE_CEILINGS = {
    "source-observed": 3,
    "source-inferred": 4,
    "runtime-observed": 5,
}


def validate_card(card: dict) -> list[str]:
    name = card.get("candidate", "<unnamed>")
    errors: list[str] = []
    weights = card.get("weights", {})
    grades = card.get("grades", {})
    if set(weights) != CS or set(grades) != CS:
        return [f"{name}: weights and grades must contain exactly the four Cs"]
    if any(type(weight) is not int or not 0 <= weight <= 100 for weight in weights.values()):
        errors.append(f"{name}: every weight must be an integer from 0 to 100")
    if sum(weights.values()) != 100:
        errors.append(f"{name}: active-C weights must sum to 100")

    stage = card.get("evidence_stage")
    ceiling = EVIDENCE_CEILINGS.get(stage)
    if ceiling is None:
        errors.append(f"{name}: invalid evidence_stage {stage!r}")
        ceiling = 0
    for pressure in CS:
        weight = weights[pressure]
        grade = grades[pressure]
        if weight == 0 and grade is not None:
            errors.append(f"{name}: inactive {pressure} must use a null grade")
        if weight > 0 and (type(grade) is not int or not 0 <= grade <= ceiling):
            errors.append(
                f"{name}: active {pressure} grade must be an integer from 0 to {ceiling}"
            )

    calculated = sum(
        weights[pressure] * grades[pressure] / 5
        for pressure in CS
        if weights[pressure] > 0 and type(grades[pressure]) is int
    )
    if abs(calculated - card.get("score", -1)) > 1e-9:
        errors.append(f"{name}: score is {card.get('score')!r}, calculated {calculated:g}")
    if card.get("boundary_status") not in BOUNDARY_STATUSES:
        errors.append(f"{name}: invalid boundary_status")
    if not re.fullmatch(r"[0-9a-f]{40}", card.get("exact_commit", "")):
        errors.append(f"{name}: exact_commit must be a 40-character SHA")
    elif KNOWN_COMMITS.get(name) != card["exact_commit"]:
        errors.append(f"{name}: exact_commit differs from the pinned source cohort")
    report = card.get("source_report", "")
    if not report or not (ROOT / report).is_file():
        errors.append(f"{name}: source_report does not resolve to a file")
    if not isinstance(card.get("terrain"), str) or not card["terrain"].strip():
        errors.append(f"{name}: terrain is required")
    return errors


def validate_evidence(card: dict, evidence: dict) -> list[str]:
    name = card.get("candidate", "<unnamed>")
    commit = card.get("exact_commit", "")
    active = {pressure for pressure, weight in card.get("weights", {}).items() if weight > 0}
    errors: list[str] = []
    if set(evidence) != active:
        return [f"{name}: evidence must contain exactly the active Cs"]
    for pressure in active:
        grade = card["grades"][pressure]
        item = evidence[pressure]
        prefix = f"{name}/{pressure}"
        if item.get("grade") != grade:
            errors.append(f"{prefix}: evidence grade differs from scorecard grade")
        claim_type = item.get("claim_type")
        if claim_type not in CLAIM_TYPES:
            errors.append(f"{prefix}: invalid claim_type {claim_type!r}")
        elif grade > CLAIM_TYPE_CEILINGS[claim_type]:
            errors.append(
                f"{prefix}: grade {grade} exceeds the {claim_type} evidence ceiling"
            )
        for field in ("claim", "implementation", "reachability", "falsifier"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"{prefix}: missing {field}")
        if grade >= 3 and not item.get("invariant"):
            errors.append(f"{prefix}: grade {grade} requires an executable invariant")
        for field in ("implementation", "invariant", "reachability"):
            url = item.get(field)
            if url is None and field == "invariant" and grade < 3:
                continue
            pinned_pattern = (
                r"https://github\.com/[^/?#]+/[^/?#]+/(?:blob|tree)/"
                + re.escape(commit)
                + r"/[^?#]+(?:#[A-Za-z0-9_.:+-]+)?"
            )
            if not isinstance(url, str) or not re.fullmatch(pinned_pattern, url):
                errors.append(f"{prefix}: {field} is not pinned to {commit}")
    return errors


def validate_comparison(comparison: dict, evidence_ledger: dict) -> list[str]:
    comparison_id = comparison.get("comparison_id", "<unnamed comparison>")
    weights = comparison.get("weights", {})
    terrain = comparison.get("terrain")
    report = comparison.get("source_report")
    candidates = comparison.get("candidates", [])
    errors: list[str] = []
    if set(weights) != CS or sum(weights.values()) != 100:
        errors.append(f"{comparison_id}: shared weights must contain four Cs and sum to 100")
        return errors
    if not isinstance(terrain, str) or not terrain.strip():
        errors.append(f"{comparison_id}: terrain is required")
    names = [candidate.get("candidate") for candidate in candidates]
    if not candidates or len(names) != len(set(names)):
        errors.append(f"{comparison_id}: candidates must be present and unique")
    for candidate in candidates:
        card = {
            **candidate,
            "terrain": terrain,
            "weights": weights,
            "source_report": report,
        }
        errors.extend(
            f"{comparison_id}: {error}" for error in validate_card(card)
        )
        candidate_evidence = evidence_ledger.get(candidate.get("candidate"), {})
        for pressure, weight in weights.items():
            if weight == 0:
                continue
            supported = candidate_evidence.get(pressure, {}).get("grade", -1)
            if candidate.get("grades", {}).get(pressure, -1) > supported:
                errors.append(
                    f"{comparison_id}: {candidate.get('candidate')}/{pressure} "
                    "exceeds its evidence-supported grade"
                )
    return errors


def main() -> int:
    payload = json.loads(SCORE_PATH.read_text())
    evidence_payload = json.loads(EVIDENCE_PATH.read_text())
    evidence_ledger = evidence_payload.get("evidence", {})
    cards = payload.get("scorecards", [])
    errors = [error for card in cards for error in validate_card(card)]
    errors.extend(
        error
        for card in cards
        for error in validate_evidence(card, evidence_ledger.get(card.get("candidate"), {}))
    )
    comparisons = payload.get("comparisons", [])
    errors.extend(
        error
        for comparison in comparisons
        for error in validate_comparison(comparison, evidence_ledger)
    )
    names = [card.get("candidate") for card in cards]
    if len(names) != len(set(names)):
        errors.append("candidate names must be unique")
    if set(names) != set(evidence_ledger):
        errors.append("evidence ledger candidates must exactly match scorecard candidates")
    if not cards:
        errors.append("at least one scorecard is required")
    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1
    print(f"PASS 4C Fit scorecards: {len(cards)} cards, {len(comparisons)} comparison")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
