# csv_to_json.py
# Convert STIGs in .csv to .json

import csv
import json
from datetime import datetime
from pathlib import Path


def convert_csv_to_json(csv_file, json_path):
    """Converts .csv to .json for Splunk events
    :param csv_file: The location of the .ckl file to convert
    :param json_path: The location path to write the .json file
    :return: The absolute path of the new .json file
    """

    # Create a list of findings
    json_array = []
    current_date = datetime.now().strftime("%Y%m%d")
    csv_path = Path(csv_file)
    json_path = Path(json_path)

    if not csv_path.is_file():
        raise FileNotFoundError(f"[X] CSV file does not exist: {csv_path}")

    if json_path.is_dir():
        new_json_path = json_path / f"{csv_path.stem}-{current_date}.json"
    else:
        if not json_path.exists():
            raise FileNotFoundError(f"[X] JSON directory does not exist: {json_path.parent}")
        new_json_path = json_path

    # Read in the CSV
    print(f"[*] Converting CSV: {csv_path}")
    with open(csv_path, encoding="utf-8") as read_file:
        csv_reader = csv.DictReader(read_file)
        for row in csv_reader:
            json_array.append(row)
        # Create a JSON file
        with open(new_json_path, "w", encoding="utf-8") as json_file:
            json_string = json.dumps(json_array, indent=4)
            json_file.write(json_string)

    # Return the location of the new JSON file
    print(f"[*] New JSON file created: {new_json_path}")
    return new_json_path


if __name__ == "__main__":
    data_dir = Path(__file__).parent.parent / "data"
    input_file = data_dir / "stig_checklist-20240406.csv"
    out = convert_csv_to_json(csv_file=input_file, json_path=data_dir)
