# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`stig_converter` is a unified CLI tool that converts DISA STIG checklists between file formats and downloads the latest STIG data from remote sources.

## Core Architecture

- **CLI entry point**: `stig_converter/stig_converter.py` — `STIGConverter` class with a `_DISPATCH` table, `create_parser()`, and `main()`
- **Converters**: `stig_converter/converters/` — one file per conversion pair, each exposing a single public `convert_*` function
- **Fetch utilities**: `stig_converter/get_new_stigs.py` — downloads STIGs from stigviewer.com and DISA Cyber Exchange
- **Security**: `stig_converter/security_utils.py` — path validation anchored to project root

### Supported conversions

| Input   | Output                          | Notes                                             |
| ------- | ------------------------------- | ------------------------------------------------- |
| `.ckl`  | `.csv`, `.json`, `.md`, `.cklb` |                                                   |
| `.cklb` | `.ckl`                          |                                                   |
| `.csv`  | `.json`                         |                                                   |
| `.json` | `.ckl`, `.md`                   | JSON → CKL requires `--template-ckl`              |
| `.xml`  | `.ckl`, `.cklb`                 | DISA XCCDF Benchmark; all findings → Not_Reviewed |

### Converter files

| File | Conversion |
| ---- | ---------- |
| `ckl_to_csv.py` | CKL → CSV |
| `ckl_to_json.py` | CKL → JSON |
| `ckl_to_markdown.py` | CKL → Markdown (via JSON intermediate) |
| `ckl_to_cklb.py` | CKL → CKLB |
| `cklb_to_ckl.py` | CKLB → CKL |
| `csv_to_json.py` | CSV → JSON |
| `json_to_ckl.py` | JSON → CKL |
| `json_to_markdown.py` | JSON → Markdown |
| `xccdf_to_ckl.py` | XCCDF XML → CKL |
| `xccdf_to_cklb.py` | XCCDF XML → CKLB |

## Development Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

## Common Commands

```bash
# Convert
stig_converter convert -i data/checklist.ckl -o data/report.csv
stig_converter convert -i data/U_ASD_STIG_V6R4_Manual-xccdf.xml -o data/checklist.ckl

# Fetch latest STIGs
stig_converter fetch --json data/latest_stigs.json
stig_converter fetch --zip data/U_ASD_V6R4_STIG.zip

# Run tests (always do this after any change)
python -m pytest tests/ -v
```

## File Formats

**CKL**: XML-based STIG checklist used by DISA STIG Viewer.
**CKLB**: JSON-based STIG checklist used by DISA STIG Viewer 3+.
**XCCDF XML**: DISA Benchmark definition included in official STIG ZIP packages.
**JSON**: Normalized flat list of findings produced by `ckl_to_json`/`csv_to_json`.

## Key Implementation Details

- All paths validated against project root via `security_utils.get_default_allowed_dirs()`
- XML parsing uses `defusedxml` (falls back to stdlib with a warning)
- XCCDF description fields are XML-escaped sub-tags parsed with regex
- UUIDs in CKL/CKLB are generated deterministically with `uuid.uuid5` from rule/benchmark IDs
- Status mapping: CKL `Not_Reviewed` ↔ CKLB `not_reviewed`, `Open` ↔ `open`, `NotAFinding` ↔ `not_a_finding`, `Not_Applicable` ↔ `not_applicable`
- Date stamps follow `YYYYMMDD` format
- UTF-8 encoding throughout

## Non-Negotiable Development Rules

These rules apply to every change, no exceptions:

1. **Run tests after every change**: `python -m pytest tests/ -v` must pass before a task is considered done. Add new tests when fixing bugs or adding features.

2. **Update README.md with every functional change**: New converters, CLI options, or behaviors must be reflected in the Usage section with accurate, working examples. Examples must include the subcommand (`stig_converter convert ...`).

3. **Clean up orphaned files immediately**: Any file that is moved, replaced, or accidentally created must be deleted before finishing. Run `git status` to verify before marking a task done.

4. **No stale functionality**: When a feature is moved or replaced, remove the old location and all references to it. Do not leave dead imports, unused functions, or outdated comments.

5. **Live smoke test CLI changes**: For any change to the CLI (new subcommand, new option, new converter), do a live `stig_converter ...` run from the project root to confirm it works end-to-end before finishing.
