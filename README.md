# The 4C Theory of AI Harness

> **Models create intelligence. Infrastructure creates computation.
> Harnesses create execution. Applications create user value.**

A model call is not a task. A **Harness** is the engineering layer that turns
bounded, mostly stateless model calls into task execution across tools, state,
providers and time.

4C is a compact way to ask **why Harness execution policy must change**:

| 4C | Reality | Harness question |
|---|---|---|
| **Cost** | Resources are finite | What should change because tokens, latency, context, attempts or money are bounded? |
| **Compatibility** | Systems differ | What should change because models, providers, tools or environments have different semantics? |
| **Continuity** | Tasks unfold through time | What state and lifecycle control must survive across inference boundaries? |
| **Cognition** | Past runs produce evidence | What reusable future policy should change because of prior execution? |

![The 3 + 1 structure of 4C](assets/diagrams/3-plus-1.svg)

Cost, Compatibility and Continuity are pressures on current execution.
Cognition is the cross-run feedback plane. That is the entire core theory.

## What 4C is not

1. **Not a feature taxonomy.** One mechanism can answer several questions.
   Compression may serve Cost and Continuity; learned compression policy may
   also involve Cognition.
2. **Not a complete Harness checklist.** Evidence access, result validity and
   action authority are real Harness obligations, but they are not additional
   causes of policy variation forced into the acronym.
3. **Not a product-label taxonomy.** Classify the controlled object, not the
   vendor. vLLM's batching, kernels and GPU scheduling optimize model
   computation, so they are Infrastructure. A task-level route, retry or context
   decision can be Harness policy even when the same product contains both.

## Use it in sixty seconds

Name the task execution you are analyzing, then ask:

1. Would policy change if resources were unconstrained? → **Cost**
2. Would it change if every component had identical semantics? → **Compatibility**
3. Would it change if the task fit in one instantaneous call? → **Continuity**
4. Would it change only because prior runs taught the system something reusable?
   → **Cognition**

If none applies, do not stretch a C. The concern may be an evidence, validity or
authority obligation; model intelligence; infrastructure; application policy;
or a candidate that can break the theory.

## Why the qualification matters

The original claim that four unavoidable constraints exhaust Harness
engineering did not survive hostile testing. Consequential tool calls still
need Authority; a correct answer still needs task-relevant evidence and
Validity—even with free resources, one provider, one call and no learning.

The revision preserves the useful 4C lens and rejects the overclaim. The deeper
validation model—boundary obligations plus a mediated transition system—is a
way to test where 4C stops. It is **not an expanded seven-letter theory** and is
not required to use 4C.

## Evidence and falsification

The revised theory was tested against inference infrastructure, gateways, agent
runtimes, coding Harnesses and eval platforms, including adversarial cases for
browser/embodied agents, asynchronous execution, multiple principals and
self-modification. Representative counterfactual experiments cover LangGraph,
LiteLLM, Braintrust Autoevals, Codex sandboxing and ONNX Runtime.

The rule remains:

> **Try to break 4C before promoting 4C.**

A single recurring Harness-owned policy cause outside scarcity, semantic
difference, temporal dependence and reusable experience reopens the theory.

## Read further

- [Theory](docs/theory.md) — precise definitions; the first four sections are
  the complete core
- [Review guide](REVIEW_GUIDE.md) — 5-minute, 30-minute and adversarial paths
- [Evidence matrix](docs/evidence.md) — claim-level sources and reopening
  conditions
- [Counterarguments](docs/counterarguments.md) — strongest attacks
- [Landscape](docs/landscape.md) — mechanism-level system mapping
- [Case studies](docs/case-studies.md) — concrete boundary decisions
- [Predictions](docs/predictions.md) — claims that can later be wrong
- [Validation ledger](docs/validation/README.md) — full hostile research record
- [Empirical reproductions](experiments/README.md) — pinned executable tests

Status: **v1.0 promotion gate passed for the revised, explicitly falsifiable
theory. The original exhaustive formulation remains rejected.**
