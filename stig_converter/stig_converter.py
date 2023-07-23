"""
Name: stig_converter.py
Converts STIG Checklists to/from various file formats
Author: Allen Montgomery, IO Security 7/2023
Version 2.1
"""

import argparse
from datetime import datetime
import os
from pathlib import Path
import re
import sys
from scripts.json_to_ckl import convert_json_to_ckl
from scripts.ckl_to_csv import convert_ckl_to_csv
from scripts.ckl_to_json import convert_ckl_to_json
from scripts.csv_to_json import convert_csv_to_json


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

    def convert(self) -> None:
        """Takes in a checklist and converts it to the desired output type"""

        if self.config.input_file_type == "ckl":
            if self.config.output_file_type == "csv":
                convert_ckl_to_csv(self.config.input_file_path, self.config.output_file_path)
            elif self.config.output_file_type == "json":
                convert_ckl_to_json(self.config.input_file_path, self.config.output_file_path)
        elif self.config.input_file_type == "csv":
            if self.config.output_file_type == "json":
                convert_csv_to_json(self.config.input_file_path, self.config.output_file_path)
        elif self.config.input_file_type == "json":
            if self.config.output_file_type == "ckl":
                convert_json_to_ckl(self.config.input_file_path, self.config.output_file_path)
        else:
            print("[-] Error: Invalid conversion")
            sys.exit(1)


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

    # python stig_converter.py -i "../data/stig_checklist.ckl" -o "../data.json"
    config = Interface()
    converter = STIGConverter(config=config)
    converter.convert()


if __name__ == "__main__":
    main()
