# ckl_to_json.py
# Convert STIG .ckl to .json

import json
import logging
from datetime import datetime
from pathlib import Path

try:
    from defusedxml.ElementTree import parse as safe_parse

    DEFUSEDXML_AVAILABLE = True
except ImportError:
    import xml.etree.ElementTree as ET

    DEFUSEDXML_AVAILABLE = False
    logging.warning(
        "defusedxml not installed — XML parsing has reduced XXE protection. "
        "Install it with: pip install defusedxml"
    )

from stig_converter.security_utils import validate_output_path, get_default_allowed_dirs

_VULN_ATTRIBUTES = {
    "Vuln_Num", "Severity", "Group_Title", "Rule_ID",
    "Rule_Ver", "Rule_Title", "Fix_Text",
}


def _text(element) -> str:
    """Safely return element text, or empty string if element is missing or has no text."""
    if element is None:
        return ""
    return element.text or ""


def convert_ckl_to_json(ckl_file, json_path) -> str:
    """
    Converts a STIG Checklist .CKL file to .JSON.
    :param ckl_file: Path to the .ckl file to convert
    :param json_path: Output directory or file path for the .json
    :return: Path to the created .json file
    """
    current_date = datetime.now().strftime("%Y%m%d")
    ckl_path = Path(ckl_file)

    if not ckl_path.is_file():
        raise FileNotFoundError(f"[X] CKL file does not exist: {ckl_path}")

    new_json_path = validate_output_path(
        json_path, ckl_file, get_default_allowed_dirs(), extension=".json"
    )

    print(f"[*] Converting CKL: {ckl_path}")

    if DEFUSEDXML_AVAILABLE:
        tree = safe_parse(ckl_path)
        root = tree.getroot()
    else:
        tree = ET.parse(ckl_path)
        root = tree.getroot()

    # Parse asset-level details once; last ASSET element wins if multiple exist
    host_name = ""
    host_ip = ""
    for asset in root.iter("ASSET"):
        host_name = _text(asset.find("HOST_NAME"))
        host_ip = _text(asset.find("HOST_IP"))

    findings = []
    for vuln in root.iter("VULN"):
        # Build a fresh dict per vuln so no stale data from prior iterations
        finding = {
            "DATE": current_date,
            "HOST_NAME": host_name,
            "HOST_IP": host_ip,
        }

        for stig_data in vuln.findall("./STIG_DATA"):
            attr_name = _text(stig_data.find("VULN_ATTRIBUTE"))
            if attr_name in _VULN_ATTRIBUTES:
                finding[attr_name] = _text(
                    stig_data.find("ATTRIBUTE_DATA")
                ).replace("\n", " ")

        finding["STATUS"] = _text(vuln.find("./STATUS"))
        finding["FINDING_DETAILS"] = _text(vuln.find("./FINDING_DETAILS"))
        finding["COMMENTS"] = _text(vuln.find("./COMMENTS"))

        findings.append(finding)

    with open(new_json_path, "w", encoding="utf-8") as json_file:
        json.dump(findings, json_file, indent=4)

    print(f"[*] New JSON Created: {new_json_path}")
    return str(new_json_path)
