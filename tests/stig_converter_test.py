"""
Name: stig_converter_test.py
"""

import argparse
import csv
import json
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path


class STIGConverter:
    """Converts STIG Checklists to/from various file formats (CSV, JSON, CKL)"""

    def __init__(self, interface_opts) -> None:
        self.config = interface_opts
        self.input_file = interface_opts.input_file
        self.output_file = interface_opts.output_file
        self.events = False  # TODO: Add events to splunk
        self.encoding = "utf-8"
        self.date = datetime.now().strftime("%Y%m%d")

    def parse_hostname(self, checklist, project_list) -> str:
        """Takes a checklist location and a list of projects to look for in the path provided"""

        # TODO refactor with pathlib
        project_path = checklist.split(r"/")

        # Check if the project is in the path and return empty string if not
        for item in project_path:
            if item.lower() in project_list:
                return item
        return ""

    def update_filename(self, filename) -> str:
        """Updates the timestamp of the checklist to the current date
        If the file already has a date in the filename, then it will replace it with the current date
        If the file doesn't have a date in the filename, then it will append the current date to the end
        Example: stig_checklist-20210723.ckl -> stig_checklist-20210724.ckl
        Example: stig_checklist.ckl -> stig_checklist-20210724.ckl
        """

        # Check if the filename has a date in it (eg -20210723)
        pattern = r"-(\d{8})"
        match = re.search(pattern, filename)

        if match:
            matched_sequence = match.group(1)
            # replace the date in the filename with the current date
            updated_filename = filename.replace(matched_sequence, self.date)
            # return the name of the file with the updated date
            return updated_filename
        else:
            # if there is no date in the filename, then add the current date to the end
            name, ext = filename.split(".")[:2]
            updated_filename = f"{name}-{self.date}.{ext}"
            return updated_filename

    def convert_json_to_ckl(self, input_file, output_file):
        """Populates a STIG Checklist with the JSON equivalent values"""

        # We need a base checklist to populate with the JSON data
        # TODO: handle the filename and path without relative path
        base_ckl = "../data/stig_checklist.ckl"

        try:
            # Read in the JSON Data
            with open(input_file, "r") as read_file:
                loaded_data = json.load(read_file)
            # Read in the STIG Checklist we are using as a template
            ckl_tree = ET.parse(base_ckl)
            ckl_root = ckl_tree.getroot()
            # List of elements under the ASSET element in the CKL/XML structure
            asset = ["HOST_NAME", "HOST_IP", "HOST_MAC", "HOST_FQDN", "TARGET_COMMENT"]
            for element in ckl_root.iter("ASSET"):
                # Populate the element in the ASSET section
                if element.tag in asset:
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

            # Turn the XML Root back into a string for writing
            new_xml = ET.tostring(ckl_root, encoding=self.encoding)

            # Write the modified XML to the new file
            with open(output_file, "wb") as output_file:
                # Custom header for xml declaration and STIG header comment
                output_file.write(f'<?xml version="1.0" encoding="{self.encoding.upper()}"?>\n'.encode(self.encoding))
                output_file.write("<!--DISA STIG Viewer :: 2.16-->\n".encode(self.encoding))
                output_file.write(new_xml)

        except UnboundLocalError as unbound_error:
            print(f"[X] Error parsing {base_ckl}:\n\t{unbound_error}")

        except FileNotFoundError as fnf:
            print(f"[X] JSON file not found: {fnf}")

        except KeyError as ke:
            print(f"[X] JSON doesn't contain the expected key: {ke}")

        except Exception as e:
            print(f"[X] Invalid checklist {base_ckl}:\n\t{e}")

    def convert_csv_to_json(self, input_file, output_file, as_event=False):
        """Converts .csv to .json file out or Splunk events"""

        # Create a list of findings
        json_array = []

        # Read in the CSV
        with open(input_file, encoding=self.encoding) as csvf:
            csv_reader = csv.DictReader(csvf)
            for row in csv_reader:
                json_array.append(row)

        # TODO: Add events to splunk
        # If events, it will print to stdout for Splunk events
        if as_event:
            for entry in json_array:
                print(entry)
        # If not events, it will create a new file
        else:
            # Open the new file and dump the list of findings
            with open(output_file, "w", encoding=self.encoding) as jsonf:
                json_string = json.dumps(json_array, indent=4)
                jsonf.write(json_string)
        return output_file

    def convert_ckl_to_json(self, input_file, output_file, as_event=False):
        """Converts a STIG Checklist .CKL file to .JSON file"""

        with open(output_file, "w", newline="", encoding=self.encoding) as jsonf:
            # Create an xml object from the ckl file
            tree = ET.parse(input_file)
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
                finding = {"HOST_NAME": host_name, "HOST_IP": host_ip}
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
                # Add the finding to our finding list
                findings.append(finding)
            # Dump the finding dictionary into the file we are creating
            json.dump(findings, jsonf, indent=4)

        # TODO: Add events to splunk
        # If events, it will print to stdout for Splunk events
        if as_event:
            for entry in findings:
                print(entry)

        # Return the location of the new json doc
        return output_file

    def convert_ckl_to_csv(self, input_file, output_file) -> str:
        """Converts a CKL file to a CSV file"""

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

        with open(output_file, "w", newline="", encoding=self.encoding) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            tree = ET.parse(input_file)
            root = tree.getroot()

            # create a dictionary to hold findings
            finding = {
                "DATE": datetime.now().strftime("%Y%m%d"),
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
                finding["Unique_ID"] = f"{finding['HOST_NAME']}-{finding['Rule_ID']}-{finding['DATE']}"
                # Write the finding to the CSV
                writer.writerow(finding)
        # Return the location of the new CSV
        return output_file


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

    try:
        # python stig_converter.py -i "../data/stig_checklist.ckl" -o "../data.json"
        config = Interface()
        converter = STIGConverter(config)
        # Run the conversion
        print("Run conversion now")
    except Exception as e:
        print("[-] Error: Unable to run STIG conversion [-]")
        print(e)

if __name__ == "__main__":
    main()
