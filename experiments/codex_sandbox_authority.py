#!/usr/bin/env python3
"""Test Codex sandbox effect scope without invoking a model."""

from __future__ import annotations

import json
import platform
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    codex = shutil.which("codex")
    assert codex, "Codex CLI is required for this local enforcement experiment"

    version_text = subprocess.run(
        [codex, "--version"], check=True, text=True, capture_output=True
    ).stdout
    version_match = re.search(r"\d+(?:\.\d+)+", version_text)
    assert version_match

    with tempfile.TemporaryDirectory(prefix=".codex-scope-", dir=ROOT) as allowed_dir:
        with tempfile.TemporaryDirectory(
            prefix=".codex-outside-", dir=ROOT.parent
        ) as denied_dir:
            allowed_path = Path(allowed_dir, "effect.txt")
            denied_path = Path(denied_dir, "effect.txt")
            completed = subprocess.run(
                [
                    codex,
                    "sandbox",
                    "-P",
                    ":workspace",
                    "-C",
                    allowed_dir,
                    "--",
                    "/bin/sh",
                    "-c",
                    'touch "$1"; touch "$2"',
                    "sh",
                    str(allowed_path),
                    str(denied_path),
                ],
                text=True,
                capture_output=True,
            )

            allowed_exists = allowed_path.exists()
            denied_exists = denied_path.exists()
            assert allowed_exists, "workspace-scoped effect was unexpectedly denied"
            assert not denied_exists, "effect escaped the workspace authorization scope"
            assert completed.returncode != 0, "denied effect did not fail the command"

            report = {
                "experiment": "codex-sandbox-authority-enforcement",
                "platform": platform.system(),
                "codex": version_match.group(0),
                "permission_profile": ":workspace",
                "controlled_variables": [
                    "Codex binary",
                    "permission profile",
                    "command executable",
                    "operation",
                    "filesystem owner and mode",
                ],
                "independent_variable": "effect target inside versus outside authorized workspace",
                "observations": {
                    "inside_workspace": "allowed",
                    "outside_workspace": "denied",
                    "command_exit": completed.returncode,
                    "denial_observed": bool(completed.stderr.strip()),
                },
                "result": {
                    "authority_enforcement_observed": True,
                    "claim": (
                        "With capability and operation held fixed, delegated "
                        "effect scope changes whether the coding Harness admits the effect."
                    ),
                },
            }
            print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
