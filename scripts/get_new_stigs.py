import json
import zipfile
from pathlib import Path

import httpx


def get_stig_json(file_name):
    """
    Pulls down the latest STIG checklist from the STIG Viewer website at:
    https://stigviewer.com/stigs/application_security_and_development
    """

    try:
        new_filepath = Path(file_name)
        print(f"[*] Downloading STIGs to {new_filepath}")
        target = "https://stigviewer.com/stigs/application_security_and_development/json"
        response = httpx.get(target)
        json_checklist = response.json()
        with open(new_filepath, "w", encoding="utf-8") as new_stigs:
            new_stigs.write(json.dumps(json_checklist, indent=2))
        print(f"[*] Successfully downloaded {new_filepath.name}!")
        return new_filepath
    except Exception as e:
        print(f"[X] Failed to download: {e}")


def get_stig_zip(file_name):
    """
    Downloads the latest STIG ZIP from DISA Cyber Exchange
    The checklist itself is an xml file included in the zip
    """

    # Create a Path object for the file
    file_path =  Path(file_name)

    # Check if the file already exists
    if file_path.exists():
        print(f"[!] The file '{file_path}' already exists.")
        return file_path

    # Download the ZIP file
    url = "https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_ASD_V6R3_STIG.zip"
    print(f"[*] Downloading STIG Zip to {file_path}...")
    try:
        with httpx.Client() as client:
            response = client.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Save the content to a file
                with open(file_path, "wb") as f:
                    f.write(response.content)
                print(f"[*] File successfully saved to {file_path}")
                return file_path
            else:
                print(f"[X] Failed to download the file. Status code: {response.status_code}")
    except Exception as e:
        print(f"[X] Failed to download STIG zip. Error: {e}")


def extract_zip(file_path):
    """
    Extracts the zip file, presumably the zipped up STIG file from DISA Cyber Exchange
    """

    try:
        if file_path.suffix == ".zip" and Path(file_path).exists():
            print(f"[*] Extracting {file_path}...")
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(file_path.parent / file_path.stem)
                print(f"[*] Successfully extracted files to {file_path.stem}!")
        else:
            print(f"[X] The file '{file_path}' is not a ZIP file or doesn't exist.")
    except TypeError as te:
        print(f"[X] Failed to extract filetype. Error: {te}")
    except Exception as e:
        print(f"[X] Failed to extract file. Error: {e}")


if __name__ == "__main__":
    # Define file name outputs
    data_dir = Path().cwd().parent / "data"
    zip_name = data_dir / "U_ASD_V6R3_STIG.zip"
    json_stigs = data_dir / "application_security_development.json"

    # Download and write Application Security and Development STIG checklist in JSON format
    get_stig_json(file_name=json_stigs)

    # Download Application Security and Development zip file from DISA Cyber Exchange
    stig_zip = get_stig_zip(file_name=zip_name)

    # Unzip downloaded STIGs
    extract_zip(file_path=stig_zip)
