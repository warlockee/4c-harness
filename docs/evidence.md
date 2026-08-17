# 4C Evidence Matrix

Status: **v1.0 evidence index; promotion gate passed**<br>
Last checked: **2026-08-15**

## How to read this file

Primary sources document systems, mechanisms and observed study results. They do
not directly prove 4C. Every theoretical classification is explicitly marked as
an inference or falsification result.

- **Documented:** the linked primary source states or specifies the mechanism.
- **Cross-source inference:** 4C's interpretation of documented mechanisms.
- **Falsification result:** a counterfactual argument recorded in the validation
  ledger; reproducible reasoning, not a vendor claim.
- **Unknown:** empirical evidence still required.

Product marketing is evidence that a feature is claimed or implemented, not
that it works well. Benchmark scores are not used to establish completeness.

The evidence target is the composed Harness model, not `3 + 1` in isolation:
transition structure describes what execution does; Epistemic Access, Validity
and Authority mediate its boundaries; the 4C lens explains recurring causes of
policy variation. Evidence for one part does not establish the other two.

## Layer and execution-unit claims

| ID | Claim | Evidence | Type | What the evidence does not prove |
|---|---|---|---|---|
| L1 | Inference serving and Harness task execution are different controlled objects. | vLLM describes inference/serving, PagedAttention, continuous batching and optimized kernels ([vLLM](https://docs.vllm.ai/en/latest/)); the [ONNX Runtime boundary reproduction](../experiments/onnxruntime_infra_boundary.py) varies threads/graph optimization while holding forward-pass result fixed; the OpenAI Agents SDK runner handles model turns, tools, handoffs and final output ([runner](https://openai.github.io/openai-agents-python/running_agents/)). | Cross-source inference + behavioral boundary control | That every vendor product occupies one layer, or that ONNX Runtime reproduces vLLM's GPU scheduler. |
| L2 | One product can span layers. | SGLang documents a frontend for multi-call language-model programs and a runtime with inference optimizations ([paper](https://arxiv.org/abs/2312.07104)). | Cross-source inference | Where every current SGLang component belongs without mechanism-level inspection. |
| L3 | Mechanism ownership follows the controlled object, not the feature name. | vLLM/SGLang caching optimizes model computation; LangGraph checkpoints task graph state ([LangGraph](https://docs.langchain.com/oss/python/langgraph/persistence)). | Cross-source inference | A universal organizational/code ownership boundary. |

## 3 + 1 claims

| ID | Claim | Evidence | Type | Reopening condition |
|---|---|---|---|---|
| C1 | Finite resources can change Harness task policy; Cost is broader than money. | OpenAI exposes reasoning-effort and truncation controls that affect tokens/context/cache behavior ([Realtime API](https://platform.openai.com/docs/api-reference/realtime)); Portkey enforces token and monetary limits ([budget limits](https://portkey.ai/docs/product/ai-gateway/virtual-keys/budget-limits)). | Cross-source inference | A recurring task-level resource decision survives removal of scarcity or belongs solely to computation. |
| C2 | Execution-relevant semantic heterogeneity changes translation, negotiation or target policy. | MCP negotiates versions and capabilities ([lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)); A2A declares capabilities, modalities and security requirements ([A2A](https://a2a-protocol.org/latest/specification/)). | Cross-source inference | Homogeneous capabilities make Harness translation/selection immaterial across the domain. |
| C3 | Temporal dependence requires task-state and lifecycle semantics beyond storage alone. | LangGraph checkpoints, resumes, replays and forks state ([persistence](https://docs.langchain.com/oss/python/langgraph/persistence)); Temporal replays event history and records workflow state transitions ([Temporal](https://docs.temporal.io/workflow-execution)). | Cross-source inference | Runtime substrate alone determines task meaning, safe replay and completion semantics. |
| C4 | Cognition requires past evidence to change reusable future Harness policy. | Reflexion stores linguistic feedback for subsequent trials without weight updates ([paper](https://arxiv.org/abs/2303.11366)); DSPy compiles examples/metrics into changed prompts or program parameters ([paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f1cf02ce09757f57c3b93c0db83181e0-Abstract-Conference.html)); Voyager stores successful programs as reusable skills ([paper](https://arxiv.org/abs/2305.16291)). | Cross-source inference | That traces, scores or all software improvement are Cognition. |
| C5 | Cognition is a feedback plane, not a peer current-execution constraint. | DSPy separates metric-guided compilation from later program execution; Reflexion and Voyager reuse prior outcomes in later trials. | Falsification result | A uniform type rule admits all four as equivalent constraints without semantic loss. |

## Boundary-obligation claims

| ID | Claim | Evidence | Type | Reopening condition |
|---|---|---|---|---|
| B1 | Epistemic Access is independent: a model cannot use task-relevant current evidence it does not observe. | ReAct actions gather external information for later reasoning ([paper](https://arxiv.org/abs/2210.03629)); MemGPT moves information across memory tiers into bounded active context ([paper](https://arxiv.org/abs/2310.08560)); BrowserGym defines explicit observation/action spaces ([paper](https://arxiv.org/abs/2412.05467)). | Falsification result + cross-source inference | Evidence acquisition/relevance selection reduces fully to 3 + 1 without losing a decision. |
| B2 | Validity applies to evidence, candidates and observed postconditions, not only schemas. | OpenAI Agents SDK guardrails check workflow input, tool calls and final output ([guardrails](https://openai.github.io/openai-agents-python/guardrails/)); OSWorld uses execution-based evaluators over resulting computer state ([paper](https://arxiv.org/abs/2404.07972)). | Cross-source inference | Transport success or pre-action checking proves intended outcomes across changing environments. |
| B3 | Authority is independent from technical capability and correctness. | Claude Code separates permission rules from OS-level sandbox enforcement ([permissions](https://code.claude.com/docs/en/permissions), [sandbox](https://code.claude.com/docs/en/sandboxing)); Codex permission profiles define filesystem effect scope ([permissions](https://learn.chatgpt.com/docs/permissions)) and the local [enforcement reproduction](../experiments/codex_sandbox_authority.py) holds operation/capability fixed while changing target scope; Agents SDK pauses and resumes for tool approvals ([HITL](https://openai.github.io/openai-agents-python/human_in_the_loop/)); MCP binds tokens to intended audiences and forbids passthrough ([authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)). | Falsification result + cross-source inference + behavioral reproduction | Capability negotiation supplies sufficient delegation, consent, scope and revocation semantics. |
| B4 | Identity/provenance feed the three obligations rather than forming a fourth. | A2A separates authentication from implementation-specific authorization; MCP documents audience/confused-deputy requirements. | Falsification result | A recurring security decision survives fixed evidence authenticity, Validity and Authority. |

## Mediated transition-system claims

| ID | Claim | Evidence | Type | Reopening condition |
|---|---|---|---|---|
| T1 | Transition selection can come from model, code, human or event. | Agents SDK models emit calls while runner code handles handoffs/errors ([runner](https://openai.github.io/openai-agents-python/running_agents/)); HITL supplies human decisions; Temporal Signals/Updates and Inngest events change workflow state ([Temporal messages](https://docs.temporal.io/encyclopedia/workflow-message-passing), [Inngest](https://www.inngest.com/docs/learn/inngest-functions)). | Cross-source inference | A recurring selection source cannot be represented as a state/evidence/event input. |
| T2 | Mediation recurs at input, tool, state-update and output boundaries. | Agents SDK input/tool/output guardrails; Temporal validates Updates before acceptance. | Cross-source inference | A Harness boundary decision cannot be represented as Validity or Authority mediation. |
| T3 | The system can have concurrent in-flight transitions and late outcomes. | Inngest race losers can continue and active steps can complete after cancellation ([parallelism](https://www.inngest.com/docs/guides/step-parallelism), [cancellation](https://www.inngest.com/docs/features/inngest-functions/cancellation)); Temporal workflows execute concurrently and issue multiple commands. | Cross-source inference | Concurrency leaves an independent residual after Continuity, Validity and Authority are fixed. |
| T4 | Apply/dispatch does not prove the intended effect. | Browser/desktop benchmarks evaluate resulting functional state; Voyager consumes environment feedback, errors and self-verification. | Cross-source inference | Postcondition observation has negligible value once dispatch succeeds. |
| T5 | Self-modification is recursively representable as a mediated policy transition. | DSPy changes program parameters; Voyager versions reusable code skills; Claude hooks can alter runtime behavior ([hooks](https://code.claude.com/docs/en/hooks-guide)). | Falsification result | A policy change cannot be modeled as a versioned candidate artifact, or can legitimate its own root metric/authority. |

## Rejected peer candidates

| Candidate | Result | Primary mechanism evidence | Validation record |
|---|---|---|---|
| Reliability | Composite outcome; transport/replay recovery maps mainly to Continuity, semantic failure to Validity. | Temporal workflow/activity semantics; LangGraph fault tolerance. | [Decomposition](validation/reliability-decomposition.md) |
| Coordination | Multiplicity activates difference, shared temporal state, delegation and aggregation; no single residual. | Agents SDK handoffs; AutoGen teams; A2A task exchange. | [Attack](validation/coordination-attack.md) |
| Planning | Plan generation is Model/Application; execution decomposes across the system. | Agents SDK/Anthropic orchestration patterns. | [Attack](validation/planning-control-attack.md) |
| Generic Control | Functional role, not a cause. | Termination, guardrail, budget and permission mechanisms have different predicates. | [Attack](validation/planning-control-attack.md) |
| Grounding / Controllability | Compound of evidence, representation, Validity, Authority and recovery. | BrowserGym, WebArena, OSWorld, Voyager. | [Attack](validation/browser-embodied-attack.md) |
| Uncertainty | Deep background reality; current consequences decompose across boundary obligations and Continuity. | Browser/embodied outcome loops. | [Attack](validation/browser-embodied-attack.md) |
| Identity / Governance / Trust | Evidence, permission or broader process, not one transition question. | A2A and MCP security specifications. | [Attack](validation/multi-principal-security-attack.md) |

## Evidence limits

The current corpus is strong for documented mechanisms and counterfactual layer
reasoning. It is weaker in four ways:

1. most mappings are desk research rather than instrumented reproductions;
2. vendor documentation can describe intended behavior without proving efficacy;
3. absence of a new residual in the sampled systems does not prove universal
   completeness;
4. the counterfactual-removal test is adjudicated in prose by the same authors
   who defined the categories.

The fourth limit is the structural one and is worth stating plainly rather than
leaving for a hostile reader to notice. Every rejected peer candidate —
Reliability, Coordination, Planning, generic Control, Grounding, Uncertainty,
Identity — was rejected by decomposing it into categories this repository
already contains. A framework that could absorb anything would produce exactly
that record. Three defenses are available, and only the second is strong:

- The categories were fixed before the attacks, and each attack states its
  reopening condition in advance, so a later dispute is about evidence rather
  than definitions.
- The method has actually fired. Authority, Validity and Epistemic Access
  survived removal and **broke the original exhaustive claim**, which remains
  rejected in the canonical documents. A purely self-confirming procedure does
  not produce that outcome, and predictions P8 and P9 record their own
  falsification.
- Some rejections rest on primary sources rather than on the classification
  alone.

What is still missing is independent adjudication: no attack in this ledger was
authored or scored by someone with an interest in 4C failing. Until that
happens, treat the rejected-candidate table as this repository's best attempt at
self-refutation, not as a settled result. A counterexample from a reader
outranks any entry in it — see the [review guide](../REVIEW_GUIDE.md).

Experiment evidence carries a third label beyond documented/inferred: whether
the observed policy delta is produced by the upstream system or by locally
authored instrumentation. See [`experiments/README.md`](../experiments/README.md);
claims resting on an instrumented illustration are not independently
corroborated.

Those limits are why the theory includes explicit kill criteria and why future
case studies should record executable configurations, traces and failure cases.
