# System Mappings — Tranche 02

Date checked: **2026-08-15**<br>
Method: primary documentation and original papers; mechanism-level mapping

## Why this tranche

Tranche 01 assigned each product a primary archetype. That is too coarse for
systems that deliberately span layers. This tranche maps mechanisms through the
mediated transition loop:

``` text
state/evidence → select transition → mediate → apply/expose → outcome/update
```

It then asks which 4C pressure, if any, changes policy. Product membership is
not the unit of proof.

## Summary

| System | Main boundary result | Loop attack | New residual? |
|---|---|---|---|
| SGLang | Frontend language can be Harness; serving runtime is Infrastructure. | Product-level layer labels fail. | No |
| Portkey | Gateway spans routing, lifecycle and input/output mediation. | Mediation is recurrent, not one stage. | No |
| OpenAI Agents SDK | Explicit model/code/human transition loop. | Strong fit after replacing “model proposal.” | No |
| Claude Code | Full coding Harness with deterministic hooks and layered authority. | Strong fit; shows multiple mediation points. | No |
| Braintrust | Evaluation/learning plane adjacent to live execution. | Evidence and Validity need not own application. | No |

## 1. SGLang — one product, two layers

**Documented.** The original SGLang paper describes a frontend language for
programs containing multiple generation calls, control flow and structured
inputs/outputs, plus a runtime with RadixAttention and compressed finite-state
machines for efficient execution
([paper](https://arxiv.org/abs/2312.07104)). The current project describes
itself primarily as high-performance serving infrastructure and exposes
parallelism, device, cache and backend controls
([repository](https://github.com/sgl-project/sglang),
[server arguments](https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/server_arguments.mdx)).

**Mapping.** Runtime scheduling, KV-cache reuse, device parallelism and decoding
kernels optimize model computation: Infrastructure. A frontend program that
sequences several model calls or branches based on results selects task
transitions and carries state: a narrow Harness surface, principally Continuity
and Compatibility.

**Verdict: split by mechanism.** SGLang falsifies the rule “one system belongs
to one layer,” not the computation/execution boundary. The boundary question is
what a mechanism controls. Structured decoding inside the server is not
semantic Validity merely because it constrains syntax.

## 2. Portkey — gateway with mediation

**Documented.** Portkey's gateway supports a universal API, conditional routing,
fallbacks, retries, circuit breakers, caching, rate/budget limits and timeouts
([gateway](https://portkey.ai/docs/product/ai-gateway)). Its guardrails can
inspect both requests and responses; synchronous verdicts can deny, retry,
fallback or change orchestration, while asynchronous verdicts can be logged
without changing the request
([guardrails](https://portkey.ai/docs/product/guardrails)).

**Mapping.** Provider normalization is Compatibility. Token/cost budgets and
route selection are Cost. Retry, fallback and circuit state are limited
Continuity across attempts. A synchronous guardrail performs Validity or policy
mediation when given a predicate; an asynchronous logged score supplies evidence
but does not mediate execution.

**Verdict: loop pass with ownership caution.** The same gateway mechanism can
observe, mediate and select a fallback transition. This supports a logical loop,
not physical modules. The gateway does not invent the task predicate or
authority policy merely because it enforces one.

**No new residual.** Generic “policy” decomposes by what its decision means:
resource, capability, temporal recovery, Validity or Authority.

## 3. OpenAI Agents SDK — explicit transition loop

**Documented.** The runner repeatedly calls a model, returns final output,
switches agents on handoff, executes tool calls and feeds results into another
turn; it also stops at a maximum-turn boundary
([runner](https://openai.github.io/openai-agents-python/running_agents/)). Input,
tool and output guardrails operate at different workflow boundaries
([guardrails](https://openai.github.io/openai-agents-python/guardrails/)). HITL
approval serializes run state, records approve/reject decisions and resumes the
original run
([HITL](https://openai.github.io/openai-agents-python/human_in_the_loop/)).

**Mapping.** The model proposes tool calls or final output, while runner code
selects handoff, retry, error and termination transitions. Tool results update
evidence. Guardrails mediate input, tool and output transitions. Approval adds
Authority; state serialization and resumption add Continuity. Model/provider and
tool differences add Compatibility; turn/concurrency limits can express Cost or
Continuity according to their cause.

**Verdict: strong loop fit.** This system would not fit a single
`Model Proposal → Admission` sequence, but it fits repeated transition
selection and mediation with mixed model/code/human sources.

## 4. Claude Code — coding Harness and authority stack

**Documented.** Claude Code permissions control tools, files and domains, while
OS-level sandboxing separately enforces filesystem/network boundaries
([permissions](https://code.claude.com/docs/en/permissions),
[sandboxing](https://code.claude.com/docs/en/sandboxing)). Hooks execute at
session, prompt, pre-tool, permission, post-tool, failure and stop events and can
block, approve or transform behavior
([hooks](https://code.claude.com/docs/en/hooks-guide)).

**Mapping.** Repository inspection and tool results repeatedly update evidence.
The model selects many candidate actions; deterministic hooks and human
permission decisions also select or alter transitions. Permissions and sandbox
crossings expose Authority. Session state, compaction/resumption and lifecycle
hooks expose Continuity. Tool/environment differences expose Compatibility;
context and effort choices expose Cost. Past evidence counts as Cognition only
if it changes reusable future policy, not merely because a transcript exists.

**Verdict: strong loop fit and authority replication.** Claude Code independently
reproduces the earlier Codex authority residual. Permission policy and OS
sandboxing are distinct enforcement layers, while both affect whether a proposed
action can be applied.

## 5. Braintrust — evaluation is not automatically execution

**Documented.** Braintrust defines evaluations using data, a task and scorers;
it supports immutable experiments, CI checks, asynchronous production scoring
and turning production traces into new test cases
([evaluation](https://www.braintrust.dev/docs/evaluate)). Traces contain nested
task, model, function, tool and score spans
([traces](https://www.braintrust.dev/docs/observe/examine-traces)).

**Mapping.** Traces and datasets preserve evidence. Scorers provide Validity
evidence under supplied criteria. CI can mediate a deployment transition. Online
asynchronous scoring does not mediate the already completed live execution.
Moving production failures into datasets supports Cognition, but Cognition is
complete only when a prompt, route, retrieval rule or other future Harness policy
actually changes.

**Verdict: adjacent learning plane.** The transition loop applies to the system
being evaluated and also to release/deployment decisions, but those are different
executions. Mixing them would make “Harness execution” scale-free and
unfalsifiable. The unit of execution must be named before mapping.

## Cross-system attacks

### Is there a missing policy/configuration primitive?

No independent residual. Configuration materializes Application intent,
resource/capability/lifecycle policy, Validity criteria or Authority rules. It is
an artifact and input to the loop, not a new causal reality.

### Is observability a fifth pressure?

No. Passive logging need not change execution. When trace evidence changes
future policy it participates in Cognition; when it supports a current judgment
it participates in Validity or Authority. Audit retention may satisfy governance
outside the named task execution without becoming an adaptation pressure.

### Is error handling a missing stage?

No. An error is an observed event. Its classification can invoke Compatibility
or Validity; retry/fallback/resume uses Continuity; stopping may follow Cost or
policy. The transition loop represents it without a dedicated fundamental
category.

## Findings forced by tranche 02

1. **Map mechanisms, not products.** A product can contain Model,
   Infrastructure, Harness and Application surfaces.
2. **Name the execution unit.** A user task, model request, evaluation run and
   deployment decision have different state and boundaries.
3. **Separate predicate ownership from enforcement.** Gateways and runtimes can
   enforce Validity/Authority rules supplied elsewhere.
4. **Do not infer Cognition from evidence storage.** A later policy delta is
   required.
5. **The mediated transition loop survives this tranche.** No operation required
   a fifth loop primitive beyond state/evidence update, selection, mediation and
   application.

This is evidence against obvious failure, not proof of completeness. The next
tranche should target embodied agents, asynchronous event-driven systems and
systems that modify their own tools or policies, where the loop and layer
boundary are most likely to break.
