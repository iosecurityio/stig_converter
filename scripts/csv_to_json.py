# csv_to_json.py
# Convert STIGs in .csv to .json

import csv
from datetime import datetime
import json
import os

INPUT_FILE = r"tests/stig_checklist-20230620.csv"
OUTPUT_LOC = r"tests/"
# Current date timestamp to append to filename
DATE = datetime.now().strftime("%Y%m%d")


def convert_csv_to_json(csv_file, json_path):
    """Converts .csv to .json for Splunk events
    :param csv_file: The location of the .ckl file to convert
    :param json_path: The location path to write the .json file
    :return: The absolute path of the new .json file
    """

    # Create a list of findings
    json_array = []

    # Read in the CSV
    with open(csv_file, encoding="utf-8") as csvf:
        csv_reader = csv.DictReader(csvf)

        for row in csv_reader:
            json_array.append(row)

    # If you pass None as location, it will print to stdout for Splunk events
    if json_path is None:
        for entry in json_array:
            print(entry)
    else:
        filename = os.path.basename(csv_file)
        new_name = os.path.splitext(filename)
        new_location = f"{json_path}{new_name[0].replace(' ', '_')}-{DATE}.json"
        # Open the new file and dump the list of findings
        with open(new_location, "w", encoding="utf-8") as jsonf:
            json_string = json.dumps(json_array, indent=4)
            jsonf.write(json_string)

    return new_location


if __name__ == "__main__":
    try:
        if not INPUT_FILE or not OUTPUT_LOC:
            print("[X] Specify both input file and output location.")
            exit()
        out = convert_csv_to_json(INPUT_FILE, OUTPUT_LOC)
        print(f"[*] Success! Output: {out}")
    except Exception as e:
        print(f"[X] Failed: {e}")
