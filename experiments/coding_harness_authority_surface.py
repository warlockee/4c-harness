#!/usr/bin/env python3
"""Inspect installed coding-Harness binaries for independent authority controls.

This is an interface reproduction, not an enforcement test. It is intentionally
excluded from credential-free CI because the third-party CLIs are not installed
on the runner.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess


def output(*command: str) -> str:
    return subprocess.run(
        command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    ).stdout


def version(binary: str) -> str:
    text = output(binary, "--version")
    match = re.search(r"\d+(?:\.\d+)+", text)
    assert match, f"could not parse {binary} version"
    return match.group(0)


def main() -> None:
    missing = [binary for binary in ("codex", "claude") if not shutil.which(binary)]
    assert not missing, f"required local CLIs missing: {', '.join(missing)}"

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
    assert all(codex_controls.values())
    assert all(claude_controls.values())

    report = {
        "experiment": "coding-harness-authority-interface",
        "evidence_level": "installed-binary interface; enforcement not tested",
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
