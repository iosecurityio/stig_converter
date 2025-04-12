# json_to_ckl
# Convert .json to STIG checklist .ckl file

import json
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path


def convert_json_to_ckl(json_file, ckl_path, base_ckl) -> str:
    """
    Populates a pre-existing STIG Checklist with the values of the equivalent items in a JSON file
    """

    current_date = datetime.now().strftime("%Y%m%d")
    json_path = Path(json_file)
    ckl_path = Path(ckl_path)
    base_ckl_path = Path(base_ckl)

    if not json_path.exists():
        raise FileNotFoundError(f"[X] JSON file does not exist: {json_path}")
    if not base_ckl_path.exists():
        raise FileNotFoundError(f"[X] Base checklist does not exist: {base_ckl_path}")

    if ckl_path.is_dir():
        new_ckl_path = ckl_path / f"{json_path.stem}-{current_date}.ckl"
    else:
        if not ckl_path.parent.exists():
            raise FileNotFoundError(f"[X] Destination directory does not exist: {ckl_path.parent}")
        new_ckl_path = ckl_path

    # Read in the JSON Data
    try:
        with open(json_path, "r") as read_file:
            loaded_data = json.load(read_file)
    except KeyError as ke:
        print(f"[X] JSON didn't load properly: {ke}")

    try:
        # Read in the STIG Checklist we are using as a template
        ckl_tree = ET.parse(base_ckl_path)
        ckl_root = ckl_tree.getroot()
    except Exception as e:
        print(f"[X] Invalid checklist {base_ckl_path}:\n\t{e}")

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
        print(f"[X] Error parsing {base_ckl_path}:\n\t{unbound_error}")

    # Turn the XML Root back into a string for writing
    encoding = "utf-8"
    new_xml = ET.tostring(ckl_root, encoding=encoding)

    # Write the modified XML to the new file
    with open(new_ckl_path, "wb") as ckl_file:
        # Custom header for xml declaration and STIG header comment
        ckl_file.write('<?xml version="1.0" encoding="UTF-8"?>\n'.encode(encoding))
        ckl_file.write("<!--DISA STIG Viewer :: 2.16-->\n".encode(encoding))
        ckl_file.write(new_xml)

    # Return the location of the new CKL
    print(f"[*] New CKL created: {new_ckl_path}")
    return new_ckl_path


if __name__ == "__main__":
    data_dir = Path(__file__).parent.parent / "data"
    json_file = data_dir / "stig_checklist-20230620.json"
    base_ckl = data_dir / "stig_checklist.ckl"
    convert_json_to_ckl(json_file=json_file, ckl_path=data_dir, base_ckl=base_ckl)
