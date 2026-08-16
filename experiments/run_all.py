#!/usr/bin/env python3
"""Run every credential-free empirical reproduction as one CI gate."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPERIMENTS = [
    "langgraph_authority_continuity.py",
    "litellm_compatibility.py",
    "autoevals_cognition_boundary.py",
]


def main() -> None:
    for experiment in EXPERIMENTS:
        subprocess.run(
            [sys.executable, str(ROOT / experiment)],
            check=True,
            stdout=subprocess.DEVNULL,
        )
        print(f"PASS {experiment}")
    print(f"empirical suite: {len(EXPERIMENTS)}/{len(EXPERIMENTS)} passed")


if __name__ == "__main__":
    main()
