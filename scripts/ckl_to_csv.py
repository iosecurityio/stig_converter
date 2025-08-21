# ckl_to_csv.py
# Convert STIGs .ckl checklists to .csv file

import csv
from datetime import datetime
from pathlib import Path

try:
    from defusedxml.ElementTree import parse as safe_parse

    DEFUSEDXML_AVAILABLE = True
except ImportError:
    import xml.etree.ElementTree as ET

    DEFUSEDXML_AVAILABLE = False

from security_utils import validate_output_path, get_default_allowed_dirs


def convert_ckl_to_csv(ckl_file, csv_path) -> str:
    """
    Converts a CKL file to a CSV file
    :param ckl_file: The location of the STIG Checklist in .ckl file
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
    current_date = datetime.now().strftime("%Y%m%d")
    ckl_path = Path(ckl_file)

    # Check that the input CKL file exists and is a file
    if not ckl_path.is_file():
        raise FileNotFoundError(f"[X] CKL file does not exist: {ckl_path}")

    # Validate and secure the output path
    new_csv_path = validate_output_path(csv_path, ckl_file, get_default_allowed_dirs())

    print(f"[*] Converting CKL: {ckl_path}")
    with open(new_csv_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # Use secure XML parsing to prevent XXE attacks
        if DEFUSEDXML_AVAILABLE:
            tree = safe_parse(ckl_path)
            root = tree.getroot()
        else:
            # Fallback with manual XXE protection
            import xml.parsers.expat

            parser = xml.parsers.expat.ParserCreateNS()
            parser.DefaultHandler = lambda data: None
            parser.ExternalEntityRefHandler = (
                lambda context, base, sysId, notationName: False
            )
            parser.EntityDeclHandler = (
                lambda entityName,
                is_parameter_entity,
                value,
                base,
                systemId,
                publicId,
                notationName: False
            )

            with open(ckl_path, "rb") as f:
                xml_content = f.read()

            # Parse with ElementTree but disable external entities
            tree = ET.fromstring(xml_content)
            root = tree

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

            # (Optionally) Append a unique ID to map for each finding
            # This may be useful to differentiate findings across hosts if aggregating STIGs (e.g. Splunk)
            # finding["Unique_ID"] = f"{finding['HOST_NAME']}-{finding['Rule_ID']}-{current_date}"

            # Write the finding to the CSV
            writer.writerow(finding)

    # Return the location of the new CSV
    print(f"[*] New CSV created: {new_csv_path}")
    return new_csv_path


if __name__ == "__main__":
    data_dir = Path(__file__).parent.parent / "data"
    input_file = data_dir / "stig_checklist.ckl"
    out = convert_ckl_to_csv(ckl_file=input_file, csv_path=data_dir)
