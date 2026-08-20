#!/usr/bin/env python3
"""Verify that the published ladder matches the frozen source exam."""

from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAM = ROOT / "docs" / "scouts" / "interactive-coding-v2-exam.json"
RESULTS = ROOT / "docs" / "scouts" / "interactive-coding-v2-results.json"
MARKET = ROOT / "docs" / "scouts" / "market-universe.json"
LADDER = ROOT / "assets" / "4c-harness-ladder.svg"
COMPARISON_ID = "interactive-coding-v2"
SVG_NS = "{http://www.w3.org/2000/svg}"
ROW_BAR_ORIGIN = 414.0
THRESHOLDS = (50, 65, 80, 100)


def elements_with_class(root: ET.Element, class_name: str) -> list[ET.Element]:
    return [
        element
        for element in root.iter()
        if class_name in element.get("class", "").split()
    ]


def one_with_class(root: ET.Element, class_name: str) -> ET.Element:
    matches = elements_with_class(root, class_name)
    if len(matches) != 1:
        raise ValueError(f"expected one {class_name!r} element, found {len(matches)}")
    return matches[0]


def display_number(value: float) -> str:
    return str(int(value)) if value.is_integer() else f"{value:g}"


def display_stars(value: int) -> str:
    thousands = value / 1000
    rendered = f"{thousands:.1f}".removesuffix(".0")
    return f"{rendered}K"


def competition_ranks(candidates: list[dict]) -> list[int]:
    ranks: list[int] = []
    previous_score: float | None = None
    previous_rank = 0
    for position, candidate in enumerate(candidates, start=1):
        score = float(candidate["score"])
        if score != previous_score:
            previous_rank = position
            previous_score = score
        ranks.append(previous_rank)
    return ranks


def pressure_weights(exam: dict) -> dict[str, int]:
    return {
        pressure: sum(q["weight"] for q in exam["questions"] if q["pressure"] == pressure)
        for pressure in ("Cost", "Compatibility", "Continuity")
    } | {"Cognition": 0}


def pressure_contributions(exam: dict, candidate: dict) -> dict[str, float]:
    values = {"Cost": 0.0, "Compatibility": 0.0, "Continuity": 0.0, "Cognition": 0.0}
    questions = {q["id"]: q for q in exam["questions"]}
    for question_id, answer in candidate["answers"].items():
        question = questions[question_id]
        values[question["pressure"]] += question["weight"] * answer["level"]
    return values


def main() -> int:
    exam = json.loads(EXAM.read_text())
    payload = json.loads(RESULTS.read_text())
    market = json.loads(MARKET.read_text())
    products = market.get("products", [])
    products_by_name = {product.get("name"): product for product in products}
    weights = pressure_weights(exam)
    indexed = list(enumerate(payload["candidates"]))
    candidates = [
        candidate
        for _, candidate in sorted(indexed, key=lambda item: (-item[1]["score"], item[0]))
    ]
    ranks = competition_ranks(candidates)

    svg = ET.parse(LADDER).getroot()
    errors: list[str] = []
    if svg.get("data-comparison-id") != COMPARISON_ID:
        errors.append("SVG comparison id does not match the fixed comparison")
    if svg.get("data-contract-sha256") != exam["contract_sha256"]:
        errors.append("SVG is not bound to the frozen exam contract")
    if svg.get("data-market-snapshot") != market["snapshot_date"]:
        errors.append("SVG market snapshot does not match the market universe")
    if svg.get("data-github-metrics-captured-at") != market.get("github_metrics_captured_at"):
        errors.append("SVG GitHub metrics timestamp does not match the market universe")
    pixels_per_point = float(svg.get("data-pixels-per-point", "nan"))
    global_bar_origin = float(svg.get("data-bar-origin", "nan"))

    rows = elements_with_class(svg, "candidate-row")
    if len(rows) != len(candidates):
        errors.append(f"SVG has {len(rows)} candidate rows; expected {len(candidates)}")
    else:
        for row, candidate, rank in zip(rows, candidates, ranks):
            name = candidate["candidate"]
            score = float(candidate["score"])
            prefix = f"{name}:"
            product = products_by_name.get(name, {})
            official_url = str(product.get("official_url", ""))
            stars = int(product.get("stars_at_snapshot", 0))
            if row.get("data-candidate") != name:
                errors.append(f"{prefix} row order/name differs from scorecard")
            if row.get("data-score") != display_number(score):
                errors.append(f"{prefix} data-score differs from {display_number(score)}")
            if row.get("data-rank") != str(rank):
                errors.append(f"{prefix} rank differs from {rank}")
            if row.get("data-url") != official_url:
                errors.append(f"{prefix} row URL differs from the market snapshot")
            if row.get("data-stars") != str(stars):
                errors.append(f"{prefix} row stars differ from the market snapshot")

            try:
                candidate_label = one_with_class(row, "candidate-label").text or ""
                candidate_link = one_with_class(row, "candidate-link")
                candidate_url = one_with_class(row, "candidate-url").text or ""
                star_label = one_with_class(row, "star-label").text or ""
                rank_label = one_with_class(row, "rank-label").text or ""
                score_label = one_with_class(row, "score-label").text or ""
                stage_label = one_with_class(row, "stage-label").text or ""
            except ValueError as error:
                errors.append(f"{prefix} {error}")
                continue
            if candidate_label != name:
                errors.append(f"{prefix} visible candidate label is stale")
            if candidate_link.get("href") != official_url:
                errors.append(f"{prefix} visible candidate link is stale")
            if candidate_url != official_url.removeprefix("https://"):
                errors.append(f"{prefix} visible GitHub URL is stale")
            if star_label != f"★ {display_stars(stars)}":
                errors.append(f"{prefix} visible GitHub stars are stale")
            if rank_label != f"{rank:02d}":
                errors.append(f"{prefix} visible rank label is stale")
            if score_label != display_number(score):
                errors.append(f"{prefix} visible score label is stale")
            if stage_label != candidate["evidence_stage"].upper():
                errors.append(f"{prefix} visible evidence stage is stale")

            segments = elements_with_class(row, "score-segment")
            active_pressures = [
                pressure
                for pressure, weight in weights.items()
                if weight > 0
            ]
            if [segment.get("data-pressure") for segment in segments] != active_pressures:
                errors.append(f"{prefix} score segments differ from active-C order")
                continue
            expected_x = ROW_BAR_ORIGIN
            contribution_values = pressure_contributions(exam, candidate)
            contribution_sum = 0.0
            for segment, pressure in zip(segments, active_pressures):
                contribution = contribution_values[pressure]
                contribution_sum += contribution
                width = contribution * pixels_per_point
                segment_x = float(segment.get("x", "nan"))
                segment_width = float(segment.get("width", "nan"))
                if abs(segment_x - expected_x) > 1e-9:
                    errors.append(f"{prefix} {pressure} segment starts at the wrong point")
                if abs(segment_width - width) > 1e-9:
                    errors.append(
                        f"{prefix} {pressure} width is {segment_width:g}; expected {width:g}"
                    )
                expected_x += width
            if abs(contribution_sum - score) > 1e-9:
                errors.append(f"{prefix} segment contributions do not sum to score")

    legend = {
        item.get("data-pressure"): item.get("data-weight")
        for item in elements_with_class(svg, "legend-item")
    }
    expected_legend = {
        pressure: str(weight) for pressure, weight in weights.items()
    }
    if legend != expected_legend:
        errors.append("legend weights differ from the fixed comparison")

    threshold_elements = elements_with_class(svg, "score-threshold")
    if [int(item.get("data-score", "-1")) for item in threshold_elements] != list(THRESHOLDS):
        errors.append("score thresholds are incomplete or out of order")
    else:
        for threshold, element in zip(THRESHOLDS, threshold_elements):
            expected_x = global_bar_origin + threshold * pixels_per_point
            if abs(float(element.get("x1", "nan")) - expected_x) > 1e-9:
                errors.append(f"threshold {threshold} is not aligned to the score scale")

    leader_score_value = float(candidates[0]["score"])
    leaders = [
        candidate for candidate in candidates
        if float(candidate["score"]) == leader_score_value
    ]
    leader_names = [(item.text or "") for item in elements_with_class(svg, "leader-candidate")]
    if leader_names != [item["candidate"] for item in leaders]:
        errors.append("leader callout candidates are stale")
    try:
        leader_score = one_with_class(svg, "leader-score").text or ""
        if leader_score != display_number(leader_score_value):
            errors.append("leader callout score is stale")
    except ValueError as error:
        errors.append(str(error))

    product_names = [product.get("name") for product in products]
    if len(product_names) != len(set(product_names)):
        errors.append("market universe contains duplicate product names")

    allowed_statuses = {"ranked", "source-audit-queued", "runtime-evidence-needed"}
    for product in products:
        name = product.get("name", "<unnamed>")
        status = product.get("status")
        if status not in allowed_statuses:
            errors.append(f"{name}: unsupported market status {status!r}")
        if not str(product.get("official_url", "")).startswith("https://"):
            errors.append(f"{name}: official_url must be HTTPS")
        if status == "ranked":
            if not str(product.get("official_url", "")).startswith("https://github.com/"):
                errors.append(f"{name}: ranked candidate requires an official GitHub URL")
            if int(product.get("stars_at_snapshot", 0)) < 10_000:
                errors.append(f"{name}: ranked candidate misses the market-presence gate")
        if status in {"source-audit-queued", "ranked"} and "pinned_commit" in product:
            commit = str(product.get("pinned_commit", ""))
            if len(commit) != 40 or any(character not in "0123456789abcdef" for character in commit):
                errors.append(f"{name}: public source entry requires a 40-character commit")

    ranked_names = {product["name"] for product in products if product["status"] == "ranked"}
    scorecard_names = {candidate["candidate"] for candidate in candidates}
    if ranked_names != scorecard_names:
        errors.append("ranked market products differ from the fixed comparison")

    expected_unranked = [product for product in products if product["status"] != "ranked"]
    expected_count = f"{len(candidates)} OPEN-SOURCE PRODUCTS · {len(candidates)} PINNED CODE AUDITS"
    try:
        visible_count = one_with_class(svg, "coverage-count").text or ""
        if visible_count != expected_count:
            errors.append("visible source coverage count is stale")
    except ValueError as error:
        errors.append(str(error))

    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1
    leader_text = (
        f"leader {leaders[0]['candidate']} at {display_number(leader_score_value)}"
        if len(leaders) == 1
        else f"{len(leaders)} leaders tied at {display_number(leader_score_value)}"
    )
    print(
        f"PASS 4C Harness Ladder: {len(candidates)} ranked, "
        f"{len(expected_unranked)} runtime-only tracked, {leader_text}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
