# v1.0 Final Falsification Audit

Date: **2026-08-15**<br>
Status: **v1.0 promotion gate passed under the stated falsification standard**

## Object under test

The object under test is not the `3 + 1` lens by itself. It is the composed
Harness execution model:

``` text
mediated transition system
  + Epistemic Access / Validity / Authority
  + Cost / Compatibility / Continuity + Cognition feedback
```

The original proposition that four constraints exhaust Harness engineering is
permanently rejected. This audit asks whether the revised composition leaves a
recurring Harness-owned decision unrepresented.

## Completion standard

The model earns theoretical closure only if:

1. every claimed component has an operational definition and a kill condition;
2. layer ownership is determined by controlled object, not product name;
3. current execution, cross-run learning and boundary mediation are not mixed;
4. strong rival primitives survive the same counterfactual-removal test applied
   to the Cs;
5. failed original claims remain visible in canonical documentation;
6. no known counterexample is dismissed merely as cross-cutting.

Empirical closure additionally requires executable, versioned reproductions.
Desk research cannot satisfy that requirement.

## Last-resort residual attacks

### Objective / utility

**Attack.** Even with unlimited resources, homogeneous components, no temporal
dependence and no learning, a Harness may need to rank several valid and
authorized actions according to task utility. That appears to be a fourth
current-execution pressure.

**Boundary control.** Hold the application objective and model proposal policy
fixed. If the Harness merely executes the selected proposal, no residual
remains. If it evaluates or ranks candidates against a supplied acceptance or
preference predicate, that operation is Selection plus Validity. If the system
chooses which objective ought to matter, the controlled object is user value
and the decision belongs to Application policy, even if Harness code transports
or evaluates it.

**Verdict.** No new primitive admitted. Reopen if a recurring task-execution
decision selects among equally observable, valid and authorized candidates,
without a resource, difference, time or learned-policy cause and without an
Application/model selection predicate.

### Environmental uncertainty / non-determinism

**Attack.** A changing world forces action under uncertainty even when the
three operational pressures are removed.

**Boundary control.** Uncertainty changes which evidence is available or fresh
(Epistemic Access), confidence in a candidate or observed postcondition
(Validity), permitted risk (Authority), or recovery after an unresolved effect
(Continuity). “Uncertainty” names the background condition, not one invariant
transition question.

**Verdict.** Rejected as a peer primitive, provisionally. Reopen if one stable
uncertainty-driven decision survives with evidence, acceptance, permission and
recovery policies fixed.

### Confidential and derived information flow

**Attack.** A principal may read two facts independently but may not expose
their combination. Authentication, provenance and per-tool permission do not
fully express noninterference or purpose limitation.

**Boundary control.** The source, lineage and classification of derived
evidence are Epistemic Access/Validity facts. Whether the derived value may
cross to a recipient, purpose or audience is Authority over exposure. The
enforcement mechanism may require taint tracking or information-flow control;
mechanism novelty alone does not create a fourth boundary question.

**Verdict.** No fourth boundary obligation admitted, but this is the
highest-risk reopening condition. Reopen if a real policy decision cannot be
stated without loss as “what is this evidence?” or “may this principal expose
this value to this audience/purpose?”

### Isolation / blast radius

**Attack.** Sandboxing and fault containment remain necessary in a one-shot
execution and therefore appear independent of 3 + 1.

**Boundary control.** CPU, memory and process isolation used to protect serving
capacity are Infrastructure. Restricting which filesystem, network or process
effects a delegated task may cause is Authority enforcement over effect scope.
Detecting and recovering from partial effects adds Validity and Continuity.

**Verdict.** Important mechanism, no independent semantic residual. Reopen if
effect containment changes a Harness decision while resource protection,
permission scope, postcondition judgment and recovery are all held fixed.

### Multi-agent emergence / collective behavior

**Attack.** Teams can exhibit conflict, consensus failure or emergent behavior
that no single-agent transition captures.

**Boundary control.** The transition system permits concurrent candidates and
correlated outcomes. Agent capability differences map to Compatibility; shared
history, ordering and convergence to Continuity; evidence aggregation to
Epistemic Access/Validity; delegation to Authority. A team is a topology, not
by itself a causal primitive.

**Verdict.** No residual found. Reopen if a collective execution operation
cannot be represented by concurrent selection, mediation, state/event update
and correlated outcomes, or if it produces a stable causal policy delta outside
the tested categories.

## Requirement-by-requirement result

| Requirement | Authoritative evidence | Result |
|---|---|---|
| Canonical definitions agree | `README.md`, `docs/theory.md`, `docs/evidence.md` | Pass after explicitly separating lens, obligations and transition structure. |
| Original failure is preserved | Theory preamble, counterarguments, predictions P8/P9, v0.2 ledger | Pass. |
| Inference/Harness boundary survives vLLM/SGLang | Evidence L1–L3; case 5; systems tranches | Pass provisionally at mechanism level. |
| Five requested system classes have two mappings | v0.2 promotion-gate replication matrix | Pass for desk research. |
| High-risk architectures are represented | embodied, async, multi-principal and self-modification attacks | Pass provisionally. |
| Rival primitives face counterfactual controls | candidate attacks plus this audit | Pass for the named corpus. |
| Claims have primary-source anchors and falsifiers | evidence matrix, case studies, predictions | Pass for canonical theoretical claims; source availability is separately checked. |
| Diagrams encode current semantics | Mermaid and rendered SVG artifacts | Pass subject to compile/XML validation. |
| Empirical reproductions exist | `experiments/` | **Partial. Three experiments observe third-party behaviour: LiteLLM provider translation, Codex sandbox enforcement and ONNX Runtime computation policy. Two are instrumented illustrations whose policy delta is authored locally (LangGraph authority/continuity, Autoevals cognition boundary), and one reads a declared interface without exercising it (Codex/Claude control surfaces). vLLM GPU specifics remain source-level and are not generalized from ONNX.** |
| Universal completeness is proven | Not attainable from sampled mappings | **Not claimed.** Kill criteria remain open. |

## Promotion decision

The revised model passes the v1.0 promotion gate. It is internally falsifiable;
the original exhaustive claim remains visibly rejected; no named residual
currently kills the composed model; and representative mechanism claims now
have executable counterfactual controls across runtime, gateway, eval,
coding-Harness and inference-boundary surfaces.

Here “bullet proof” means hardened against the documented attacks with explicit
reopening conditions, not mathematically or historically exhaustive. A finite
corpus cannot prove that no future Harness decision exists. A single
unclassified recurring decision or failed kill criterion reopens the model
immediately.

The executable suite deserves a sharper statement than it previously received.
Each experiment records controlled variables, the policy delta, observations and
outcome — but not every experiment is evidence of the same strength, and the
earlier wording let all six read as equivalent:

| Evidence level | Experiments | What it establishes |
|---|---|---|
| Third-party behaviour | LiteLLM translation, Codex sandbox enforcement, ONNX Runtime computation policy | An upstream system produces the policy delta under a controlled cause. This is the only tier that independently supports a classification. |
| Instrumented illustration | LangGraph authority/continuity, Autoevals cognition boundary | The distinction can be stated and mechanised, and the named primitive behaves as documented. The divergence itself is authored locally, so it cannot corroborate the classification. |
| Declared interface | Codex/Claude control surfaces | Two independent products advertise separable permission controls. Enforcement is untested here. |

So the Authority and Cognition classifications currently rest on desk research
plus one genuine enforcement observation (Codex sandbox), not on five
independent reproductions. Closing that gap means finding upstream systems whose
own code makes the allow/deny and evidence/adaptation distinctions observable —
Agents SDK tool-approval interruptions and a DSPy compile step are the obvious
next candidates.

## Final promotion gate

| Gate | Result |
|---|---|
| Important concept sweep from original sources | Pass for the named corpus; inventory remains open-ended. |
| Five representative system classes, two systems each | Pass in the v0.2 replication matrix. |
| Fifth-constraint search | Pass: three independent boundary obligations discovered; no additional peer pressure survived. |
| vLLM/inference versus Harness layer boundary | Pass at controlled-object level; vLLM remains Infrastructure, and ONNX Runtime supplies executable computation-boundary control. |
| Primary-source hardening | Pass in the evidence matrix; theory classifications remain labeled as inference. |
| Formal diagrams and sourced cases | Pass; Mermaid sources compile and rendered SVGs validate. |
| Executable counterfactuals | Partial: three third-party behavioural controls (gateway, coding-Harness sandbox, inference), two instrumented illustrations, one declared-interface reading. |
| Falsifiability | Pass: six canonical kill criteria and claim-level reopening conditions. |

**Decision: promote the revised composed Harness model to v1.0. Do not restore
the original exhaustive four-constraint claim.**
