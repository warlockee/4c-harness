#!/usr/bin/env python3
"""Instrument the Authority/Continuity boundary on real LangGraph primitives.

Evidence level: instrumented illustration. LangGraph supplies the suspension,
checkpoint and resume behaviour that is genuinely observed here. The allow/deny
divergence itself is produced by the locally authored `request_authority` node,
so this experiment shows that the two questions are separable and mechanisable,
not that LangGraph independently distinguishes them.
"""

from __future__ import annotations

import importlib.metadata
import json
import platform
from typing import Literal, TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

from _support import INSTRUMENTED_ILLUSTRATION, require


class State(TypedDict):
    account_id: str
    status: Literal["requested", "deleted", "denied"]


def request_authority(state: State) -> dict[str, str]:
    approved = interrupt(
        {
            "operation": "delete_account",
            "account_id": state["account_id"],
            "question": "May this execution cause the effect?",
        }
    )
    return {"status": "deleted" if approved else "denied"}


def build_graph():
    builder = StateGraph(State)
    builder.add_node("authority_gate", request_authority)
    builder.add_edge(START, "authority_gate")
    builder.add_edge("authority_gate", END)
    return builder.compile(checkpointer=InMemorySaver())


def run_branch(graph, thread_id: str, approved: bool) -> dict[str, object]:
    config = {"configurable": {"thread_id": thread_id}}
    initial = graph.invoke(
        {"account_id": "acct-fixed", "status": "requested"}, config=config
    )
    pending = initial.get("__interrupt__", ())
    require(len(pending) == 1, "execution did not suspend at the authority gate")
    require(
        pending[0].value["operation"] == "delete_account",
        "suspended candidate operation changed between branches",
    )

    snapshot = graph.get_state(config)
    require(
        snapshot.values["status"] == "requested",
        "checkpointed state advanced before the decision",
    )
    require(
        snapshot.next == ("authority_gate",),
        "checkpoint did not preserve the pending decision point",
    )

    resumed = graph.invoke(Command(resume=approved), config=config)
    expected = "deleted" if approved else "denied"
    require(resumed["status"] == expected, "resumed outcome did not follow the decision")
    require(graph.get_state(config).next == (), "execution did not reach a terminal state")

    return {
        "thread_id": thread_id,
        "fixed_candidate": pending[0].value,
        "checkpoint_status": snapshot.values["status"],
        "checkpoint_next": list(snapshot.next),
        "authority_decision": "approve" if approved else "deny",
        "outcome": resumed["status"],
    }


def main() -> None:
    graph = build_graph()
    approved = run_branch(graph, "authority-approved", True)
    denied = run_branch(graph, "authority-denied", False)

    require(
        approved["fixed_candidate"] == denied["fixed_candidate"],
        "candidate action was not held fixed across branches",
    )
    require(
        approved["checkpoint_status"] == denied["checkpoint_status"],
        "checkpointed state was not held fixed across branches",
    )
    require(approved["outcome"] != denied["outcome"], "decision produced no policy delta")

    report = {
        "experiment": "langgraph-authority-continuity",
        "evidence_level": INSTRUMENTED_ILLUSTRATION,
        "runtime": platform.python_version(),
        "langgraph": importlib.metadata.version("langgraph"),
        "controlled_variables": [
            "graph topology",
            "candidate operation",
            "account id",
            "checkpoint state",
            "tool capability",
        ],
        "independent_variable": "authority decision",
        "observed_from_upstream": [
            "suspension at interrupt()",
            "checkpointed state and pending next node",
            "resumption under Command(resume=...)",
        ],
        "authored_locally": [
            "the authority gate node",
            "the mapping from decision to outcome",
        ],
        "branches": [approved, denied],
        "result": {
            "authority_residual": True,
            "continuity_observed": True,
            "claim": (
                "Authority changes admissibility while Continuity preserves "
                "the suspended execution; neither substitutes for the other."
            ),
            "not_proven": (
                "that LangGraph itself separates permission from lifecycle; the "
                "divergence is authored in this file"
            ),
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
