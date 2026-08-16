# 4C Case Studies

This document is for concrete examples showing how the same mechanism maps
differently according to its cause, controlled object and execution boundary.

## Case Study Template

For each provider or system:

### 1. Execution unit and controlled object

Is the unit a model request, user task, agent task, evaluation run or deployment
transition? Is the mechanism controlling computation, task execution or user
value?

### 2. Documented semantics

What does the provider officially specify?

### 3. Counterfactual policy delta

What decision changes when one candidate cause changes and the others are held
fixed?

### 4. 3 + 1 mapping

Which current pressure—Cost, Compatibility or Continuity—is activated? Does
prior execution evidence produce a reusable Cognition policy delta?

### 5. Boundary mapping

What evidence is observable and attributable? What Validity predicate applies
before and after effects? Which principal/delegation has Authority?

### 6. Empirical findings

What behavior has been discovered through experiments but is not
guaranteed by documentation?

### 7. Harness policy

What execution strategy follows from those facts?

### 8. Outcome and falsifier

What changes, and what observation would disprove the mapping?

## Case 1: Provider/resource semantics → Cost policy

A core Cost thesis is:

> **Resource semantics become task-execution semantics only when they change
> Harness policy.**

Different billing functions can rationally produce different harnesses:

``` text
pricing / limits / cache behavior
              ↓
      provider-specific policy
              ↓
cache | compress | route | summarize | stop
              ↓
        actual task economics
```

The important asset may be less the implementation than the **empirical
findings** behind it.

Kernel choice, GPU placement and continuous batching remain Infrastructure even
when they change monetary cost. The controlled object prevents feature-name
mapping.

**Documented mechanisms.** OpenAI exposes reasoning effort and truncation
controls that change token use, context retention and cache behavior
([source](https://platform.openai.com/docs/api-reference/realtime)). Portkey
supports both monetary and token-denominated limits
([source](https://portkey.ai/docs/product/ai-gateway/virtual-keys/budget-limits)).

**Inference.** These become Harness Cost only when the task policy chooses
effort, retained context, route or stopping behavior because of the resource
envelope. Provider-side execution of the call remains Infrastructure.

**Falsifier.** If changing the task resource envelope never changes a Harness
decision—or all resulting decisions occur solely inside model serving—this case
does not support Cost at the Harness layer.

A few hundred lines of policy code can be rewritten. Hundreds of trials
that discover cache boundaries, latency cliffs, undocumented
incompatibilities or context-price transitions may be substantially
harder to reproduce.

## Planned provider studies

The initial research queue should include:

-   DeepSeek: caching economics and prefix reuse
-   Anthropic: prompt caching and long-context economics
-   OpenAI: cached input, tool-loop semantics and model routing
-   Kimi: context-window economics and truncation/summarization policy
-   Qwen: context tiers and execution-policy implications

**Publication rule:** exact prices, cache rules and provider behaviors
must be verified against current primary sources before being stated as
facts.

## Case 2: Context compression

Compression illustrates why 4C is a causal taxonomy of policy adaptation.

-   Compress to reduce paid tokens → **Cost**
-   Compress to keep a long-running task alive → **Continuity**
-   Learn when compression is safe from historical outcomes →
    **Cognition**
-   Select which current evidence survives compression → **Epistemic Access**
-   Check that the compressed representation preserves task-critical facts →
    **Validity**

The implementation may be one function; the reasons for its existence
span the operational, feedback and boundary planes.

**Documented mechanisms.** Anthropic describes context engineering as curating
the token set available during inference, including retrieval and compaction
([source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).
MemGPT explicitly moves information across memory tiers to work beyond a bounded
active context
([source](https://arxiv.org/abs/2310.08560)).

**Falsifier.** If relevance/evidence selection can be removed while only token
capacity and history persistence remain, Epistemic Access is not independent in
this case.

## Case 3: Consequential tool call

A model emits a syntactically correct `delete_account(id)` call.

- schema/provider differences → **Compatibility**;
- task state and suspension for review → **Continuity**;
- whether the account and intent are correctly identified → **Epistemic Access
  + Validity**;
- whether the delegated principal may delete it → **Authority**;
- whether deletion actually occurred → observed postcondition **Validity**.

No amount of free compute, interface homogeneity, state persistence or historical
learning supplies permission. This is the minimal authority counterexample.

**Documented mechanisms.** Claude Code separates tool/file/domain permissions
from OS-level sandbox enforcement
([permissions](https://code.claude.com/docs/en/permissions),
[sandbox](https://code.claude.com/docs/en/sandboxing)). The OpenAI Agents SDK
can pause a run for approval, serialize its state and resume after approval or
rejection
([source](https://openai.github.io/openai-agents-python/human_in_the_loop/)).

**Falsifier.** If capability/schema negotiation plus task correctness always
determines legitimate dispatch across consequential systems, Authority is not
independent.

## Case 4: Learned prompt or skill

Past executions produce scores and diagnoses; an optimizer proposes a changed
prompt or reusable skill.

- scores are **Validity evidence**, not Cognition by themselves;
- a reusable Harness-policy delta is **Cognition**;
- changing model weights belongs to the **Model** layer;
- changing the success predicate requires Application-level **Validity and
  Authority**;
- version, rollout and rollback are **Continuity**.

The optimizer cannot prove improvement by weakening its own metric, and cannot
self-authorize a permission expansion.

**Documented mechanisms.** DSPy optimizes parameterized language-model programs
against a supplied metric
([source](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f1cf02ce09757f57c3b93c0db83181e0-Abstract-Conference.html)).
Voyager improves generated programs from environment feedback and stores
successful ones for reuse
([source](https://arxiv.org/abs/2305.16291)).

**Falsifier.** If no reusable future Harness artifact changes—or only model
weights change—the mechanism is not Harness Cognition.

## Case 5: Inference runtime versus Harness frontend

SGLang is a useful product-level boundary trap. Its original design contains a
frontend language for multi-call programs and a runtime with RadixAttention and
structured-decoding optimizations
([paper](https://arxiv.org/abs/2312.07104)). Current project documentation
emphasizes high-performance model serving
([source](https://github.com/sgl-project/sglang)).

- KV-cache reuse, device parallelism and decoding kernels control model
  computation → **Infrastructure**;
- frontend sequencing or branching across model calls can control task
  transitions → **Harness Continuity/Compatibility**;
- constrained token decoding does not prove semantic **Validity**.

**Falsifier.** If one product label consistently determines layer ownership,
component-level classification adds no predictive value. SGLang currently shows
the opposite.

## Case 6: Asynchronous state-changing message

Temporal distinguishes read-only Queries, asynchronous state-changing Signals
and tracked Updates that may be validated before acceptance
([source](https://docs.temporal.io/encyclopedia/workflow-message-passing)).
Workflow executions preserve local state, issue commands, await events and
recover through event-history replay
([source](https://docs.temporal.io/workflow-execution)).

- event delivery and history persistence → runtime substrate;
- correlation and task-state meaning → **Continuity**;
- accepting/rejecting an Update → task-specific **Validity/Authority** when used
  by a model-driven execution;
- an incoming Signal/event can make a transition eligible without a model
  proposal.

**Falsifier.** If concurrent messages, replay and late outcomes require an
independent Harness operation outside evidence/state/event update, selection,
mediation, application and correlated outcome, the transition-system model
fails.
