#!/usr/bin/env python3
"""Exercise Orze on a bounded GPU-research 4C terrain.

This experiment uses Orze's shipped code paths.  It deliberately separates
mechanism evidence from task-yield evidence: no source or fault-injection pass
can set ``competitive_claim_proven`` without a paired GPU campaign.
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
import tempfile

from _support import THIRD_PARTY_BEHAVIOUR, require, skip


ROOT = Path(__file__).resolve().parents[1]
ORZE_ROOT = Path(
    os.environ.get("ORZE_SOURCE_ROOT", ROOT.parent / "orze")
).resolve()
ORZE_PRO_ROOT = Path(
    os.environ.get("ORZE_PRO_SOURCE_ROOT", ROOT.parent / "orze-pro")
).resolve()


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _git(root: Path, *command: str) -> str:
    return subprocess.run(
        ["git", "-C", str(root), *command],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    ).stdout.strip()


def _child_env() -> dict[str, str]:
    env = dict(os.environ)
    source_path = os.pathsep.join(
        [str(ORZE_PRO_ROOT / "src"), str(ORZE_ROOT / "src")]
    )
    env["PYTHONPATH"] = source_path
    for name in (
        "CUDA_VISIBLE_DEVICES",
        "NVIDIA_VISIBLE_DEVICES",
        "HIP_VISIBLE_DEVICES",
        "ROCR_VISIBLE_DEVICES",
    ):
        env.pop(name, None)
    return env


def _terminal_lake(path: Path) -> Path:
    from orze.idea_lake import IdeaLake

    database = path / "lake.db"
    lake = IdeaLake(str(database))
    lake.insert("idea-clean", "clean", "seed: 1\n", "", status="queued")
    require(
        lake.record_state_transition("idea-clean", "QUEUED", "CLAIMED"),
        "clean lifecycle did not reach CLAIMED",
    )
    require(
        lake.record_state_transition("idea-clean", "CLAIMED", "IN_PROGRESS"),
        "clean lifecycle did not reach IN_PROGRESS",
    )
    require(
        lake.record_stage_transition(
            "idea-clean", "training", "IN_PROGRESS", "COMPLETE", "trained"
        ),
        "training stage did not complete",
    )
    require(
        lake.record_state_transition(
            "idea-clean", "IN_PROGRESS", "COMPLETE", "experiment_terminal"
        ),
        "clean lifecycle did not reach COMPLETE",
    )
    lake.close()
    return database


def _lease_probe() -> dict:
    from orze.core.gpu_lease import acquire_gpu_leases

    synthetic_gpu = 800_000 + (os.getpid() % 10_000)
    code = (
        "from orze.core.gpu_lease import acquire_gpu_leases; "
        f"lease=acquire_gpu_leases([{synthetic_gpu}]); lease.close()"
    )
    held = acquire_gpu_leases([synthetic_gpu])
    try:
        overlap = subprocess.run(
            [sys.executable, "-c", code],
            env=_child_env(),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    finally:
        held.close()
    released = subprocess.run(
        [sys.executable, "-c", code],
        env=_child_env(),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    require(overlap.returncode != 0, "overlapping lease was accepted")
    require("gpu_lease_contended" in overlap.stderr, "contention was not typed")
    require(released.returncode == 0, "released lease remained stuck")
    return {
        "overlap_rejected": True,
        "typed_failure": "gpu_lease_contended",
        "released_scope_reusable": True,
        "physical_accelerator_queried": False,
    }


def _policy_probe(path: Path) -> dict:
    from orze_pro.agents.meta_research import (
        promote_strategy,
        rollback_strategy,
        stage_strategy_proposal,
    )

    rules = path / ".orze" / "rules" / "RESEARCH_RULES.md"
    rules.parent.mkdir(parents=True)
    original = "# Research rules\n\n- Preserve the measured control.\n"
    rules.write_text(original, encoding="utf-8")
    strategy = """## Auto-Generated Strategy

- Stop the observed regressing family after three qualified failures.
- Allocate the released attempt budget to the strongest under-explored family.
"""
    proposal = stage_strategy_proposal(path, strategy, "plateau", "experiment")
    promote_strategy(rules, strategy, proposal)
    promoted = rules.read_text(encoding="utf-8")
    active = json.loads(
        (path / ".orze" / "policy" / "active.json").read_text(encoding="utf-8")
    )
    require(strategy.strip() in promoted, "policy proposal was not promoted")
    require(active.get("sha256") == hashlib.sha256(promoted.encode()).hexdigest(),
            "active policy identity did not match promoted bytes")
    rollback_strategy(rules, path)
    require(rules.read_text(encoding="utf-8") == original,
            "policy rollback did not restore exact prior bytes")
    return {
        "proposal_content_addressed": True,
        "promotion_atomic_and_versioned": True,
        "rollback_exact": True,
        "future_yield_uplift_proven": False,
    }


def _cognition_feedback_probe(path: Path) -> dict:
    """Exercise rejection feedback and the standalone context boundary."""
    from orze.engine.collab_bus import post
    from orze_pro.agents.research_context import build_context

    results = path / "results"
    results.mkdir(parents=True)
    ideas = path / "ideas.md"
    ideas.write_text("# Ideas\n", encoding="utf-8")
    rejection = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "idea_id": "idea-rejected",
        "validator": "research_preflight",
        "rejection": "validator[sealed_axis]: measured branch is closed",
        "stage": "prequeue",
    }
    (results / "_validator_rejections.jsonl").write_text(
        "not-json\n" + json.dumps(rejection) + "\n",
        encoding="utf-8",
    )
    composite_marker = "SYNTHETIC_COMPOSITE_STEERING_MUST_NOT_APPEAR"
    post(
        results,
        "ensemble_strategist",
        "research",
        "diversity_report",
        composite_marker,
    )
    context = build_context(
        results,
        ideas,
        {},
        project_cfg={
            "research_policy": {"model_form": "single_model_single_pass"}
        },
    )
    require(
        "## Recently Observed Validator Rejections" in context
        and "sealed_axis" in context,
        "recent validator rejection did not reach research context",
    )
    require(
        composite_marker not in context
        and "## Ensemble Diversity Analysis" not in context,
        "composite steering reached a standalone-only research context",
    )
    return {
        "recent_rejection_feedback_closed_loop": True,
        "malformed_ledger_row_ignored": True,
        "standalone_context_rejected_composite_steering": True,
        "physical_accelerator_queried": False,
    }


def main() -> None:
    for source in (ORZE_ROOT / "src" / "orze", ORZE_PRO_ROOT / "src" / "orze_pro"):
        if not source.is_dir():
            skip(f"source checkout missing: {source}")
    sys.path[:0] = [str(ORZE_PRO_ROOT / "src"), str(ORZE_ROOT / "src")]

    from orze import __version__ as orze_version
    from orze.core.research_policy import validate_idea_against_research_policy
    from orze.data_boundaries import audit_training_access_log
    from orze.engine.launcher import LaunchIntegrityError, _assert_gpu_authorized
    from orze.engine.recovery_audit import audit_recovery_state
    from orze_pro import __version__ as orze_pro_version

    with tempfile.TemporaryDirectory(prefix="orze-4c-") as raw:
        work = Path(raw)

        benchmark_path = work / "cpu-control-plane.json"
        benchmark = subprocess.run(
            [
                sys.executable,
                "-m",
                "orze.benchmarks.harness_efficiency",
                "--work-dir",
                str(work / "benchmark"),
                "--ideas",
                "50000",
                "--queue-limit",
                "2000",
                "--iterations",
                "20",
                "--output",
                str(benchmark_path),
            ],
            cwd=ORZE_ROOT,
            env=_child_env(),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        require(benchmark.returncode == 0, "CPU control-plane benchmark failed")
        cpu = json.loads(benchmark_path.read_text(encoding="utf-8"))
        require(cpu.get("status") == "VERIFIED", "CPU receipt was not VERIFIED")
        require(
            cpu.get("scope", {}).get("accelerator_access") == "none",
            "CPU receipt accessed an accelerator",
        )

        clean_root = work / "recovery-clean"
        clean_root.mkdir()
        clean_db = _terminal_lake(clean_root)
        clean_recovery = audit_recovery_state(clean_db, clean_root / "results")
        require(clean_recovery["status"] == "VERIFIED", "clean recovery failed")

        corrupt_root = work / "recovery-corrupt"
        corrupt_root.mkdir()
        corrupt_db = corrupt_root / "lake.db"
        shutil.copy2(clean_db, corrupt_db)
        connection = sqlite3.connect(corrupt_db)
        connection.execute(
            "UPDATE idea_transitions SET to_state='FAILED' "
            "WHERE idea_id='idea-clean' AND id=("
            "SELECT MAX(id) FROM idea_transitions WHERE idea_id='idea-clean')"
        )
        connection.commit()
        connection.close()
        corrupt_recovery = audit_recovery_state(corrupt_db, corrupt_root / "results")
        require(corrupt_recovery["status"] == "FAILED",
                "transition corruption was not rejected")

        scope_cfg = {
            "gpu_scheduling": {
                "allowed_gpus": [4, 5, 6, 7],
                "reserved_gpus": [0, 1, 2, 3],
            },
            "_managed_gpu_ids": [4, 5, 6, 7],
        }
        _assert_gpu_authorized(4, scope_cfg)
        forbidden_reason = None
        try:
            _assert_gpu_authorized(0, scope_cfg)
        except LaunchIntegrityError as exc:
            forbidden_reason = str(exc)
        require(forbidden_reason == "gpu_outside_managed_scope:0",
                "forbidden GPU was not rejected by the shipped boundary")

        single_cfg = {
            "research_policy": {"model_form": "single_model_single_pass"}
        }
        require(
            validate_idea_against_research_policy(
                {"strategy": "single_model_finetune"}, single_cfg
            ) is None,
            "standalone candidate was rejected",
        )
        composite_reason = validate_idea_against_research_policy(
            {"ensemble_models": ["a", "b"]}, single_cfg
        )
        require(
            composite_reason == "research_policy_composite_forbidden:config.ensemble_models",
            "composite candidate escaped the standalone boundary",
        )

        access_root = work / "access"
        access_root.mkdir()
        clean_access = audit_training_access_log(access_root)
        (access_root / "_access_log.tsv").write_text(
            "FORBIDDEN\t/private/eval\t/private/eval/sample.bin\n",
            encoding="utf-8",
        )
        tainted_access = audit_training_access_log(access_root)
        require(clean_access["status"] == "CLEAN", "empty synthetic access was not clean")
        require(tainted_access["status"] == "TAINTED", "forbidden access was not tainted")

        lease = _lease_probe()
        cognition = _policy_probe(work / "policy")
        cognition.update(_cognition_feedback_probe(work / "feedback"))

        source_files = {
            "orze_cpu_benchmark": ORZE_ROOT / "src/orze/benchmarks/harness_efficiency.py",
            "orze_recovery": ORZE_ROOT / "src/orze/engine/recovery_audit.py",
            "orze_gpu_scope": ORZE_ROOT / "src/orze/engine/launcher.py",
            "orze_gpu_lease": ORZE_ROOT / "src/orze/core/gpu_lease.py",
            "orze_research_policy": ORZE_ROOT / "src/orze/core/research_policy.py",
            "orze_access_audit": ORZE_ROOT / "src/orze/data_boundaries/__init__.py",
            "orze_pro_policy": ORZE_PRO_ROOT / "src/orze_pro/agents/meta_research.py",
            "orze_pro_research_context": (
                ORZE_PRO_ROOT / "src/orze_pro/agents/research_context.py"
            ),
            "experiment": Path(__file__),
        }
        report = {
            "experiment": "orze-gpu-research-4c",
            "evidence_level": THIRD_PARTY_BEHAVIOUR,
            "terrain": "bounded, GPU-constrained ML research with external validity gates",
            "systems": {
                "orze": {
                    "version": orze_version,
                    "commit": _git(ORZE_ROOT, "rev-parse", "HEAD"),
                    "tree_clean": not bool(
                        _git(ORZE_ROOT, "status", "--porcelain")
                    ),
                },
                "orze_pro": {
                    "version": orze_pro_version,
                    "commit": _git(ORZE_PRO_ROOT, "rev-parse", "HEAD"),
                    "tree_clean": not bool(
                        _git(ORZE_PRO_ROOT, "status", "--porcelain")
                    ),
                },
            },
            "observations": {
                "cost": {
                    "status": "VERIFIED",
                    "idea_count": cpu["metrics"]["idea_count"],
                    "iterations": cpu["metrics"]["iterations"],
                    "steady_control_tick_p95_ms": cpu["metrics"]["steady_control_tick"]["p95_ms"],
                    "lifecycle_round_trip_p95_ms": cpu["metrics"]["lifecycle_round_trip"]["p95_ms"],
                    "bulk_insert_rows_per_second": cpu["metrics"]["bulk_insert_rows_per_second"],
                    "accelerator_access": "none",
                },
                "compatibility": {
                    "status": "PARTIAL",
                    "source_pair_imported": True,
                    "orze_version": orze_version,
                    "orze_pro_version": orze_pro_version,
                    "cross_provider_task_trial_run": False,
                },
                "continuity": {
                    "status": "VERIFIED",
                    "clean_terminal_ledger": clean_recovery["status"],
                    "corrupt_transition_ledger": corrupt_recovery["status"],
                    "cross_process_gpu_lease": lease,
                },
                "cognition": {
                    "status": "MECHANISM_VERIFIED_YIELD_UNVERIFIED",
                    **cognition,
                },
            },
            "boundaries": {
                "gpu_scope": {
                    "mechanism_status": "VERIFIED",
                    "allowed_physical_gpus": [4, 5, 6, 7],
                    "forbidden_physical_gpus": [0, 1, 2, 3],
                    "forbidden_probe_result": forbidden_reason,
                    "live_gpu_campaign_run": False,
                },
                "standalone_model": {
                    "mechanism_status": "VERIFIED",
                    "composite_probe_result": composite_reason,
                },
                "data_access": {
                    "mechanism_status": "VERIFIED",
                    "clean_probe": clean_access["status"],
                    "forbidden_probe": tainted_access["status"],
                    "real_campaign_absence_of_leakage_proven": False,
                },
            },
            "source_sha256": {name: _sha256(path) for name, path in source_files.items()},
            "result": {
                "status": "PARTIAL",
                "competitive_claim_proven": False,
                "task_proven": False,
                "reason": (
                    "Cost, recovery, scope, lease, standalone, access-audit, "
                    "versioned-policy, and validator-feedback mechanisms behaved "
                    "as specified; no paired GPU yield trial or cross-provider "
                    "task trial has completed."
                ),
                "not_proven": [
                    "higher qualified research yield than a same-stack control",
                    "GPU duty cycle or tail behaviour on physical GPUs 4-7",
                    "cross-provider task compatibility",
                    "absence of leakage in a real training campaign",
                    "an independent 4C rank",
                ],
            },
        }
        print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
