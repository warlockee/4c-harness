#!/usr/bin/env python3
"""Tests for the machine-checked 4C Harness Ladder."""

from __future__ import annotations

import io
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from unittest.mock import patch

import harness_ladder_check as ladder


class HarnessLadderTests(unittest.TestCase):
    def test_published_ladder_matches_scorecards(self) -> None:
        self.assertEqual(ladder.main(), 0)

    def test_changed_segment_width_is_rejected(self) -> None:
        source = ladder.LADDER.read_text()
        altered = source.replace('width="360"', 'width="359"', 1)
        self.assertNotEqual(source, altered)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ladder.svg"
            path.write_text(altered)
            with patch.object(ladder, "LADDER", path), redirect_stderr(io.StringIO()):
                self.assertEqual(ladder.main(), 1)

    def test_changed_visible_score_is_rejected(self) -> None:
        source = ladder.LADDER.read_text()
        altered = source.replace(
            'class="score-label" x="1632" y="41" text-anchor="end" '
            'fill="#FFFFFF" font-family="Arial Narrow,Helvetica Neue,Arial,sans-serif" '
            'font-size="37" font-weight="900">86</text>',
            'class="score-label" x="1632" y="41" text-anchor="end" '
            'fill="#FFFFFF" font-family="Arial Narrow,Helvetica Neue,Arial,sans-serif" '
            'font-size="37" font-weight="900">87</text>',
            1,
        )
        self.assertNotEqual(source, altered)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ladder.svg"
            path.write_text(altered)
            with patch.object(ladder, "LADDER", path), redirect_stderr(io.StringIO()):
                self.assertEqual(ladder.main(), 1)

    def test_changed_ranked_candidate_is_rejected(self) -> None:
        source = ladder.LADDER.read_text()
        altered = source.replace(
            'data-candidate="Qwen Code" data-score="82.5"',
            'data-candidate="Missing Product" data-score="82.5"',
            1,
        )
        self.assertNotEqual(source, altered)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ladder.svg"
            path.write_text(altered)
            with patch.object(ladder, "LADDER", path), redirect_stderr(io.StringIO()):
                self.assertEqual(ladder.main(), 1)


if __name__ == "__main__":
    unittest.main()
