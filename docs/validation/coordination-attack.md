# Coordination Attack

Date checked: **2026-08-15**<br>
Status: **rejected as an independent fundamental constraint**

## Attack claim

Multiple model-driven actors may create a fifth constraint: Coordination.
Candidate mechanisms include delegation, routing, shared context, scheduling,
conflict resolution, aggregation, ownership transfer and group termination.

The proposed independent reality is:

> Several actors have partial views, capabilities and control over one task.

## Primary-source observations

### OpenAI Agents SDK

The SDK distinguishes manager orchestration, where one agent retains control and
combines specialist outputs, from handoffs, where a specialist becomes the
active agent. It also distinguishes model-directed orchestration from explicit
code-directed sequencing and parallelism
([orchestration](https://openai.github.io/openai-agents-python/multi_agent/)).
Handoffs can filter which history the receiving agent sees and can be enabled or
disabled dynamically
([handoffs](https://openai.github.io/openai-agents-python/handoffs/)).

### LangChain

LangChain's supervisor pattern keeps memory and user interaction in a main agent,
calling stateless subagents as tools and combining their results. Handoff state
can persist the active agent across turns, while context filters determine what
the receiver sees
([subagents](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents),
[handoffs](https://docs.langchain.com/oss/python/langchain/multi-agent/handoffs)).

### AutoGen

AutoGen teams implement round-robin and selector-style turns, shared message
context, termination conditions, reset/resume and team-state persistence. Its
documentation warns that saving a running team can capture inconsistent state
([teams](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html),
[team state reference](https://microsoft.github.io/autogen/stable/reference/python/autogen_agentchat.teams.html)).

These sources establish recurring multi-actor mechanisms. They do not establish
an independent cause.

## Minimal counterfactual

Start with two identical, stateless agents using the same model and interface.
Give them independent read-only subtasks, run them without shared resources, and
return both outputs without aggregation.

There is multiplicity but no coordination problem: neither worker waits for,
communicates with, owns state with, delegates to or conflicts with the other.

Now add candidate coordination requirements one at a time:

| Added requirement | What creates the problem | Mapping |
|---|---|---|
| Different agent schemas or capabilities | Heterogeneity | Compatibility |
| Ordered turns or dependencies | State transition through time | Continuity |
| Shared mutable context | Concurrent temporal ownership | Continuity |
| Handoff of conversation ownership | State/control transfer | Continuity |
| Permission to delegate or expose data | Bounded authority | Authority residual |
| Select the correct worker | Capability fit plus task validity | Compatibility + Validity |
| Merge conflicting answers | Determine acceptable task result | Validity residual |
| Allocate scarce parallel workers | Finite resources | Cost |
| Improve team topology from outcomes | Prior experience | Cognition |
| Decide task decomposition and roles | Product/task policy | Application boundary |

The coordination problem appears only after another relation—difference,
dependency, shared state, delegation, scarcity or joint validity—is introduced.

## Hard case: simultaneous shared action

Two homogeneous agents may race to update the same record. Even with identical
interfaces and goals, the system needs mutual exclusion, ordering, optimistic
concurrency control or conflict resolution.

This is the strongest case for independent Coordination. But the conflict is
defined by overlapping state transitions. Remove shared state across time and
the race disappears. The same problem exists for ordinary concurrent workers
without models and is handled by runtime/database primitives.

At Harness granularity, deciding which task branch owns or commits an effect is
Continuity control. Infrastructure may enforce the lock or transaction.

**Result:** no independent residual.

## Hard case: collective output with no leader

A decentralized group may need consensus on one answer. Consensus sounds more
than Compatibility or Continuity.

But the Harness question is why one group result is accepted:

- agreement protocol and message semantics → Compatibility;
- rounds, quorum state and termination → Continuity;
- whether the agreed result satisfies the task → Validity;
- who may commit the result → Authority.

Consensus is a composite algorithm over those concerns. Agreement alone can
still converge on a wrong or unauthorized result.

## Why "multi-agent" is not the unit of theory

An agent can be exposed as a tool, a handoff destination, a parallel worker or a
stateful peer. The same logical task can often be implemented as one agent with
tools, several agents, or deterministic code. A fundamental taxonomy should not
change merely because a component boundary is redrawn.

Multi-agent is therefore an architecture and composition pattern. It amplifies
several constraints but does not yet supply a new one.

## Verdict

Coordination does not pass the independence criterion:

1. Multiplicity without dependency creates no coordination obligation.
2. Communication differences reduce to Compatibility.
3. Shared state, ordering and ownership reduce to Continuity.
4. Delegation boundaries reduce to Authority.
5. Aggregation and conflict adjudication reduce to Validity.
6. Goal and role design remain Application policy.

**Coordination is rejected as a fundamental peer constraint.** This result
supports the two-level hypothesis and reduces the fifth-constraint candidate
set without protecting the original exhaustive 4C claim.
