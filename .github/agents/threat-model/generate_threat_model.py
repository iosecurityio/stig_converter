#!/usr/bin/env python3
"""
Generate a simple threat model markdown artifact for compliance evidence.
This script produces a timestamped markdown file under the repository `output/` directory.

It performs lightweight repository scanning to build a skeleton threat model.
"""
import os
from pathlib import Path
from datetime import datetime
import json

# When placed under `.github/agents/threat-model/` the repo root is two parents up
ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "output"
NOW = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
REPO_NAME = ROOT.name


def gather_files(root: Path):
    files = []
    for p in root.rglob("*"):
        if p.is_file() and not any(part.startswith(".git") for part in p.parts):
            files.append(str(p.relative_to(ROOT)))
    return sorted(files)


def detect_entrypoints(files):
    candidates = [f for f in files if f.endswith('.py') and ('main' in f or 'app' in f or 'server' in f)]
    if not candidates:
        candidates = [f for f in files if f.endswith('.py')][:3]
    return candidates


def write_threat_model(path: Path, files, entrypoints):
    now_iso = datetime.utcnow().isoformat() + 'Z'
    with path.open('w', encoding='utf-8') as fh:
        fh.write(f"# Threat Model — {REPO_NAME}\n")
        fh.write(f"**Generated:** {now_iso}\n\n")
        fh.write("## Executive Summary\n")
        fh.write("Short summary of scope, key assets, and top risks.\n\n")
        fh.write("## System Decomposition\n")
        fh.write("Describe components, services, and integrations.\n\n")
        fh.write("## Assets\n")
        fh.write("List of sensitive assets and where they reside.\n\n")
        fh.write("## Data Flows\n")
        fh.write("Describe main data flows and entries/exits.\n\n")
        fh.write("## Trust Boundaries\n")
        fh.write("Identify trust boundaries between components.\n\n")
        fh.write("## Threats (STRIDE)\n")
        fh.write("Enumerate threats by STRIDE categories with brief descriptions and examples.\n\n")
        fh.write("## Risk Prioritization\n")
        fh.write("Prioritize risks with rationale and risk rating (High/Medium/Low).\n\n")
        fh.write("## Mitigations and Controls\n")
        fh.write("Recommended design and implementation level mitigations.\n\n")
        fh.write("## Evidence and File References\n")
        fh.write("Files examined during threat modeling (partial list):\n\n")
        for f in entrypoints:
            fh.write(f"- {f}\n")
        fh.write("\nFull file inventory attached in JSON below.\n\n")
        fh.write("```")
        json.dump(files, fh, indent=2)
        fh.write("\n```")
        fh.write("\n## Control Mapping\n")
        fh.write("Map key mitigations to controls (e.g., NIST 800-53, DISA STIGs).\n\n")
        fh.write("## Generated-By\n")
        fh.write(f"Tool: generate_threat_model.py\nRepository: {REPO_NAME}\nTimestamp: {now_iso}\n")


if __name__ == '__main__':
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    files = gather_files(ROOT)
    entrypoints = detect_entrypoints(files)
    out_name = f"threat_model-{REPO_NAME}-{NOW}.md"
    out_path = OUTPUT_DIR / out_name
    write_threat_model(out_path, files, entrypoints)
    print(f"Wrote threat model to {out_path}")
