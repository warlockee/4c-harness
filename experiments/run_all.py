#!/usr/bin/env python3
"""Run every credential-free empirical reproduction as one CI gate.

Experiments whose preconditions are unmet — a local CLI that CI does not
install — exit with `SKIP_EXIT_CODE` and are reported as skipped. Only a failed
claim fails the suite, so an unmet precondition can never be mistaken for a
falsification, or for a pass.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from _support import SKIP_EXIT_CODE


ROOT = Path(__file__).resolve().parent

#: Runs anywhere the pinned requirements install.
PORTABLE = [
    "langgraph_authority_continuity.py",
    "litellm_compatibility.py",
    "autoevals_cognition_boundary.py",
]

#: Needs a locally installed third-party CLI; skipped when absent.
LOCAL_ONLY = [
    "codex_sandbox_authority.py",
    "coding_harness_authority_surface.py",
]


def run(experiment: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(ROOT / experiment)],
        stdout=subprocess.DEVNULL,
    )
    if completed.returncode == SKIP_EXIT_CODE:
        return "SKIP"
    if completed.returncode != 0:
        raise SystemExit(f"FAIL {experiment} (exit {completed.returncode})")
    return "PASS"


def main() -> None:
    passed = skipped = 0
    for experiment in PORTABLE + LOCAL_ONLY:
        status = run(experiment)
        print(f"{status} {experiment}")
        if status == "PASS":
            passed += 1
        else:
            skipped += 1

    total = len(PORTABLE) + len(LOCAL_ONLY)
    print(f"empirical suite: {passed}/{total} passed, {skipped} skipped")
    if passed < len(PORTABLE):
        raise SystemExit("a portable experiment was skipped; check the environment")


if __name__ == "__main__":
    main()
