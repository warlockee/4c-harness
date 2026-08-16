# v0.2 Promotion Gate Audit

Date: **2026-08-15**<br>
Status: **v0.2 gate passed for the revised model; original model rejected**

## Standard

“Bullet proof” cannot mean impossible to falsify. For this phase it means:

1. every canonical claim has a named falsifier;
2. original categories and rival candidates face symmetric tests;
3. layer and execution-unit boundaries survive heterogeneous systems;
4. major concept families are checked against primary sources;
5. known counterexamples are incorporated, not hidden in validation notes;
6. remaining uncertainty is explicit enough for an outsider to reproduce.

## Requirement matrix

| Requirement | Evidence | Status | Gap |
|---|---|---|---|
| Define Harness unit and neighboring layers | Theory; system tranches; embodied, async, multi-principal and self-modification attacks | Pass for v0.2 | Continue empirical reproduction in v1 case studies. |
| Apply a symmetric burden to all four Cs | Core-Four, Cognition and optimizer attacks | Pass | Result forced 3 + 1 rather than false type symmetry. |
| Search for independent residuals | Authority, Correctness and Context attacks | Pass | Stable names: Epistemic Access, Validity, Authority. |
| Eliminate attractive false peers | Reliability, Coordination, Planning, Control, Grounding, Uncertainty, Identity and Governance attacks | Pass provisionally | Every rejection has a reopening condition. |
| Cover the five requested system classes twice | Tranches 01–02 | Pass | See replication matrix below. |
| Attack the execution structure | Execution-model, embodied, async and self-modification attacks; tranche 02 | Pass for v0.2 | Serial loop was replaced by a concurrent, recursively closed mediated transition system. |
| Complete named important-concept tranche | Concept inventory; optimizer and foundational-concepts audits | Pass for queued set | Continue counterexample-driven search; historical exhaustiveness is unprovable. |
| State revision/abandonment criteria | Theory classification procedure and six kill criteria; prediction falsifiers | Pass | Apply them in every future tranche. |
| Keep canonical docs consistent | README, theory, landscape, case studies, counterarguments and predictions | Pass | Automated stale-claim scan, link validation and diff check pass. |
| Produce formal diagrams and sourced cases | Deferred to v1.0 by phase plan | Not required for v0.2 | Must not be used to claim current validation completeness. |

## Requested system-class replication

| Class | First system | Second system | Result |
|---|---|---|---|
| Inference infrastructure | vLLM | SGLang serving runtime | Boundary-control replicated; SGLang also exposes a separate frontend surface. |
| Gateway | LiteLLM | Portkey | Cost/Compatibility plus limited Continuity; Portkey also mediates request/response policy. |
| Agent runtime / harness | LangGraph | OpenAI Agents SDK | Durable substrate separated from task transition and mediation semantics. |
| Coding harness | Codex | Claude Code | Authority residual independently replicated. |
| Eval platform | LangSmith | Braintrust | Evidence/Validity separated from actual cross-run Cognition. |

This satisfies the explicitly requested representative-system sweep. Additional
archetypes were attacked through DSPy, Reflexion, Voyager, BrowserGym/WebArena,
OSWorld, Inngest, Temporal, A2A, MCP, Toolformer, MRKL and Generative Agents.

## Highest-risk architecture results

### Optimizing/self-improving harnesses — tested provisionally

DSPy-style prompt/program optimization and systems that rewrite their own
skills or policies can blur Cognition, Validity, Application goals and model
training. DSPy, Reflexion and Voyager replicate cross-run policy/skill updates;
Claude Code hooks provide a separate policy-control mechanism. The
self-modification attack found recursive closure by treating policy deltas as
mediated transitions with an external root predicate/authority.

### Browser and embodied agents — tested provisionally

BrowserGym, WebArena, OSWorld and Voyager forced postcondition Validity and
freshness/provenance into the model. Grounding and controllability decomposed;
Uncertainty remains a named reopening condition rather than a new primitive.

### Event-driven/asynchronous agents — tested provisionally

Inngest events, races, late completion and cancellation falsified a serial-loop
reading but fit a concurrent mediated transition system. Temporal independently
replicated concurrent workflow state, external messages, validated updates and
event-history replay. This risk is closed provisionally.

### Multi-principal systems — tested provisionally

A2A and MCP identity, delegation, audience and confused-deputy mechanisms did
not produce a fourth boundary obligation. Identity/provenance feed Epistemic
Access and Validity; disclosure/delegation remain Authority. Derived/tainted
information flow remains a reopening condition.

## Current theory status

### Supported

- 4C works as a `3 + 1` causal model: scarcity, heterogeneity and temporal
  extension pressure current execution; experience can update future policy.
- A mechanism belongs to a layer according to the object and semantics it
  controls, not its product name or feature vocabulary.
- Observation/Epistemic Access, Validity and Authority cannot currently be
  reduced to 4C.
- The execution structure is a concurrent, recursively closed mediated
  transition system, not a linear or model-only loop.

### Not supported

- that four constraints exhaust Harness engineering;
- that every Harness activates every C;
- that every caching, adapter, persistence or evaluation feature belongs to the
  Harness;
- that a vendor product occupies exactly one layer;
- that passing ten desk-research mappings proves completeness.

## Promotion decision

**Pass the revised model through the v0.2 validation gate. Reject the original
model permanently.**

The following formulation survived the planned hostile tests:

1. `3 + 1`: Cost/resource scarcity, Compatibility/semantic heterogeneity and
   Continuity/temporal dependence form the operational plane; Cognition is the
   cross-run feedback plane.
2. Epistemic Access, Validity and Authority are separate boundary obligations,
   not hidden Cs.
3. Harness execution is a concurrent mediated transition system over state,
   evidence and events, recursively closed over policy changes.
4. Layer ownership follows the controlled object and causal decision, not
   feature or vendor names.

This is permission to enter the planned v1.0 phase—primary-source hardening,
formal diagrams and deeper empirical case studies—not permission to launch or
restore the exhaustive slogan. Any future kill-criterion hit reopens v0.2.
