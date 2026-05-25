# json_to_markdown.py
# Generate Markdown reports from STIG JSON data

import json
from pathlib import Path

from stig_converter.security_utils import validate_output_path, get_default_allowed_dirs

_HR = "---\n\n"

_SEVERITY_EMOJI = {
    "high":   ("🔴", "CAT-1"),
    "medium": ("🟠", "CAT-2"),
    "low":    ("🟡", "CAT-3"),
}


def _severity_label(severity: str) -> str:
    """Return an emoji-prefixed severity label, e.g. '🔴 CAT-1: High'."""
    severity = (severity or "low").lower()
    emoji, cat = _SEVERITY_EMOJI.get(severity, ("🟡", "CAT-3"))
    return f"{emoji} {cat}: {severity.capitalize()}"


def _write_finding_md(outfile, finding: dict) -> None:
    """Write a single checklist finding as a Markdown section."""
    vuln_num = finding.get("Vuln_Num", "")
    rule_title = finding.get("Rule_Title", "")
    severity = (finding.get("Severity") or "low").lower()
    status = finding.get("STATUS", "")
    details = finding.get("FINDING_DETAILS", "")
    comments = finding.get("COMMENTS", "")
    fix_text = finding.get("Fix_Text", "")

    outfile.write(f"### {vuln_num}: {rule_title}\n\n")
    outfile.write(f"**Severity:** {_severity_label(severity)} | **Status:** {status}\n\n")
    if details:
        outfile.write(f"**Finding Details:**\n\n{details}\n\n")
    if comments:
        outfile.write(f"**Comments:**\n\n{comments}\n\n")
    if fix_text:
        outfile.write(f"**Fix Text:**\n\n{fix_text}\n\n")
    outfile.write(_HR)


def _write_stigviewer_md(data: dict, output_path) -> str:
    """
    Write a Markdown report from an already-loaded stigviewer-format dict.
    Expected structure: {"stig": {"date": ..., "description": ..., "findings": {...}}}
    :param data: Parsed stigviewer JSON dict
    :param output_path: Output file path for the .md report
    :return: Path to the created Markdown file
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    header = data["stig"]
    vulnids = header["findings"]

    print(f"[*] Writing {output_path}.")
    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write("# Application Security and Development STIGs\n\n")
        outfile.write(f"**Date:** {header['date']}\n\n")
        outfile.write(f"**Description:** {header['description']}\n\n")
        outfile.write(_HR)

        for v in vulnids.values():
            outfile.write("## " + (v.get("title") or "") + "\n\n")
            outfile.write("| Severity | Vulnerability ID | Rule ID |\n")
            outfile.write("|:---:|:---:|:---:|\n")
            outfile.write(
                f"| {_severity_label(v.get('severity') or 'low')}"
                f" | {v.get('id') or ''}"
                f" | {v.get('ruleID') or ''} |\n\n"
            )
            outfile.write("### Description\n\n")
            outfile.write((v.get("description") or "") + "\n\n")
            outfile.write("### Check Text\n\n")
            outfile.write((v.get("checktext") or "") + "\n\n")
            outfile.write("| Check ID |\n")
            outfile.write("|---|\n")
            outfile.write(f"| {v.get('checkid') or ''} |\n\n")
            outfile.write("### Fix Text\n\n")
            outfile.write((v.get("fixtext") or "") + "\n\n")
            outfile.write("| Fix ID |\n")
            outfile.write("|---|\n")
            outfile.write(f"| {v.get('fixid') or ''} |\n\n")
            outfile.write(_HR)

    print(f"[*] File {output_path} written.")
    return str(output_path)


def write_stigs(json_file, markdown_file) -> str:
    """
    Generate a Markdown report from a stigviewer-format JSON file.
    Expected JSON structure: {"stig": {"date": ..., "description": ..., "findings": {...}}}
    :param json_file: Path to the stigviewer JSON file
    :param markdown_file: Output directory or file path for the .md
    :return: Path to the created Markdown file
    """
    validated_path = validate_output_path(
        markdown_file, json_file, get_default_allowed_dirs(), extension=".md"
    )
    with open(json_file, encoding="utf-8") as f:
        data = json.load(f)
    return _write_stigviewer_md(data, validated_path)


def _write_checklist_header(outfile, findings: list) -> None:
    """Write the host/date header block for a checklist report."""
    if not findings:
        return
    first = findings[0]
    host = first.get("HOST_NAME", "")
    ip = first.get("HOST_IP", "")
    date = first.get("DATE", "")
    if host or ip:
        line = f"**Host:** {host} ({ip})" if ip else f"**Host:** {host}"
        outfile.write(line + "\n\n")
    if date:
        outfile.write(f"**Date:** {date}\n\n")


def convert_checklist_to_md(findings: list, output_path) -> str:
    """
    Generate a Markdown report from a flat checklist findings list (ckl_to_json format).
    :param findings: List of finding dicts from convert_ckl_to_json or convert_csv_to_json
    :param output_path: Output file path for the .md report
    :return: Path to the created Markdown file
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    status_counts: dict = {}
    for f in findings:
        status = f.get("STATUS", "Unknown")
        status_counts[status] = status_counts.get(status, 0) + 1

    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write("# STIG Checklist Report\n\n")
        _write_checklist_header(outfile, findings)

        outfile.write("## Summary\n\n")
        outfile.write("| Status | Count |\n")
        outfile.write("|:---|:---:|\n")
        for status, count in sorted(status_counts.items()):
            outfile.write(f"| {status} | {count} |\n")
        outfile.write("\n---\n\n")

        open_findings = [f for f in findings if f.get("STATUS") == "Open"]
        if open_findings:
            outfile.write("## Open Findings\n\n")
            for finding in open_findings:
                _write_finding_md(outfile, finding)

        other_findings = [f for f in findings if f.get("STATUS") != "Open"]
        if other_findings:
            outfile.write("## All Other Findings\n\n")
            for finding in other_findings:
                _write_finding_md(outfile, finding)

    print(f"[*] New Markdown created: {output_path}")
    return str(output_path)


def convert_json_to_md(json_path, output_path) -> str:
    """
    Convert a JSON file to Markdown, dispatching on format.
    Handles both checklist format (list) produced by ckl_to_json/csv_to_json
    and stigviewer format (dict) produced by get_stig_json.
    :param json_path: Path to the input JSON file
    :param output_path: Output file path for the .md report
    :return: Path to the created Markdown file
    """
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return convert_checklist_to_md(data, output_path)
    return _write_stigviewer_md(data, output_path)
