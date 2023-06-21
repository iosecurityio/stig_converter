# ckl_to_csv.py
# Convert STIGs .ckl checklists to .csv file

import csv
from datetime import datetime
import os
import xml.etree.ElementTree as ET


def convert_ckl_to_csv(ckl, csv_path) -> str:
    """Converts a CKL file to a CSV file
    :param ckl: The location of the .ckl file to convert
    :param csv_path: The location to write the .csv file
    :return: The location of the new .csv file
    """

    # CKL is a custom XML and these are the field names we will pull from the document
    # Define your table headers as fieldnames
    fieldnames = [
        "DATE",
        "HOST_NAME",
        "HOST_IP",
        "Vuln_Num",
        "Severity",
        "Group_Title",
        "Rule_ID",
        "Rule_Ver",
        "Rule_Title",
        "Fix_Text",
        "STATUS",
        "FINDING_DETAILS",
        "COMMENTS",
        "Unique_ID",
    ]
    current_date = datetime.now().strftime('%Y%m%d')
    filename = os.path.basename(ckl)
    new_filename = os.path.splitext(filename)
    new_csv = f"{csv_path}{new_filename[0].replace(' ', '_')}-{current_date}.csv"

    with open(new_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        tree = ET.parse(ckl)
        root = tree.getroot()

        # create a dictionary to hold findings
        finding = {
            "DATE": current_date,
            "HOST_NAME": "",
            "HOST_IP": "",
        }
        # Parse the checklist Asset details
        for asset in root.iter("ASSET"):
            if asset.find("HOST_NAME").text:
                finding["HOST_NAME"] = asset.find("HOST_NAME").text
            if asset.find("HOST_IP").text:
                finding["HOST_IP"] = asset.find("HOST_IP").text

        for vuln in root.iter("VULN"):
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
            finding["Unique_ID"] = f"{finding['HOST_NAME']}-{finding['Rule_ID']}-{current_date}"
            # Write the finding to the CSV
            writer.writerow(finding)
    # Return the location of the new CSV
    return new_csv


if __name__ == "__main__":
    INPUT_FILE = r"data/stig_checklist.ckl"
    OUTPUT_LOC = r"tests/"
    out = convert_ckl_to_csv(ckl=INPUT_FILE, csv_path=OUTPUT_LOC)
    print(f"[*] Success! Output: {out}")
