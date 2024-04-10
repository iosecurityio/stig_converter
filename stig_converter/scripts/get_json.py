import httpx
import json

def get_json(filename="stigviewer_checklist.json", output_path="../../data/"):
    """
    Pulls down the latest STIG checklist from the STIG Viewer website at:
    https://www.stigviewer.com/stig/application_security_and_development/
    """
    target = "https://www.stigviewer.com/stig/application_security_and_development/2023-06-08/MAC-3_Sensitive/json"
    response = httpx.get(target)
    json_checklist = response.json()
    new_filepath = f"{output_path}{filename}"

    with open(new_filepath, "w", encoding='utf-8') as newstigs:
        newstigs.write(json.dumps(json_checklist, indent=2))

if __name__ == "__main__":
    # Pulls down the latest stigviewer checklist in json and puts it in the data directory
    get_json()