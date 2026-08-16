# Authority Attack

Date checked: **2026-08-15**<br>
Status: **provisional theory failure; reproduction required**

## Attack claim

4C may omit a fundamental harness constraint:

> A harness delegates consequential actions to a probabilistic actor, but the
> actor's proposed action is not identical to authority to execute it.

Call the residual **bounded authority** for now. This is a description, not a
proposed fifth-C name.

## Scope guard

This attack does not argue that all security is part of the Harness layer.
Identity providers, operating-system isolation, secret storage and organization
policy may live elsewhere. The narrower claim is that a harness must make or
enforce an execution decision between a model-proposed action and a tool's
actual dispatch.

The object under test is therefore task execution, not GPU computation,
organization governance or model alignment.

## Primary-source observations

### Claude Code — coding harness

Claude Code supports allow, ask and deny rules; the first applicable class
determines whether a tool call runs. Its documentation explicitly says that
permission rules are enforced by Claude Code rather than by the model. It also
distinguishes application-level permission matching from OS-level sandbox
enforcement ([permissions](https://code.claude.com/docs/en/permissions),
[sandboxing](https://code.claude.com/docs/en/sandboxing)).

**Relevant semantics:** the model may propose the same command while harness
policy removes the tool, rejects the call, asks a principal, or dispatches it.

### OpenAI Codex — coding harness

Codex combines a technical sandbox boundary with approval policy for actions
outside that boundary. Writable paths and network access are constrained, and
requests crossing the boundary can stop for review
([deployment safety](https://openai.com/index/running-codex-safely/)).

**Relevant semantics:** execution authority is mediated separately from the
model's ability to generate a command.

### OpenAI Agents SDK — general agent runtime

Tools can declare call-specific approval rules. A proposed call becomes an
interruption; the caller can approve or reject it, persist that decision in run
state, and resume. A rejection returns a model-visible result instead of
executing the tool. The mechanism applies to function tools, shell, patches,
nested agents and MCP tools
([human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/)).

**Relevant semantics:** approve and reject are two different transitions from
the same proposed action. Pause/resume preserves the decision point, but does
not explain why the two branches exist.

### MCP hosts — tool protocol boundary

MCP security guidance treats authorization, user consent, token audience and
confused-deputy protection as host/server responsibilities. Its architecture
places the host between model-facing clients and servers
([architecture](https://modelcontextprotocol.io/docs/learn/architecture),
[security practices](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices)).

**Relevant semantics:** protocol compatibility can make a tool callable without
making a particular call authorized.

### Playwright CLI — browser execution harness

The agent-oriented CLI exposes separate controls for allowed and blocked
origins, browser permissions, isolated profiles and secrets
([configuration](https://playwright.dev/agent-cli/configuration)).

**Relevant semantics:** browser compatibility and session continuity do not
determine which origins or capabilities an agent may exercise.

### Stripe agent tooling — financial-action harness integration

Stripe lets agents create and manage financial objects, recommends restricted
API keys that expose only configured functionality, recommends human
confirmation for MCP tools, and warns about prompt injection when tools from
multiple servers are combined
([agent toolkit](https://docs.stripe.com/agents),
[Stripe MCP](https://docs.stripe.com/mcp)).

**Relevant semantics:** provider compatibility makes financial APIs callable;
restricted credentials and confirmation determine which consequential calls an
agent is empowered to make. This reproduces the residual outside coding.

## Counterfactual reduction

Use a minimal case: one model, one provider, one local tool, one call, unlimited
resources, no stored history. The tool is `delete_account(account_id)` and the
model proposes a syntactically valid call.

| Remove candidate cause | What remains | Reduction result |
|---|---|---|
| Cost | Assume execution is free, instant and unlimited. Authorization is still required. | Not Cost |
| Compatibility | Use one fixed model and one perfectly compatible tool schema. The principal may still deny the call. | Not Compatibility |
| Continuity | Complete the task in one inference and one tool call, with no retry, memory or resumption. The allow/deny branch remains. | Not Continuity |
| Cognition | Use no traces, history, evaluation or adaptation. A static policy must still decide whether dispatch is permitted. | Not Cognition |

The residual changes execution semantics: `allow` produces an external side
effect; `deny` does not. It persists after all four proposed realities are held
constant or removed.

## Necessary distinction: waiting versus authorizing

Human-in-the-loop combines two different operations:

| Operation | Question | 4C result |
|---|---|---|
| Information wait | What missing value is needed to continue? | Continuity: suspend, persist and resume. |
| Authority decision | May this already-specified action execute? | Unreduced residual: choose the permitted transition. |

Implementations often serialize both as an interrupt. Shared implementation is
not shared causation.

## Admission-test result

| Requirement | Current evidence | Result |
|---|---|---|
| Independent durable fact | Proposed action and legitimate authority can diverge even in the minimal case. | Pass |
| Cross-provider and cross-architecture recurrence | Codex, Claude Code, Agents SDK, MCP hosts, browser tooling and Stripe agent tooling implement the mechanism family across coding, general tools, web and finance. | Pass |
| Changes execution semantics | Allow/deny changes whether a side effect occurs. | Pass |
| Not merely outcome or mechanism | The constraint predicts sandboxing, capability restriction and approval mediation; no single mechanism defines it. | Provisional pass |
| Folding into a C loses information | Continuity cannot distinguish information waits from authorization decisions. Compatibility cannot distinguish callable from permitted. | Pass |

## Strongest rival explanations

### Rival 1: authority is Compatibility

Permissions may look like differences among users, tools and environments. But
perfectly normalizing those differences only answers whether a call can be
expressed. It does not answer whether this principal authorizes this side
effect. Compatibility predicts adapters and negotiation; authority predicts
deny-by-default, least privilege and mediation.

**Current result: rejected.**

### Rival 2: authority is Continuity control

Continuity explains how execution pauses and later resumes. It does not predict
the rejection branch in a one-step execution, nor why the model cannot choose
its own permission. Expanding "control" to include every rule governing
execution would make Continuity absorb Cost routing, Compatibility negotiation
and application policy as well.

**Current result: rejected unless Continuity is radically redefined.**

### Rival 3: authority is a cross-cutting invariant, not a coordinate

Authority may constrain every action selected under all four Cs, much as a type
or safety invariant constrains a program without becoming an optimization axis.
This would preserve 4C as four pressures on execution while conceding that 4C
is not a complete taxonomy of harness constraints.

The distinction is weaker than it first appears. Cost budgets can define an
economically admissible set; Compatibility defines technically expressible
executions; Continuity defines valid temporal transitions; authority defines
permitted actions. All four proposed Cs already mix pressure, feasibility and
policy. Calling only authority an invariant therefore needs an independent
classification rule.

**Current result: weakened but live.** It is the strongest alternative to adding
a fifth fundamental constraint, but it cannot rest on the word "invariant."

### Rival 4: authority belongs outside Harness

External policy may define the rule, and OS/container infrastructure may enforce
isolation. Yet the harness still maps a proposed action plus context to dispatch,
reject or escalation. Excluding that decision would also exclude approvals and
tool dispatch from the Harness definition.

**Current result: rejected for the narrow execution-mediation claim.**

## Current conclusion

The original completeness suggestion—four unavoidable constraints explain the
Harness layer—does not survive this attack as currently written. The evidence
supports three intellectually honest paths:

1. **Add a fundamental constraint** based on delegated consequence/authority.
2. **Change the claim:** 4C describes four execution-optimization pressures but
   is not exhaustive of harness constraints.
3. **Produce a stronger reduction** showing that authority follows from an
   existing C without making that C universal and unfalsifiable.

Path 3 has not been demonstrated. The residual now recurs in coding, generic
tool, browser and financial domains. No rename or promotion should happen until
the invariant-versus-axis question is resolved and harnesses without local
authority machinery are examined as counterevidence.

## Counterevidence: automatic tool execution

Some harnesses execute model-selected tools without an approval prompt.
LangChain's minimal agent is constructed with a tool list and runs the
model/tool loop; human review is added through middleware rather than required
by the minimal API
([agent documentation](https://docs.langchain.com/oss/python/langchain/agents),
[human-in-the-loop](https://docs.langchain.com/oss/python/langchain/human-in-the-loop)).
AutoGen likewise executes tools by default; its code-executor approval callback
is optional and defaults to automatic approval
([tool documentation](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/components/tools.html),
[code executor reference](https://microsoft.github.io/autogen/stable/reference/python/autogen_agentchat.agents.html)).

This initially appears to be counterevidence. It is not evidence that authority
is absent. It shows **blanket pre-authorization**:

1. The application chooses which tools enter the harness.
2. Credentials and runtime identity bound what those tools can do.
3. A container or host process bounds where effects occur.
4. The default dispatch policy authorizes every valid call within that supplied
   capability set.

Removing the approval prompt coarsens the decision from per call to per
configuration. It does not make an unavailable tool callable or an uncredentialed
operation authorized. An allow-all policy over a bounded set is still a policy.

Three ownership patterns should therefore be distinguished:

| Pattern | Where the decision occurs | Example |
|---|---|---|
| Intrinsic mediation | Harness evaluates each proposed call. | ask/allow/deny, intervention handler |
| Pre-delegation | Application grants a capability when constructing the harness. | tool list, restricted key, runtime identity |
| External enforcement | Another layer rejects effects after dispatch. | OS sandbox, API authorization, network policy |

Real systems combine all three. 4C only needs to explain the harness-owned
portion, but the existence of pre-delegation prevents "no prompt" from serving
as a counterexample.

## Next attacks

1. Repeat the minimal-case test for email/send, browser purchase and
   physical/robotic action. Financial tooling now supplies one non-coding
   reproduction.
2. Separate **authority** (who may authorize), **risk** (expected harm),
   **policy** (which actions are allowed) and **enforcement** (where the boundary
   is implemented). Determine which, if any, is fundamental.
3. Search for a system where the model can cause effects without any configured
   capability, runtime identity or enforcement boundary. Automatic dispatch is
   insufficient counterevidence because it can be blanket pre-authorization.
4. Test whether every proposed fifth constraint is an invariant rather than a
   coordinate—and apply the same challenge back to Cost and Cognition.
