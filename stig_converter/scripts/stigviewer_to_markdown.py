#! python3

import requests
import json

STIG_URL = "https://stigviewer.com/stig/application_security_and_development/2022-09-21/MAC-3_Sensitive/json"
FILENAME = "tests/AppSecDevSTIGs_Markdown.md"


def get_stigs(url=STIG_URL):
    """Takes a URL of a STIG Checklist in JSON, generally STIG Viewer API"""

    response = requests.get(url, timeout=5)
    stiglist = json.loads(response.text)
    return stiglist


def color_severity(severity) -> str:
    """Colors the finding based on level of severity"""

    if severity == "high":
        color = "#ff0000"
    elif severity == "medium":
        color = "#ff8c00"
    else:
        color = "#b3b31a"

    title = severity.capitalize()
    tag = f'<span style="color:{color};font-size:150%;">{title} Severity</span>'
    return tag


def write_stigs(stigs, newfile):
    """Takes in a STIG checklist in JSON and outputs a new Markdown file"""

    header = stigs["stig"]
    vulnids = header["findings"]
    print(f"[*] Writing {newfile}.")
    with open(newfile, "w", encoding="utf-8") as outfile:
        outfile.write("# Application Security and Development STIGs\n\n")
        outfile.write(f"**Date:** {header['date']}\n\n")
        outfile.write(f"**Description:** {header['description']}\n\n")
        outfile.write("---\n\n")

        for v in vulnids.values():
            outfile.write("## " + v.get("title") + "\n\n")
            outfile.write(color_severity(v.get("severity")) + "\n\n")
            outfile.write("### Description\n\n")
            outfile.write(v.get("description") + "\n\n")
            outfile.write("### Check Text\n\n")
            outfile.write(v.get("checktext") + "\n\n")
            outfile.write("**Check ID:**  " + v.get("checkid") + "\n\n")
            outfile.write("### Fix Text \n\n")
            outfile.write(v.get("fixtext") + "\n\n")
            outfile.write("**Fix ID:**  " + v.get("fixid") + "\n\n")
            outfile.write("**Vulnerability ID:**  " + v.get("id") + "\n\n")
            outfile.write("**Rule ID:**  " + v.get("ruleID") + "\n\n")
            outfile.write("---\n\n")
    print(f"[*] File {newfile} written.")


def main():
    """Takes a STIG Checklist in JSON and outputs a markdown file."""

    stiglist = get_stigs(url=STIG_URL)
    write_stigs(stigs=stiglist, newfile=FILENAME)


if __name__ == "__main__":
    main()
