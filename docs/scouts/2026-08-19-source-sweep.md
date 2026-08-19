# Harness Scout Source Sweep — 2026-08-19

This sweep reruns the current project list through the 4C Harness Scout rather
than reusing the feature-coverage table as a product ranking. Every repository
is pinned to an exact commit. The result is a **source-level trial queue**, not a
runtime leaderboard.

Calibration status: **inaugural discovery cohort, not trial-ready and excluded
from Bole hit-rate claims.** P1 below means high information value for an
archetypal terrain, not a calibrated probability of success. No owner-supplied
task portfolio, primary uplift threshold, budget or deadline was locked before
the audit. See the [calibration ledger](calibration-ledger.md).

## Result

The source audit found five high-information prospects, four conditional
prospects and two holds:

| Queue | Candidates | Meaning |
|---|---|---|
| **P1 — run first** | DeepSeek Harness, Aider, browser-use; LangGraph and LiteLLM in their ecosystem roles | The source exposes a narrow causal edge, a cheap discriminating trial and a meaningful upside if the prediction holds. |
| **P2 — conditional trial** | Codex, Gemini CLI, OpenHands, Cline | The source exposes a real terrain-specific edge, but the trial is broader, the product is already a mature baseline, or attribution crosses more layers. |
| **Hold at Mapped** | CrewAI, Langflow | Mechanisms are present, but this pass did not isolate a default-path yield edge sharp enough to spend the next trial budget on. |

`P1` does not mean globally better. It means the next experiment has higher
information value for the named terrain. `Mapped` is not rejection. No
candidate becomes `Qualified` without a pinned runtime trace.

## Terrain-specific source scorecards

For an apples-to-apples coding comparison, lock one terrain before looking at
the candidates: latency- and quota-sensitive interactive coding with on-demand
local extension. The weights are Cost 45, Compatibility 35, Continuity 20 and
Cognition 0 for every row.

| Candidate | Cost | Compatibility | Continuity | 4C Fit | Evidence / boundary |
|---|---:|---:|---:|---:|---|
| **DeepSeek Harness** | 4 | 4 | 4 | **80** | Source-predicted / Unknown |
| Aider | 4 | 3 | 4 | **73** | Source-predicted / Unknown |
| Gemini CLI | 3 | 4 | 4 | **71** | Source-predicted / Unknown |
| Codex | 3 | 3 | 4 | **64** | Source-predicted / Unknown |
| Cline | 2 | 3 | 3 | **51** | Mechanism-backed / Unknown |
| OpenHands | 2 | 3 | 3 | **51** | Mechanism-backed / Unknown |

browser-use and the ecosystem systems are excluded because they do not execute
the same product unit on this terrain. This fixed-weight card is the actual
comparison; the following best-fit cards answer a different question—whether
4C notices quality where each specialized product is designed to win.
Because this terrain was formalized after the DeepSeek experience was already
public, the table validates the sensitivity of the scale but cannot count as a
prospective Bole hit.

These scores apply the same [4C Fit rubric](../harness-scout.md#21-the-4c-fit-score)
to each candidate's named best-fit terrain. They are not a global leaderboard:
the weights differ because the tasks differ. Grade 4 is the source-only ceiling;
no row can receive grade 5 without paired runtime evidence.

| Candidate | Named terrain | Locked active-C weights | Realization grades | 4C Fit | Evidence / boundary |
|---|---|---|---|---:|---|
| **DeepSeek Harness** | latency/quota-sensitive interactive coding + on-demand extension | Cost 45 / Compatibility 35 / Continuity 20 | 4 / 4 / 4 | **80** | Source-predicted / Unknown |
| Codex | high-authority resumable coding | Cost 15 / Compatibility 25 / Continuity 60 | 3 / 4 / 4 | **77** | Source-predicted / Unknown |
| browser-use | authenticated stateful browser work | Cost 20 / Compatibility 35 / Continuity 45 | 3 / 4 / 4 | **76** | Source-predicted / Unknown |
| Cline | reversible cross-surface coding sessions | Cost 10 / Compatibility 30 / Continuity 60 | 2 / 4 / 4 | **76** | Source-predicted / Unknown |
| Gemini CLI | long governed generalist sessions | Cost 25 / Compatibility 35 / Continuity 40 | 3 / 4 / 4 | **75** | Source-predicted / Unknown |
| Aider | low-amplification repository editing | Cost 50 / Compatibility 20 / Continuity 30 | 4 / 3 / 4 | **76** | Source-predicted / Unknown |
| OpenHands | isolated concurrent autonomous runs | Cost 10 / Compatibility 30 / Continuity 60 | 2 / 3 / 4 | **70** | Source-predicted / Unknown |
| LangGraph | durable stateful workflows | Continuity 100 | 4 | **80** | Source-predicted / Unknown |
| LiteLLM | quota/cost-aware multi-provider gateway | Cost 55 / Compatibility 45 | 4 / 4 | **80** | Source-predicted / Unknown |
| Langflow | visual workflow composition and deployment | Compatibility 45 / Continuity 55 | 3 / 3 | **60** | Mechanism-backed / Unknown |
| CrewAI | role-separated multi-agent workflow | Compatibility 40 / Continuity 45 / Cognition 15 | 3 / 3 / 2 | **57** | Mechanism-backed / Unknown |

DeepSeek reaches the source ceiling because every active C exposes a sharp
default-path yield hypothesis. Gemini exposes broader machinery, but breadth
does not add points. CrewAI and Langflow remain conditional because their
machinery has not yet been converted into an equally discriminating edge.
The machine-readable cards are in [`fit-scores.json`](fit-scores.json), their
per-C claims, implementation paths, executable invariants, shipped paths and
falsifiers are in [`fit-score-evidence.json`](fit-score-evidence.json), and CI
recomputes and cross-checks both with
[`tools/fit_score_check.py`](../../tools/fit_score_check.py).
On 2026-08-19, a GitHub Contents API audit resolved all 71 unique pinned
implementation, invariant and reachability paths in that ledger. Path existence
does not prove the prediction; that is why every grade 4 remains explicitly
`source-inferred` and carries a falsifier. CI repeats the live audit with
[`tools/evidence_link_check.py`](../../tools/evidence_link_check.py).

## 4C activation and realization view

This is the actual 4C pass behind the queue. A named C means removing that
pressure changes the candidate policy for the stated terrain; it is not a
feature count. Boundary columns remain obligations, not extra points.

| Candidate | Activated 4C pressure | Strongest source realization path | Boundary that the trial must preserve |
|---|---|---|---|
| DeepSeek Harness | Cost, Compatibility, Continuity | execution, Model-fit, change | Validity, Authority |
| Aider | Cost, Compatibility, Continuity | execution, human-control | Validity, Authority |
| browser-use | Cost, Compatibility, Continuity | Model-fit, continuity/recovery | Epistemic Access, Validity, Authority |
| Codex | Cost, Compatibility, Continuity | execution, human-control | Validity, Authority |
| Gemini CLI | Cost, Compatibility, Continuity | Model-fit, human-control, change | Validity, Authority |
| OpenHands | Cost, Compatibility, Continuity | onboarding, human-control | Validity, Authority |
| Cline | Cost, Compatibility, Continuity | human-control, continuity/recovery | Validity, Authority |
| LangGraph | Continuity | execution, continuity/recovery | Validity, Authority |
| LiteLLM | Cost, Compatibility; adaptive routing can activate Cognition | Model-fit, execution | Validity |
| CrewAI | Compatibility, Continuity; memory may activate Cognition | execution, change not yet discriminating | Validity, Authority |
| Langflow | Compatibility, Continuity | onboarding/change not yet discriminating | Validity, Authority |

The table also explains why broad 4C coverage does not determine queue order.
The queue follows the sharpness and testability of the realized causal edge.

## Like-for-like Harnesses

### DeepSeek Harness (P1, Nominated)

- **Pinned commit:** [`141eb6f`](https://github.com/deepseek-ai/deepseek-harness/tree/141eb6fef83422698aef7a981029e843e8161534)
- **Terrain:** latency-sensitive interactive work, quota-constrained delegation
  and on-demand extension.
- **Source edge:** a direct native DeepSeek stream, off-hot-path persistence and
  telemetry, bounded parallel tool execution, provider-native semantics and an
  agent-operable reversible plugin loop.
- **Prediction:** lower Harness-added wait and amplification, plus a shorter
  missing-capability-to-working-extension loop.
- **Falsifier:** same-model traces expose hidden blocking work or no meaningful
  latency/cost advantage; representative extensions still require core edits,
  restarts or human repair.
- **Evidence:** the full path analysis and links are in the [DeepSeek Scout
  Card](deepseek-harness.md).

This remains the most important discovery test for 4C: ordinary feature
coverage made DeepSeek look merely incomplete, while the execution and change
paths expose why it may change a person's delegation policy.

### Aider (P1, Nominated)

- **Pinned commit:** [`5dc9490`](https://github.com/Aider-AI/aider/tree/5dc9490bb35f9729ef2c95d00a19ccd30c26339c)
- **Terrain:** small and medium repository edits where context tax, correction
  speed and safe undo matter more than autonomous breadth.
- **Source edge:** the [repository map](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/aider/repomap.py)
  ranks definitions with a dependency graph and fits them to an explicit token
  budget; the [command loop](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/aider/commands.py)
  exposes token cost, lint/test feedback, Git commits and guarded undo.
- **Prediction:** fewer context tokens and less orchestration overhead per
  verified local edit, with a short inspect/correct/rollback loop.
- **Falsifier:** on representative cross-file tasks the compact map omits
  decisive context, produces more repair turns, or Git mediation costs more
  time than it saves.

The source says Aider's smaller surface is a design hypothesis, not missing
coverage. That makes it a genuine low-amplification prospect.

### browser-use (P1, Nominated)

- **Pinned commit:** [`85ddbf8`](https://github.com/browser-use/browser-use/tree/85ddbfedf609166b2d2c76c3d80506649fee82a9)
- **Terrain:** authenticated, stateful browser tasks whose difficulty is DOM,
  tab, navigation and session continuity rather than general code editing.
- **Source edge:** the [browser session](https://github.com/browser-use/browser-use/blob/85ddbfedf609166b2d2c76c3d80506649fee82a9/browser_use/browser/session.py)
  owns CDP lifecycle, selector-map caching, reconnects and event watchdogs;
  [serializable agent state](https://github.com/browser-use/browser-use/blob/85ddbfedf609166b2d2c76c3d80506649fee82a9/browser_use/agent/views.py)
  carries pause/resume and compact history semantics; the DOM serializer emits
  a model-facing interactive-element map rather than raw page HTML.
- **Prediction:** fewer stale-element and lost-session failures, and lower page
  representation tax, than a generic computer-use loop on browser-heavy work.
- **Falsifier:** matched browser tasks show no success/tail advantage, or DOM
  capture and recovery dominate tokens and wall time.

Specialization is exactly why it deserves a trial on this terrain and exactly
why it should not be promoted as a general Harness.

### Codex (P2, Nominated)

- **Pinned commit:** [`3b45c29`](https://github.com/openai/codex/tree/3b45c29062ff0e76e71c91b6753290400e7fa8da)
- **Terrain:** high-authority repository work that needs sandboxed execution,
  resumability, visible progress and controlled parallel delegation.
- **Source edge:** tool calls pass through explicit sandbox and approval
  machinery; the [parallel runtime](https://github.com/openai/codex/blob/3b45c29062ff0e76e71c91b6753290400e7fa8da/codex-rs/core/src/tools/parallel.rs)
  separates parallel-safe calls while preserving model-visible order; the
  [rollout](https://github.com/openai/codex/blob/3b45c29062ff0e76e71c91b6753290400e7fa8da/codex-rs/core/src/rollout.rs)
  and session tests support reconstruction, resume and compaction.
- **Prediction:** fewer unsafe effects and less recovery loss on long coding
  tasks without giving up useful streaming or independent tool overlap.
- **Falsifier:** under equal authority and validity requirements, approvals and
  session machinery add delay without reducing incidents or recovery work.

Codex is a strong controlled-execution baseline. It is P2 because the next
trial mostly calibrates a known mature path rather than testing a missed source
signal.

### Gemini CLI (P2, Nominated)

- **Pinned commit:** [`eaa3042`](https://github.com/google-gemini/gemini-cli/tree/eaa30429a72a2a76c173ced853e9a15b14d92a64)
- **Terrain:** long generalist sessions where model routing, checkpointing,
  organizational policy and extension governance must coexist.
- **Source edge:** the [policy engine](https://github.com/google-gemini/gemini-cli/blob/eaa30429a72a2a76c173ced853e9a15b14d92a64/packages/core/src/policy/policy-engine.ts)
  combines approval modes, sandbox knowledge and ordered hook checkers; its
  configuration exposes recovery checkpoints, compression, model fallback,
  tool-level sandboxing, worktrees and live extension reload, while rejecting
  extension attempts to grant unsafe policy.
- **Prediction:** fewer manual mode switches and safer customization across
  long mixed workloads, with recoverable edits and policy that survives the
  extension boundary.
- **Falsifier:** routing/compression/hook layers add more latency and context
  churn than they save, or extensions still need restart and manual repair in
  representative use.

The candidate is broad rather than lean; the trial must attribute each optional
layer instead of treating breadth itself as value.

### OpenHands (P2, Nominated)

- **Pinned commit:** [`f2dd330`](https://github.com/OpenHands/OpenHands/tree/f2dd33090592f8777e3f2d1a519ddb44866e595e)
- **Terrain:** supervising several local or remote autonomous coding runs,
  especially when workspace isolation and scheduled/event-triggered work matter.
- **Source edge:** Agent Canvas explicitly separates UI from the Agent Server
  execution boundary; its [child-conversation launcher](https://github.com/OpenHands/OpenHands/blob/f2dd33090592f8777e3f2d1a519ddb44866e595e/src/services/child-conversation-launch.ts)
  claims calls before network work, supports worktree or cloud isolation,
  records parent/child lineage and surfaces unsafe shared-workspace fallbacks.
- **Prediction:** lower operator load and fewer cross-agent workspace conflicts
  when managing concurrent autonomous tasks across backends.
- **Falsifier:** provisioning and frontend/server hops dominate useful progress,
  lineage cannot reconstruct outcomes, or fallback-to-shared workspaces causes
  conflicts at an unacceptable rate.

Attribution spans Agent Canvas and its separately versioned Agent Server, so a
runtime trial must pin both. That is why this is conditional rather than P1.

### Cline (P2, Nominated)

- **Pinned commit:** [`d9bb228`](https://github.com/cline/cline/tree/d9bb22883daa3df2c917a73b6af911f2551f68b0)
- **Terrain:** human-supervised coding that moves among IDE, CLI, SDK and remote
  clients while preserving the same live session.
- **Source edge:** the [SDK architecture](https://github.com/cline/cline/blob/d9bb22883daa3df2c917a73b6af911f2551f68b0/sdk/ARCHITECTURE.md)
  separates stateless agent execution from stateful orchestration; hub clients
  attach/detach without stopping the authority runtime and preserve structured
  text, reasoning, tool and completion events. [Checkpoint restore](https://github.com/cline/cline/blob/d9bb22883daa3df2c917a73b6af911f2551f68b0/sdk/packages/core/src/session/checkpoint-restore.ts)
  supplies a reversible workspace path.
- **Prediction:** lower session-loss and correction cost when a person changes
  surfaces or interrupts long-running work.
- **Falsifier:** cross-surface transport creates stale UI or duplicate state,
  checkpoint restoration loses user edits, or the layered runtime adds more
  repair work than a single-process tool.

The code contains a serious continuity design, but its size and multi-surface
path make a narrow P1 experiment less obvious.

## Ecosystem candidates — not drop-in Harness replacements

### LangGraph (P1 substrate trial, Nominated)

- **Pinned commit:** [`837212b`](https://github.com/langchain-ai/langgraph/tree/837212b9699bc4c3400b97714988344d348598f8)
- **Terrain:** long-running stateful workflows where completed parallel work
  must survive failure and a human may inspect, modify and resume state.
- **Source edge:** checkpointers save graph state at every superstep; [pending
  writes](https://github.com/langchain-ai/langgraph/blob/837212b9699bc4c3400b97714988344d348598f8/libs/checkpoint/README.md#pending-writes)
  keep successful node results when a peer fails so resume does not rerun them;
  the repository also ships a conformance suite across checkpoint backends.
- **Prediction:** fewer repeated expensive steps and less recovery loss than an
  ad-hoc agent loop after injected mid-graph failures.
- **Falsifier:** checkpoint writes dominate the workload, resume repeats effects,
  or application code still has to rebuild the missing durability semantics.

This is a Continuity prospect for builders, not a better coding UI.

### LiteLLM (P1 infrastructure trial, Nominated)

- **Pinned commit:** [`4bb3152`](https://github.com/BerriAI/litellm/tree/4bb3152cc52415cf19a5d43eba2158718e924239)
- **Terrain:** multi-provider portfolios constrained by quotas, budgets,
  availability and provider-specific cache economics.
- **Source edge:** the [router](https://github.com/BerriAI/litellm/blob/4bb3152cc52415cf19a5d43eba2158718e924239/litellm/router.py)
  combines health-aware cooldown, exception-specific retry/fallback, latency,
  cost and usage strategies; budget and prompt-cache affinity are explicit
  pre-call filters rather than after-the-fact reports.
- **Prediction:** more verified outcomes per dollar and fewer quota-induced
  failures for a heterogeneous request portfolio.
- **Falsifier:** routing adds unacceptable TTFT, provider translation loses
  decisive semantics, or fallback increases cost while hiding task failures.

This is a Cost/Compatibility layer. A win here improves a Harness stack but
does not prove that the end-user Harness is good.

### CrewAI (Hold, Mapped)

- **Pinned commit:** [`4dfd074`](https://github.com/crewAIInc/crewAI/tree/4dfd074fae84fc287af9f9e8cce7e74096c4f626)
- **Observed mechanisms:** event-driven flows, persistence, async feedback,
  streaming and local/remote A2A delegation are all real source surfaces; see
  the [flow engine](https://github.com/crewAIInc/crewAI/blob/4dfd074fae84fc287af9f9e8cce7e74096c4f626/lib/crewai/src/crewai/flow/flow.py)
  and [A2A wrapper](https://github.com/crewAIInc/crewAI/blob/4dfd074fae84fc287af9f9e8cce7e74096c4f626/lib/crewai/src/crewai/a2a/wrapper.py).
- **Why no nomination yet:** this pass did not isolate a default terrain where
  extra roles and handoffs predict higher verified yield rather than additional
  model calls, context duplication and failure edges.
- **Promotion trigger:** name a real workflow whose roles require different
  tools, context or authority, then show that Crew delegation removes custom
  orchestration while bounding request amplification.

### Langflow (Hold, Mapped)

- **Pinned commit:** [`09ef6b2`](https://github.com/langflow-ai/langflow/tree/09ef6b2b7119e35a6787fc249f916f8b47b28615)
- **Observed mechanisms:** visual graph composition, checkpoint/resume support,
  extension bundles and API/MCP exposure are implemented surfaces; see the
  [graph runtime](https://github.com/langflow-ai/langflow/blob/09ef6b2b7119e35a6787fc249f916f8b47b28615/src/lfx/src/lfx/graph/graph/base.py),
  [checkpoint package](https://github.com/langflow-ai/langflow/tree/09ef6b2b7119e35a6787fc249f916f8b47b28615/src/lfx/src/lfx/graph/checkpoint)
  and [bundle contract](https://github.com/langflow-ai/langflow/blob/09ef6b2b7119e35a6787fc249f916f8b47b28615/BUNDLE_API.md).
- **Why no nomination yet:** a visual surface and broad component catalog do not
  alone predict a shorter idea-to-verified-deployment path after debugging,
  versioning and upgrade cost are included.
- **Promotion trigger:** compare a representative non-trivial workflow against
  code-first composition, measuring authoring, diagnosis, deployment and change
  time rather than node count.

## What this says about 4C as a scout

This rerun changes the answer in three important ways:

1. **It recovers the DeepSeek signal that coverage missed.** Direct streaming,
   off-path work and an agent-operable change loop become a P1 trial instead of
   a footnote under `Partial Cost`.
2. **It notices different horses for different terrain.** Aider's restraint,
   browser-use's specialization, LangGraph's pending writes and LiteLLM's
   pre-call economics are advantages that a universal feature score would
   flatten.
3. **It can still say “not yet.”** CrewAI and Langflow remain mapped because
   feature presence has not been converted into a sharp yield prediction.

That is credible scouting at the source stage. It is not yet proof of being a
good judge of winners. The proof comes next: publish the P1 qualification runs,
retain failed predictions, and measure whether `Nominated` candidates are
promoted at a better rate than popularity- or feature-selected baselines.

## Next qualification batch

Run five bounded tests first:

| Candidate | Discriminating test | Primary observations |
|---|---|---|
| DeepSeek Harness | Same-model interactive task set plus one missing-capability extension | first useful output, calls, cache tokens, verified completion, extension and rollback time |
| Aider | Cross-file edits matched against a broad coding Harness | input tokens, repair turns, lint/test pass, undo safety |
| browser-use | Authenticated multi-page forms and recovery cases matched against generic computer use | success, stale actions, session loss, p95 time and tokens |
| LangGraph | Inject failure after one of several parallel nodes succeeds | duplicate effects, repeated model calls, resume time and checkpoint tax |
| LiteLLM | Replay a mixed provider/quota portfolio with routing off and on | verified outcomes, TTFT tails, fallback semantics and total cost |

Only trace confirmation moves a row to `Qualified`; representative external
postconditions are still required for `Task-proven`.
