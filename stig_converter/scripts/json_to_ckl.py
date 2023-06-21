# json_to_ckl
# Convert .json to STIG checklist .ckl file

from datetime import datetime
import json
import xml.etree.ElementTree as ET


def convert_json_to_ckl(
    json_data, ckl_path, base_ckl=r"data/stig_checklist.ckl"
) -> str:
    """Populates a STIG Checklist with the JSON equivalent values"""

    # Read in the JSON Data
    try:
        with open(json_data, "r") as read_file:
            loaded_data = json.load(read_file)
    except FileNotFoundError as fnf:
        print(f"[X] JSON didn't load properly: {fnf}")
    except KeyError as ke:
        print(f"[X] JSON didn't load properly: {ke}")

    try:
        # Read in the STIG Checklist we are using as a template
        ckl_tree = ET.parse(base_ckl)
        ckl_root = ckl_tree.getroot()
    except Exception as e:
        print(f"[X] Invalid checklist {base_ckl}:\n\t{e}")

    # List of elements under the Asset element in the XML structure
    ASSET = ["HOST_NAME", "HOST_IP", "HOST_MAC", "HOST_FQDN", "TARGET_COMMENT"]
    try:
        for element in ckl_root.iter("ASSET"):
            # Populate the element in the Asset section
            if element.tag in ASSET:
                element.text = loaded_data[0][element]

        # For every Vulnerability in the checklist
        for vuln in ckl_root.iter("VULN"):
            # Iterate through every finding Dict in the JSON
            for json_finding in loaded_data:
                for stig_data in vuln.iter("STIG_DATA"):
                    if (
                        stig_data.tag == "VULN_ATTRIBUTE"
                        and stig_data.text in json_finding
                    ):
                        attribute_data = stig_data.find("ATTRIBUTE_DATA")
                        attribute_data.text = json_finding[stig_data.text]
    except UnboundLocalError as unbound_error:
        print(f"[X] Error parsing {base_ckl}:\n\t{unbound_error}")

    # Turn the XML Root back into a string for writing
    encoding = "utf-8"
    new_xml = ET.tostring(ckl_root, encoding=encoding)

    # Write the modified XML to the new file
    with open(ckl_path, "wb") as output_file:
        # Custom header for xml declaration and STIG header comment
        output_file.write('<?xml version="1.0" encoding="UTF-8"?>\n'.encode(encoding))
        output_file.write("<!--DISA STIG Viewer :: 2.16-->\n".encode(encoding))
        output_file.write(new_xml)


if __name__ == "__main__":
    JSON_DATA = r"tests/stig_checklist-20230620.json"
    # TODO: Handle output of filename in this script
    OUTPUT_LOC = r"tests/stig_checklist-20230620.ckl"
    # Current date timestamp to append to filename
    DATE = datetime.now().strftime("%Y%m%d")

    print("[*] Converting JSON to CKL...")
    convert_json_to_ckl(json_data=JSON_DATA, ckl_path=OUTPUT_LOC)
    print(f"[*] Converted! {OUTPUT_LOC}")
