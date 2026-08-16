# Multi-Principal Security Attack

Date: **2026-08-15**<br>
Status: **Identity, provenance and confidentiality decompose; no fourth boundary obligation admitted**

## Threat

In a multi-principal system, a user, client, host, remote agent, tool server,
resource owner and organization may all have different identities, authority and
information. This raises candidates that look independent from Authority:

- Authentication / Identity;
- Provenance / Integrity;
- Confidentiality / Privacy;
- Accountability / Auditability;
- Trust.

If any changes Harness execution after Epistemic Access, Validity and Authority
are held fixed, the current three-obligation boundary is incomplete.

## Primary evidence

A2A treats remote agents as potentially opaque systems. Agent Cards declare
identity/capabilities/authentication requirements; authentication is handled at
the transport layer; authorization remains server-specific and can depend on
identity, skill, action, data policy and OAuth scope
([specification](https://a2a-protocol.org/latest/specification/)).

MCP requires access tokens to be audience-bound, forbids token passthrough and
describes the confused-deputy risk when an intermediary misuses credentials or
downstream trust
([authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)).
Its security guidance notes that passthrough can also destroy the ability to
distinguish clients for accountability and audit
([security guidance](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)).

These mechanisms establish recurring multi-principal problems. They do not by
themselves determine taxonomic independence.

## Authentication / Identity

Authentication answers an epistemic question:

> What evidence supports that the actor, service or resource is the claimed
> principal?

Authorization then answers a normative/execution question:

> Given that principal and delegation chain, may this transition expose or cause
> the requested effect?

Authentication can succeed while authorization denies, so the mechanisms must
not be conflated. But Identity does not create a fourth mediation decision:

- acquisition and verification of identity evidence → Epistemic Access plus
  evidence Validity;
- use of that identity to allow/deny/delegate → Authority;
- preservation of identity/delegation across task state → Continuity;
- token/protocol differences → Compatibility.

**Verdict: not an independent boundary obligation.** Identity is an evidence
subject required by Authority, not a synonym for Authority and not a fourth
allow/deny predicate.

## Provenance / Integrity

Provenance records where evidence, policy, code or an action came from. Its
meaning depends on what decision consumes it:

- can this evidence be attributed and authenticated? → Epistemic Access;
- is the evidence/artifact unaltered and suitable for the task? → Validity;
- is this source allowed to influence or trigger this transition? → Authority;
- can provenance survive retries, handoffs and merges? → Continuity.

An untrusted tool result may be observable but not valid evidence; a valid fact
may still be forbidden from crossing a disclosure boundary. Provenance connects
the questions but does not replace them.

**Verdict: cross-boundary mechanism, not a fourth primitive.**

## Confidentiality / Privacy

Reading or exposing information is itself an effect. Therefore:

- which principal may receive which data → Authority over exposure;
- what data is present/retrieved → Epistemic Access;
- whether transformed/redacted data satisfies policy → Validity;
- retention/deletion across time → Continuity;
- serialization/provider differences → Compatibility.

Privacy law and organizational governance can originate outside the Harness, as
do cost budgets and success predicates. Once compiled into whether evidence may
enter a model/tool or leave as output, the Harness enforces Authority and
Validity boundaries.

**Verdict: no separate live-execution primitive.** Privacy is broader than
Harness Authority organizationally, but its Harness-level disclosure decision
is an Authority decision.

## Accountability / Auditability

An audit log can be passive and have no effect on the current task. In that
case, it is a governance/observability requirement rather than an execution
pressure. When the log is later used:

- to reconstruct events → evidence substrate;
- to reject or verify an outcome → Validity;
- to prove who approved/performed an effect → Authority evidence;
- to update future policy → Cognition;
- to survive/replay task history → Continuity.

**Verdict: desired property and evidence mechanism, not an independent
transition question.** This does not make audit optional for regulated systems;
it locates its causal role.

## Trust

“Trust” is too compressed to classify. It can mean estimated correctness,
authenticated identity, delegated permission, provider reliability or historical
performance. Each meaning maps differently. A trust score only changes
execution after a policy specifies whether it affects evidence, Validity,
Authority, routing or learning.

**Verdict: rejected as a primitive.** Always expand “trust” into the claim,
evidence, principal and decision involved.

## Confused-deputy counterexample

An agent receives a token intended for service A and forwards it to service B.
The interfaces are compatible and the task state is intact, but the credential
does not authorize that audience. Correct behavior requires:

1. observe and validate token issuer/audience evidence;
2. bind the requesting principal and delegated authority to the intended
   resource;
3. reject passthrough or obtain a separate downstream credential;
4. preserve the delegation/correlation across the task lifecycle.

This cleanly reproduces Epistemic Access + Validity + Authority + Continuity. It
does not reveal a residual after those questions are fixed.

## Verdict

No fourth boundary obligation is admitted:

- **Epistemic Access** includes identity, source, freshness and provenance of
  evidence.
- **Validity** includes integrity and fitness of evidence, candidates and
  observed outcomes.
- **Authority** includes principal identity, delegation, scope, audience,
  disclosure and revocation policy.

Continuity transports these semantics across time; Compatibility represents
them across systems; Cognition may adapt future policy from audit evidence.

The result is provisional because information-flow systems with derived/tainted
data may still expose a residual. Reopen if two executions with identical
evidence authenticity, task validity and legitimate authority still require
different Harness behavior solely because of a security property not represented
above.
