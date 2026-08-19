#!/usr/bin/env python3
"""Tests for the 4C Fit scorecard contract."""

from __future__ import annotations

import copy
import unittest

from fit_score_check import validate_card


BASE_CARD = {
    "candidate": "DeepSeek Harness",
    "exact_commit": "141eb6fef83422698aef7a981029e843e8161534",
    "terrain": "interactive coding",
    "weights": {"Cost": 45, "Compatibility": 35, "Continuity": 20, "Cognition": 0},
    "grades": {"Cost": 4, "Compatibility": 4, "Continuity": 4, "Cognition": None},
    "score": 80,
    "evidence_stage": "Source-predicted",
    "boundary_status": "Unknown",
    "source_report": "docs/scouts/deepseek-harness.md",
}


class FitScoreTests(unittest.TestCase):
    def test_deepseek_card_is_valid(self) -> None:
        self.assertEqual(validate_card(BASE_CARD), [])

    def test_source_evidence_cannot_claim_runtime_grade(self) -> None:
        card = copy.deepcopy(BASE_CARD)
        card["grades"]["Cost"] = 5
        card["score"] = 89
        self.assertTrue(any("Cost grade" in error for error in validate_card(card)))

    def test_inactive_c_cannot_add_points(self) -> None:
        card = copy.deepcopy(BASE_CARD)
        card["grades"]["Cognition"] = 4
        self.assertTrue(any("inactive Cognition" in error for error in validate_card(card)))

    def test_arithmetic_is_recomputed(self) -> None:
        card = copy.deepcopy(BASE_CARD)
        card["score"] = 95
        self.assertTrue(any("calculated 80" in error for error in validate_card(card)))


if __name__ == "__main__":
    unittest.main()
