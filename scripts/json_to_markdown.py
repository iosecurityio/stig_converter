#! python3

import json
from pathlib import Path


def color_severity(severity) -> str:
    """
    Colors the finding based on level of severity
    """

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
    tag = f'<span style="color:{color};font-size:110%;">{cat}: {title}</span>'
    return tag


def write_stigs(json_file, markdown_file):
    """
    Takes in a STIG checklist in JSON and outputs a new Markdown file
    """

    try:
        with open(json_file) as json_file:
            data = json.load(json_file)
        header = data["stig"]
        vulnids = header["findings"]
        print(f"[*] Writing {markdown_file}.")
        with open(markdown_file, "w", encoding="utf-8") as outfile:
            outfile.write("# Application Security and Development STIGs\n\n")
            outfile.write(f"**Date:** {header['date']}\n\n")
            outfile.write(f"**Description:** {header['description']}\n\n")
            outfile.write("---\n\n")

            for v in vulnids.values():
                outfile.write("## " + v.get("title") + "\n\n")
                outfile.write("|Severity|Vulnerability ID|Rule ID|\n")
                outfile.write("|:---:|:---:|:---:|\n")
                outfile.write(f"|{color_severity(v.get('severity'))}|{v.get('id')}|{v.get('ruleID')}|\n\n")
                outfile.write("### Description\n\n")
                outfile.write(v.get("description") + "\n\n")
                outfile.write("### Check Text\n\n")
                outfile.write(v.get("checktext") + "\n\n")
                outfile.write("|Check ID|\n")
                outfile.write("|---|\n")
                outfile.write(f"|{v.get('checkid')}|\n\n")
                outfile.write("### Fix Text \n\n")
                outfile.write(v.get("fixtext") + "\n\n")
                outfile.write("|Fix ID|\n")
                outfile.write("|---|\n")
                outfile.write(f"|{v.get('fixid')}|\n\n")

                outfile.write("---\n\n")
        print(f"[*] File {markdown_file} written.")
    except Exception as e:
        print(f"[X] Exception: {e}")


if __name__ == "__main__":
    data_dir = Path(__file__).parent.parent / "data"
    markdown_file = data_dir / "application_security_development.md"
    json_file = data_dir / "application_security_development.json"
    write_stigs(json_file=json_file, markdown_file=markdown_file)
