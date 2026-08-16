# System Mappings — Tranche 01

Date checked: **2026-08-15**

These are desk-research mappings from primary product documentation. They show
where 4C does and does not explain documented mechanisms; they do not validate
performance claims.

## Summary

| System | Primary abstraction | Initial result | Main pressure point |
|---|---|---|---|
| vLLM | Inference and serving | Out of scope; boundary-control pass | 4C words also describe infra features. |
| LiteLLM | Model gateway | Strong Cost + Compatibility; partial Continuity | Reliability does not map cleanly by feature name alone. |
| LangGraph | Durable agent runtime | Strong Continuity | Human approval exposes authority, not just time. |
| OpenAI Codex | Coding harness | Cross-C with unresolved fifth candidate | Sandboxing and approvals resist reduction to 4C. |
| LangSmith | Observability and evaluation | Cognition infrastructure, sometimes Cognition | Measurement alone is not learning or adaptation. |

## 1. vLLM — inference infrastructure

**Documented.** vLLM describes itself as a library for LLM inference and
serving. Its documented mechanisms include PagedAttention, continuous batching,
prefix caching, quantization, speculative decoding, distributed inference,
structured outputs, tool parsers and compatible APIs ([vLLM documentation](https://docs.vllm.ai/en/latest/)).

**Inferred mapping.** Most of these optimize a forward-pass serving workload,
not a task across model calls. They therefore belong to infrastructure even
when their names resemble Cost or Compatibility mechanisms in a harness.
OpenAI-compatible and Anthropic-compatible serving APIs provide a narrow
Compatibility surface, but do not by themselves make vLLM a harness.

**Verdict: out of scope; boundary-control pass.** This is a useful negative
control. If 4C classifies prefix caching as Cost without first identifying the
optimized object, it overclaims. The computation/execution boundary is
essential. vLLM is not expected to be covered by a Harness policy model.

**Unknown.** Whether tool parsing and structured output have accumulated enough
task semantics in the serving layer to weaken the proposed stack boundary.

## 2. LiteLLM — model gateway

**Documented.** LiteLLM exposes routing and load balancing across deployments.
Its fallback system retries and fails over across model groups, distinguishes
ordinary, context-window and content-policy failures, and combines timeouts,
cooldowns and failure thresholds ([fallback documentation](https://docs.litellm.ai/docs/proxy/reliability),
[load-balancing documentation](https://docs.litellm.ai/docs/proxy/load_balancing)).

**Inferred mapping.** Provider and model normalization is Compatibility.
Budget- and load-sensitive routing is Cost plus Compatibility. Retry, timeout,
cooldown and failover introduce bounded control across calls, giving the gateway
a limited Continuity role even though it does not own a long-lived task.

**Verdict: cross-C, with a boundary warning.** Reliability is an outcome; the
underlying mechanisms map differently. Content-policy fallback is especially
ambiguous: provider error normalization is Compatibility, while the policy that
decides whether execution may proceed could be authority/safety rather than any
current C.

**Unknown.** Whether production gateway policy learns from prior outcomes or
only exposes telemetry and static routing configuration.

## 3. LangGraph — durable agent runtime

**Documented.** LangGraph interrupts save graph state, suspend execution and
resume later with external input. Resumption restarts the interrupted node, so
side effects before an interrupt must be designed accordingly
([interrupt documentation](https://docs.langchain.com/oss/python/langgraph/interrupts)).
The Agent Server persists checkpoints, memories, thread metadata and related
resources ([storage documentation](https://docs.langchain.com/langsmith/data-storage-and-privacy)).

**Inferred mapping.** Checkpoints, thread identity, suspension, replay
semantics and recovery are a clean Continuity fit. They demonstrate why
Continuity must include control, not only memory.

**Verdict: clean fit for durability; unresolved for approval.** Waiting for a
human is temporal control. Requiring human authorization before a consequential
action is more than temporal control: the answer changes what the agent is
allowed to do. Treating both as Continuity may erase an important distinction.

## 4. OpenAI Codex — coding harness

**Documented.** Codex runs tasks in isolated environments, executes commands,
edits files, runs checks and supports parallel tasks. The current app uses
separate threads and worktrees for parallel agents. Its sandbox limits writable
locations and network access, while approval policy governs boundary crossings
([Codex introduction](https://openai.com/index/introducing-codex/),
[Codex app](https://openai.com/index/introducing-the-codex-app/),
[deployment safety](https://openai.com/index/running-codex-safely/)).

**Inferred mapping.** Tool and environment integration is Compatibility.
Threads, long-running work, parallel isolation and iterative verification are
Continuity. Rate limits and resource use introduce Cost. Logs and learned
procedures can support Cognition, but documentation of telemetry alone is not
evidence that future execution improves.

**Verdict: cross-C plus a high-threat residual.** Sandboxing, network policy,
credential boundaries and approvals determine the permitted action set. This
is harness-level execution semantics and is not naturally derived from money,
difference, time or experience.

**Potential theory failure.** The residual may arise from a fifth underlying
reality: delegated model actions are consequential but not fully trusted.

## 5. LangSmith — observability and evaluation platform

**Documented.** LangSmith records traces and runs, supports offline evaluation
on datasets and online evaluation on production traces, and describes a loop in
which production failures become test cases used to validate fixes
([observability concepts](https://docs.langchain.com/langsmith/observability-concepts),
[evaluation documentation](https://docs.langchain.com/langsmith/evaluation)).

**Inferred mapping.** Traces supply evidence; evaluators judge outcomes;
datasets preserve experience; comparison and feedback loops can inform changes.
This covers several stages of the proposed Cognition chain.

**Verdict: Cognition infrastructure, with conditional mature Cognition.** The
platform supports Observe, Reconstruct and Evaluate. A user or external system
may still perform Diagnose, Learn and Adapt. Calling all observability
"Cognition" would make the category too permissive.

**Unknown.** Which documented product mechanisms autonomously change future
execution policy rather than helping humans make those changes.

## Tranche conclusion

The first five systems do not produce a clean fifth C, but they do expose one
serious residual: **bounded authority over consequential action**. The result is
not "4C survived." The result is that one candidate now deserves an explicit
attempt at promotion or refutation.
