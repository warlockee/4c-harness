#!/usr/bin/env python3
"""Reproduce Authority/Continuity separation with real LangGraph primitives."""

from __future__ import annotations

import importlib.metadata
import json
import platform
from typing import Literal, TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


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
    assert len(pending) == 1, "execution did not suspend at the authority gate"
    assert pending[0].value["operation"] == "delete_account"

    snapshot = graph.get_state(config)
    assert snapshot.values["status"] == "requested"
    assert snapshot.next == ("authority_gate",)

    resumed = graph.invoke(Command(resume=approved), config=config)
    expected = "deleted" if approved else "denied"
    assert resumed["status"] == expected
    assert graph.get_state(config).next == ()

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

    assert approved["fixed_candidate"] == denied["fixed_candidate"]
    assert approved["checkpoint_status"] == denied["checkpoint_status"]
    assert approved["outcome"] != denied["outcome"]

    report = {
        "experiment": "langgraph-authority-continuity",
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
        "branches": [approved, denied],
        "result": {
            "authority_residual": True,
            "continuity_observed": True,
            "claim": (
                "Authority changes admissibility while Continuity preserves "
                "the suspended execution; neither substitutes for the other."
            ),
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
