# Concept Inventory

This is a queue of important agent and harness concepts, not a list of 4C
successes. Initial mappings are hypotheses to attack.

| Concept | Provisional mapping | Pressure on 4C | Status |
|---|---|---|---|
| Tool use / function calling | Compatibility + Continuity + Authority | Schema/capability and lifecycle mechanics do not determine whether the action is permitted. | Decomposed; Authority residual |
| ReAct / agent loop | Model selection + Harness evidence/action cycle | Reasoning is Model behavior; action mediation, result return and trajectory state are Harness. | Decomposed from original paper |
| Structured output | Layer-dependent | Grammar decoding in SGLang/vLLM is Infrastructure; semantic acceptance in a task is Validity; provider/schema differences are Compatibility. | Decomposed |
| RAG | Epistemic access + Compatibility + Validity | Retrieval remains necessary in a free, one-shot, homogeneous system when required facts are not observed. | Provisional theory failure |
| Context engineering | Cost + Continuity + epistemic access | Capacity and history decompose, but evidence acquisition and selection do not reduce to 4C. | Provisional theory failure |
| Short- and long-term memory | Cost + Epistemic Access + Continuity; sometimes Cognition | MemGPT confirms that capacity, active evidence, persistence and learning use must be separated. | Decomposed from original paper |
| Durable execution / checkpointing | Continuity | Strong fit if Continuity includes control as well as state. | Provisional fit |
| Human-in-the-loop | Continuity | Approval is not only pause/resume; it enforces authority. | High-threat ambiguity |
| Multi-agent orchestration | Continuity + Compatibility + Authority + Validity | Multiplicity alone left no independent Coordination residual. | Decomposed |
| MCP and tool protocols | Compatibility | Protocols standardize exchange but do not settle trust or authorization. | Provisional fit |
| A2A agent protocol | Compatibility + Continuity + Authority | Discovery/modality/task exchange does not define parent-task Validity or legitimate delegation. | Decomposed from specification |
| Model routing / cascades | Cost + Compatibility + Cognition | Correctness- or risk-driven routing may not be economic. | Open |
| Guardrails | Validity and/or Authority; sometimes Cost | Must classify the predicate and boundary; “guardrail” is an enforcement mechanism, not one cause. | Decomposed |
| Sandboxing / permissioning | Unreduced residual | Changes executable actions because delegated actors are not fully trusted. | Provisional theory failure |
| Observability / tracing | Evidence substrate | A trace alone does not improve future execution; it can support Validity, Authority audit or Cognition. | Decomposed |
| Offline and online evals | Validity evidence; possible Cognition input | Scoring alone does not change execution; a later Harness policy delta is required for Cognition. | Decomposed |
| Reflection / self-critique | Layer- and horizon-dependent | Same-run reflection is inference plus Validity/Continuity; retained reflection changing later policy is Cognition. | Decomposed |
| Prompt optimization / teleprompting | Cognition | Clean only when evidence from past runs changes future execution. | Provisional fit |
| DSPy compilation / program optimization | Cognition + Validity + layer-dependent optimization | Prompt/program deltas are Harness feedback; weight deltas are Model training; the metric originates outside Cognition. | 3 + 1 asymmetry confirmed |
| Computer/browser use | Epistemic Access + Compatibility + Continuity + Validity + Authority | Grounding and controllability decompose; postcondition Validity is required because accepted actions do not guarantee effects. | Decomposed; uncertainty remains monitored |
| Skills / reusable procedures | Compatibility + Cognition | Static instructions may be packaging rather than cognition. | Open |
| Parallel agent work | Continuity + Compatibility + Authority + Validity | Shared state and merges do not establish a new Coordination primitive. | Provisional decomposition |
| Policy/configuration | Materialized Application or Harness policy | Artifact form does not identify the causal pressure or boundary obligation. | Rejected as peer primitive |
| Error/exception handling | Observation + cause-specific transition | Error classification and response decompose across Compatibility, Continuity, Cost, Validity and Authority. | Rejected as peer primitive |
| Embodied lifelong learning | Continuity + Cognition + boundary obligations | Voyager's environment feedback, self-verification and reusable skills fit the mediated loop and 3 + 1 structure. | Provisional fit |
| Event-driven/asynchronous execution | Continuity + boundary obligations | Events can select transitions; races, late results and cancellation require correlation, postcondition Validity and Authority-aware compensation. | Transition-system fit |
| Generative Agents | Observation + Continuity + Cognition; planning is Model/Application | Stored experience becomes Cognition only when synthesized reflection changes later behavior. | Decomposed from original paper |
| Toolformer / learned tool use | Model training + Harness execution boundary | Weight-trained tool selection is Model capability; dispatch, permission and result handling remain Harness. | Layer-boundary pass |
| MRKL / neuro-symbolic routing | Compatibility + Epistemic Access + Validity | Modularity and routing are mechanisms, not a new causal primitive. | Decomposed from original paper |

## Next concept tranche

The named original-source queue—ReAct, Reflexion, Generative Agents, MemGPT,
DSPy, Toolformer/MRKL, A2A and agent evaluation—has been covered. The next pass
should target concepts most likely to break the current structure rather than
collect synonyms:

- self-modifying tools, skills and policy;
- multi-principal delegation, revocation and provenance;
- real-time control with deadlines and continuously changing environments;
- confidential/tainted information flow across agents and tools;
- mechanisms practitioners treat as essential but current agent vocabulary
  obscures.
