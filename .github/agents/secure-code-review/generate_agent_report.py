#!/usr/bin/env python3
"""
Generate a simple secure review markdown artifact.
This is a helper to produce a lightweight report for the `secure-code-review` agent to deposit in `output/`.

It enumerates files and dependencies (from requirements.txt) and creates a timestamped markdown file.
"""
from pathlib import Path
from datetime import datetime
import re

# When placed under `.github/agents/secure-code-review/` the repo root is two parents up
ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "output"
NOW = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
REPO_NAME = ROOT.name


def read_requirements(path: Path):
    reqs = []
    if path.exists():
        for line in path.read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if line and not line.startswith('#'):
                reqs.append(line)
    return reqs


def write_report(path: Path, files, reqs):
    now_iso = datetime.utcnow().isoformat() + 'Z'
    with path.open('w', encoding='utf-8') as fh:
        fh.write(f"# Secure Code Review — {REPO_NAME}\n")
        fh.write(f"**Generated:** {now_iso}\n\n")
        fh.write("## Summary Findings\n")
        fh.write("Provide validated findings, severity, and remediation steps here.\n\n")
        fh.write("## Files Examined\n")
        for f in files[:50]:
            fh.write(f"- {f}\n")
        fh.write("\n## Dependencies (requirements.txt)\n")
        if reqs:
            for r in reqs:
                fh.write(f"- {r}\n")
        else:
            fh.write("No `requirements.txt` found or it is empty.\n")
        fh.write("\n## Notes\n")
        fh.write("For full dependency vulnerability scanning, run a supply-chain scanner (e.g., `safety`, `dependabot`, or GH advisories) and attach results.\n\n")
        fh.write("## Generated-By\n")
        fh.write(f"Tool: generate_agent_report.py\nRepository: {REPO_NAME}\nTimestamp: {now_iso}\n")


if __name__ == '__main__':
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    files = [str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file()]
    reqs = read_requirements(ROOT / 'requirements.txt')
    out_name = f"secure_review-{REPO_NAME}-{NOW}.md"
    out_path = OUTPUT_DIR / out_name
    write_report(out_path, files, reqs)
    print(f"Wrote secure review report to {out_path}")
