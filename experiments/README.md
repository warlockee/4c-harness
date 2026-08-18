# Empirical Reproduction Suite

These experiments test 4C classifications against executable system behavior.
Each imports and runs the named upstream package at the version pinned in
`requirements.txt`.

## Evidence levels

Running real code is not by itself independent evidence. Every report states
which of three levels applies, and the level is part of the result:

| Level | Meaning | Weight |
|---|---|---|
| **Third-party behaviour** | The upstream system produces the observed policy delta; this repository only fixes the controlled variables. | Supports a classification independently. |
| **Instrumented illustration** | The policy delta is produced by locally authored code, with the upstream package supplying the named primitive. | Shows the distinction is statable and mechanisable. Does **not** corroborate it. |
| **Declared interface** | A shipped binary's advertised controls are read, not exercised. | Shows independent products expose the surface. Says nothing about enforcement. |

An earlier version of this file let all six experiments read as equivalent
counterfactual evidence. Three are; three are not.

## Rules

An experiment must:

1. run without provider credentials where possible;
2. record the package/runtime versions and an ordered transition trace;
3. vary one proposed cause while holding the execution graph fixed;
4. check the observed outcome rather than relying on prose, using
   `_support.require` so that checks survive `python -O`;
5. name both the supported classification and the result that would falsify it;
6. declare its evidence level and what it does not prove;
7. exit with `_support.SKIP_EXIT_CODE` when a precondition such as a local CLI
   is unmet, so that an unrunnable experiment is never reported as a pass or
   confused with a falsification.

## Run

``` shell
python3 -m venv .venv
.venv/bin/pip install -r experiments/requirements.txt
.venv/bin/python experiments/run_all.py
```

The inference boundary test uses Python 3.12 or 3.13 because the pinned ONNX
Runtime wheel is not available for every newer interpreter:

``` shell
python3.13 -m venv .venv-inference
.venv-inference/bin/pip install -r experiments/requirements-inference.txt
.venv-inference/bin/python experiments/onnxruntime_infra_boundary.py
```

`run_all.py` also runs the two experiments that need a locally installed CLI
(`codex`, `claude`) and reports them as `SKIP` when the binary is absent, which
is why the same command is useful locally and in CI. It exits nonzero if an
expected transition or counterfactual fails, or if a portable experiment is
skipped.

The first verified run is preserved in
[`results/langgraph-authority-continuity.json`](results/langgraph-authority-continuity.json);
the gateway run is in
[`results/litellm-provider-compatibility.json`](results/litellm-provider-compatibility.json).
The local binary-interface observation is in
[`results/coding-harness-authority-interface.json`](results/coding-harness-authority-interface.json).
The Codex enforcement trace is in
[`results/codex-sandbox-authority-enforcement.json`](results/codex-sandbox-authority-enforcement.json).
The eval/feedback result is in
[`results/autoevals-cognition-boundary.json`](results/autoevals-cognition-boundary.json).
The inference boundary result is in
[`results/onnxruntime-infrastructure-boundary.json`](results/onnxruntime-infrastructure-boundary.json).
Reruns print the same semantic fields while the Python runtime may differ.
The same clean-install run is enforced by
[`empirical.yml`](../.github/workflows/empirical.yml) on pushes and pull
requests.

## Coverage

| Experiment | Evidence level | Real system surface | Counterfactual | Theory boundary |
|---|---|---|---|---|
| `litellm_compatibility.py` | Third-party behaviour | LiteLLM provider-parameter transformation | Same canonical request; change only target provider semantics | Compatibility changes representation while task intent remains fixed. |
| `codex_sandbox_authority.py` | Third-party behaviour | Codex command sandbox with built-in `:workspace` permission profile | Same `touch`; target inside versus outside the authorized workspace | Behavioral enforcement of delegated effect scope as Authority. |
| `onnxruntime_infra_boundary.py` | Third-party behaviour | ONNX Runtime forward-pass execution | Same graph/input/output; vary threads and graph optimization | Computation policy remains Infrastructure and does not create task-transition semantics. |
| `langgraph_authority_continuity.py` | Instrumented illustration | LangGraph `interrupt`, `Command` and in-memory checkpointing | Same graph and pending state; approve versus deny | Authority changes admissibility; Continuity preserves and resumes the decision point. LangGraph supplies suspend/resume; the allow/deny divergence is authored locally. |
| `autoevals_cognition_boundary.py` | Instrumented illustration | Braintrust Autoevals local scorer | Same output and score; passive evaluation versus explicit reusable policy update | Evaluation evidence alone is not Cognition; adaptation is. Autoevals supplies the score; the adaptation operator is authored locally. |
| `coding_harness_authority_surface.py` | Declared interface | Installed Codex and Claude Code binary interfaces | Two independent products expose permission, sandbox and bypass controls | Interface-level replication of Authority; does **not** prove enforcement efficacy. |

This is a first executable reproduction, not empirical closure, and only the
three third-party rows independently support a classification. The Authority and
Cognition boundaries therefore rest on desk research plus one genuine
enforcement observation. The next candidates are upstream systems whose own code
makes those distinctions observable: Agents SDK tool-approval interruptions and
a DSPy compile step.

The ONNX Runtime experiment makes the Infrastructure/Harness controlled-object
test executable without pretending to reproduce vLLM's GPU-specific kernels or
scheduler. The two CLI experiments skip in the dependency-only CI job because
the binaries are not installed there; neither invokes a model or needs
credentials.

One incidental finding is worth recording, since it shapes how the enforcement
experiment must be written: the Codex `:workspace` profile grants the system
temporary directory in addition to the `-C` workspace. An unauthorized target
placed under `$TMPDIR` is written successfully, so the denied path must sit
outside every granted root: here, a scratch directory inside this repository.
