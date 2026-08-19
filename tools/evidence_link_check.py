#!/usr/bin/env python3
"""Resolve every commit-pinned 4C Fit evidence path through the GitHub API."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from urllib.parse import urlparse

from fit_score_check import EVIDENCE_PATH


FIELDS = ("implementation", "invariant", "reachability")


def api_endpoint(url: str) -> str:
    parts = [part for part in urlparse(url).path.split("/") if part]
    if len(parts) < 5 or parts[2] not in {"blob", "tree"}:
        raise ValueError(f"not a pinned GitHub source URL: {url}")
    owner, repo, _kind, commit, *path = parts
    return f"/repos/{owner}/{repo}/contents/{'/'.join(path)}?ref={commit}"


def evidence_endpoints() -> list[str]:
    ledger = json.loads(EVIDENCE_PATH.read_text())["evidence"]
    urls = {
        item[field]
        for candidate in ledger.values()
        for item in candidate.values()
        for field in FIELDS
        if item.get(field)
    }
    return sorted({api_endpoint(url) for url in urls})


def main() -> int:
    if shutil.which("gh") is None:
        print("FAIL GitHub CLI is required for the live evidence-path audit", file=sys.stderr)
        return 1
    endpoints = evidence_endpoints()
    for endpoint in endpoints:
        result = subprocess.run(
            ["gh", "api", endpoint, "--silent"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode:
            detail = result.stderr.strip() or "GitHub API request failed"
            print(f"FAIL {endpoint}: {detail}", file=sys.stderr)
            return 1
    print(f"PASS pinned GitHub evidence paths: {len(endpoints)}/{len(endpoints)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
