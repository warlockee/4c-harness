#!/usr/bin/env python3
"""Validate the candidate-blind 4C source exam and mechanically rescore answers."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAM_PATH = ROOT / "docs/scouts/interactive-coding-v2-exam.json"
RESULTS_PATH = ROOT / "docs/scouts/interactive-coding-v2-results.json"
EVIDENCE_PATH = ROOT / "docs/scouts/fit-score-evidence.json"
MARKET_PATH = ROOT / "docs/scouts/market-universe.json"
COHORT_PATH = ROOT / "docs/scouts/cohorts/2026-08-19-source-sweep.json"
LEVELS = {0, 0.5, 1}


def contract_hash(exam: dict) -> str:
    core = {key: exam[key] for key in ("exam_id", "terrain", "levels", "questions")}
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(canonical.encode()).hexdigest()


def contributions(exam: dict, candidate: dict) -> dict[str, float]:
    values = {"Cost": 0.0, "Compatibility": 0.0, "Continuity": 0.0, "Cognition": 0.0}
    questions = {item["id"]: item for item in exam["questions"]}
    for question_id, answer in candidate["answers"].items():
        question = questions[question_id]
        values[question["pressure"]] += question["weight"] * answer["level"]
    return values


def validate(exam: dict, results: dict, evidence: dict, market: dict, commits: dict) -> list[str]:
    errors: list[str] = []
    if exam.get("contract_sha256") != contract_hash(exam):
        errors.append("exam contract hash is stale; question changes require an explicit new contract")
    if results.get("exam_id") != exam.get("exam_id") or results.get("contract_sha256") != exam.get("contract_sha256"):
        errors.append("results are not bound to the frozen exam contract")
    questions = exam.get("questions", [])
    question_ids = [item.get("id") for item in questions]
    if len(question_ids) != len(set(question_ids)) or not questions:
        errors.append("exam questions must be present and unique")
    if sum(item.get("weight", 0) for item in questions) != 100:
        errors.append("exam question weights must sum to 100")
    pressure_weights = {pressure: sum(q["weight"] for q in questions if q["pressure"] == pressure) for pressure in ("Cost", "Compatibility", "Continuity")}
    if pressure_weights != {"Cost": 45, "Compatibility": 35, "Continuity": 20}:
        errors.append("exam must preserve the locked 45/35/20 pressure weights")
    serialized_exam = json.dumps(exam, ensure_ascii=False)
    candidates = results.get("candidates", [])
    names = [item.get("candidate") for item in candidates]
    if any(name and name in serialized_exam for name in names):
        errors.append("candidate-blind exam contains a candidate name")
    ranked = {item["name"] for item in market["products"] if item["status"] == "ranked"}
    if set(names) != ranked:
        errors.append("exam answers must cover every ranked product exactly once")
    if len(names) != len(set(names)):
        errors.append("exam answer candidates must be unique")
    evidence_ledger = evidence["evidence"]
    for candidate in candidates:
        name = candidate.get("candidate", "<unnamed>")
        if candidate.get("exact_commit") != commits.get(name):
            errors.append(f"{name}: exact commit differs from the source cohort")
        answers = candidate.get("answers", {})
        if set(answers) != set(question_ids):
            errors.append(f"{name}: answers differ from the frozen question set")
            continue
        for question in questions:
            answer = answers[question["id"]]
            level = answer.get("level")
            if level not in LEVELS:
                errors.append(f"{name}/{question['id']}: level must be 0, 0.5 or 1")
                continue
            if level == 0:
                if answer.get("evidence_pressure") is not None:
                    errors.append(f"{name}/{question['id']}: zero answer cannot cite qualifying evidence")
                continue
            if answer.get("evidence_pressure") != question["pressure"]:
                errors.append(f"{name}/{question['id']}: evidence pressure does not match the question")
                continue
            row = evidence_ledger.get(name, {}).get(question["pressure"], {})
            if not re.fullmatch(r"https://github\.com/.+/blob/[0-9a-f]{40}/.+", str(row.get("implementation", ""))):
                errors.append(f"{name}/{question['id']}: missing pinned implementation evidence")
            if level == 1 and not row.get("invariant"):
                errors.append(f"{name}/{question['id']}: full credit requires an executable invariant")
        calculated = sum(contributions(exam, candidate).values())
        if abs(float(candidate.get("score", -1)) - calculated) > 1e-9:
            errors.append(f"{name}: score is {candidate.get('score')}, calculated {calculated:g}")
        if not str(candidate.get("audit_note", "")).strip():
            errors.append(f"{name}: audit note is required")
    return errors


def load_and_validate() -> tuple[dict, dict, list[str]]:
    exam = json.loads(EXAM_PATH.read_text())
    results = json.loads(RESULTS_PATH.read_text())
    evidence = json.loads(EVIDENCE_PATH.read_text())
    market = json.loads(MARKET_PATH.read_text())
    commits = json.loads(COHORT_PATH.read_text())["exact_commits"]
    return exam, results, validate(exam, results, evidence, market, commits)


def main() -> int:
    exam, results, errors = load_and_validate()
    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1
    scores = sorted((item["score"], item["candidate"]) for item in results["candidates"])
    print(f"PASS {exam['exam_id']}: {len(scores)} candidate-blind answer sheets; leader {scores[-1][1]} at {scores[-1][0]:g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
