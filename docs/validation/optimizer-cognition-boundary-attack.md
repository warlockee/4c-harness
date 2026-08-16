# Optimizer / Cognition Boundary Attack

Date: **2026-08-15**<br>
Status: **Cognition survives as a feedback dimension; peer-constraint symmetry fails**

## Threat

DSPy-style optimizers learn prompts, demonstrations, program parameters and
sometimes model weights against a supplied metric. This is the strongest case
for Cognition, but also exposes its weakest boundary:

- the metric is usually an Application success predicate;
- scoring is Validity evidence;
- prompt/program changes affect Harness policy;
- weight changes affect the Model;
- compilation often happens offline, outside live task execution.

If all software improvement from test results counts as Cognition, the category
is not Harness-specific. If offline optimization is excluded, an important
class of self-improving Harness mechanisms disappears.

## Primary evidence

DSPy represents language-model pipelines as parameterized computational graphs.
Its compiler collects or creates demonstrations and optimizes a pipeline to
maximize a supplied metric
([ICLR paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f1cf02ce09757f57c3b93c0db83181e0-Abstract-Conference.html)).
The project explicitly separates program flow from parameters and describes
optimizers that tune prompts and/or model weights against a metric
([Berkeley project](https://sky.cs.berkeley.edu/project/dspy/)).

This is not merely passive evaluation: an artifact used by future executions
changes as a result of accumulated examples and scores.

## Mechanism decomposition

``` text
Application metric + dataset
             │
             ▼
execute candidate program → trace/output → score (Validity evidence)
             ▲                              │
             └──── optimizer search ────────┘
                              │
                              ▼
             compiled prompt/program or weights
```

| Operation | Primary classification |
|---|---|
| Define what “better” means | Application intent / success predicate |
| Produce outputs and traces | Harness execution + evidence |
| Score an output | Validity evidence |
| Search candidate prompts/demonstrations | Cognition over Harness policy |
| Fine-tune weights | Model training, even if launched by the same optimizer |
| Select and deploy compiled program | Application release policy + Harness configuration |

The product or optimizer can span all rows. Layer ownership follows the object
being changed, not the process name “optimization.”

## The software-engineering objection

Ordinary software also improves after tests and production incidents. Therefore
“developers learned from experience” cannot by itself establish a distinct
Harness dimension.

The minimum Harness-specific Cognition mechanism is narrower:

1. evidence comes from executions of the model-driven policy;
2. an explicit adaptation operator uses that evidence;
3. the changed artifact controls future model-driven execution;
4. the delta is reusable beyond retrying the current proposal;
5. the claim names whether the changed object is Harness policy or Model
   weights.

Human insight alone is not **system Cognition**. A human may close the loop, but
then the platform supplies Cognition infrastructure rather than autonomously
performing adaptation. This is the same distinction already applied to
LangSmith and Braintrust.

## Symmetry failure

Cost, Compatibility and Continuity are exogenous conditions on execution:

- resources are bounded;
- execution targets differ;
- task semantics extend across bounded operations.

When activated, ignoring them can make an intended execution infeasible or
semantically broken. Cognition is different:

- historical evidence exists only after executions;
- a static Harness can ignore it and still execute correctly now;
- Cognition changes the policy that later encounters the other pressures and
  boundary obligations.

Thus Cognition passes the **causal policy-delta** test but not the stronger
**same kind of fundamental constraint** test.

## Competing formulations

### Flat four constraints

Rejected. It hides the exogenous/feedback asymmetry and invites every eval or
software change to be labelled Cognition.

### Four adaptation directions

Defensible but weak. It truthfully says policy can vary because of resources,
differences, time or experience, while saying little about their structure.

### 3 + 1 model

Current leader:

``` text
Operational pressure plane: Cost · Compatibility · Continuity
                              ▲
                              │ updates policy
Feedback learning plane:     Cognition
```

The three operational Cs shape execution under current conditions. Cognition
uses cross-run evidence to revise their policies, Observation strategy and
possibly mediation strategy. Validity supplies many learning signals but remains
distinct from the adaptation operator.

## Verdict

DSPy supports a real Harness Cognition mechanism when it compiles execution
evidence into prompts, demonstrations or program policy. It also proves that:

> **Cognition is not a fourth peer constraint. It is the feedback learning plane
> over Harness policy.**

The 4C name can survive as a `3 + 1` model. The claim that four items pass one
uniform fundamental-constraint type test cannot. Any canonical text that calls
them four equivalent or unavoidable constraints must be removed.
