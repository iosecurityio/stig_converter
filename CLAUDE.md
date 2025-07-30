# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a STIG (Security Technical Implementation Guide) converter that transforms DISA STIG checklists between various file formats. The project converts between CKL (XML-based STIG checklists), CSV, JSON, and Markdown formats.

## Core Architecture

The codebase is currently in refactor mode, transitioning from individual scripts to a unified converter:

- **Main converter**: `stig_converter/stig_converter.py` contains the `STIGConverter` class and `Interface` CLI handler
- **Individual scripts**: `scripts/` directory contains standalone conversion utilities:
  - `ckl_to_csv.py` - Converts CKL (XML) to CSV format
  - `ckl_to_json.py` - Converts CKL to JSON format  
  - `csv_to_json.py` - Converts CSV to JSON format
  - `json_to_ckl.py` - Converts JSON back to CKL format
  - `json_to_markdown.py` - Generates readable Markdown reports from JSON
  - `get_new_stigs.py` - Downloads latest STIGs from stigviewer.com and DISA Cyber Exchange

## Development Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Common Commands

Since the main `stig_converter.py` is incomplete, use individual scripts for conversions:

```bash
# Convert CKL to CSV
python scripts/ckl_to_csv.py

# Convert JSON to Markdown report
python scripts/json_to_markdown.py

# Download latest STIGs
python scripts/get_new_stigs.py
```

## File Formats and Data Flow

**CKL Format**: XML-based STIG checklist format used by DISA. Contains vulnerability details, findings status, and asset information.

**JSON Format**: Normalized format with structure:
```json
[
  {
    "HOST_NAME": "hostname",
    "HOST_IP": "ip_address", 
    "Vuln_Num": "V-######",
    "Severity": "high|medium|low",
    "Rule_ID": "SV-######_rule",
    "Rule_Title": "Description",
    "STATUS": "Open|NotAFinding|Not_Reviewed",
    "FINDING_DETAILS": "details",
    "COMMENTS": "comments"
  }
]
```

**Conversion Flow**:
- CKL → CSV/JSON (primary input format)
- CSV → JSON (intermediate processing)
- JSON → CKL/Markdown (output formats)

## Key Implementation Details

- All scripts use `pathlib.Path` for cross-platform file handling
- XML parsing uses `xml.etree.ElementTree` for CKL files
- Date stamping follows `YYYYMMDD` format (e.g., `20250730`)
- Severity levels map to CAT-1 (high), CAT-2 (medium), CAT-3 (low)
- UTF-8 encoding is used throughout for international character support

## Data Directory Structure

The `data/` directory contains:
- Sample STIG checklists in various formats
- Downloaded STIG packages from DISA
- Generated output files with date stamps

## Current State

The main `stig_converter.py` is incomplete - the `STIGConverter` class lacks the actual conversion method implementations. The working functionality exists in the individual scripts under `scripts/`. The TODO indicates consolidating these into the main converter class.