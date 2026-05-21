# json_to_ckl.py
# Convert .json to STIG checklist .ckl file

import json
import xml.etree.ElementTree as ET
from pathlib import Path

from stig_converter.security_utils import validate_output_path, get_default_allowed_dirs

# Asset child tags that can be populated from JSON findings
_ASSET_FIELDS = {"HOST_NAME", "HOST_IP", "HOST_MAC", "HOST_FQDN", "TARGET_COMMENT"}


def _populate_asset(ckl_root, finding: dict) -> None:
    """Write asset-level fields from a JSON finding into the CKL template."""
    for asset in ckl_root.iter("ASSET"):
        for child in asset:
            if child.tag in _ASSET_FIELDS and child.tag in finding:
                child.text = finding[child.tag]


def _get_vuln_num(vuln):
    """Return the Vuln_Num value from a VULN element's STIG_DATA, or None."""
    for stig_data in vuln.findall("./STIG_DATA"):
        attr_elem = stig_data.find("VULN_ATTRIBUTE")
        if attr_elem is not None and attr_elem.text == "Vuln_Num":
            data_elem = stig_data.find("ATTRIBUTE_DATA")
            return data_elem.text if data_elem is not None else None
    return None


def _apply_finding(vuln, finding: dict) -> None:
    """Write STATUS, FINDING_DETAILS, and COMMENTS from a JSON finding into a VULN element."""
    for tag in ("STATUS", "FINDING_DETAILS", "COMMENTS"):
        elem = vuln.find(f"./{tag}")
        if elem is not None and tag in finding:
            elem.text = finding[tag]


def convert_json_to_ckl(json_file, ckl_path, base_ckl) -> str:
    """
    Populates a pre-existing STIG Checklist with the values of the equivalent items in a JSON file.
    :param json_file: Path to the JSON findings file
    :param ckl_path: Output directory or file path for the new .ckl
    :param base_ckl: Path to the base CKL template to populate
    :return: Path to the created .ckl file
    """
    json_path = Path(json_file)
    base_ckl_path = Path(base_ckl)

    if not json_path.exists():
        raise FileNotFoundError(f"[X] JSON file does not exist: {json_path}")
    if not base_ckl_path.exists():
        raise FileNotFoundError(f"[X] Base checklist does not exist: {base_ckl_path}")

    new_ckl_path = validate_output_path(
        ckl_path, json_file, get_default_allowed_dirs(), extension=".ckl"
    )

    with open(json_path, "r", encoding="utf-8") as read_file:
        loaded_data = json.load(read_file)

    ckl_tree = ET.parse(base_ckl_path)
    ckl_root = ckl_tree.getroot()

    if loaded_data:
        _populate_asset(ckl_root, loaded_data[0])

    # Build a lookup of findings by Vuln_Num for O(1) matching
    findings_by_vuln = {f["Vuln_Num"]: f for f in loaded_data if "Vuln_Num" in f}

    for vuln in ckl_root.iter("VULN"):
        vuln_num = _get_vuln_num(vuln)
        if vuln_num in findings_by_vuln:
            _apply_finding(vuln, findings_by_vuln[vuln_num])

    # Serialize without ET's own XML declaration, then write our canonical header
    new_xml = ET.tostring(ckl_root, encoding="unicode")

    with open(new_ckl_path, "w", encoding="utf-8") as ckl_file:
        ckl_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        ckl_file.write("<!--DISA STIG Viewer :: 2.16-->\n")
        ckl_file.write(new_xml)

    print(f"[*] New CKL created: {new_ckl_path}")
    return str(new_ckl_path)
