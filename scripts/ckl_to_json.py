# ckl_to_json.py
# Convert STIG .ckl to .json

from datetime import datetime
import json
import os
import xml.etree.ElementTree as ET

INPUT_FILE = r"data/stig_checklist.ckl"
OUTPUT_LOC = r"tests/"
# Current date timestamp to append to filename
DATE = datetime.now().strftime("%Y%m%d")


def convert_ckl_to_json(ckl, json_path) -> str:
    """Converts a STIG Checklist .CKL file to .JSON
    :param ckl: The location of the .ckl file to convert
    :param json_path: The location path to write the .json file
    :return: The absolute path of the new .json file
    """

    filename = os.path.basename(ckl)
    new_filename = os.path.splitext(filename)
    # TODO Handle the / in the path
    new_location = f"{json_path}/{new_filename[0].replace(' ', '_')}-{DATE}.json"

    with open(new_location, "w", newline="", encoding="utf-8") as jsonf:
        # Create an xml object from the ckl file
        tree = ET.parse(ckl)
        root = tree.getroot()
        # Initialize hostname and IP before we parse checklist
        host_name = ""
        host_ip = ""
        # Create a list of findings
        findings = []

        # Parse the checklist Asset details
        for asset in root.iter("ASSET"):
            if asset.find("HOST_NAME").text:
                host_name = asset.find("HOST_NAME").text
            if asset.find("HOST_IP").text:
                host_ip = asset.find("HOST_IP").text

        # Parse the checklists individual Vulnerabilities
        for vuln in root.iter("VULN"):
            # Create a finding dict to hold each finding info
            finding = {}
            finding["DATE"] = DATE
            finding["HOST_NAME"] = host_name
            finding["HOST_IP"] = host_ip
            for stig_data in vuln.findall("./STIG_DATA"):
                if stig_data.find("VULN_ATTRIBUTE").text in [
                    "Vuln_Num",
                    "Severity",
                    "Group_Title",
                    "Rule_ID",
                    "Rule_Ver",
                    "Rule_Title",
                    "Fix_Text",
                ]:
                    finding[stig_data.find("VULN_ATTRIBUTE").text] = stig_data.find(
                        "ATTRIBUTE_DATA"
                    ).text.replace("\n", " ")
            finding["STATUS"] = vuln.find("./STATUS").text
            finding["FINDING_DETAILS"] = vuln.find("./FINDING_DETAILS").text
            finding["COMMENTS"] = vuln.find("./COMMENTS").text
            # Append a unique ID to map for each finding
            finding["Unique_ID"] = f"{host_name}-{finding['Rule_ID']}-{DATE}"
            # Add the finding to our finding list
            findings.append(finding)
        # Dump the finding dictionary into the file we are creating
        json.dump(findings, jsonf, indent=4)

    # Return the location of the new json doc
    return new_location


if __name__ == "__main__":
    try:
        if not INPUT_FILE or not OUTPUT_LOC:
            print("[X] Specify both input file and output location.")
            exit()
        out = convert_ckl_to_json(ckl=INPUT_FILE, json_path=OUTPUT_LOC)
        print(f"[*] Success! Output: {out}")
    except Exception as e:
        print(f"[X] Failed: {e}")
