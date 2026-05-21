# json_to_markdown.py
# Generate Markdown reports from STIG JSON data

import json
from pathlib import Path

from stig_converter.security_utils import validate_output_path, get_default_allowed_dirs


def color_severity(severity) -> str:
    """Colors the finding based on level of severity (stigviewer HTML format)."""
    if severity == "high":
        color = "#ff0000"
        cat = "CAT-1"
    elif severity == "medium":
        color = "#ff8c00"
        cat = "CAT-2"
    else:
        color = "#b3b31a"
        cat = "CAT-3"

    title = severity.capitalize()
    return f'<span style="color:{color};font-size:110%;">{cat}: {title}</span>'


def write_stigs(json_file, markdown_file) -> str:
    """
    Generate a Markdown report from a stigviewer-format JSON file.
    Expected JSON structure: {"stig": {"date": ..., "description": ..., "findings": {...}}}
    :param json_file: Path to the stigviewer JSON file
    :param markdown_file: Output directory or file path for the .md
    :return: Path to the created Markdown file
    """
    validated_markdown_file = validate_output_path(
        markdown_file, json_file, get_default_allowed_dirs(), extension=".md"
    )

    try:
        with open(json_file, encoding="utf-8") as f:
            data = json.load(f)
        header = data["stig"]
        vulnids = header["findings"]
        print(f"[*] Writing {validated_markdown_file}.")
        with open(validated_markdown_file, "w", encoding="utf-8") as outfile:
            outfile.write("# Application Security and Development STIGs\n\n")
            outfile.write(f"**Date:** {header['date']}\n\n")
            outfile.write(f"**Description:** {header['description']}\n\n")
            outfile.write("---\n\n")

            for v in vulnids.values():
                outfile.write("## " + (v.get("title") or "") + "\n\n")
                outfile.write("|Severity|Vulnerability ID|Rule ID|\n")
                outfile.write("|:---:|:---:|:---:|\n")
                outfile.write(
                    f"|{color_severity(v.get('severity') or 'low')}|{v.get('id') or ''}|{v.get('ruleID') or ''}|\n\n"
                )
                outfile.write("### Description\n\n")
                outfile.write((v.get("description") or "") + "\n\n")
                outfile.write("### Check Text\n\n")
                outfile.write((v.get("checktext") or "") + "\n\n")
                outfile.write("|Check ID|\n")
                outfile.write("|---|\n")
                outfile.write(f"|{v.get('checkid') or ''}|\n\n")
                outfile.write("### Fix Text \n\n")
                outfile.write((v.get("fixtext") or "") + "\n\n")
                outfile.write("|Fix ID|\n")
                outfile.write("|---|\n")
                outfile.write(f"|{v.get('fixid') or ''}|\n\n")
                outfile.write("---\n\n")
        print(f"[*] File {validated_markdown_file} written.")
    except Exception as e:
        print(f"[X] Exception: {e}")

    return str(validated_markdown_file)


def _write_finding_md(outfile, finding: dict) -> None:
    """Write a single checklist finding as a Markdown section."""
    vuln_num = finding.get("Vuln_Num", "")
    rule_title = finding.get("Rule_Title", "")
    severity = (finding.get("Severity") or "").capitalize()
    status = finding.get("STATUS", "")
    details = finding.get("FINDING_DETAILS", "")
    comments = finding.get("COMMENTS", "")
    fix_text = finding.get("Fix_Text", "")

    outfile.write(f"### {vuln_num}: {rule_title}\n\n")
    outfile.write(f"**Severity:** {severity} | **Status:** {status}\n\n")
    if details:
        outfile.write(f"**Finding Details:**\n\n{details}\n\n")
    if comments:
        outfile.write(f"**Comments:**\n\n{comments}\n\n")
    if fix_text:
        outfile.write(f"**Fix Text:**\n\n{fix_text}\n\n")
    outfile.write("---\n\n")


def convert_checklist_to_md(findings: list, output_path) -> str:
    """
    Generate a Markdown report from a flat checklist findings list (ckl_to_json format).
    :param findings: List of finding dicts from convert_ckl_to_json or convert_csv_to_json
    :param output_path: Output file path for the .md report
    :return: Path to the created Markdown file
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Compute status summary
    status_counts: dict = {}
    for f in findings:
        status = f.get("STATUS", "Unknown")
        status_counts[status] = status_counts.get(status, 0) + 1

    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write("# STIG Checklist Report\n\n")

        if findings:
            first = findings[0]
            host = first.get("HOST_NAME", "")
            ip = first.get("HOST_IP", "")
            date = first.get("DATE", "")
            if host or ip:
                outfile.write(f"**Host:** {host}")
                if ip:
                    outfile.write(f" ({ip})")
                outfile.write("\n\n")
            if date:
                outfile.write(f"**Date:** {date}\n\n")

        outfile.write("## Summary\n\n")
        outfile.write("| Status | Count |\n")
        outfile.write("|:---|:---:|\n")
        for status, count in sorted(status_counts.items()):
            outfile.write(f"| {status} | {count} |\n")
        outfile.write("\n---\n\n")

        # Open findings first for immediate visibility
        open_findings = [f for f in findings if f.get("STATUS") == "Open"]
        if open_findings:
            outfile.write("## Open Findings\n\n")
            for finding in open_findings:
                _write_finding_md(outfile, finding)

        # All other findings
        other_findings = [f for f in findings if f.get("STATUS") != "Open"]
        if other_findings:
            outfile.write("## All Other Findings\n\n")
            for finding in other_findings:
                _write_finding_md(outfile, finding)

    print(f"[*] New Markdown created: {output_path}")
    return str(output_path)
