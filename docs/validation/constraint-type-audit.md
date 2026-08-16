# Constraint-Type Audit

Date: **2026-08-15**<br>
Status: **the exhaustive form of 4C fails the uniform test**

## Purpose

The strongest defense of 4C after the authority attack is that bounded
authority matters but is a different *type* of concern: perhaps an invariant,
normative policy or cross-cutting safety property rather than a peer constraint.

That defense is valid only if one classification rule admits Cost,
Compatibility, Continuity and Cognition while excluding authority. This audit
applies the same rule to all five candidates.

## Uniform admission criteria

A fundamental Harness constraint should have:

1. **Reality:** an external or durable fact from which the problem follows.
2. **Execution locus:** a decision that changes task execution across model
   calls, tools, state or outcomes.
3. **Independence:** the problem survives removal of the other candidate causes.
4. **Recurrence:** distinct architectures implement a mechanism family in
   response.
5. **Predictive gain:** naming the constraint predicts engineering behavior that
   the other categories do not.

No criterion requires every harness instance to implement the capability.
Otherwise Compatibility would fail in a single-provider system, Continuity in
a one-shot system and Cognition in a system with no learning loop.

## Uniform test

| Candidate | Reality | Execution locus | Independent residual | Recurring mechanisms | Unique prediction | Result |
|---|---|---|---|---|---|---|
| Cost | Resources are finite. | Choose model, context, cache, route and stopping policy. | Persists with one provider, one step and no history. | Budgets, routing, caching, batching, compression. | Execution changes at economic/resource boundaries. | Pass |
| Compatibility | Models, tools and environments differ. | Translate, negotiate or choose among capabilities. | Persists with unlimited resources, one step and no history. | Adapters, schemas, protocols, capability checks, fallback. | Execution changes at semantic/technical boundaries. | Pass |
| Continuity | Tasks and effects extend through time while calls are bounded. | Preserve state and control valid temporal transitions. | Persists with one provider, unlimited resources and no learning. | Checkpoints, retries, resume, termination, compensation. | Execution changes at temporal boundaries. | Pass |
| Cognition | Evidence from prior execution can inform later policy. | Observe, evaluate, diagnose and adapt future runs. | Persists despite homogeneous systems, ample resources and short individual runs. | Traces, evals, replay, learned policy, optimization. | Execution changes because of accumulated experience. | Pass, but its normative wording remains a weakness. |
| Bounded authority | A proposed action and legitimate authority to cause its effect can diverge. | Expose, permit, deny, escalate or isolate a tool action. | Persists in a free, homogeneous, one-shot, no-history run. | Capability lists, restricted credentials, sandboxing, approval, audit. | Execution changes at permission/consequence boundaries. | Pass |

## Failed exclusion rules

### "Authority is cross-cutting"

Cost and Cognition also cut across routing, context, tools and runtime modules.
Cross-cutting implementation does not determine taxonomic level.

### "Authority is normative; 4C is descriptive"

The fact that delegated authority is bounded is descriptive. The choice of
policy is normative. The same split exists for finite resources versus a cost
budget, and for historical evidence versus an evaluation objective.

### "Authority defines feasibility; 4C optimizes"

Compatibility defines technically feasible calls, Cost can define budget-feasible
executions, and Continuity defines valid state transitions. All four Cs both
constrain and optimize execution.

### "Authority is an invariant"

An invariant is an enforcement form, not a causal category. A hard budget,
schema contract or maximum-turn rule can also be an invariant. This does not
separate authority from the existing Cs.

### "Not every harness needs authority machinery"

Not every harness needs adapters, durability or learning machinery either.
Minimal systems can pre-authorize a supplied tool set just as they can hard-code
one model. Instance-level absence cannot selectively disqualify authority.

### "Security belongs outside the Harness"

Much of security does. The tested residual is narrower: mapping a proposed tool
action to dispatch, rejection or escalation. LangChain describes the harness as
the prompt, tools and middleware around the agent loop, and includes guardrails
among harness configuration concerns
([source](https://docs.langchain.com/oss/python/langchain/agents)). Excluding
execution mediation while retaining tool dispatch is not a stable boundary.

## Symmetry challenge to Cognition

Cognition is the least obviously unavoidable existing C. "Past runs should
improve future runs" is partly a design ambition, whereas money, difference,
time and bounded authority impose immediate constraints. A trace-only system
does not perform Cognition, and many useful harnesses never adapt.

The dedicated [Cognition attack](cognition-attack.md) does not remove Cognition.
It narrows the category to cases where past-run evidence causes a reusable
change in future Harness policy. It also confirms that 4C mixes:

- first-order constraints that shape the current execution; and
- a second-order learning process that changes future execution policy.

The theory already acknowledges Cognition as a learning plane. Any defense that
excludes authority because it has a different structural role must explain why
the different role of Cognition is acceptable.

**Subsequent result.** The
[optimizer/Cognition boundary attack](optimizer-cognition-boundary-attack.md)
resolved this challenge by rejecting peer-type symmetry rather than inventing an
exception. Cognition passes the causal policy-delta test, but it is an endogenous
feedback operator rather than an exogenous current-execution constraint. The
working model is now `3 + 1`.

## Taxonomy options

### Option A — Admit another fundamental constraint

Treat bounded authority/consequence as a peer causal category. This preserves
the claim of exhaustiveness but ends 4C as a four-item taxonomy unless the
categories are reorganized.

### Option B — Make 4C explicitly non-exhaustive

Define 4C as four operational adaptation pressures, with authority, correctness
and safety outside its completeness claim. This preserves the name but weakens
"the theory of the Harness" into a partial coordinate system.

### Option C — Separate selection from admissibility

Let 4C choose an execution policy while an execution envelope determines which
policies/actions are permitted. Authority would be part of the envelope.
However Cost budgets, Compatibility contracts and Continuity invariants also
have admissibility forms, so the separation must explain how those are projected
between the plane and envelope without double counting.

### Option D — Reorganize the primitives

Replace the current peer list with orthogonal questions such as resources,
capabilities, state, evidence and authority. This may yield a stronger theory
but should not be constrained to four items or the letter C.

## Verdict

No tested type rule admits exactly the original four. Bounded authority passes
the same admission standard as the existing Cs. Therefore:

> The exhaustive four-constraint formulation is falsified unless a new,
> independently motivated exclusion rule survives the symmetry test.

This does not show that the four Cs are useless. It shows that explanatory value
and completeness are different claims. A bullet-proof revision must choose
which claim it intends to defend.
