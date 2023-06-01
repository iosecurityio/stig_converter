# ckl_to_csv.py
# Convert STIGs .ckl checklists to .csv file

import csv
from datetime import datetime
import os
import xml.etree.ElementTree as ET

INPUT_FILE = r"tests/blank_checklist.ckl"  # Absolute path to CSV file
OUTPUT_LOC = r"tests"  # Absolute path for json output directory
# Current date timestamp to append to filename
DATE = datetime.now().strftime("%Y%m%d")


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
    filename = os.path.basename(ckl)
    new_filename = os.path.splitext(filename)
    new_csv = f"{csv_path}/{new_filename[0].replace(' ', '_')}-{DATE}.csv"

    with open(new_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        tree = ET.parse(ckl)
        root = tree.getroot()

        # create a dictionary to hold findings
        finding = {
            "DATE": DATE,
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
            finding["Unique_ID"] = f"{finding['HOST_NAME']}-{finding['Rule_ID']}-{DATE}"
            # Write the finding to the CSV
            writer.writerow(finding)
    # Return the location of the new CSV
    return new_csv


if __name__ == "__main__":
    try:
        if not INPUT_FILE or not OUTPUT_LOC:
            print("[X] Specify both input file and output location.")
            exit()
        out = convert_ckl_to_csv(ckl=INPUT_FILE, csv_path=OUTPUT_LOC)
        print(f"[*] Success! Output: {out}")
    except Exception as e:
        print(f"[X] Failed: {e}")
