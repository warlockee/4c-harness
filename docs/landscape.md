# 4C Harness Landscape

4C can describe the **shape** of an execution system without forcing
every product into one category.

## Archetypes are test fixtures, not scores

| Archetype | Common operational pressure | Possible feedback role | Boundary question it does not answer by name |
|---|---|---|---|
| API adapter | Compatibility | Learned translation policy | Is the exposed evidence valid and the operation authorized? |
| Model gateway | Cost + Compatibility; attempt-level Continuity | Learned routing | Does the result satisfy the task? |
| Optimizer | Cost during search; target/model Compatibility | Cognition when evidence changes Harness policy | Who defines the metric and may deploy the delta? |
| Agent framework | Compatibility + Continuity | Optional policy learning | What evidence, acceptance predicate and authority apply? |
| Durable runtime | Continuity; sometimes Cost | Replay evidence only unless policy changes | What does state mean for the model-driven task? |
| Observability/eval platform | None required merely to record/score | Cognition infrastructure | Does a score mediate execution or alter future policy? |
| Coding/browser Harness | All three can activate | Cognition if experience is reused | Are observations fresh, actions permitted and outcomes valid? |
| Self-improving Harness | Operational plane depends on task | Strong Cognition | May the system modify the metric, skill or permission policy? |

These rows predict questions to ask, not maturity or product quality. A product
may implement several archetypes, and an archetype need not activate every
listed dimension.

## Inference infrastructure vs. Harness

Low-level inference systems primarily optimize **computation**.
Harnesses optimize **task execution across model calls**.

A cache inside an inference engine and a cache policy inside a harness
may share a name while operating at different abstraction layers.

The useful question is:

> **What object is being optimized: computation or execution?**

The mapping unit is a **mechanism or decision**, not a vendor product. A single
system can contain a serving runtime that optimizes computation and a frontend
that orchestrates task execution. Before mapping, name the execution unit—for
example a model request, user task, evaluation run or deployment decision.

## Evidence-based mapping template

For every real system, document:

1.  name the execution unit;
2.  identify each mechanism/decision rather than assigning the whole product;
3.  state the controlled object: computation, task execution or user value;
4.  state the counterfactual policy delta;
5.  classify Cost, Compatibility and Continuity only when causally activated;
6.  classify Cognition only when prior evidence changes reusable future policy;
7.  map evidence source/freshness/provenance;
8.  map precondition, candidate and postcondition Validity;
9.  map principal, delegation, scope, audience and Authority;
10. separate documented, observed, inferred and unknown claims.

Use the [validation ledger](validation/README.md) for sourced mappings. Universal
product scores are intentionally excluded: the optional [4C Fit
Score](harness-scout.md#21-the-4c-fit-score) belongs to a locked task terrain,
not to this mechanism landscape.
