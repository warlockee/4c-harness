# Self-Modification Attack

Date: **2026-08-15**<br>
Status: **transition system is recursively closed; root-policy boundary required**

## Threat

A Harness may generate or alter prompts, retrieval rules, routes, skills, tool
code, validators or permission policy. If policy is merely an input to the
execution model, self-modification can appear to stand outside it. Worse, a
system that evaluates and authorizes its own evaluator/authority rules creates
an infinite regress or silently grants itself power.

Candidate missing primitives include Self-Reference, Meta-Control and
Governance.

## Evidence cases

DSPy compiles execution examples and metric scores into changed prompts,
demonstrations or model weights
([paper](https://arxiv.org/abs/2310.03714)). Voyager generates executable code,
improves it from environment feedback and stores successful programs in a skill
library for later tasks
([paper](https://arxiv.org/abs/2305.16291)). Claude Code hooks can deterministically
block or alter behavior at lifecycle boundaries
([hooks](https://code.claude.com/docs/en/hooks-guide)).

Together these cover offline policy optimization, generated reusable tools and
runtime policy hooks.

## Treat policy changes as transitions

The mediated transition system is recursively closed if a policy artifact is
ordinary versioned state and changing it is itself a candidate transition:

``` text
execution evidence
       ↓
candidate policy/tool/skill delta
       ↓
meta-Validity + meta-Authority
       ↓
version / apply / deploy / rollback
       ↓
future execution policy
```

No new operation is required. The object being applied differs, but selection,
mediation, application and observed outcomes remain.

## Object-by-object boundary test

| Changed object | Classification |
|---|---|
| Prompt, demonstrations, retrieval/routing/tool policy | Harness policy; Cognition if prior evidence drives reusable change |
| Skill/tool code used only in the current task | Candidate artifact; Validity + Authority + Continuity, not necessarily Cognition |
| Reusable generated skill/tool | Harness policy/capability; Cognition when retained from evaluated experience |
| Success predicate or business goal | Application policy; Harness may propose but cannot unilaterally legitimate it |
| Permission/approval policy | Authority policy; requires authority at a higher or external trust boundary |
| Model weights | Model/training layer |
| Kernel, scheduler or device configuration | Infrastructure |

“The system improved itself” is therefore too coarse. The changed object and
the principal allowed to change it must be named.

## Validator self-modification

Suppose an optimizer raises its own score by weakening the validator. This is
not successful Cognition under the task's original semantics:

- the score is evidence, not the success predicate itself;
- changing the predicate is a separate candidate policy transition;
- meta-Validity asks whether that delta preserves the Application objective;
- meta-Authority asks whether the optimizer may change the predicate;
- versioning, comparison and rollback are Continuity;
- evaluation of later behavior supplies new evidence.

The theory therefore predicts reward hacking whenever a learner can modify its
metric without an external invariant. Cognition cannot define its own legitimacy.

## Permission self-modification

An agent that can rewrite the rule authorizing that rewrite collapses the
Authority boundary. A stable design needs a root policy or principal outside the
candidate's delegated authority. That root can authorize bounded policy updates,
but the fact that it exists is not a new Harness primitive; it is the termination
condition of delegated Authority.

There is no infinite regress in an implemented system because some policy is
treated as externally fixed for the execution under analysis. If nothing is
fixed, “authorized” has no determinate meaning and the Application/Harness
contract is undefined.

## Does Governance become a fourth obligation?

Governance includes organizational ownership, review, compliance, audit,
deployment and rollback. Its Harness-level decisions decompose into:

- who may change which policy → Authority;
- whether the change preserves objectives/invariants → Validity;
- what evidence supports the change → Epistemic Access;
- how versions, rollout and rollback evolve → Continuity;
- how experience proposes improvements → Cognition.

**Verdict: Governance is a broader process, not one additional transition
question.** This conclusion is scoped to Harness execution, not a claim that
organizational governance is unimportant.

## Reflexivity verdict

Self-reference changes the level at which the existing questions are asked, not
their causal kind. A policy update can itself be modeled as an execution with a
named intent, evidence, candidate delta, mediation and applied outcome.

**No new primitive is admitted.** The current model gains two mandatory rules:

1. policy, validator, skill and permission changes are first-class mediated
   transitions, not invisible configuration writes;
2. the root success/authority policy for an execution cannot be justified solely
   by the candidate it governs.

## Falsifier

Reopen Self-Reference or Meta-Control if a recurring Harness self-modification
operation cannot be represented as a mediated transition over a versioned
artifact, or if a system can establish the legitimacy of its own root predicate
and authority without relying on any external invariant or principal.
