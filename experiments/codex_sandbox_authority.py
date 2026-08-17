#!/usr/bin/env python3
"""Test Codex sandbox effect scope without invoking a model.

Evidence level: third-party behaviour. The denial is enforced by the Codex
sandbox, not by this file.

Choosing the unauthorized target takes care. The `:workspace` profile grants
the system temporary directory in addition to the `-C` workspace, so a sibling
under `$TMPDIR` is *inside* the authorized scope and is written successfully.
The unauthorized target is therefore a scratch directory under this repository,
which is neither the workspace nor a granted root. Both scratch directories are
removed on exit, and the experiment writes nowhere but its own temporary
workspace and its own repository.
"""

from __future__ import annotations

import json
import platform
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from _support import THIRD_PARTY_BEHAVIOUR, require, skip


ROOT = Path(__file__).resolve().parents[1]


def codex_version(codex: str) -> str:
    text = subprocess.run(
        [codex, "--version"], check=True, text=True, capture_output=True
    ).stdout
    match = re.search(r"\d+(?:\.\d+)+", text)
    require(match, "could not parse the Codex version")
    return match.group(0)


def attempt_both_effects(
    codex: str, allowed_dir: Path, denied_dir: Path
) -> subprocess.CompletedProcess[str]:
    """Run one `touch` per target under a workspace-scoped sandbox."""
    return subprocess.run(
        [
            codex,
            "sandbox",
            "-P",
            ":workspace",
            "-C",
            str(allowed_dir),
            "--",
            "/bin/sh",
            "-c",
            'touch "$1"; touch "$2"',
            "sh",
            str(allowed_dir / "effect.txt"),
            str(denied_dir / "effect.txt"),
        ],
        text=True,
        capture_output=True,
    )


def main() -> None:
    codex = shutil.which("codex")
    if not codex:
        skip("codex CLI not installed; local enforcement experiment not run")
    version = codex_version(codex)

    with tempfile.TemporaryDirectory(prefix="4c-codex-workspace-") as workspace:
        with tempfile.TemporaryDirectory(prefix=".4c-codex-outside-", dir=ROOT) as outside:
            allowed_dir, denied_dir = Path(workspace), Path(outside)
            completed = attempt_both_effects(codex, allowed_dir, denied_dir)

            require(
                (allowed_dir / "effect.txt").exists(),
                "workspace-scoped effect was unexpectedly denied",
            )
            require(
                not (denied_dir / "effect.txt").exists(),
                "effect escaped the workspace authorization scope",
            )
            require(completed.returncode != 0, "denied effect did not fail the command")
            denial_observed = bool(completed.stderr.strip())

    report = {
        "experiment": "codex-sandbox-authority-enforcement",
        "evidence_level": THIRD_PARTY_BEHAVIOUR,
        "platform": platform.system(),
        "codex": version,
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
            "denial_observed": denial_observed,
        },
        "result": {
            "authority_enforcement_observed": True,
            "claim": (
                "With capability and operation held fixed, delegated "
                "effect scope changes whether the coding Harness admits the effect."
            ),
            "not_proven": (
                "that the sandbox resists an adversarial escape attempt; only "
                "that the declared scope is enforced for this operation"
            ),
            "scope_note": (
                "the :workspace profile also grants $TMPDIR, so an unauthorized "
                "target must be chosen outside every granted root"
            ),
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
