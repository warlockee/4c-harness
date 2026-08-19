# Execution Yield: From 4C Classification to a Product Verdict

4C identifies **why** task-execution policy has to vary. That is not enough to
choose a product. A source tree can contain the right mechanisms while putting
extra model calls, blocking writes, unstable prompt prefixes or unnecessary
human handoffs on the hot path. A smaller implementation can deliver better
results with fewer controls.

Product selection therefore requires five separate passes:

``` text
Task frontier → 4C activation → Realization → Observed yield → Migration
what becomes worth trying       how code carries it       what the task gets
```

`Strong`, `Partial` and `Evidence` describe **mechanism coverage only**. They
must never be used as performance grades.

## 1. Start with the task frontier

A fixed task contract is necessary for comparison but insufficient for product
selection. The contract is partly endogenous: lower latency, lower marginal
cost or a shorter change path can make a user attempt work they previously
considered too trivial, uncertain or expensive. Evaluating only today's
delegated tasks systematically hides that value.

Build three small portfolios before activating 4C:

| Portfolio | Contents | Why it matters |
|---|---|---|
| **Current** | Tasks the user already delegates | Supports controlled current-vs-candidate comparison. |
| **Rejected backlog** | Real tasks the user does manually, postpones or discards because the current system is slow, costly or awkward | Tests whether the candidate expands economically feasible delegation. |
| **Adjacent probes** | Bounded experiments suggested by the candidate's inspectable affordances, each with a success predicate and effect limit | Tests discovery value without turning a feature demo into evidence. |

Report **frontier expansion** as newly attempted task classes that reach a
verified postcondition within the user's limits. Also record failed exploration
and its cost. Counting more generated artifacts without user value or Validity
does not expand the frontier.

Source can expose affordances that deserve a probe; it cannot determine which
new tasks a person values. That observation belongs at the Application and
human-evidence boundary, not inside a fifth C.

## 2. Five paths to inspect

### Onboarding path: install to first verified task

Trace the shipped path a new user follows, not the path a maintainer already
knows:

- installation prerequisites, downloads, builds and platform-specific steps;
- credential and provider setup, including whether a restart is required;
- which model, prompt, tools, permissions and workspace the default composition
  actually selects;
- the number of user decisions before the first task can run;
- whether missing credentials, unsupported capabilities and sandbox failures
  explain the corrective action without source-code knowledge;
- cold-start time and whether an upgrade preserves working configuration.

Measure time, actions and failed attempts to the first externally verified
postcondition. A powerful architecture with a broken default or opaque first
failure is not easy to use.

### Execution path: request to verified outcome

Trace one representative task through the actual default composition, not an
ideal architecture diagram. Mark:

- every serial await before the first useful output;
- every model request, provider/IPC/network hop and retry;
- prompt and tool-schema tokens added, retained, replaced or independently
  requested;
- prefix changes that can invalidate provider KV-cache reuse;
- synchronous work performed for each streamed chunk;
- persistence, telemetry or validation work that blocks forward progress;
- independent tool calls serialized despite being safe to overlap;
- approval, evidence and validation gates, including the obligation that
  justifies each one;
- the observation that proves the intended postcondition, rather than merely
  proving dispatch.

Call the resulting overhead the **path tax**. A tax is not automatically bad:
validation or authority mediation can be essential. It is bad when it consumes
a scarce resource without serving an activated 4C pressure or a named boundary
obligation.

### Model-fit path: provider capability to model-visible semantics

Generic compatibility can erase the advantage of a vertically integrated
path. Inspect:

- whether the default route uses a native adapter or a lowest-common-denominator
  protocol;
- how reasoning, tool calls, images, usage, cache accounting and provider error
  semantics survive serialization and replay;
- whether the adapter adds hidden prompts, extra calls or lossy translations;
- which model-specific controls can change on the next request without restart;
- whether the shipped prompt and tool schemas match the model's trained
  affordances;
- whether the default composition keeps stable prefixes and avoids capability
  negotiation on every turn.

This path predicts **Model–Harness fit**, not model intelligence. A direct
adapter can preserve a model's strengths while still being slow because of the
provider; a fast provider can hide a wasteful Harness path.

### Human-control path: intent to correction

Trace the loop the person actually experiences:

- when the first meaningful state becomes visible, not only the first token;
- whether streaming survives every server, event and UI boundary;
- how follow-up, steering, interruption, cancellation and queued input reach a
  running task;
- whether tool progress, errors, approvals and completion evidence are visible
  early enough to change the next decision;
- whether the product forces parallel task management merely to hide waiting;
- how many actions and how much elapsed time one correction requires.

This is where low latency becomes flow. Source can show that control and stream
events exist on a short path; only a human trial can establish comprehension,
predictability, delight or the threshold at which attention switches away.

### Change path: missing capability to verified extension

Trace what happens when the product lacks one capability. Mark:

- whether the running system exposes its real interfaces and schemas for
  inspection;
- whether the change attaches at a documented seam or patches a privileged
  core;
- how many packages, files and ownership boundaries must change;
- whether the extension can load without rebuilding or restarting unrelated
  work;
- whether effects unload cleanly and a previous version can be restored;
- whether the agent can inspect, author, run, diagnose and revise the extension
  through supported tools;
- whether the extension survives restart and product upgrade without patching
  generated or vendor-owned files;
- which validation and authority checks stand between generated code and a live
  effect.

This path is how source inspection can predict on-demand self-extension.
Counting plugin APIs alone is insufficient; the relevant question is the
length and safety of the complete change loop.

## 3. Yield is a vector, not one score

For the representative task, report these values separately:

| Yield dimension | Minimum observation |
|---|---|
| Interaction | time to first useful output; correction-loop latency; the wait at which the human context-switches |
| Onboarding | time, decisions and failed attempts from clean install to the first verified task |
| Completion | cold/warm time to an externally verified postcondition; successful tasks per wall-clock hour |
| Economic | input/output/cache tokens and money per verified outcome, not per request |
| Amplification | model requests, retries, tool calls and remote hops per verified outcome |
| Human load | interventions, approvals and manual recovery steps per verified outcome |
| Model fit | native capabilities preserved or lost; hidden prompts/calls and model-specific configuration required |
| Frontier | rejected or adjacent task classes newly completed within the user's limits; failed exploration cost |
| Change | time and touchpoints from missing capability to validated extension; restart, upgrade and rollback cost |
| Distribution | p50/p95/p99 latency and success, cold start, long-session degradation, retry and recovery tails |

Do not collapse the vector into a universal score. The terrain-specific [4C Fit
Score](harness-scout.md#21-the-4c-fit-score) is allowed only when its weights are
locked and the vector, evidence stage and boundaries stay visible. An approval
that hurts interaction yield can be mandatory for Authority; a checkpoint that
adds write traffic can be required by Continuity. The task contract supplies
the weights and hard limits.

Do not report only the mean. A five-second median with a five-minute p95 can
destroy the same human flow that the median appears to enable. Run enough
repetitions to expose warm/cold, cache-hit/miss, short/long-session and
success/failure paths.

## 4. Evidence ladder

Keep four evidence levels distinct:

| Level | What it supports |
|---|---|
| **Source-predicted** | The code path contains or avoids a specific wait, hop, token tax, invalidation or extension touchpoint. |
| **Trace-observed** | A pinned configuration records the predicted path and timings at runtime. |
| **Task-validated** | The trace ends in the task's external success predicate on representative inputs. |
| **Human-observed** | A named interaction threshold or workflow effect, such as retaining flow instead of opening parallel tasks, is reported or measured. |

Source can reveal Harness-added friction. It cannot prove provider latency,
model capability, price, task correctness or subjective flow. Those require the
later levels. Conversely, a testimonial can reveal a decisive outcome while
leaving its model, Infrastructure and Harness causes unresolved.

## 5. Attribution, not storytelling

A user adopts a product stack, but an engineering claim should localize the
cause when possible. Use controlled substitutions:

| Comparison | Primary effect isolated |
|---|---|
| Same model/provider, different Harness | Harness and UI realization |
| Same Harness, different model/provider | Model/provider service |
| Same Harness/model, optional layer disabled | That layer's path tax or benefit |
| Same task/config, cold vs warm and cache miss vs hit | startup, caching and retained-state effects |
| Same output candidate, independent postcondition checker | validity rather than self-reported completion |

Record configuration, commit, model identifier, endpoint, region, prompt/preset,
tool set, cache state and run time. If the product does not permit a controlled
substitution, label the observation **stack-level** rather than assigning it to
the Harness. The combined product result can still justify adoption.

## 6. The combined audit

For every candidate:

1. **Build the frontier.** Collect current tasks, the rejected backlog and a
   small set of bounded adjacent probes.
2. **Activate.** Run the four removal tests against each task class; activation
   may differ across the portfolio.
3. **Trace source.** Inspect the shipped default composition across onboarding,
   execution, Model-fit, human-control and change paths. Record the exact commit.
4. **Predict.** State which observable result each code fact should change and
   what would falsify that prediction.
5. **Run a distribution.** Execute representative inputs repeatedly on current
   and candidate systems. Capture the yield vector, cold/warm states and tails.
6. **Validate.** Check external postconditions and effect scope; do not accept
   self-reported completion or artifact count as value.
7. **Attribute.** Run controlled substitutions where available. Otherwise label
   the result stack-level rather than inventing a Harness cause.
8. **Observe the human loop.** Record the correction cycle, context-switch
   threshold, newly attempted work and experienced control; name anecdotal
   evidence as anecdotal.
9. **Price migration.** Apply the seven migration line items only after the
   candidate demonstrates a task-relevant or frontier-expanding advantage.

The decision record for one claim has this shape:

``` text
Pressure:       Cost — interactive latency changes the human work policy
Portfolio:      current task / rejected backlog / adjacent probe
Source fact:    persistence is queued off the response hot path
Prediction:     persistence adds no awaited write before streamed output
Runtime trace:  p50/p95 request → useful output = ...; blocked write time = ...
Task result:    postcondition passed / failed
Human effect:   stayed in loop / context-switched; correction cycle = ...
Attribution:    isolated Harness / provider / UI, or stack-level
Verdict:        stay / switch / adopt for one subtask
```

## 7. DeepSeek Harness: what source inspection should have surfaced

Snapshot: upstream commit
[`141eb6f`](https://github.com/deepseek-ai/deepseek-harness/tree/141eb6fef83422698aef7a981029e843e8161534),
2026-08-19. These are source predictions, not comparative benchmark results.

| Source fact | Predicted user-visible effect | Still requires execution evidence |
|---|---|---|
| The DeepSeek adapter performs a direct streaming request and yields parsed SSE chunks without an extra shared HTTP layer ([adapter](https://github.com/deepseek-ai/deepseek-harness/blob/141eb6fef83422698aef7a981029e843e8161534/packages/llm/llm-deepseek/src/adapter.ts#L228-L385)). | Low Harness amplification between provider chunks and the agent stream. | Provider time-to-first-token, UI rendering delay and comparative end-to-end latency. |
| The native adapter maps DeepSeek thinking, reasoning effort, tool calls, reasoning replay, cache-read accounting and provider error semantics, and documents exactly one provider request per stream ([adapter contract](https://github.com/deepseek-ai/deepseek-harness/blob/141eb6fef83422698aef7a981029e843e8161534/packages/llm/llm-deepseek/README.md)). | The default route preserves provider-specific semantics instead of paying a lowest-common-denominator compatibility tax. | Whether the model uses those semantics better, and the result of same-model/different-Harness substitution. |
| The loop appends each arriving chunk immediately, while session durability uses a detached write-behind queue and telemetry requires non-blocking enqueue ([loop](https://github.com/deepseek-ai/deepseek-harness/blob/141eb6fef83422698aef7a981029e843e8161534/packages/core/agent-loop/src/agent.ts#L332-L419), [write-behind](https://github.com/deepseek-ai/deepseek-harness/blob/141eb6fef83422698aef7a981029e843e8161534/packages/session/session-persistence/src/write-behind.ts#L18-L158), [telemetry](https://github.com/deepseek-ai/deepseek-harness/blob/141eb6fef83422698aef7a981029e843e8161534/packages/session/session-telemetry/README.md#the-backend-contract)). | Persistence and observability are designed not to insert awaited storage/network work into the response path. | CPU/event-loop cost per chunk, crash-loss trade-off and measured first-useful-output latency. |
| Parallel-safe tool calls use a bounded rolling pool while results commit in model order ([scheduler](https://github.com/deepseek-ai/deepseek-harness/blob/141eb6fef83422698aef7a981029e843e8161534/packages/core/agent-loop/src/tool-calls.ts#L121-L239)). | Independent tools can reduce wall time without making model-visible history nondeterministic. | The task's actual parallelism, tool bottlenecks and rate-limit effects. |
| Every package documents its direct token effect and KV-cache behavior as a repository invariant ([package contract](https://github.com/deepseek-ai/deepseek-harness/blob/141eb6fef83422698aef7a981029e843e8161534/docs/cookbook/adding-a-package.md#4-write-the-package-readme)). | Prompt tax and cache invalidation are inspectable at the package boundary instead of hidden in one assembled prompt. | Actual cache availability, hit rate, billed tokens and cost per verified task. |
| The `cordis` preset tells the agent it can inspect and modify the running Harness, supplies live interface inspection, and defines a reversible define/run/stop workflow ([preset](https://github.com/deepseek-ai/deepseek-harness/blob/141eb6fef83422698aef7a981029e843e8161534/apps/cli/config/agent-presets/cordis/agent.cordis.yml), [development skill](https://github.com/deepseek-ai/deepseek-harness/blob/141eb6fef83422698aef7a981029e843e8161534/apps/cli/config/agent-presets/cordis/skills/cordis-plugin-development/SKILL.md)). | The change path from a missing capability to a live extension is short, inspectable and reversible; this is stronger evidence than “plugin-based.” | Time to a validated extension, failure/rollback rate and whether the granted authority is acceptable. |

The earlier 4C profile found Compatibility and Continuity machinery but missed
these realization properties. The corrected interpretation is conditional:

> When interactive latency, quota or time-to-extension changes the user's work
> policy—or makes previously rejected work worth attempting—DeepSeek Harness
> has source-level reasons to deserve a trial. Only a runtime distribution
> ending in verified task outcomes can justify a switch.

## 8. What this method still cannot get from source

- provider/model latency, availability, price and rate limits;
- model capability and the correctness of completed work;
- human comprehension, accessibility, trust, flow, delight and fatigue;
- the value of a newly discovered task to a particular person or organization;
- support quality, community, legal terms, roadmap and vendor durability.

Runtime, postcondition, human and organizational evidence remain mandatory.
This audit is not claimed to be exhaustive. Reopen it when a recurring
product-selection factor cannot be represented as task-frontier movement, one
of the five realization paths, the yield vector or migration cost without
losing decision-relevant information.
