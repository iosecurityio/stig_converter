# ckl_to_cklb.py
# Convert a STIG .ckl (XML) checklist to .cklb (JSON) format

import json
import logging
import uuid
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


def _text(element) -> str:
    """Safely return element text, or empty string if element is missing or has no text."""
    if element is None:
        return ""
    return element.text or ""


def _parse_stig_info(stig_info_el) -> dict:
    """Return a flat dict of SID_NAME → SID_DATA from a STIG_INFO element."""
    result = {}
    for si_data in stig_info_el.findall("SI_DATA"):
        name = _text(si_data.find("SID_NAME"))
        data = _text(si_data.find("SID_DATA"))
        if name:
            result[name] = data
    return result


def _parse_vuln(vuln_el) -> dict:
    """Parse a VULN element into a CKLB rule dict."""
    attrs = {}
    legacy_ids = []
    ccis = []

    for stig_data in vuln_el.findall("STIG_DATA"):
        attr_name = _text(stig_data.find("VULN_ATTRIBUTE"))
        attr_data = _text(stig_data.find("ATTRIBUTE_DATA"))
        if attr_name == "LEGACY_ID":
            legacy_ids.append(attr_data)
        elif attr_name == "CCI_REF":
            ccis.append(attr_data)
        elif attr_name:
            attrs[attr_name] = attr_data

    group_id = attrs.get("Vuln_Num", "")
    rule_id_src = attrs.get("Rule_ID", "")
    # Rule_ID in CKL is stored as "SV-xxxxxxx_rule"; strip the suffix for rule_id
    rule_id = rule_id_src.removesuffix("_rule")

    check_content_ref_name = attrs.get("Check_Content_Ref", "M")
    stig_ref = attrs.get("STIGRef", "")
    stig_uuid = attrs.get("STIG_UUID", "")
    rule_uuid = attrs.get("Rule_UUID", str(uuid.uuid4()))

    # CKL status values → CKLB lowercase equivalents
    ckl_status = _text(vuln_el.find("STATUS"))
    status_map = {
        "Not_Reviewed": "not_reviewed",
        "Open": "open",
        "NotAFinding": "not_a_finding",
        "Not_Applicable": "not_applicable",
    }
    status = status_map.get(ckl_status, "not_reviewed")

    return {
        "group_id_src": group_id,
        "group_tree": [
            {
                "id": group_id,
                "title": attrs.get("Group_Title", ""),
                "description": "<GroupDescription></GroupDescription>",
            }
        ],
        "group_id": group_id,
        "severity": attrs.get("Severity", ""),
        "group_title": attrs.get("Rule_Title", ""),
        "rule_id_src": rule_id_src,
        "rule_id": rule_id,
        "rule_version": attrs.get("Rule_Ver", ""),
        "rule_title": attrs.get("Rule_Title", ""),
        "fix_text": attrs.get("Fix_Text", ""),
        "weight": attrs.get("Weight", "10.0"),
        "check_content": attrs.get("Check_Content", ""),
        "check_content_ref": {"name": check_content_ref_name, "href": ""},
        "classification": attrs.get("Class", "Unclassified"),
        "discussion": attrs.get("Vuln_Discuss", ""),
        "false_positives": attrs.get("False_Positives", ""),
        "false_negatives": attrs.get("False_Negatives", ""),
        "documentable": attrs.get("Documentable", "false"),
        "security_override_guidance": attrs.get("Security_Override_Guidance", ""),
        "potential_impacts": attrs.get("Potential_Impact", ""),
        "third_party_tools": attrs.get("Third_Party_Tools", ""),
        "ia_controls": attrs.get("IA_Controls", ""),
        "responsibility": attrs.get("Responsibility", ""),
        "mitigations": attrs.get("Mitigations", ""),
        "mitigation_control": attrs.get("Mitigation_Control", ""),
        "legacy_ids": legacy_ids,
        "ccis": ccis,
        "reference_identifier": attrs.get("TargetKey", ""),
        "uuid": rule_uuid,
        "stig_uuid": stig_uuid,
        "status": status,
        "overrides": {},
        "comments": _text(vuln_el.find("COMMENTS")),
        "finding_details": _text(vuln_el.find("FINDING_DETAILS")),
        "srg_id": attrs.get("Group_Title", ""),
    }


def convert_ckl_to_cklb(ckl_file, cklb_path) -> str:
    """
    Convert a STIG CKL (XML) checklist to CKLB (JSON) format.
    :param ckl_file: Path to the input .ckl file
    :param cklb_path: Output directory or file path for the .cklb
    :return: Path to the created .cklb file
    """
    ckl_path = Path(ckl_file)
    if not ckl_path.is_file():
        raise FileNotFoundError(f"[X] CKL file does not exist: {ckl_path}")

    new_cklb_path = validate_output_path(
        cklb_path, ckl_file, get_default_allowed_dirs(), extension=".cklb"
    )

    print(f"[*] Converting CKL → CKLB: {ckl_path}")

    if DEFUSEDXML_AVAILABLE:
        tree = safe_parse(ckl_path)
    else:
        import xml.etree.ElementTree as ET
        tree = ET.parse(ckl_path)

    root = tree.getroot()

    # Asset / target data
    asset_el = root.find("ASSET")
    target_data = {
        "target_type": _text(asset_el.find("ASSET_TYPE")) if asset_el is not None else "Computing",
        "host_name": _text(asset_el.find("HOST_NAME")) if asset_el is not None else "",
        "ip_address": _text(asset_el.find("HOST_IP")) if asset_el is not None else "",
        "mac_address": _text(asset_el.find("HOST_MAC")) if asset_el is not None else "",
        "fqdn": _text(asset_el.find("HOST_FQDN")) if asset_el is not None else "",
        "comments": _text(asset_el.find("TARGET_COMMENT")) if asset_el is not None else "",
        "role": _text(asset_el.find("ROLE")) if asset_el is not None else "None",
        "is_web_database": _text(asset_el.find("WEB_OR_DATABASE")).lower() == "true" if asset_el is not None else False,
        "technology_area": _text(asset_el.find("TECH_AREA")) if asset_el is not None else "",
        "web_db_site": _text(asset_el.find("WEB_DB_SITE")) if asset_el is not None else "",
        "web_db_instance": _text(asset_el.find("WEB_DB_INSTANCE")) if asset_el is not None else "",
        "classification": None,
    }

    stigs = []
    for istig in root.findall(".//iSTIG"):
        stig_info_el = istig.find("STIG_INFO")
        info = _parse_stig_info(stig_info_el) if stig_info_el is not None else {}

        rules = [_parse_vuln(v) for v in istig.findall("VULN")]

        stigs.append({
            "stig_name": info.get("title", ""),
            "display_name": info.get("title", ""),
            "stig_id": info.get("stigid", ""),
            "release_info": info.get("releaseinfo", ""),
            "version": info.get("version", ""),
            "uuid": info.get("uuid", str(uuid.uuid4())),
            "reference_identifier": "",
            "size": len(rules),
            "rules": rules,
        })

    cklb = {
        "title": ckl_path.stem,
        "id": str(uuid.uuid4()),
        "stigs": stigs,
        "active": False,
        "mode": 1,
        "has_path": True,
        "target_data": target_data,
        "cklb_version": "1.0",
    }

    with open(new_cklb_path, "w", encoding="utf-8") as f:
        json.dump(cklb, f, indent=2)

    print(f"[*] New CKLB created: {new_cklb_path}")
    return str(new_cklb_path)
