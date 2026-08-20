#!/usr/bin/env python3

from __future__ import annotations

import copy
import json
import unittest

from source_exam_check import (
    COHORT_PATH,
    EVIDENCE_PATH,
    EXAM_PATH,
    MARKET_PATH,
    RESULTS_PATH,
    validate,
)


class SourceExamTests(unittest.TestCase):
    def setUp(self) -> None:
        self.exam = json.loads(EXAM_PATH.read_text())
        self.results = json.loads(RESULTS_PATH.read_text())
        self.evidence = json.loads(EVIDENCE_PATH.read_text())
        self.market = json.loads(MARKET_PATH.read_text())
        self.commits = json.loads(COHORT_PATH.read_text())["exact_commits"]

    def errors(self, exam: dict | None = None, results: dict | None = None) -> list[str]:
        return validate(exam or self.exam, results or self.results, self.evidence, self.market, self.commits)

    def test_published_exam_is_valid(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_candidate_cannot_change_its_questions(self) -> None:
        results = copy.deepcopy(self.results)
        del results["candidates"][0]["answers"]["cost.hot_path"]
        self.assertTrue(any("frozen question set" in error for error in self.errors(results=results)))

    def test_score_is_mechanical(self) -> None:
        results = copy.deepcopy(self.results)
        results["candidates"][0]["score"] = 100
        self.assertTrue(any("calculated" in error for error in self.errors(results=results)))

    def test_question_change_breaks_contract_hash(self) -> None:
        exam = copy.deepcopy(self.exam)
        exam["questions"][0]["weight"] += 1
        self.assertTrue(any("contract hash" in error for error in self.errors(exam=exam)))

    def test_full_credit_requires_invariant(self) -> None:
        results = copy.deepcopy(self.results)
        target = next(item for item in results["candidates"] if item["candidate"] == "OpenHands")
        target["answers"]["cost.safe_parallelism"]["level"] = 1
        target["score"] += 5.5
        self.assertTrue(any("full credit requires" in error for error in self.errors(results=results)))


if __name__ == "__main__":
    unittest.main()
