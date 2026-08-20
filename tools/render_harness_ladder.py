#!/usr/bin/env python3
"""Render the README ladder from the frozen candidate-blind source exam."""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAM = ROOT / "docs/scouts/interactive-coding-v2-exam.json"
RESULTS = ROOT / "docs/scouts/interactive-coding-v2-results.json"
MARKET = ROOT / "docs/scouts/market-universe.json"
OUTPUT = ROOT / "assets/4c-harness-ladder.svg"
COMPARISON_ID = "interactive-coding-v2"
COLORS = {"Cost": "#FDBD2E", "Compatibility": "#2CC6B7", "Continuity": "#8B7CFF"}
LABELS = {"Cost": "COST EFFICIENCY", "Compatibility": "COMPATIBILITY", "Continuity": "CONTINUITY"}
PX = 9
ROW_X = 56
BAR_X = 414
GLOBAL_BAR_X = ROW_X + BAR_X


def competition_ranks(items: list[dict]) -> list[int]:
    out, last_score, last_rank = [], None, 0
    for position, item in enumerate(items, 1):
        if item["score"] != last_score:
            last_score, last_rank = item["score"], position
        out.append(last_rank)
    return out


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


def display(value: float) -> str:
    return str(int(value)) if float(value).is_integer() else f"{value:g}"


def display_stars(value: int) -> str:
    thousands = value / 1000
    rendered = f"{thousands:.1f}".removesuffix(".0")
    return f"{rendered}K"


def main() -> None:
    exam = json.loads(EXAM.read_text())
    data = json.loads(RESULTS.read_text())
    market = json.loads(MARKET.read_text())
    products = {product["name"]: product for product in market["products"]}
    indexed = list(enumerate(data["candidates"]))
    candidates = [x for _, x in sorted(indexed, key=lambda pair: (-pair[1]["score"], pair[0]))]
    weights = pressure_weights(exam)
    ranks = competition_ranks(candidates)
    top = candidates[0]["score"]
    leaders = [x for x in candidates if x["score"] == top]
    row_start, row_step, row_height = 318, 66, 56
    row_end = row_start + row_step * (len(candidates) - 1) + row_height
    footer_y = row_end + 52
    height = footer_y + 178
    esc = html.escape
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1792" height="{height}" viewBox="0 0 1792 {height}" role="img" aria-labelledby="title desc" data-comparison-id="{COMPARISON_ID}" data-contract-sha256="{exam["contract_sha256"]}" data-market-snapshot="{market["snapshot_date"]}" data-github-metrics-captured-at="{market["github_metrics_captured_at"]}" data-bar-origin="{GLOBAL_BAR_X}" data-pixels-per-point="{PX}">',
        '<title id="title">4C open-source Harness ladder for interactive coding</title>',
        f'<desc id="desc">Fifteen active open-source coding Harnesses answer the same frozen source exam. {esc(leaders[0]["candidate"])} leads at {display(top)}. Each row links to its official GitHub repository and shows a dated star snapshot. Stars do not affect the score. Longer bars mean better fit, not higher cost.</desc>',
        '<defs><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#B8C5D6" stroke-width="1" opacity=".28"/></pattern></defs>',
        f'<rect width="1792" height="{height}" fill="#EEF3F9"/><rect width="1792" height="{height}" fill="url(#grid)"/>',
        '<rect width="1792" height="44" fill="#101826"/>',
        '<text x="52" y="29" fill="#fff" font-family="SFMono-Regular,Menlo,monospace" font-size="15" font-weight="700" letter-spacing="3">4C // THE HARNESS EVALUATION STANDARD</text>',
        '<rect x="1480" y="8" width="260" height="28" fill="#FF5A36"/><text x="1610" y="28" text-anchor="middle" fill="#fff" font-family="SFMono-Regular,Menlo,monospace" font-size="14" font-weight="700" letter-spacing="2">PINNED · AUDITABLE</text>',
        '<text x="56" y="105" fill="#2457FF" font-family="SFMono-Regular,Menlo,monospace" font-size="18" font-weight="700" letter-spacing="3">4C OPEN-SOURCE HARNESS LADDER / 2026-08-19</text>',
        '<text x="52" y="163" fill="#101826" font-family="Arial Narrow,Helvetica Neue,Arial,sans-serif" font-size="62" font-weight="900" letter-spacing="-2">SEE A HARNESS. THINK 4C.</text>',
        '<text x="56" y="198" fill="#53657A" font-family="Helvetica Neue,Arial,sans-serif" font-size="19">Candidate-blind exam · 12 frozen questions · Exact commits · Missing evidence scores zero</text>',
        f'<text class="coverage-count" x="56" y="232" fill="#101826" font-family="SFMono-Regular,Menlo,monospace" font-size="14" font-weight="700">{len(candidates)} OPEN-SOURCE PRODUCTS · {len(candidates)} PINNED CODE AUDITS</text>',
        f'<text x="682" y="232" fill="#53657A" font-family="SFMono-Regular,Menlo,monospace" font-size="11">GITHUB STARS SNAPSHOT · {market["github_metrics_captured_at"]}</text>',
        '<g transform="translate(1160 70)"><rect width="576" height="174" fill="#101826"/>',
        '<text x="24" y="29" fill="#8FA3BC" font-family="SFMono-Regular,Menlo,monospace" font-size="12" letter-spacing="2">SOURCE EXAM LEADER · FIXED TEST V2</text>',
    ]
    for i, leader in enumerate(leaders):
        lines.append(f'<text class="leader-candidate" x="24" y="{61+i*21}" fill="#fff" font-family="Helvetica Neue,Arial,sans-serif" font-size="18" font-weight="800">{esc(leader["candidate"])}</text>')
    lines += [
        f'<text class="leader-score" x="546" y="144" text-anchor="end" fill="#FDBD2E" font-family="Arial Narrow,Helvetica Neue,Arial,sans-serif" font-size="58" font-weight="900">{display(top)}</text>',
        '<text x="546" y="163" text-anchor="end" fill="#8FA3BC" font-family="SFMono-Regular,Menlo,monospace" font-size="11">4C SOURCE EXAM / 100</text></g>',
        '<text x="56" y="284" fill="#6D7E92" font-family="SFMono-Regular,Menlo,monospace" font-size="11">RANK</text><text x="158" y="284" fill="#6D7E92" font-family="SFMono-Regular,Menlo,monospace" font-size="11">HARNESS / EVIDENCE</text>',
    ]
    for threshold, label in ((50, "CONDITIONAL"), (65, "STRONG"), (80, "EXCELLENT"), (100, "100")):
        x = GLOBAL_BAR_X + threshold * PX
        lines.append(f'<text x="{x}" y="272" text-anchor="middle" fill="#6D7E92" font-family="SFMono-Regular,Menlo,monospace" font-size="11">{threshold}</text>')
        lines.append(f'<text x="{x}" y="289" text-anchor="middle" fill="#6D7E92" font-family="SFMono-Regular,Menlo,monospace" font-size="10">{label}</text>')
        lines.append(f'<line class="score-threshold" data-score="{threshold}" x1="{x}" y1="298" x2="{x}" y2="{row_end}" stroke="#8393A7" stroke-width="1" stroke-dasharray="4 6" opacity=".5"/>')

    for idx, (item, rank) in enumerate(zip(candidates, ranks)):
        y = row_start + idx * row_step
        leader = item["score"] == top
        product = products[item["candidate"]]
        official_url = product["official_url"]
        visible_url = official_url.removeprefix("https://")
        stars = int(product["stars_at_snapshot"])
        bg, fg, sub, stroke = ("#101826", "#FFFFFF", "#8FA3BC", "#2457FF") if leader else ("#FFFFFF", "#101826", "#718196", "#C7D2E0")
        lines += [
            f'<!-- {esc(item["candidate"])} -->',
            f'<g class="candidate-row" data-candidate="{esc(item["candidate"])}" data-score="{display(item["score"])}" data-rank="{rank}" data-url="{esc(official_url)}" data-stars="{stars}" transform="translate({ROW_X} {y})">',
            f'<rect width="1680" height="{row_height}" fill="{bg}" stroke="{stroke}" stroke-width="{2 if leader else 1}"/>',
            f'<text class="rank-label" x="18" y="38" fill="{fg}" font-family="Arial Narrow,Helvetica Neue,Arial,sans-serif" font-size="31" font-weight="900">{rank:02d}</text>',
            f'<text class="candidate-label" x="98" y="23" fill="{fg}" font-family="Helvetica Neue,Arial,sans-serif" font-size="20" font-weight="800">{esc(item["candidate"])}</text>',
            f'<text class="candidate-url" x="98" y="43" fill="{sub}" font-family="SFMono-Regular,Menlo,monospace" font-size="8">{esc(visible_url)}</text>',
            f'<text class="star-label" x="398" y="43" text-anchor="end" fill="{sub}" font-family="SFMono-Regular,Menlo,monospace" font-size="10" font-weight="700">★ {display_stars(stars)}</text>',
            f'<a class="candidate-link" href="{esc(official_url)}" xlink:href="{esc(official_url)}" target="_blank" aria-label="Open {esc(item["candidate"])} on GitHub"><rect x="90" y="3" width="312" height="48" fill="#FFFFFF" fill-opacity="0"/></a>',
            f'<rect x="{BAR_X}" y="15" width="900" height="27" fill="{("#27354A" if leader else "#D9E1EB")}"/>',
        ]
        cursor = BAR_X
        contribution_values = pressure_contributions(exam, item)
        for pressure, weight in weights.items():
            if weight == 0:
                continue
            contribution = contribution_values[pressure]
            width = contribution * PX
            lines.append(f'<rect class="score-segment" data-pressure="{pressure}" x="{cursor:g}" y="15" width="{width:g}" height="27" fill="{COLORS[pressure]}"/>')
            cursor += width
        grade_text = f'CE{display(contribution_values["Cost"])} · K{display(contribution_values["Compatibility"])} · N{display(contribution_values["Continuity"])}'
        lines += [
            f'<text x="1360" y="23" fill="{sub}" font-family="SFMono-Regular,Menlo,monospace" font-size="9">{grade_text}</text>',
            f'<text class="stage-label" x="1360" y="42" fill="{sub}" font-family="SFMono-Regular,Menlo,monospace" font-size="8">{item["evidence_stage"].upper()}</text>',
            f'<text class="commit-label" x="1516" y="42" fill="{fg}" font-family="SFMono-Regular,Menlo,monospace" font-size="10" font-weight="700">{item["exact_commit"][:7]}</text>',
            f'<text class="score-label" x="1632" y="41" text-anchor="end" fill="{fg}" font-family="Arial Narrow,Helvetica Neue,Arial,sans-serif" font-size="37" font-weight="900">{display(item["score"])}</text>',
            '</g>',
        ]

    lines.append(f'<g transform="translate(56 {footer_y})" font-family="SFMono-Regular,Menlo,monospace">')
    lx = 0
    for pressure, weight in weights.items():
        if pressure == "Cognition":
            lines.append(f'<g class="legend-item" data-pressure="{pressure}" data-weight="{weight}"><text x="1120" y="17" fill="#718196" font-size="12">COGNITION 0% / INACTIVE</text></g>')
        else:
            lines.append(f'<g class="legend-item" data-pressure="{pressure}" data-weight="{weight}"><rect x="{lx}" width="18" height="18" fill="{COLORS[pressure]}"/><text x="{lx+28}" y="15" fill="#101826" font-size="13" font-weight="700">{LABELS[pressure]} {weight}%</text></g>')
            lx += {"Cost": 340, "Compatibility": 300, "Continuity": 270}[pressure]
    lines += [
        '<text x="0" y="52" fill="#2457FF" font-size="13" font-weight="700">LONGER BAR = MORE VERIFIED OUTPUT PER LIMIT. COST EFFICIENCY IS BETTER WHEN LONGER.</text>',
        '<line x1="0" y1="74" x2="1680" y2="74" stroke="#C7D2E0"/>',
        '<text x="0" y="102" fill="#101826" font-size="12">SCOPE  Active general-purpose open-source coding Harnesses with ≥10k GitHub stars</text>',
        '<text x="0" y="126" fill="#53657A" font-size="11">EXAM  12 frozen questions · 0 / HALF / FULL · No candidate-specific weights · Missing evidence = 0</text>',
        '<text x="0" y="150" fill="#53657A" font-size="11">BOUNDARY  Source examination only. Paired runtime trials may overturn this order. Contract hash pins the test.</text>',
        '<text x="0" y="172" fill="#53657A" font-size="11">POPULARITY  GitHub stars are dated context only and contribute 0 points to the 4C score.</text>',
        '</g></svg>',
    ]
    OUTPUT.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
