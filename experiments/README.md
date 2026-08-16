# Empirical Reproduction Suite

These experiments test 4C classifications against executable system behavior.
They are not demonstrations written to resemble a framework: each experiment
imports and runs the named upstream package at the version pinned in
`requirements.txt`.

## Rules

An experiment must:

1. run without provider credentials where possible;
2. record the package/runtime versions and an ordered transition trace;
3. vary one proposed cause while holding the execution graph fixed;
4. assert the observed outcome rather than relying on prose;
5. name both the supported classification and the result that would falsify it.

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

The command exits nonzero if an expected transition or counterfactual fails.
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

| Experiment | Real system surface | Counterfactual | Theory boundary |
|---|---|---|---|
| `langgraph_authority_continuity.py` | LangGraph graph execution, `interrupt`, `Command`, in-memory checkpointing | Same graph and pending state; approve versus deny | Authority changes admissibility; Continuity preserves and resumes the decision point. |
| `litellm_compatibility.py` | LiteLLM provider-parameter transformation | Same canonical request; change only target provider semantics | Compatibility changes representation while task intent remains fixed. |
| `autoevals_cognition_boundary.py` | Braintrust Autoevals local scorer | Same output and score; passive evaluation versus explicit reusable policy update | Evaluation evidence alone is not Cognition; adaptation is. |
| `coding_harness_authority_surface.py` | Installed Codex and Claude Code binary interfaces | Two independent products expose permission, sandbox and bypass controls | Interface-level replication of Authority; does **not** prove enforcement efficacy. |
| `codex_sandbox_authority.py` | Codex command sandbox with built-in `:workspace` permission profile | Same `touch`; target inside versus outside the authorized workspace | Behavioral enforcement of delegated effect scope as Authority. |
| `onnxruntime_infra_boundary.py` | ONNX Runtime forward-pass execution | Same graph/input/output; vary threads and graph optimization | Computation policy remains Infrastructure and does not create task-transition semantics. |

This is the first executable reproduction, not empirical closure. Inference,
The ONNX Runtime experiment makes the Infrastructure/Harness controlled-object
test executable without pretending to reproduce vLLM's GPU-specific kernels or
scheduler. The Codex enforcement experiment is local-only because the CLI is not installed in
the dependency-only CI job; it invokes no model and needs no credentials.
