# Context Attack

Date checked: **2026-08-15**<br>
Status: **provisional theory failure; P8 provisionally falsified**

## Attack claim

4C may omit a fundamental constraint on model-driven execution:

> A model can condition only on observations represented in its current input
> and accessible state. Information required by the task is not automatically
> present, relevant or usable.

Call the residual **epistemic access**. "Context" is broader and overloaded: it
also refers to token capacity, conversation state and application dependencies.

## Scope guard

This attack does not classify every prompt or database as Harness. The tested
Harness decision is what observations, instructions, tools and retrieved facts
are made available to a model at a particular inference boundary.

The Application defines which knowledge matters to the task. Infrastructure may
store and index it. The Harness assembles the model-visible evidence state during
execution.

## Primary-source observations

### LangChain

LangChain defines context engineering as providing the right information and
tools in the right format. It distinguishes transient model context, persistent
tool context and lifecycle context, and describes control over what enters each
model call and what happens between calls
([context engineering](https://docs.langchain.com/oss/python/langchain/context-engineering)).
Its agent documentation calls the harness everything around the loop—prompt,
tools and shaping middleware—and says its job is to provide the right context at
the right time
([agents](https://docs.langchain.com/oss/python/langchain/agents)).

### Anthropic

Anthropic describes context engineering as curating tokens from a constantly
evolving universe of possible information. It distinguishes pre-inference
retrieval from just-in-time agent search and argues that longer windows still
suffer relevance and context-pollution problems
([context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).

### OpenAI Codex / Responses API

OpenAI describes compaction as preserving important prior state while removing
extraneous material so long-running agents can continue within a new context
window
([computer environment and compaction](https://openai.com/index/equip-responses-api-computer-environment/),
[Codex loop](https://openai.com/index/unrolling-the-codex-agent-loop/)).

### MemGPT

MemGPT models context management as movement between memory tiers to expose
information beyond a model's limited window, combining retrieval and control
flow ([paper](https://arxiv.org/abs/2310.08560)).

The sources establish that context mechanisms span both one-shot evidence
selection and long-horizon state management. Those causes must be separated.

## Minimal counterfactual

Task: answer `What is account 123's current internal risk tier?` The fact exists
only in one private database. Assume:

- one model and provider;
- one perfectly normalized database tool;
- unlimited tokens, latency and money;
- one inference boundary and no conversation history;
- no prior execution data or learning;
- full authorization to read the record;
- a deterministic validator that can check the final answer.

Before retrieval, the model does not observe the fact. After the Harness invokes
or exposes the query and places its result into model context, the model can use
it.

| Candidate reduction | Why it fails |
|---|---|
| Cost | Retrieval remains necessary when tokens, calls and attention capacity are free. |
| Compatibility | A perfectly callable source does not put the relevant row into the model's observation. |
| Continuity | The problem exists in one call with no state to preserve across time. |
| Cognition | No past run or adaptation is used. |
| Authority | Permission to read does not reveal the value. |
| Validity | A checker can reject an unsupported answer but does not supply the missing evidence. |

**Residual:** acquire and present task-relevant evidence to inference.

## Decomposing "Context"

| Context problem | Primary cause | Mapping |
|---|---|---|
| Token/window limit | Finite model resource | Cost |
| Provider-specific context formats and limits | Heterogeneity | Compatibility |
| Preserve task history across calls | Task outlives inference | Continuity |
| Learn better retrieval from prior runs | Experience | Cognition |
| Keep a tool or fact hidden from an unauthorized actor | Permission | Authority |
| Determine whether evidence supports the result | Task acceptance | Validity |
| Discover and expose currently unobserved relevant information | Bounded observation | Epistemic-access residual |
| Select among unlimited visible information for relevance | Bounded effective attention / task evidence | Epistemic access + Validity |

Context Engineering is therefore not one constraint. But it also does not fully
collapse into the original four.

## Hard case: infinite context window

If every possible fact fit in the window, relevance would still matter: adding
irrelevant or conflicting facts can alter behavior, and the world changes after
the prompt is assembled. More importantly, private databases, files, sensors and
tool state are not automatically copied into any window.

An infinite token budget removes capacity pressure, not the observation boundary
between model and world.

## Strongest objection: this is Compatibility

Compatibility makes sources and representations interoperable. It predicts
adapters, schemas, parsers and capability negotiation. Epistemic access predicts
search, retrieval, observation, evidence selection and context assembly even
after every interface is normalized.

Broadening Compatibility from "systems differ" to "the model lacks some
information" would erase the distinction between translation and discovery and
would absorb most data engineering.

**Current result: rejected.**

## Strongest objection: this is Validity

Validity supplies an acceptance predicate: does the candidate answer satisfy
the task given available evidence? Epistemic access changes which evidence is
available before the candidate is produced.

The two interact—retrieval relevance is judged against task validity—but neither
implies the other. A model can observe the correct record and still calculate
wrongly; a validator can detect an unsupported answer without locating the
record.

**Current result: rejected as a reduction; accepted as a cross-plane relation.**

## Strongest objection: retrieval belongs to Application

Domain sources, query semantics and relevance criteria often belong to the
Application. But provider prices, budgets and evaluation criteria also originate
outside the Harness. The theory already includes their compilation into runtime
policy.

A stable ownership split may be:

- **Application:** declares sources, task semantics and relevance goals.
- **Infrastructure:** stores, indexes and serves information.
- **Harness:** decides when and what to retrieve, transforms results, and
  assembles model-visible context during task execution.

If the Harness definition excludes that runtime decision, it conflicts with the
observed definition of modern harnesses and with 4C's existing inclusion of
context shaping.

## Admission-test result

| Requirement | Evidence | Result |
|---|---|---|
| Independent durable fact | Model inference is conditioned on bounded observations, not the full task world. | Pass |
| Cross-architecture recurrence | RAG, agentic search, tool-result shaping, memory tiers and repo/environment discovery. | Pass |
| Changes execution semantics | Retrieval and assembly change model input and subsequent action selection. | Pass |
| Not merely one mechanism | Search, observation, retrieval, pruning and assembly implement the same causal need. | Provisional pass |
| Folding into 4C loses information | Cost explains capacity; Continuity explains history; neither explains missing one-shot evidence. | Pass |

## Prediction P8 result

P8 predicted that Context Engineering's durable mechanisms would be understood
primarily as Cost and Continuity, and named a distinct fundamental execution
constraint as its falsifier.

The minimal counterfactual produces exactly that falsifier. P8 is therefore
**provisionally falsified**, not silently rewritten. It may be restored only by
defeating the epistemic-access residual.

## Current conclusion

Context Engineering decomposes, but one component survives:

> **Epistemic access:** execution must acquire and shape the observations on
> which model inference can condition.

This is a third provisional residual alongside Validity and Authority. The
two-level pressure/admission hypothesis is now insufficient because epistemic
access is neither an acceptance predicate nor cleanly one of the four pressures.

A stronger structural model may require three planes:

1. **Observation:** what the model can know now.
2. **Proposal and adaptation:** what execution the system generates under Cost,
   Compatibility, Continuity and Cognition.
3. **Admission:** what is valid and authorized to commit.

This is a working model, not a revision. Planning and Control must be attacked
before reorganizing the canonical theory.
