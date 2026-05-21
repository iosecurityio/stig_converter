# csv_to_json.py
# Convert STIGs in .csv to .json

import csv
import json
from pathlib import Path

from stig_converter.security_utils import validate_output_path, get_default_allowed_dirs


def convert_csv_to_json(csv_file, json_path) -> str:
    """
    Converts .csv to .json.
    :param csv_file: Path to the .csv file to convert
    :param json_path: Output directory or file path for the .json
    :return: Path to the created .json file
    """
    csv_path = Path(csv_file)

    if not csv_path.is_file():
        raise FileNotFoundError(f"[X] CSV file does not exist: {csv_path}")

    new_json_path = validate_output_path(
        json_path, csv_file, get_default_allowed_dirs(), extension=".json"
    )

    print(f"[*] Converting CSV: {csv_path}")
    with open(csv_path, encoding="utf-8") as read_file:
        json_array = list(csv.DictReader(read_file))

    with open(new_json_path, "w", encoding="utf-8") as json_file:
        json.dump(json_array, json_file, indent=4)

    print(f"[*] New JSON file created: {new_json_path}")
    return str(new_json_path)
