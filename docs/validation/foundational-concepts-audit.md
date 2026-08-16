# Foundational Agent Concepts Audit

Date: **2026-08-15**<br>
Status: **named original-source tranche complete; no new primitive admitted**

## Purpose

This audit tests influential concepts from original papers and specifications,
not their later framework labels. The question is whether their architectural
novelty leaves a residual outside the mediated transition system, the `3 + 1`
model and the three boundary obligations.

## Summary

| Concept | Main contribution | Layer/result | New residual? |
|---|---|---|---|
| ReAct | Interleave model reasoning and environment action | Model selection + Harness evidence/action cycle | No |
| MemGPT | Virtual context over memory tiers and interrupts | Cost + Epistemic Access + Continuity | No |
| Generative Agents | Memory, reflection, retrieval and planning | Cognition + Observation; planning remains Model/Application | No |
| A2A | Agent discovery, modality negotiation and task exchange | Compatibility + Continuity + Authority | No |
| Toolformer | Train model weights to select/use APIs | Model capability; Harness still mediates execution | No |
| MRKL | Route between neural and symbolic modules | Selection + Compatibility + Observation/Validity | No |
| MCP primitives | User/Application/Model-controlled prompts, resources and tools | Confirms mixed transition sources and authority boundary | No |

## ReAct

ReAct interleaves model-generated reasoning traces and task-specific actions;
actions gather information from external sources that then informs later
reasoning
([paper](https://arxiv.org/abs/2210.03629)).

- reasoning trace generation is Model behavior;
- exposing available actions is Compatibility plus Authority;
- executing an action and returning its result is Harness application and
  evidence update;
- carrying the trajectory across turns is Continuity;
- checking task completion is Validity.

**Attack result.** “Reasoning + Acting” is a topology across Model and Harness,
not a fifth Harness constraint. It is an early instance of the mediated
transition system.

## MemGPT

MemGPT manages data across memory tiers to provide virtual context beyond a
limited model window and uses interrupts for control flow
([paper](https://arxiv.org/abs/2310.08560)).

- limited active context activates Cost/resource scarcity;
- deciding which information enters active context is Epistemic Access;
- retaining conversation/document state and handling interrupts is Continuity;
- provider/tool representations can add Compatibility;
- reflection counts as Cognition only if it produces reusable future policy or
  findings, not merely because memory persists.

**Attack result.** “Memory” is not one primitive. Capacity, information
selection, temporal persistence and learning must remain separated.

## Generative Agents

Generative Agents stores experience records, synthesizes higher-level
reflections, retrieves memories and plans behavior in an interactive environment
([paper](https://arxiv.org/abs/2304.03442)).

- observation/retrieval changes available evidence;
- persistence of the experience stream is Continuity;
- higher-level reflections reused in later behavior are Cognition;
- plan generation is primarily Model behavior conditioned by Application goals;
- “believability” is an Application evaluation objective, not a Harness
  constraint.

**Attack result.** Reflection is not automatically Cognition. It qualifies here
because accumulated experience is transformed and reused; a transient
self-critique inside one run would instead be inference plus Validity/Continuity.

## A2A

The A2A specification defines interoperability among independent, potentially
opaque agents, including capability discovery, modality negotiation, task
management, delegation and context exchange
([specification](https://a2a-protocol.org/latest/specification/)).

- discovery, formats and modalities → Compatibility;
- task identity, status, messages and asynchronous lifecycle → Continuity;
- delegation and disclosure across principals → Authority;
- supplied/withheld remote context → Epistemic Access;
- deciding whether a remote result satisfies the parent task → Validity.

**Attack result.** Agent opacity strengthens the boundaries; it does not produce
an independent Coordination primitive. A protocol can transport delegation and
task state without defining the parent application's truth or permission policy.

## Toolformer

Toolformer trains a model to decide which API to call, when, with which
arguments, and how to incorporate results into token prediction
([paper](https://arxiv.org/abs/2302.04761)).

This is a decisive layer test:

- learning tool-selection behavior through weight updates belongs to Model
  training, not Harness Cognition;
- the trained model emits a candidate tool call;
- a Harness still exposes available tools, mediates Authority/Validity, applies
  the call and returns observable results;
- API representation and capability differences remain Compatibility.

**Attack result.** Moving selection intelligence into model weights does not
move execution or its boundaries into the Model. Tool learning and tool
execution are different objects.

## MRKL

MRKL combines language models with external knowledge and discrete reasoning
modules in a routed neuro-symbolic system
([paper](https://arxiv.org/abs/2205.00445)).

Routing selects a candidate module/transition. Module interfaces activate
Compatibility; external knowledge activates Epistemic Access; symbolic checks
can supply Validity. State across a multi-module task activates Continuity.

**Attack result.** “Modularity” is an architecture pattern. It introduces no
independent constraint after module difference, information access and result
acceptance are named.

## MCP control hierarchy

MCP distinguishes prompts controlled by users, resources controlled by
applications and tools controlled by models
([specification](https://modelcontextprotocol.io/specification/2025-06-18/server/index)).
The protocol separately warns that tool/data access requires consent and user
control
([security principles](https://modelcontextprotocol.io/specification/2024-11-05/index)).

**Attack result.** This supports, rather than merely resembles, the mixed-source
transition model: user, Application and Model can initiate different artifacts,
while the host mediates evidence and effects. Protocol Compatibility does not
erase Authority.

## Cross-concept conclusions

1. **Reasoning is not Harness execution.** The Harness owns mediation and
   application around model-selected candidates.
2. **Memory is not one C.** It decomposes by capacity, evidence selection,
   temporal state and learning use.
3. **Reflection is horizon-sensitive.** Same-run critique differs from reusable
   cross-run policy learning.
4. **Protocols transport semantics; they do not supply task truth or legitimate
   authority.**
5. **Training can relocate selection capability into the Model without
   relocating execution boundaries.**
6. **None of the named foundational concepts requires an operation outside the
   concurrent mediated transition system.**

## Remaining concept risk

This completes the specifically queued ReAct, MemGPT, Generative Agents, A2A,
tool-learning and modular-tool concepts. It is not a claim that the historical
inventory is exhaustive. The next useful concept search should be driven by
counterexamples from multi-principal, self-modifying and real-time systems, not
by adding more synonyms for memory, tools or loops.
