#!/usr/bin/env python3
"""Vary inference-engine policy while holding the task-facing result fixed.

Evidence level: third-party behaviour. ONNX Runtime executes the forward pass
under two different computation policies; this file only fixes the graph, input
and requested output and compares what the runtime returns.
"""

from __future__ import annotations

import importlib.metadata
import json
import platform
import tempfile
from pathlib import Path

import numpy as np
import onnx
import onnxruntime as ort
from onnx import TensorProto, helper

from _support import THIRD_PARTY_BEHAVIOUR, require


def build_model(path: Path) -> None:
    weight = helper.make_tensor(
        "weight", TensorProto.FLOAT, [2, 2], [2.0, 0.0, 0.0, 3.0]
    )
    bias = helper.make_tensor("bias", TensorProto.FLOAT, [2], [1.0, -1.0])
    graph = helper.make_graph(
        [
            helper.make_node("MatMul", ["input", "weight"], ["product"]),
            helper.make_node("Add", ["product", "bias"], ["output"]),
        ],
        "fixed-forward-pass",
        [helper.make_tensor_value_info("input", TensorProto.FLOAT, [1, 2])],
        [helper.make_tensor_value_info("output", TensorProto.FLOAT, [1, 2])],
        [weight, bias],
    )
    model = helper.make_model(
        graph,
        ir_version=10,
        opset_imports=[helper.make_opsetid("", 21)],
    )
    onnx.checker.check_model(model)
    onnx.save(model, path)


def infer(model_path: Path, threads: int, optimize: bool) -> list[list[float]]:
    options = ort.SessionOptions()
    options.intra_op_num_threads = threads
    options.graph_optimization_level = (
        ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        if optimize
        else ort.GraphOptimizationLevel.ORT_DISABLE_ALL
    )
    session = ort.InferenceSession(
        str(model_path), sess_options=options, providers=["CPUExecutionProvider"]
    )
    value = np.array([[4.0, 5.0]], dtype=np.float32)
    return session.run(["output"], {"input": value})[0].tolist()


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="4c-ort-") as temporary:
        model_path = Path(temporary, "fixed.onnx")
        build_model(model_path)
        conservative = infer(model_path, threads=1, optimize=False)
        optimized = infer(model_path, threads=2, optimize=True)

    expected = [[9.0, 14.0]]
    require(conservative == expected, "unoptimized forward pass changed the result")
    require(optimized == expected, "optimized forward pass changed the result")

    report = {
        "experiment": "onnxruntime-infrastructure-boundary",
        "evidence_level": THIRD_PARTY_BEHAVIOUR,
        "runtime": platform.python_version(),
        "onnxruntime": importlib.metadata.version("onnxruntime"),
        "execution_provider": "CPUExecutionProvider",
        "controlled_variables": [
            "model graph and weights",
            "input tensor",
            "requested output tensor",
            "task-facing result",
        ],
        "independent_variable": "inference threads and graph-optimization policy",
        "runs": {
            "conservative": {
                "threads": 1,
                "graph_optimization": "disabled",
                "output": conservative,
            },
            "optimized": {
                "threads": 2,
                "graph_optimization": "all",
                "output": optimized,
            },
        },
        "result": {
            "controlled_object": "model computation",
            "task_transition_semantics_observed": False,
            "claim": (
                "Inference scheduling/optimization policy changes how a forward "
                "pass is computed; it does not by itself define task execution."
            ),
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
