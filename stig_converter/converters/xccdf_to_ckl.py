# xccdf_to_ckl.py
# Convert a DISA XCCDF Benchmark XML file to a STIG Viewer CKL (XML) checklist

import logging
import re
import uuid
import xml.etree.ElementTree as ET
from pathlib import Path

try:
    from defusedxml.ElementTree import parse as safe_parse

    DEFUSEDXML_AVAILABLE = True
except ImportError:
    DEFUSEDXML_AVAILABLE = False
    logging.warning(
        "defusedxml not installed — XML parsing has reduced XXE protection. "
        "Install it with: pip install defusedxml"
    )

from stig_converter.security_utils import validate_output_path, get_default_allowed_dirs

_NS = "http://checklists.nist.gov/xccdf/1.1"

# Sub-tags embedded (XML-escaped) inside the XCCDF <description> element
_DESC_TAGS = [
    ("VulnDiscussion",       "Vuln_Discuss"),
    ("FalsePositives",       "False_Positives"),
    ("FalseNegatives",       "False_Negatives"),
    ("Documentable",         "Documentable"),
    ("Mitigations",          "Mitigations"),
    ("SeverityOverrideGuidance", "Security_Override_Guidance"),
    ("PotentialImpacts",     "Potential_Impact"),
    ("ThirdPartyTools",      "Third_Party_Tools"),
    ("MitigationControl",    "Mitigation_Control"),
    ("Responsibility",       "Responsibility"),
    ("IAControls",           "IA_Controls"),
]


def _x(el) -> str:
    """Return element text or empty string."""
    return (el.text or "") if el is not None else ""


def _find(el, tag: str):
    return el.find(f"{{{_NS}}}{tag}")


def _parse_description(raw: str) -> dict:
    """Extract named sub-tags from the XML-escaped description string."""
    result = {}
    for xml_tag, _ in _DESC_TAGS:
        m = re.search(rf"<{xml_tag}>(.*?)</{xml_tag}>", raw, re.DOTALL)
        result[xml_tag] = m.group(1).strip() if m else ""
    return result


def _sub(parent, tag: str, text: str = "") -> ET.Element:
    el = ET.SubElement(parent, tag)
    el.text = text
    return el


def _add_stig_data(vuln_el: ET.Element, attr_name: str, attr_data: str) -> None:
    sd = ET.SubElement(vuln_el, "STIG_DATA")
    _sub(sd, "VULN_ATTRIBUTE", attr_name)
    _sub(sd, "ATTRIBUTE_DATA", attr_data)


def _parse_benchmark(root) -> dict:
    """Extract top-level Benchmark metadata."""
    return {
        "stigid":      root.attrib.get("id", ""),
        "title":       _x(_find(root, "title")),
        "version":     _x(_find(root, "version")),
        "releaseinfo": _x(root.find(f"{{{_NS}}}plain-text[@id='release-info']")),
    }


def _build_stig_info(meta: dict, stig_uuid: str) -> ET.Element:
    stig_info = ET.Element("STIG_INFO")
    fields = [
        ("version",        meta["version"]),
        ("classification", "UNCLASSIFIED"),
        ("customname",     ""),
        ("stigid",         meta["stigid"]),
        ("description",    ""),
        ("releaseinfo",    meta["releaseinfo"]),
        ("title",          meta["title"]),
        ("uuid",           stig_uuid),
        ("notice",         "terms-of-use"),
        ("source",         "Unknown"),
    ]
    for sid_name, sid_data in fields:
        si = ET.SubElement(stig_info, "SI_DATA")
        _sub(si, "SID_NAME", sid_name)
        _sub(si, "SID_DATA", sid_data)
    return stig_info


def _build_vuln(group, rule, meta: dict, stig_uuid: str, rule_uuid: str) -> ET.Element:
    group_id = group.attrib.get("id", "")
    group_title = _x(_find(group, "title"))
    rule_id = rule.attrib.get("id", "")
    severity = rule.attrib.get("severity", "")
    weight = rule.attrib.get("weight", "10.0")
    rule_ver = _x(_find(rule, "version"))
    rule_title = _x(_find(rule, "title"))
    fixtext = _x(_find(rule, "fixtext"))

    raw_desc = _x(_find(rule, "description"))
    desc = _parse_description(raw_desc)

    check = _find(rule, "check")
    check_content = ""
    check_content_ref = "M"
    if check is not None:
        check_content = _x(_find(check, "check-content"))
        cref = check.find(f"{{{_NS}}}check-content-ref")
        if cref is not None:
            check_content_ref = cref.attrib.get("name", "M")

    legacy_ids = []
    ccis = []
    for ident in rule.findall(f"{{{_NS}}}ident"):
        system = ident.attrib.get("system", "")
        val = ident.text or ""
        if "legacy" in system:
            legacy_ids.append(val)
        elif "cci" in system:
            ccis.append(val)

    stig_ref = (
        f"{meta['title']} :: Version {meta['version']}, {meta['releaseinfo']}"
    )

    vuln = ET.Element("VULN")

    static_fields = [
        ("Vuln_Num",    group_id),
        ("Severity",    severity),
        ("Group_Title", group_title),
        ("Rule_ID",     rule_id),
        ("Rule_Ver",    rule_ver),
        ("Rule_Title",  rule_title),
        ("Vuln_Discuss", desc.get("VulnDiscussion", "")),
        ("IA_Controls",  desc.get("IAControls", "")),
        ("Check_Content", check_content),
        ("Fix_Text",     fixtext),
    ]
    for name, data in static_fields:
        _add_stig_data(vuln, name, data)

    for xml_tag, ckl_attr in _DESC_TAGS:
        if ckl_attr in ("Vuln_Discuss", "IA_Controls"):
            continue  # already added above
        _add_stig_data(vuln, ckl_attr, desc.get(xml_tag, ""))

    trailing_fields = [
        ("Check_Content_Ref", check_content_ref),
        ("Weight",            weight),
        ("Class",             "Unclassified"),
        ("STIGRef",           stig_ref),
        ("STIG_UUID",         stig_uuid),
    ]
    for name, data in trailing_fields:
        _add_stig_data(vuln, name, data)

    for legacy_id in legacy_ids:
        _add_stig_data(vuln, "LEGACY_ID", legacy_id)
    for cci in ccis:
        _add_stig_data(vuln, "CCI_REF", cci)

    _sub(vuln, "STATUS", "Not_Reviewed")
    _sub(vuln, "FINDING_DETAILS", "")
    _sub(vuln, "COMMENTS", "")
    _sub(vuln, "SEVERITY_OVERRIDE", "")
    _sub(vuln, "SEVERITY_JUSTIFICATION", "")

    return vuln


def convert_xccdf_to_ckl(xccdf_file, ckl_path) -> str:
    """
    Convert a DISA XCCDF Benchmark XML file to a blank STIG Viewer CKL checklist.
    All findings default to Not_Reviewed with empty details and comments.
    :param xccdf_file: Path to the input XCCDF .xml file
    :param ckl_path: Output directory or file path for the .ckl
    :return: Path to the created .ckl file
    """
    xccdf_path = Path(xccdf_file)
    if not xccdf_path.is_file():
        raise FileNotFoundError(f"[X] XCCDF file does not exist: {xccdf_path}")

    new_ckl_path = validate_output_path(
        ckl_path, xccdf_file, get_default_allowed_dirs(), extension=".ckl"
    )

    print(f"[*] Converting XCCDF → CKL: {xccdf_path}")

    if DEFUSEDXML_AVAILABLE:
        tree = safe_parse(xccdf_path)
    else:
        tree = ET.parse(xccdf_path)

    root = tree.getroot()
    meta = _parse_benchmark(root)

    # Generate stable UUIDs derived from the benchmark id so repeated runs
    # produce the same output for the same STIG.
    stig_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, meta["stigid"]))

    checklist = ET.Element("CHECKLIST")

    asset = ET.SubElement(checklist, "ASSET")
    _sub(asset, "ROLE", "None")
    _sub(asset, "ASSET_TYPE", "Computing")
    _sub(asset, "HOST_NAME", "")
    _sub(asset, "HOST_IP", "")
    _sub(asset, "HOST_MAC", "")
    _sub(asset, "HOST_FQDN", "")
    _sub(asset, "TARGET_COMMENT", "")
    _sub(asset, "TECH_AREA", "")
    _sub(asset, "TARGET_KEY", "")
    _sub(asset, "WEB_OR_DATABASE", "false")
    _sub(asset, "WEB_DB_SITE", "")
    _sub(asset, "WEB_DB_INSTANCE", "")

    stigs_el = ET.SubElement(checklist, "STIGS")
    istig = ET.SubElement(stigs_el, "iSTIG")
    istig.append(_build_stig_info(meta, stig_uuid))

    groups = root.findall(f".//{{{_NS}}}Group")
    for group in groups:
        rule = group.find(f"{{{_NS}}}Rule")
        if rule is None:
            continue
        rule_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, rule.attrib.get("id", "")))
        istig.append(_build_vuln(group, rule, meta, stig_uuid, rule_uuid))

    ET.indent(checklist, space="\t")
    ET.ElementTree(checklist).write(
        new_ckl_path, encoding="UTF-8", xml_declaration=True
    )

    print(f"[*] New CKL created: {new_ckl_path}")
    return str(new_ckl_path)
