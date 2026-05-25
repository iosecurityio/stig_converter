# xccdf_to_cklb.py
# Convert a DISA XCCDF Benchmark XML file to a STIG Viewer CKLB (JSON) checklist

import json
import logging
import re
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

_NS = "http://checklists.nist.gov/xccdf/1.1"

_DESC_TAGS = [
    "VulnDiscussion",
    "FalsePositives",
    "FalseNegatives",
    "Documentable",
    "Mitigations",
    "SeverityOverrideGuidance",
    "PotentialImpacts",
    "ThirdPartyTools",
    "MitigationControl",
    "Responsibility",
    "IAControls",
]


def _x(el) -> str:
    return (el.text or "") if el is not None else ""


def _find(el, tag: str):
    return el.find(f"{{{_NS}}}{tag}")


def _parse_description(raw: str) -> dict:
    """Extract named sub-tags from the XML-escaped description string."""
    result = {}
    for tag in _DESC_TAGS:
        m = re.search(rf"<{tag}>(.*?)</{tag}>", raw, re.DOTALL)
        result[tag] = m.group(1).strip() if m else ""
    return result


def _parse_benchmark(root) -> dict:
    return {
        "stigid":      root.attrib.get("id", ""),
        "title":       _x(_find(root, "title")),
        "version":     _x(_find(root, "version")),
        "releaseinfo": _x(root.find(f"{{{_NS}}}plain-text[@id='release-info']")),
    }


def _build_rule(group, rule, stig_uuid: str) -> dict:
    group_id = group.attrib.get("id", "")
    group_title = _x(_find(group, "title"))
    rule_id_src = rule.attrib.get("id", "")
    rule_id = rule_id_src.removesuffix("_rule")
    severity = rule.attrib.get("severity", "")
    weight = rule.attrib.get("weight", "10.0")
    rule_ver = _x(_find(rule, "version"))
    rule_title = _x(_find(rule, "title"))
    fixtext = _x(_find(rule, "fixtext"))

    raw_desc = _x(_find(rule, "description"))
    desc = _parse_description(raw_desc)

    check = _find(rule, "check")
    check_content = ""
    check_content_ref = {"name": "M", "href": ""}
    if check is not None:
        check_content = _x(_find(check, "check-content"))
        cref = check.find(f"{{{_NS}}}check-content-ref")
        if cref is not None:
            check_content_ref = {
                "name": cref.attrib.get("name", "M"),
                "href": cref.attrib.get("href", ""),
            }

    legacy_ids = []
    ccis = []
    for ident in rule.findall(f"{{{_NS}}}ident"):
        system = ident.attrib.get("system", "")
        val = ident.text or ""
        if "legacy" in system:
            legacy_ids.append(val)
        elif "cci" in system:
            ccis.append(val)

    rule_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, rule_id_src))

    return {
        "group_id_src": group_id,
        "group_tree": [
            {
                "id": group_id,
                "title": group_title,
                "description": "<GroupDescription></GroupDescription>",
            }
        ],
        "group_id": group_id,
        "severity": severity,
        "group_title": rule_title,
        "rule_id_src": rule_id_src,
        "rule_id": rule_id,
        "rule_version": rule_ver,
        "rule_title": rule_title,
        "fix_text": fixtext,
        "weight": weight,
        "check_content": check_content,
        "check_content_ref": check_content_ref,
        "classification": "Unclassified",
        "discussion": desc.get("VulnDiscussion", ""),
        "false_positives": desc.get("FalsePositives", ""),
        "false_negatives": desc.get("FalseNegatives", ""),
        "documentable": desc.get("Documentable", "false"),
        "security_override_guidance": desc.get("SeverityOverrideGuidance", ""),
        "potential_impacts": desc.get("PotentialImpacts", ""),
        "third_party_tools": desc.get("ThirdPartyTools", ""),
        "ia_controls": desc.get("IAControls", ""),
        "responsibility": desc.get("Responsibility", ""),
        "mitigations": desc.get("Mitigations", ""),
        "mitigation_control": desc.get("MitigationControl", ""),
        "legacy_ids": legacy_ids,
        "ccis": ccis,
        "reference_identifier": "",
        "uuid": rule_uuid,
        "stig_uuid": stig_uuid,
        "status": "not_reviewed",
        "overrides": {},
        "comments": "",
        "finding_details": "",
        "srg_id": group_title,
    }


def convert_xccdf_to_cklb(xccdf_file, cklb_path) -> str:
    """
    Convert a DISA XCCDF Benchmark XML file to a blank STIG Viewer CKLB checklist.
    All findings default to not_reviewed with empty details and comments.
    :param xccdf_file: Path to the input XCCDF .xml file
    :param cklb_path: Output directory or file path for the .cklb
    :return: Path to the created .cklb file
    """
    xccdf_path = Path(xccdf_file)
    if not xccdf_path.is_file():
        raise FileNotFoundError(f"[X] XCCDF file does not exist: {xccdf_path}")

    new_cklb_path = validate_output_path(
        cklb_path, xccdf_file, get_default_allowed_dirs(), extension=".cklb"
    )

    print(f"[*] Converting XCCDF → CKLB: {xccdf_path}")

    if DEFUSEDXML_AVAILABLE:
        tree = safe_parse(xccdf_path)
    else:
        import xml.etree.ElementTree as ET
        tree = ET.parse(xccdf_path)

    root = tree.getroot()
    meta = _parse_benchmark(root)

    stig_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, meta["stigid"]))

    groups = root.findall(f".//{{{_NS}}}Group")
    rules = []
    for group in groups:
        rule = group.find(f"{{{_NS}}}Rule")
        if rule is None:
            continue
        rules.append(_build_rule(group, rule, stig_uuid))

    cklb = {
        "title": xccdf_path.stem,
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, meta["stigid"] + "-cklb")),
        "stigs": [
            {
                "stig_name": meta["title"],
                "display_name": meta["title"],
                "stig_id": meta["stigid"],
                "release_info": meta["releaseinfo"],
                "version": meta["version"],
                "uuid": stig_uuid,
                "reference_identifier": "",
                "size": len(rules),
                "rules": rules,
            }
        ],
        "active": False,
        "mode": 1,
        "has_path": True,
        "target_data": {
            "target_type": "Computing",
            "host_name": "",
            "ip_address": "",
            "mac_address": "",
            "fqdn": "",
            "comments": "",
            "role": "None",
            "is_web_database": False,
            "technology_area": "",
            "web_db_site": "",
            "web_db_instance": "",
            "classification": None,
        },
        "cklb_version": "1.0",
    }

    with open(new_cklb_path, "w", encoding="utf-8") as f:
        json.dump(cklb, f, indent=2)

    print(f"[*] New CKLB created: {new_cklb_path}")
    return str(new_cklb_path)
