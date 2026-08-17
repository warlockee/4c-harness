#!/usr/bin/env python3
"""Instrument the evaluation/Cognition boundary around a real scorer.

Evidence level: instrumented illustration. Autoevals supplies the scorer and
the score that both branches share; the adaptation operator is the locally
authored `adapt` function. The experiment demonstrates that identical
evaluation evidence is insufficient for a policy delta — the operator has to
exist — and deliberately claims nothing about how any upstream eval platform
handles adaptation.
"""

from __future__ import annotations

import copy
import importlib.metadata
import json
import platform

from autoevals import ExactMatch

from _support import INSTRUMENTED_ILLUSTRATION, require


INITIAL_POLICY = {"version": 1, "answer": "four"}
EXPECTED = "five"


def execute(policy: dict[str, object]) -> str:
    return str(policy["answer"])


def score(output: str) -> dict[str, object]:
    result = ExactMatch()(output=output, expected=EXPECTED)
    return {"name": result.name, "score": result.score, "error": result.error}


def adapt(policy: dict[str, object], evaluation: dict[str, object]) -> None:
    if evaluation["score"] == 0:
        policy.update(version=int(policy["version"]) + 1, answer=EXPECTED)


def main() -> None:
    passive_policy = copy.deepcopy(INITIAL_POLICY)
    passive_before = execute(passive_policy)
    passive_score = score(passive_before)
    passive_after = execute(passive_policy)
    require(passive_score["score"] == 0, "scorer did not reject the initial output")
    require(passive_policy == INITIAL_POLICY, "policy changed without an adaptation step")
    require(passive_after == passive_before, "future execution changed without adaptation")

    adaptive_policy = copy.deepcopy(INITIAL_POLICY)
    adaptive_before = execute(adaptive_policy)
    adaptive_score = score(adaptive_before)
    adapt(adaptive_policy, adaptive_score)
    adaptive_after = execute(adaptive_policy)
    require(adaptive_score == passive_score, "evaluation evidence differed between branches")
    require(adaptive_policy["version"] == 2, "adaptation did not version the policy artifact")
    require(adaptive_after == EXPECTED, "adapted policy did not change future execution")

    report = {
        "experiment": "autoevals-cognition-boundary",
        "evidence_level": INSTRUMENTED_ILLUSTRATION,
        "runtime": platform.python_version(),
        "autoevals": importlib.metadata.version("autoevals"),
        "controlled_variables": [
            "initial execution policy",
            "task output",
            "expected value",
            "ExactMatch evaluator",
            "evaluation score",
        ],
        "independent_variable": "whether evaluation triggers a reusable policy update",
        "observed_from_upstream": ["ExactMatch scoring of an identical output"],
        "authored_locally": ["the execution policy artifact", "the adaptation operator"],
        "branches": {
            "passive_evaluation": {
                "score": passive_score,
                "policy_after": passive_policy,
                "next_output": passive_after,
            },
            "adaptive_feedback": {
                "score": adaptive_score,
                "policy_after": adaptive_policy,
                "next_output": adaptive_after,
            },
        },
        "result": {
            "evaluation_is_not_sufficient_for_cognition": True,
            "reusable_policy_delta_observed_only_in_adaptive_branch": True,
            "claim": (
                "Identical evaluation evidence changes future execution only "
                "when an explicit adaptation operation updates reusable policy."
            ),
            "not_proven": (
                "that any surveyed eval platform does or does not perform that "
                "adaptation; the operator is authored in this file"
            ),
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
