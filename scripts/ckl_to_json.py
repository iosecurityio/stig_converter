# ckl_to_json.py
# Convert STIG .ckl to .json

import json
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path


def convert_ckl_to_json(ckl_file, json_path) -> str:
    """Converts a STIG Checklist .CKL file to .JSON
    :param ckl_file: The location of the .ckl file to convert
    :param json_path: The location path to write the .json file
    :return: The absolute path of the new .json file
    """

    current_date = datetime.now().strftime("%Y%m%d")

    ckl_path = Path(ckl_file)
    json_path = Path(json_path)

    if not ckl_path.is_file():
        raise FileNotFoundError(f"[X] CKL file does not exist: {ckl_path}")
    if json_path.is_dir():
        new_json_path = json_path / f"{ckl_file.stem}-{current_date}.json"
    else:
        if not json_path.parent.exists():
            raise FileNotFoundError(f"[X] Destination directory does not exist: {json_path}")
        new_json_path = json_path

    print(f"[*] Converting CKL: {ckl_path}")
    with open(new_json_path, "w", newline="", encoding="utf-8") as jsonfile:
        # Create an xml object from the ckl file
        tree = ET.parse(ckl_file)
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
            finding["DATE"] = current_date
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

            # (Optionally) Append a unique ID to map for each finding
            # This may be useful to differentiate findings across hosts if aggregating STIGs (e.g. Splunk)            # Append a unique ID to map for each finding
            # finding["Unique_ID"] = f"{host_name}-{finding['Rule_ID']}-{current_date}"

            # Add the finding to our finding list
            findings.append(finding)

        # Dump the finding dictionary into the file we are creating
        json.dump(findings, jsonfile, indent=4)

    # Return the location of the new json doc
    print(f"[*] New JSON Created: {new_json_path}")
    return new_json_path


if __name__ == "__main__":
    data_dir = Path(__file__).parent.parent / "data"
    input_file = data_dir / "stig_checklist.ckl"
    out = convert_ckl_to_json(ckl_file=input_file, json_path=data_dir)
