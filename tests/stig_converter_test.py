"""
Name: stig_converter_test.py
"""

import argparse
import csv
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path


class STIGConverter:
    """Converts STIG Checklists to/from various file formats (CSV, JSON, CKL)"""

    def __init__(self, config) -> None:
        self.config = config
        self.input_file = config.input_file
        self.output_file = config.output_file
        self.events = False

    def parse_hostname(self, checklist, project_list) -> str:
        """Takes a checklist location and a list of projects to look for in the path provided"""

        project_path = checklist.split(r"/")

        # Check if the project is in the path and return empty string if not
        for item in project_path:
            if item.lower() in project_list:
                return item
        return ""

    def update_filename(self, filename) -> str:
        """Updates the timestamp of the checklist to the current date"""

        pattern = r"-(\d{8})"
        match = re.search(pattern, filename)
        current_date = datetime.now().strftime("%Y%m%d")

        if match:
            matched_sequence = match.group(1)
            updated_filename = filename.replace(matched_sequence, current_date)
            return updated_filename
        else:
            name, ext = filename.split(".")[:2]
            updated_filename = f"{name}-{current_date}.{ext}"
            return updated_filename

    def convert_json_to_ckl(self, json_data, ckl_path, base_ckl) -> str:
        """Populates a STIG Checklist with the JSON equivalent values"""

        # Read in the JSON Data
        try:
            with open(json_data, "r") as read_file:
                loaded_data = json.load(read_file)
        except FileNotFoundError as fnf:
            print(f"[X] JSON didn't load properly: {fnf}")
        except KeyError as ke:
            print(f"[X] JSON didn't load properly: {ke}")

        try:
            # Read in the STIG Checklist we are using as a template
            ckl_tree = ET.parse(base_ckl)
            ckl_root = ckl_tree.getroot()
        except Exception as e:
            print(f"[X] Invalid checklist {base_ckl}:\n\t{e}")

        # List of elements under the Asset element in the XML structure
        ASSET = ["HOST_NAME", "HOST_IP", "HOST_MAC", "HOST_FQDN", "TARGET_COMMENT"]
        try:
            for element in ckl_root.iter("ASSET"):
                # Populate the element in the Asset section
                if element.tag in ASSET:
                    element.text = loaded_data[0][element]

            # For every Vulnerability in the checklist
            for vuln in ckl_root.iter("VULN"):
                # Iterate through every finding Dict in the JSON
                for json_finding in loaded_data:
                    for stig_data in vuln.iter("STIG_DATA"):
                        if (
                                stig_data.tag == "VULN_ATTRIBUTE"
                                and stig_data.text in json_finding
                        ):
                            attribute_data = stig_data.find("ATTRIBUTE_DATA")
                            attribute_data.text = json_finding[stig_data.text]
        except UnboundLocalError as unbound_error:
            print(f"[X] Error parsing {base_ckl}:\n\t{unbound_error}")

        # Turn the XML Root back into a string for writing
        encoding = "utf-8"
        new_xml = ET.tostring(ckl_root, encoding=encoding)

        # Write the modified XML to the new file
        with open(ckl_path, "wb") as output_file:
            # Custom header for xml declaration and STIG header comment
            output_file.write('<?xml version="1.0" encoding="UTF-8"?>\n'.encode(encoding))
            output_file.write("<!--DISA STIG Viewer :: 2.16-->\n".encode(encoding))
            output_file.write(new_xml)

    def convert_csv_to_json(self, csv_file, json_path):
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

    def convert_ckl_to_json(ckl, json_path) -> str:
        """Converts a STIG Checklist .CKL file to .JSON
        :param ckl: The location of the .ckl file to convert
        :param json_path: The location path to write the .json file
        :return: The absolute path of the new .json file
        """

        filename = os.path.basename(ckl)
        new_filename = os.path.splitext(filename)
        # TODO Handle the / in the path
        new_location = f"{json_path}/{new_filename[0].replace(' ', '_')}-{DATE}.json"

        with open(new_location, "w", newline="", encoding="utf-8") as jsonf:
            # Create an xml object from the ckl file
            tree = ET.parse(ckl)
            root = tree.getroot()
            # Initialize hostname and IP before we parse checklist
            host_name = ""
            host_ip = ""
            # Create a list of findings
            findings = []

            # Parse the checklist Asset details
            for asset in root.iter("ASSET"):
                if asset.find("HOST_NAME").text:
                    host_name = asset.find("HOST_NAME").text
                if asset.find("HOST_IP").text:
                    host_ip = asset.find("HOST_IP").text

            # Parse the checklists individual Vulnerabilities
            for vuln in root.iter("VULN"):
                # Create a finding dict to hold each finding info
                finding = {}
                finding["DATE"] = DATE
                finding["HOST_NAME"] = host_name
                finding["HOST_IP"] = host_ip
                for stig_data in vuln.findall("./STIG_DATA"):
                    if stig_data.find("VULN_ATTRIBUTE").text in [
                        "Vuln_Num",
                        "Severity",
                        "Group_Title",
                        "Rule_ID",
                        "Rule_Ver",
                        "Rule_Title",
                        "Fix_Text",
                    ]:
                        finding[stig_data.find("VULN_ATTRIBUTE").text] = stig_data.find(
                            "ATTRIBUTE_DATA"
                        ).text.replace("\n", " ")
                finding["STATUS"] = vuln.find("./STATUS").text
                finding["FINDING_DETAILS"] = vuln.find("./FINDING_DETAILS").text
                finding["COMMENTS"] = vuln.find("./COMMENTS").text
                # Append a unique ID to map for each finding
                finding["Unique_ID"] = f"{host_name}-{finding['Rule_ID']}-{DATE}"
                # Add the finding to our finding list
                findings.append(finding)
            # Dump the finding dictionary into the file we are creating
            json.dump(findings, jsonf, indent=4)

        # Return the location of the new json doc
        return new_location


class Interface:
    """Command line interface for stig_converter.py"""

    def __init__(self) -> None:
        self.args = None
        self.input_file = None
        self.input_file_path = None
        self.input_file_type = None
        self.output_file = None
        self.output_file_path = None
        self.output_file_type = None
        self.project_name = None
        self.ready = False
        self._conversions = {
            "ckl": ["csv", "json"],
            "csv": ["json"],
            "json": ["ckl"],
        }
        self.start_cli()

    def start_cli(self):
        """Runs the script with the provided arguments"""

        parser = argparse.ArgumentParser(
            description="Process input checklist and generate output checklist."
        )
        # Parse arguments

        parser.add_argument("-i", "--input", required=True, help="input file name")
        parser.add_argument(
            "-o", "--output", required=False, help="output file directory"
        )
        parser.add_argument("-n", "--name", required=False, help="project name")
        parser.add_argument("-e", "--event", required=False, help="print live events")

        try:
            # Parse arguments from the command line
            print("Parsing arguments...")
            self.args = parser.parse_args()
        except argparse.ArgumentError as arg_error:
            # TODO: Add logging and check proper way of argparse exception handling
            parser.print_usage()
            print(arg_error)
            sys.exit(1)

        try:
            # Validate the command line input file and path
            self.validate_file(self.args.input)

            # Validate the command line output file and path
            self.validate_file(self.args.output)

            # Check if its a valid conversion
            self.is_valid_conversion(self.input_file_type, self.output_file_type)

            # Set the project name
            self.project_name = self.args.name

            # if self.ready is true, then the script is ready to run
            self.ready = True

        except Exception as e:
            print(f"[-] Error: {e}")
            sys.exit(1)

    def convert_ckl_to_csv(ckl, csv_path) -> str:
        """Converts a CKL file to a CSV file
        :param ckl: The location of the .ckl file to convert
        :param csv_path: The location to write the .csv file
        :return: The location of the new .csv file
        """

        # CKL is a custom XML and these are the field names we will pull from the document
        # Define your table headers as fieldnames
        fieldnames = [
            "DATE",
            "HOST_NAME",
            "HOST_IP",
            "Vuln_Num",
            "Severity",
            "Group_Title",
            "Rule_ID",
            "Rule_Ver",
            "Rule_Title",
            "Fix_Text",
            "STATUS",
            "FINDING_DETAILS",
            "COMMENTS",
            "Unique_ID",
        ]
        current_date = datetime.now().strftime('%Y%m%d')
        filename = os.path.basename(ckl)
        new_filename = os.path.splitext(filename)
        new_csv = f"{csv_path}{new_filename[0].replace(' ', '_')}-{current_date}.csv"

        with open(new_csv, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            tree = ET.parse(ckl)
            root = tree.getroot()

            # create a dictionary to hold findings
            finding = {
                "DATE": current_date,
                "HOST_NAME": "",
                "HOST_IP": "",
            }
            # Parse the checklist Asset details
            for asset in root.iter("ASSET"):
                if asset.find("HOST_NAME").text:
                    finding["HOST_NAME"] = asset.find("HOST_NAME").text
                if asset.find("HOST_IP").text:
                    finding["HOST_IP"] = asset.find("HOST_IP").text

            for vuln in root.iter("VULN"):
                for stig_data in vuln.findall("./STIG_DATA"):
                    if stig_data.find("VULN_ATTRIBUTE").text in [
                        "Vuln_Num",
                        "Severity",
                        "Group_Title",
                        "Rule_ID",
                        "Rule_Ver",
                        "Rule_Title",
                        "Fix_Text",
                    ]:
                        finding[stig_data.find("VULN_ATTRIBUTE").text] = stig_data.find(
                            "ATTRIBUTE_DATA"
                        ).text.replace("\n", " ")

                finding["STATUS"] = vuln.find("./STATUS").text
                finding["FINDING_DETAILS"] = vuln.find("./FINDING_DETAILS").text
                finding["COMMENTS"] = vuln.find("./COMMENTS").text
                # Append a unique ID to map for each finding
                finding["Unique_ID"] = f"{finding['HOST_NAME']}-{finding['Rule_ID']}-{current_date}"
                # Write the finding to the CSV
                writer.writerow(finding)
        # Return the location of the new CSV
        return new_csv

    def validate_file(self, stig_file):
        # Validate input file and output file

        # Converts the input file into an absolute file path
        absolute_path = Path(stig_file).resolve()
        # Ensures the file extension is valid
        if absolute_path.suffix[1:] in self._conversions.keys():
            # If the absolute path is a file already then it's the input
            if absolute_path.is_file():
                self.input_file_type = absolute_path.suffix[1:]
                self.input_file = absolute_path.name
                self.input_file_path = absolute_path
            # if there is no file, then set the output file
            else:
                self.output_file_type = absolute_path.suffix[1:]
                self.output_file = absolute_path.name
                self.output_file_path = absolute_path
        else:
            print(f"[-] Error: {stig_file} is not a valid file")
            sys.exit(1)

    def is_valid_conversion(self, input_type, output_type):
        # Checks a dictionary of valid conversions

        try:
            # check to see if the input type is a key in the dictionary
            if input_type in self._conversions.keys():
                # check to see if the output type is a value in the dictionary
                if output_type in self._conversions[input_type]:
                    print("[*] Valid conversion [*]")
                    self.ready = True
            else:
                print("[-] Invalid conversion [-]")
                self.ready = False
        except KeyError as e:
            print(f"[-] File Error: {e}")
            sys.exit(1)


def main():
    """Main function to run the script"""

    # python stig_converter.py -i "../data/stig_checklist.ckl" -o "../data.json"
    config = Interface()
    converter = STIGConverter(config=config)
    converter.convert()


if __name__ == "__main__":
    main()
