#!/usr/bin/env python3
"""Separate evaluation evidence from a reusable Cognition policy update."""

from __future__ import annotations

import copy
import importlib.metadata
import json
import platform

from autoevals import ExactMatch


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
    assert passive_score["score"] == 0
    assert passive_policy == INITIAL_POLICY
    assert passive_after == passive_before

    adaptive_policy = copy.deepcopy(INITIAL_POLICY)
    adaptive_before = execute(adaptive_policy)
    adaptive_score = score(adaptive_before)
    adapt(adaptive_policy, adaptive_score)
    adaptive_after = execute(adaptive_policy)
    assert adaptive_score == passive_score
    assert adaptive_policy["version"] == 2
    assert adaptive_after == EXPECTED

    report = {
        "experiment": "autoevals-cognition-boundary",
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
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
