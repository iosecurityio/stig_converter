# cklb_to_ckl.py
# Convert a STIG .cklb (JSON) checklist to .ckl (XML) format

import json
import xml.etree.ElementTree as ET
from pathlib import Path

from stig_converter.security_utils import validate_output_path, get_default_allowed_dirs

# CKLB status values → CKL equivalents
_STATUS_MAP = {
    "not_reviewed": "Not_Reviewed",
    "open": "Open",
    "not_a_finding": "NotAFinding",
    "not_applicable": "Not_Applicable",
}


def _sub(parent, tag: str, text: str = "") -> ET.Element:
    """Append a child element with optional text and return it."""
    el = ET.SubElement(parent, tag)
    el.text = text
    return el


def _add_stig_data(vuln_el: ET.Element, attr_name: str, attr_data: str) -> None:
    """Append a STIG_DATA block to a VULN element."""
    sd = ET.SubElement(vuln_el, "STIG_DATA")
    _sub(sd, "VULN_ATTRIBUTE", attr_name)
    _sub(sd, "ATTRIBUTE_DATA", attr_data)


def _build_vuln(rule: dict) -> ET.Element:
    """Build a VULN XML element from a CKLB rule dict."""
    vuln = ET.Element("VULN")

    rule_id_src = rule.get("rule_id_src", "")
    if not rule_id_src:
        rule_id_src = rule.get("rule_id", "") + "_rule"

    check_content_ref = rule.get("check_content_ref", {})
    if isinstance(check_content_ref, dict):
        check_content_ref_name = check_content_ref.get("name", "M")
    else:
        check_content_ref_name = str(check_content_ref)

    # Derive STIGRef from stig_name + version + release_info if available
    # (stored on the rule via the caller when building)
    stig_ref = rule.get("_stig_ref", "")

    fields = [
        ("Vuln_Num",                  rule.get("group_id", "")),
        ("Severity",                  rule.get("severity", "")),
        ("Group_Title",               rule.get("srg_id", "")),
        ("Rule_ID",                   rule_id_src),
        ("Rule_Ver",                  rule.get("rule_version", "")),
        ("Rule_Title",                rule.get("rule_title", "")),
        ("Vuln_Discuss",              rule.get("discussion", "")),
        ("IA_Controls",               rule.get("ia_controls", "")),
        ("Check_Content",             rule.get("check_content", "")),
        ("Fix_Text",                  rule.get("fix_text", "")),
        ("False_Positives",           rule.get("false_positives", "")),
        ("False_Negatives",           rule.get("false_negatives", "")),
        ("Documentable",              rule.get("documentable", "false")),
        ("Mitigations",               rule.get("mitigations", "")),
        ("Potential_Impact",          rule.get("potential_impacts", "")),
        ("Third_Party_Tools",         rule.get("third_party_tools", "")),
        ("Mitigation_Control",        rule.get("mitigation_control", "")),
        ("Responsibility",            rule.get("responsibility", "")),
        ("Security_Override_Guidance",rule.get("security_override_guidance", "")),
        ("Check_Content_Ref",         check_content_ref_name),
        ("Weight",                    str(rule.get("weight", "10.0"))),
        ("Class",                     rule.get("classification", "Unclassified")),
        ("STIGRef",                   stig_ref),
        ("STIG_UUID",                 rule.get("stig_uuid", "")),
    ]

    for name, data in fields:
        _add_stig_data(vuln, name, data)

    for legacy_id in rule.get("legacy_ids", []):
        _add_stig_data(vuln, "LEGACY_ID", legacy_id)

    for cci in rule.get("ccis", []):
        _add_stig_data(vuln, "CCI_REF", cci)

    ckl_status = _STATUS_MAP.get(rule.get("status", "not_reviewed"), "Not_Reviewed")
    _sub(vuln, "STATUS", ckl_status)
    _sub(vuln, "FINDING_DETAILS", rule.get("finding_details", ""))
    _sub(vuln, "COMMENTS", rule.get("comments", ""))
    _sub(vuln, "SEVERITY_OVERRIDE", rule.get("overrides", {}).get("severity", "") if isinstance(rule.get("overrides"), dict) else "")
    _sub(vuln, "SEVERITY_JUSTIFICATION", rule.get("overrides", {}).get("justification", "") if isinstance(rule.get("overrides"), dict) else "")

    return vuln


def convert_cklb_to_ckl(cklb_file, ckl_path) -> str:
    """
    Convert a STIG CKLB (JSON) checklist to CKL (XML) format.
    :param cklb_file: Path to the input .cklb file
    :param ckl_path: Output directory or file path for the .ckl
    :return: Path to the created .ckl file
    """
    cklb_path = Path(cklb_file)
    if not cklb_path.is_file():
        raise FileNotFoundError(f"[X] CKLB file does not exist: {cklb_path}")

    new_ckl_path = validate_output_path(
        ckl_path, cklb_file, get_default_allowed_dirs(), extension=".ckl"
    )

    print(f"[*] Converting CKLB → CKL: {cklb_path}")

    with open(cklb_path, encoding="utf-8") as f:
        data = json.load(f)

    target = data.get("target_data", {})

    checklist = ET.Element("CHECKLIST")

    # ASSET block
    asset = ET.SubElement(checklist, "ASSET")
    _sub(asset, "ROLE", target.get("role", "None"))
    _sub(asset, "ASSET_TYPE", target.get("target_type", "Computing"))
    _sub(asset, "HOST_NAME", target.get("host_name", ""))
    _sub(asset, "HOST_IP", target.get("ip_address", ""))
    _sub(asset, "HOST_MAC", target.get("mac_address", ""))
    _sub(asset, "HOST_FQDN", target.get("fqdn", ""))
    _sub(asset, "TARGET_COMMENT", target.get("comments", ""))
    _sub(asset, "TECH_AREA", target.get("technology_area", ""))
    _sub(asset, "TARGET_KEY", "")
    _sub(asset, "WEB_OR_DATABASE", str(target.get("is_web_database", False)).lower())
    _sub(asset, "WEB_DB_SITE", target.get("web_db_site", ""))
    _sub(asset, "WEB_DB_INSTANCE", target.get("web_db_instance", ""))

    stigs_el = ET.SubElement(checklist, "STIGS")

    for stig in data.get("stigs", []):
        istig = ET.SubElement(stigs_el, "iSTIG")
        stig_info = ET.SubElement(istig, "STIG_INFO")

        stig_ref = f"{stig.get('stig_name', '')} :: Version {stig.get('version', '')}, {stig.get('release_info', '')}"

        si_fields = [
            ("version",        stig.get("version", "")),
            ("classification", "UNCLASSIFIED"),
            ("customname",     ""),
            ("stigid",         stig.get("stig_id", "")),
            ("description",    ""),
            ("releaseinfo",    stig.get("release_info", "")),
            ("title",          stig.get("stig_name", "")),
            ("uuid",           stig.get("uuid", "")),
            ("notice",         "terms-of-use"),
            ("source",         "Unknown"),
        ]
        for sid_name, sid_data in si_fields:
            si_data_el = ET.SubElement(stig_info, "SI_DATA")
            _sub(si_data_el, "SID_NAME", sid_name)
            _sub(si_data_el, "SID_DATA", sid_data)

        for rule in stig.get("rules", []):
            rule["_stig_ref"] = stig_ref
            istig.append(_build_vuln(rule))

    ET.indent(checklist, space="\t")
    tree = ET.ElementTree(checklist)
    tree.write(new_ckl_path, encoding="UTF-8", xml_declaration=True)

    print(f"[*] New CKL created: {new_ckl_path}")
    return str(new_ckl_path)
