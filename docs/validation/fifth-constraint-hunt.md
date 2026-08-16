# Fifth-Constraint Hunt

This file ranks threats to 4C by their chance of revealing a missing
fundamental constraint. The burden is symmetric: candidates must not be waved
away to protect 4C, and they must not be promoted merely because they matter.

## Threat register

| Candidate | Independent reality | Current threat | Main objection |
|---|---|---:|---|
| Bounded authority / consequence | Delegated model actions can affect the world while the actor is not fully trusted. | Critical | May be an invariant over execution rather than a peer optimization coordinate. |
| Coordination | Multiple actors have partial state, goals and control. | Low | Decomposes into Compatibility, Continuity, Authority, Validity and application policy. |
| Current-run validity | Model-driven outputs can be wrong despite technical validity and authorization. | Critical | Success predicates originate in the Application even when the Harness enforces them. |
| Reliability | Executions encounter transient failures, replay and partial effects. | Low | Decomposes into causes plus Continuity recovery; remains an outcome. |
| Epistemic access / Context | Models act only on bounded observations and representations of the world. | Critical | May be model/application information architecture rather than a Harness constraint. |
| Control | Open-ended execution requires steering and termination. | Rejected | Functional role, not one cause; decomposes by what is controlled and why. |
| Planning | Long-horizon tasks require decomposition and revision. | Rejected | Plan generation is model/Application; plan lifecycle decomposes across existing concerns. |
| Uncertainty / controllability | Observations, proposals and world effects can diverge from reality or intent. | Medium | Decomposes into Epistemic Access, pre/post Validity, Authority and Continuity; reopen on an unreduced decision. |

## Candidate A: bounded authority / consequence

### Strongest case

The independent reality is not simply that systems are heterogeneous or tasks
take time. It is:

> A harness delegates consequential actions to a probabilistic actor whose
> authority must be bounded and whose proposed actions may require mediation.

This reality produces recurring harness mechanisms:

- sandboxing and isolation;
- least-privilege tool access and credential separation;
- allow, deny and network policies;
- approval gates based on action risk;
- provenance and audit trails;
- rollback or compensation for side effects;
- taint and prompt-injection boundaries.

These mechanisms change the executable action set, not merely cost, provider
translation, persistence or learning. OpenAI's Codex documentation explicitly
separates the sandbox's technical boundary from approval policy for crossing
that boundary ([source](https://openai.com/index/running-codex-safely/)). MCP's
architecture also assigns security and consent responsibilities to the host,
which coordinates clients and integrations
([source](https://modelcontextprotocol.io/docs/learn/architecture)).

### Strongest case against

Security and authority apply to applications, infrastructure and organizations
as well as harnesses. They may be invariants imposed on every C rather than a
peer coordinate. Compatibility can describe tool capabilities and identity;
Continuity can describe approvals, rollback and audit history; Cognition can
adapt risk policy. A fifth category might therefore classify a desired property
rather than a distinct execution constraint.

### Why the existing rebuttal is insufficient

Saying safety is "cross-cutting" establishes scope but does not explain the
harness-specific residual. Cost and Cognition are also cross-cutting in
implementation. The relevant question is whether delegated authority creates
irreducible execution semantics inside the harness. That remains open.

### Discriminating tests

1. Remove Cost pressure, provider heterogeneity, long-lived state and learning
   from a one-shot tool-using harness. Do sandbox and approval semantics remain
   necessary? If yes, the candidate has independence evidence.
2. Compare human approval used only to provide missing information with approval
   required to authorize an already-specified destructive action. If 4C maps
   both identically to Continuity, measure what explanatory information is lost.
3. Survey coding, browser, robotics and financial agents for the same mechanism
   family across otherwise unrelated architectures.
4. Attempt a precise derivation from each existing C. Reject verbal association;
   require the derivation to predict concrete execution policy.

### Current verdict

**Provisional theory failure.** The dedicated
[authority attack](authority-attack.md) found a harness-level residual after
counterfactually removing each of the four Cs. It has not yet earned permanent
fifth-constraint status because the strongest rival model—authority as an
invariant over execution rather than a peer coordinate—still requires testing.

## Candidate B: coordination

Multiple agents introduce scheduling, delegation, communication topology,
shared-resource arbitration and conflict resolution. The strongest independent
reality would be that concurrently acting entities possess partial and possibly
conflicting views.

Current assessment: most mechanisms are derivable from Compatibility (different
actors and protocols) and Continuity (joint state and control across time). Goal
conflict often belongs to application policy. The dedicated
[coordination attack](coordination-attack.md) additionally maps delegation to
Authority and aggregation to Validity.

**Current verdict: rejected as a fundamental peer constraint.** In the minimal
homogeneous case, independent workers require no coordination; adding shared
state or ownership reintroduces temporal control. Multiplicity is an
architecture pattern that activates existing constraints rather than a new
underlying reality.

## Candidate C: current-run validity

Non-determinism, model error, tool failure and uncertain world state make
correct execution difficult. The dedicated
[correctness attack](correctness-attack.md) identifies accept, reject, retry and
escalate policy in a read-only, fully authorized, free, homogeneous, one-shot,
no-history execution. It therefore survives removal of both 4C and authority.

**Current verdict: provisional theory failure.** The strongest remaining
objection is ownership: task-specific truth conditions may belong to the
Application even when the Harness implements generic validation and recovery.
The same objection must be applied symmetrically to Cognition's evaluators.

## Reliability decomposition

The [reliability decomposition](reliability-decomposition.md) tested transport
failure, workflow nondeterminism, idempotency and partial side effects. No new
fundamental residual appeared. Transient failure and replay are temporal control
problems; idempotency and compensation preserve task semantics across retry and
resume. Validity and Authority supply separate acceptance predicates where
needed.

Current assessment: **Reliability is an outcome/composite, not a fifth
constraint.** This does not weaken the narrower current-run validity candidate.

## Candidate D: epistemic access / Context

The [context attack](context-attack.md) uses a free, homogeneous, one-shot,
no-history task whose answer depends on a private current fact. Even with perfect
interfaces and unlimited context capacity, the Harness must discover, retrieve
and expose the fact before the model can use it.

**Current verdict: provisional theory failure.** Context-window capacity and
long-run compaction still map to Cost and Continuity, but information access and
relevance selection leave a residual. Calling all retrieval Compatibility
confuses making a source callable with deciding what evidence enters inference.

## Planning and Control

The [Planning and Control attack](planning-control-attack.md) found no new
independent residual.

- Planning is an artifact or strategy. Creating it is model intelligence or
  Application policy; persisting and executing it is primarily Continuity;
  revising it uses Observation and Validity.
- Control describes what a mechanism does, not why it is required. Budget,
  capability, lifecycle, evidence, validity and permission control have distinct
  causal mappings.

**Current verdict: both rejected as fundamental peer constraints.** This does
not fold Authority into Continuity; it narrows Continuity's "control" to
lifecycle/temporal control.

## Uncertainty and environment controllability

The [browser/embodied attack](browser-embodied-attack.md) tested BrowserGym,
WebArena, OSWorld and Voyager. It found that an accepted action does not prove
its intended effect: postcondition observation and Validity are distinct from
pre-action checks.

**Current verdict: provisionally rejected as one peer primitive.** Uncertainty
is a deep reality, but its consequences currently separate into what can be
observed, whether a candidate or outcome is valid, whether an effect is
permitted, and how execution recovers over time. Reopen if that decomposition
loses a recurring execution decision.

## Kill criteria for the current theory

4C should be revised, even at the cost of the name, if the authority candidate
passes the admission test across multiple action domains. 4C should be narrowed
rather than expanded if it only explains resource, integration, temporal and
learning behavior while systematically excluding action governance from the
definition of a harness.
