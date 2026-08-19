#!/usr/bin/env python3
"""Tests for the public Bole certification gate."""

from __future__ import annotations

import unittest

from bole_certify import evaluate, status_line


def cohort(index: int, prospective: bool = True) -> dict:
    selected = [
        {"lane": "exploit", "resolution": "task_hit"} for _ in range(6)
    ] + [{"lane": "explore", "resolution": "miss"}]
    shadows = [
        {"lane": "shadow", "resolution": "miss"},
        {"lane": "shadow", "resolution": "miss"},
    ]
    return {
        "cohort_id": f"cohort-{index}",
        "status": "resolved",
        "included_in_hit_rate": True,
        "prospective": prospective,
        "terrain_id": f"terrain-{index}",
        "public_lock_url": f"https://example.test/cohort-{index}",
        "first_trial_at": "2026-09-02T00:00:00Z",
        "decision_owner": "owner",
        "outcome_adjudicator": "independent-reviewer",
        "candidates": selected + shadows,
        "selection_baseline_results": {
            "popularity": {"hits": 2, "trials": 7},
            "feature_coverage": {"hits": 2, "trials": 7},
            "random": {"hits": 2, "trials": 7},
        },
    }


class BoleCertificationTests(unittest.TestCase):
    def test_no_prospective_results_is_unproven(self) -> None:
        self.assertEqual(evaluate([])["status"], "UNPROVEN")

    def test_strong_out_of_sample_record_certifies(self) -> None:
        result = evaluate([cohort(1), cohort(2), cohort(3)])
        self.assertEqual(result["status"], "CERTIFIED")
        self.assertTrue(all(result["gates"].values()))

    def test_post_hoc_record_cannot_certify(self) -> None:
        result = evaluate([cohort(1), cohort(2), cohort(3, prospective=False)])
        self.assertEqual(result["status"], "UNPROVEN")
        self.assertFalse(result["gates"]["valid_prospective_data"])

    def test_public_status_line_comes_from_evidence(self) -> None:
        line = status_line(evaluate([]))
        self.assertEqual(
            line,
            "> **Bole status: UNPROVEN** — 0/20 prospective calls resolved, "
            "0 hits; 0/5 shadow calls.",
        )


if __name__ == "__main__":
    unittest.main()
