# stig_to_splunk.py
# Converts STIG Checklist to other various file formats (CSV, JSON) for data ingestion in other platforms
# Refactored Date: 4/6/2023

import csv
from datetime import datetime
import glob
import json
import os
import xml.etree.ElementTree as ET

#List all potential projects you want to include here; will create a new checklist if the project is in here
PROJECTS = ["project1",
            "project2",
            "project3"
            ]
INPUT_FILE = "" # Absolute path to a single .ckl file to convert
INPUT_LOC = "../**.ckl" # Regex of Potential .ckl files to look for
OUTPUT_LOC = ""    # Location to write .csv files
JSON_LOC = f"{OUTPUT_LOC}*.json"    # Location containing .json files
CSV_LOC = f"{OUTPUT_LOC}*.csv"  # Location containing .csv files
DATE = datetime.now().strftime('%Y%m%d')   # current date timestamp in format 20230406

def convert_ckl_to_csv(cklfile, csvpath) -> str:
    """Converts a CKL file to a CSV file
    :param cklfile: The location of the .ckl file to convert
    :param csvpath: The location to write the .csv file
    :return: The location of the new .csv file
    """

    # CKL is a custom XML and these are the field names we will pull from the document
    # Define your table headers as fieldnames
    fieldnames = ['DATE', 'HOST_NAME', 'HOST_IP', 'Vuln_Num', 'Severity', 'Group_Title', \
                  'Rule_ID', 'Rule_Ver', 'Rule_Title', 'Fix_Text','STATUS', \
                    'FINDING_DETAILS', 'COMMENTS', 'Unique_ID']
    filename = os.path.basename(cklfile)
    new_filename = os.path.splitext(filename)
    host_name = parse_hostname(checklist=cklfile, project_list=PROJECTS)
    new_csv = f"{csvpath}\\{new_filename[0].replace(' ', '-')}-{DATE}.csv"

    with open(new_csv, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        tree = ET.parse(cklfile)
        root = tree.getroot()

        #create a dictionary to hold findings
        finding = {}
        finding['DATE'] = DATE

        for asset in root.iter('ASSET'):
            if asset.find('HOST_NAME').text == False:
                finding['HOST_NAME'] = host_name
            else:
                finding['HOST_NAME'] = asset.find('HOST_NAME').text
            finding['HOST_IP'] = asset.find('HOST_IP').text

        for vuln in root.iter('VULN'):
            for stig_data in vuln.findall('./STIG_DATA'):
                if (stig_data.find('VULN_ATTRIBUTE').text in ['Vuln_Num', 'Severity', 'Group_Title', 'Rule_ID', 'Rule_Ver', 'Rule_Title', 'Fix_Text']):
                    finding[stig_data.find('VULN_ATTRIBUTE').text] = stig_data.find('ATTRIBUTE_DATA').text.replace('\n', ' ')

            finding['STATUS'] = vuln.find('./STATUS').text
            finding['FINDING_DETAILS'] = vuln.find('./FINDING_DETAILS').text
            finding['COMMENTS'] = vuln.find('./COMMENTS').text
            # Append a unique ID to map for each finding
            finding['Unique_ID'] = f"{host_name}-{finding['Rule_ID']}-{DATE}"
            # Write the finding to the CSV
            writer.writerow(finding)

    # Return the location of the new CSV
    return new_csv


def get_checklists(checklist_location) -> list:
    """Takes in a location 'glob' and returns a list of .ckl files detected
    :param checklist_location: The location of the .ckl files to convert
    :return: A list of .ckl files"""

    return [ckl for ckl in glob.glob(checklist_location)]


def parse_hostname(checklist, project_list) -> str:
    """Takes a checklist location and a list of projects to look for in the path provided
    :param checklist: The location of the .ckl file to convert
    :param project_list: A list of projects to look for in the path provided
    :return: The project name if found in the path, else an empty string
    """

    project_path = checklist.split("\\")

    # Check if the project is in the path and return empty string if not
    for item in project_path:
        if item.lower() in project_list:
            return item
    return ''


def convert_csv_to_json(csv_location, output_location) -> str:
    """Converts .csv to .json for Splunk events"""

    # TODO: Make sure this JSON is formatted correctly for Splunk events
    json_array = []

    with open(csv_location) as csvf:
        csv_reader = csv.DictReader(csvf)

        for row in csv_reader:
            json_array.append(row)

    # If you dont pass a location, it will print to stdout for Splunk events
    if output_location == None:
        for entry in json_array:
            print(entry)
    # Else you are going to pass in a output_location to write a json file
    else:
        filename = os.path.basename(csv_location)
        new_name = os.path.splitext(filename)
        new_location = f"{output_location}{new_name[0].replace(' ', '_')}.json"
        with open(new_location, 'w') as jsonf:
            json_string = json.dumps(json_array, indent=4)
            jsonf.write(json_string)
    return csv_location


def main():
    """Main function to convert STIG Checklists to CSVs and then to JSON for Splunk events"""

    ckls = get_checklists(INPUT_LOC)
    for ckl in ckls:
        print(f"{ckl}")


if __name__ == "__main__":
    main()
