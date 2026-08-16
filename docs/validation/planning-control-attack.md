# Planning and Control Attack

Date checked: **2026-08-15**<br>
Status: **both rejected as independent peer constraints**

## Why test them together

Planning and Control are prominent agent concepts and tempting missing Cs.
Planning appears to determine future execution; Control appears to govern the
loop itself. Both terms are also broad enough to classify almost anything, so
they need causal rather than feature-level tests.

## Primary-source observations

### OpenAI Agents SDK

The Agents SDK distinguishes LLM-directed orchestration—where model intelligence
plans and chooses steps—from code-directed orchestration that sequences, loops,
parallelizes and evaluates agents
([orchestration](https://openai.github.io/openai-agents-python/multi_agent/)).
Its runner ends on final output, changes agents on handoff, executes tool calls
and raises after a configured maximum number of turns
([running agents](https://openai.github.io/openai-agents-python/running_agents/)).

### AutoGen

AutoGen exposes stateful termination predicates for message counts, token use,
timeouts, handoffs, external stop requests and message content
([termination](https://microsoft.github.io/autogen/0.4.8/user-guide/agentchat-user-guide/tutorial/termination.html)).

### Anthropic

Anthropic's agent patterns distinguish prompt chaining, routing, parallelization,
orchestrator-workers and evaluator-optimizer workflows. The orchestrator
dynamically breaks down tasks and delegates them, while evaluator loops use
defined criteria to decide whether to continue
([building effective agents](https://www.anthropic.com/engineering/building-effective-agents)).

These sources show that planning and control mechanisms are real. The question
is whether they share an independent causal reality.

## Planning attack

### Candidate claim

Complex goals require decomposition, ordering, dependency tracking and revision.
Perhaps this is a fundamental constraint distinct from time, information and
validity.

### Layer split

"Planning" can name four different things:

| Meaning | Primary owner | Mapping |
|---|---|---|
| Decide which goal to pursue | Application | Product/task policy |
| Generate a candidate sequence or decomposition | Model | Intelligence/reasoning |
| Store, schedule, branch and resume plan steps | Harness | Continuity |
| Revise a plan after new evidence or failure | Model + Harness | Observation + Validity + Continuity |

The Harness can also generate deterministic workflow graphs, but then the plan
is program/application logic compiled into runtime control.

### Minimal counterfactual

Give a model a complex but one-shot reasoning problem and ask it to return a
plan as text. No tool or step is executed. Planning may occur entirely inside
the model's forward pass. A Harness taxonomy should not claim that model
reasoning merely because the output is called a plan.

Now execute the plan across tools. Each added Harness obligation has another
cause:

- discover current state and evidence → Epistemic access;
- choose compatible tools → Compatibility;
- fit execution within resources → Cost;
- persist dependencies, branches and progress → Continuity;
- determine whether a step or goal is satisfied → Validity;
- determine whether an action may run → Authority;
- improve planning policy from prior runs → Cognition.

Remove these relations and only a model-produced plan artifact remains.

### Planning verdict

Planning does not pass the execution-locus and independence tests. It is an
important model capability, Application policy or cross-constraint Harness
mechanism, not a fundamental peer constraint.

## Control attack

### Candidate claim

Open-ended model execution must be steered, bounded and stopped. Since every
Harness has some loop or dispatch policy, perhaps Control is the missing
fundamental constraint.

### The causal decomposition

"Control" describes the role of selecting or blocking transitions. It does not
state why a transition changes:

| Control form | Causal question | Mapping |
|---|---|---|
| Resource control | Can the execution spend more? | Cost |
| Capability control | Can this target express the requested operation? | Compatibility |
| Lifecycle/flow control | Which temporal state and attempt comes next? | Continuity |
| Adaptive control | What should change because of prior outcomes? | Cognition |
| Evidence/context control | What can the model observe now? | Epistemic access |
| Validity control | Is this proposal acceptable for the task? | Validity |
| Authority control | Is this proposal permitted to cause its effect? | Authority |

Termination conditions illustrate the decomposition. A token limit is Cost; a
timeout or max-turn boundary is Continuity, though it may also enforce Cost; a
task-complete predicate is Validity; a human stop/revoke decision is Authority
plus Continuity transport.

### Why generic Control fails

If Control means every mechanism that affects execution, then all existing Cs
become subtypes of Control and the category has no discriminating power. If it
means loop/state control, it is precisely the temporal part of Continuity. If it
means permission, it renames Authority without explaining Validity or flow.

### Control verdict

Control is a functional role, not a single fundamental cause. It should modify a
noun—resource control, lifecycle control, admission control—rather than appear as
a peer category.

## Implication for Continuity

The original theory said Continuity contained "State" and "Control." That
wording invited the defense that Authority and Validity were already included.
Such a defense would make Continuity unfalsifiable.

Continuity is therefore narrowed to:

> persistence plus **lifecycle control** across temporal boundaries.

It owns retry, timeout, branching, pause/resume, checkpoint, rollback and
recovery mechanics. It does not own every predicate that causes one of those
transitions.

For example:

- Validity may cause a retry; Continuity carries out the retry.
- Authority may cause an interruption; Continuity persists and resumes it.
- Cost may cause termination; Continuity ends the run consistently.

Cause and transition machinery must remain distinct.

## Verdict

Neither candidate produces a new residual:

- **Planning:** rejected as a peer constraint; it crosses model, Application and
  several Harness concerns.
- **Control:** rejected as a causal category; it is a generic functional role.

This completes the initial named-candidate sweep. It does not restore 4C:
Epistemic Access, Validity and Authority remain unreduced, while Reliability,
Coordination, Planning and generic Control have been eliminated as peer
constraints.
