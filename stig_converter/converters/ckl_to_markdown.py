# ckl_to_markdown.py
# Convert a STIG CKL (XML) checklist to a Markdown report via an intermediate JSON step.

import json
import tempfile
from pathlib import Path

from stig_converter.converters.ckl_to_json import convert_ckl_to_json
from stig_converter.converters.json_to_markdown import convert_checklist_to_md


def convert_ckl_to_md(ckl_path, output_path) -> str:
    """
    Convert a STIG CKL file to a Markdown report.
    Internally converts CKL → JSON (temp file) → Markdown.
    :param ckl_path: Path to the input .ckl file
    :param output_path: Output file path for the .md report
    :return: Path to the created Markdown file
    """
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        convert_ckl_to_json(ckl_path, tmp_path)
        with open(tmp_path, encoding="utf-8") as f:
            findings = json.load(f)
        return convert_checklist_to_md(findings, output_path)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()
