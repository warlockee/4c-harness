# v0.2 Validation Ledger

Status: **v0.2 hostile validation and v1.0 promotion audit complete; revised
model passed, original exhaustive model rejected**

This directory is the audit trail for attempts to falsify 4C. Its purpose is
not to accumulate examples that can be labelled with four letters. Its purpose
is to find recurring harness problems that the four proposed constraints do
not explain without distortion.

**This is an archive, not a reading list.** Nothing here is required to use or
review 4C — the README and [theory sections 1–4](../theory.md) are the claim,
and the [glossary](../glossary.md) covers the vocabulary. Come here to check a
specific rejection, starting with the
[final falsification audit](v1-final-falsification-audit.md). Note also the
adjudication limit recorded in the [evidence matrix](../evidence.md#evidence-limits):
every rejection below was written by the same authors who defined the
categories.

## Research question

> Is there a fundamental constraint on model-driven execution that is not
> derived from finite resources, heterogeneity, time or experience?

## Decision rules

A mapping passes only when a C explains both:

1. why the mechanism must exist; and
2. how the constraint changes execution semantics.

Vocabulary overlap is not evidence. A mechanism may receive one of four
verdicts:

- **Clean fit:** an existing C explains its necessity and execution effect.
- **Cross-C:** multiple existing constraints are independently necessary.
- **Out of scope:** the mechanism principally belongs to model,
  infrastructure, application or governance rather than the harness. Correctly
  rejecting it is a boundary-control pass, not a failure of the theory.
- **Theory failure:** it is a recurring harness-level constraint that cannot be
  reduced to 4C without semantic contortion.

## Fifth-constraint admission test

A candidate must satisfy all five conditions:

1. It follows from an independent, durable fact about model-driven execution.
2. It recurs across providers, models and harness architectures.
3. It changes which actions may execute, or how execution proceeds.
4. It is not merely a desired outcome, quality attribute, mechanism or
   organization-wide concern.
5. Folding it into an existing C causes important and repeatable information
   loss.

Failure on one condition does not dismiss a candidate. It records what must be
shown next.

## Evidence discipline

Each entry separates:

- **Documented:** stated by a primary source.
- **Observed:** reproduced directly; none in the first desk-research tranche.
- **Inferred:** our interpretation of documented behavior.
- **Unknown:** evidence still required.

Product marketing claims establish implemented features, not their efficacy.
Scores are deliberately avoided during validation.

## Current work

- [v1.0 final falsification audit](v1-final-falsification-audit.md) — composed
  model audit; theoretical closure provisional, empirical closure still open

- [Concept inventory](concept-inventory.md)
- [System mappings, tranche 01](systems-tranche-01.md)
- [System mappings, tranche 02](systems-tranche-02.md)
- [Fifth-constraint hunt](fifth-constraint-hunt.md)
- [Authority attack](authority-attack.md)
- [Constraint-type audit](constraint-type-audit.md)
- [Correctness attack](correctness-attack.md)
- [Reliability decomposition](reliability-decomposition.md)
- [Coordination attack](coordination-attack.md)
- [Context attack](context-attack.md)
- [Planning and Control attack](planning-control-attack.md)
- [Cognition attack](cognition-attack.md)
- [Core Four symmetry audit](core-four-symmetry-audit.md)
- [Execution model attack](execution-model-attack.md)
- [Promotion gate audit](promotion-gate-audit.md)
- [Optimizer / Cognition boundary attack](optimizer-cognition-boundary-attack.md)
- [Browser / embodied environment attack](browser-embodied-attack.md)
- [Asynchronous / event-driven attack](async-event-attack.md)
- [Foundational agent concepts audit](foundational-concepts-audit.md)
- [Multi-principal security attack](multi-principal-security-attack.md)
- [Self-modification attack](self-modification-attack.md)
- [v0.2 working model](v0.2-working-model.md)

## Promotion gate

The revised model advanced through the v0.2 gate after:

- the named concept inventory was checked against original sources;
- the five requested system classes received two independently sourced
  mappings, with additional high-risk architectures tested;
- all high-threat candidates received adversarial write-ups and reopening
  conditions;
- failed original claims remained visible rather than becoming friendly
  mappings;
- the canonical theory gained an explicit classifier and kill criteria.

See the [promotion gate audit](promotion-gate-audit.md). v1.0 source hardening,
formal diagrams and empirical cases remain separate work; no launch decision has
been made.

## Revision log

### 2026-08-15 — Tranche 01

Established the protocol, mapped five boundary-spanning systems, opened the
concept inventory, and identified bounded authority as the first high-threat
candidate. The follow-up authority attack produced a **provisional theory
failure**: authority survived reduction against all four Cs. This is a finding
to reproduce and attack, not yet a settled revision.

The counterevidence pass then examined harnesses that execute configured tools
without per-call approval. These systems move the authority decision to tool
registration, credentials and runtime selection; they do not eliminate it. A
constraint-type audit found no principled type distinction that admits all four
Cs while excluding bounded authority. The exhaustive form of 4C remains broken.

A separate correctness attack found a second independent residual: a harmless,
fully authorized, perfectly compatible one-shot output can still be wrong. This
suggests that the problem is not merely a missing fifth label; the current
taxonomy may mix environmental pressures, temporal control and learning while
omitting execution-admission criteria.

The reliability decomposition found no third residual in transport failure,
workflow replay, idempotency or partial side effects. These mechanisms are
primarily Continuity semantics, with Validity deciding acceptance and Authority
deciding permission. Reliability remains an outcome and composite property, not
a demonstrated peer constraint.

The coordination attack likewise found no independent residual. Multi-agent
systems add actors, not a new causal primitive: protocol and capability
differences map to Compatibility; ordering, shared state and ownership transfer
map to Continuity; delegation maps to Authority; result aggregation maps to
Validity; task decomposition remains Application policy.

The context attack produced a third provisional residual: **epistemic access**.
In a free, homogeneous, authorized, one-shot task with no history, a model still
cannot use private or current information it has not observed. Retrieval and
context assembly change the model's evidence state before any Validity decision.
This directly triggers the published falsifier for Prediction P8.

Planning and generic Control did not produce additional residuals. Plan
generation belongs to model intelligence or Application policy; plan execution
maps across existing concerns. "Control" is a functional role whose instances
must be classified by cause, not a peer causal category. The canonical
Continuity definition now says **lifecycle control** to prevent it from absorbing
Validity or Authority by terminology.

The synthesis step withdraws the original completeness claim rather than
protecting it by definition. The later optimizer attack further revises 4C to a
`3 + 1` structure: three operational pressures plus a feedback learning plane.
Observation and mediation obligations are modeled separately and must survive
additional system mappings before this becomes a proposed canonical revision.

The Cognition symmetry attack retained Cognition only under a stricter test:
past-run evidence must cause a reusable change in future Harness policy.
Tracing alone is observability, current-run scoring is Validity, weight updates
are model training, and business analysis remains Application work. Cognition
is a feedback adaptation pressure rather than a fourth current-run stage.

The Core Four symmetry audit then applied the same counterfactual and layer
ownership burden to the original categories. All four survived only as
conditionally activated policy pressures. It replaced Cost's underlying
“money” claim with resource scarcity and excluded generic protocol plumbing,
persistence substrates and model training from the corresponding Cs.

The execution-model attack falsified the one-pass
`Observe → Model Proposal → Admission → Commit` diagram. Admission can occur at
input, tool and output boundaries; observation recurs; and code or humans can
select transitions. The surviving model is a mediated transition loop over
state and evidence.

The DSPy optimizer attack then broke the remaining symmetry claim. Cognition is
a real cross-run adaptation mechanism when evidence changes prompts, retrieval,
routing or other future Harness policy, but it is not the same type as the three
exogenous operational pressures. The current structural candidate is therefore
`3 + 1`: Cost/Compatibility/Continuity as the operational pressure plane and
Cognition as its feedback learning plane.
