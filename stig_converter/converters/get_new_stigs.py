# get_new_stigs.py
# Download latest STIG packages from stigviewer.com and DISA Cyber Exchange

import json
import os
import zipfile
from pathlib import Path
from urllib.parse import urlparse

import httpx

from stig_converter.security_utils import validate_file_path, get_default_allowed_dirs


def secure_extract_zip(file_path, extract_to, allowed_dirs):
    """
    Securely extract ZIP files preventing path traversal attacks.
    :param file_path: Path to ZIP file
    :param extract_to: Directory to extract to
    :param allowed_dirs: List of allowed base directories
    """
    extract_to = validate_file_path(extract_to, allowed_dirs)

    with zipfile.ZipFile(file_path, "r") as zip_ref:
        for member in zip_ref.infolist():
            if os.path.isabs(member.filename) or ".." in member.filename:
                raise ValueError(f"Unsafe path in ZIP: {member.filename}")

            if member.filename.startswith("/") or member.filename.startswith("\\"):
                raise ValueError(f"Absolute path in ZIP: {member.filename}")

            normalized_path = os.path.normpath(member.filename)
            if normalized_path != member.filename or normalized_path.startswith(".."):
                raise ValueError(f"Suspicious normalized path: {member.filename}")

            zip_ref.extract(member, extract_to)


def get_stig_json(file_name, allowed_dirs=None):
    """
    Pulls down the latest STIG checklist from the STIG Viewer website at:
    https://stigviewer.com/stigs/application_security_and_development
    """
    if allowed_dirs is None:
        allowed_dirs = get_default_allowed_dirs()

    try:
        new_filepath = validate_file_path(file_name, allowed_dirs)
        print(f"[*] Downloading STIGs to {new_filepath}")
        target = (
            "https://stigviewer.com/stigs/application_security_and_development/json"
        )
        response = httpx.get(target, timeout=30.0)
        response.raise_for_status()
        json_checklist = response.json()
        with open(new_filepath, "w", encoding="utf-8") as new_stigs:
            new_stigs.write(json.dumps(json_checklist, indent=2))
        print(f"[*] Successfully downloaded {new_filepath.name}!")
        return new_filepath
    except Exception as e:
        print(f"[X] Failed to download: {e}")


def get_stig_zip(output_name, stig_sys="ASD", stig_ver="V6R4", allowed_dirs=None):
    """
    Downloads the latest STIG ZIP from DISA Cyber Exchange.
    The checklist itself is an XML file included in the zip.
    """
    if allowed_dirs is None:
        allowed_dirs = get_default_allowed_dirs()

    file_path = validate_file_path(output_name, allowed_dirs)

    if file_path.exists():
        print(f"[!] The file '{file_path}' already exists.")
        return file_path

    if not stig_sys.replace("_", "").replace("-", "").isalnum():
        raise ValueError(f"Invalid stig_sys parameter: {stig_sys}")
    if not stig_ver.replace("_", "").replace("V", "").replace("R", "").isalnum():
        raise ValueError(f"Invalid stig_ver parameter: {stig_ver}")

    url = f"https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_{stig_sys}_{stig_ver}_STIG.zip"
    zip_file = Path(urlparse(url).path).name
    print(f"[*] Downloading {zip_file} to {file_path}...")
    try:
        with httpx.Client(timeout=30.0) as client:
            response = client.get(url)

            if response.status_code == 200:
                if len(response.content) > 100 * 1024 * 1024:
                    raise ValueError("Downloaded file too large (>100MB)")

                with open(file_path, "wb") as f:
                    f.write(response.content)
                print(f"[*] File successfully saved to {file_path}")
                return file_path
            else:
                print(
                    f"[X] Failed to download the file. Status code: {response.status_code}"
                )
    except Exception as e:
        print(f"[X] Failed to download STIG zip. Error: {e}")


def extract_zip(file_path, allowed_dirs=None):
    """
    Securely extracts a ZIP file, preventing path traversal attacks.
    """
    if allowed_dirs is None:
        allowed_dirs = get_default_allowed_dirs()

    try:
        if file_path.suffix == ".zip" and Path(file_path).exists():
            print(f"[*] Extracting {file_path}...")
            extract_to = file_path.parent / file_path.stem
            secure_extract_zip(file_path, extract_to, allowed_dirs)
            print(f"[*] Successfully extracted files to {file_path.stem}!")
        else:
            print(f"[X] The file '{file_path}' is not a ZIP file or doesn't exist.")
    except TypeError as te:
        print(f"[X] Failed to extract filetype. Error: {te}")
    except ValueError as ve:
        print(f"[X] Security validation failed: {ve}")
    except Exception as e:
        print(f"[X] Failed to extract file. Error: {e}")
