#!/usr/bin/env python3
"""Inspect installed coding-Harness binaries for independent authority controls.

Evidence level: declared interface. This reads the control surfaces two shipped
binaries advertise. It is not an enforcement test, and a missing CLI is a
skipped precondition rather than a failed claim — see
`codex_sandbox_authority.py` for the enforcement observation.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess

from _support import DECLARED_INTERFACE, require, skip


def output(*command: str) -> str:
    return subprocess.run(
        command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    ).stdout


def version(binary: str) -> str:
    text = output(binary, "--version")
    match = re.search(r"\d+(?:\.\d+)+", text)
    require(match, f"could not parse {binary} version")
    return match.group(0)


def main() -> None:
    missing = [binary for binary in ("codex", "claude") if not shutil.which(binary)]
    if missing:
        skip(f"CLIs not installed: {', '.join(missing)}; interface reproduction not run")

    codex_help = output("codex", "--help")
    claude_help = output("claude", "--help")

    codex_controls = {
        "sandbox_modes": all(
            value in codex_help
            for value in ("read-only", "workspace-write", "danger-full-access")
        ),
        "approval_policy": "--ask-for-approval" in codex_help,
        "explicit_bypass": "--dangerously-bypass-approvals-and-sandbox" in codex_help,
    }
    claude_controls = {
        "allow_rules": "--allowedTools" in claude_help,
        "deny_rules": "--disallowedTools" in claude_help,
        "permission_mode": "--permission-mode" in claude_help,
        "explicit_bypass": "--dangerously-skip-permissions" in claude_help,
    }
    require(all(codex_controls.values()), f"Codex control surface changed: {codex_controls}")
    require(
        all(claude_controls.values()), f"Claude Code control surface changed: {claude_controls}"
    )

    report = {
        "experiment": "coding-harness-authority-interface",
        "evidence_level": DECLARED_INTERFACE,
        "systems": {
            "codex": {"version": version("codex"), "controls": codex_controls},
            "claude-code": {
                "version": version("claude"),
                "controls": claude_controls,
            },
        },
        "result": {
            "authority_surface_replicated": True,
            "claim": (
                "Two independent coding Harnesses expose permission decisions "
                "separately from sandbox enforcement and explicit bypass modes."
            ),
            "not_proven": "that either implementation enforces every advertised policy",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
