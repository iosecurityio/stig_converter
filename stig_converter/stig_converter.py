"""
Name: stig_converter.py
Converts STIG Checklists to/from various file formats
Author: Allen Montgomery, IO Security 7/2023
Version 2.1
"""

import argparse
from datetime import datetime
import os
import re
import sys
from scripts.json_to_ckl import convert_json_to_ckl
from scripts.ckl_to_csv import convert_ckl_to_csv
from scripts.ckl_to_json import convert_ckl_to_json
from scripts.csv_to_json import convert_csv_to_json


class STIGConverter:
    """Converts STIG Checklists to/from various file formats (CSV, JSON, CKL)"""

    def __init__(self, project_name, options) -> None:
        self.project_name = project_name
        self.input_file = options.input_file
        self.input_file_ext = self.parse_extension(options.input_file)
        self.output_file = None
        self.output_type = options.output_type
        self.output_dir = options.output_dir

    def parse_extension(self, input_path) -> str:
        # Regular expression to check for a valid file extension
        pattern = r"^(.*[\\/])?[^./\\]+\.[^./\\]+$"

        match = re.match(pattern, input_path)
        if match:
            return match.group(0).split(".")[-1]
        else:
            raise ValueError(
                "Invalid file extension. The input should have a valid extension."
            )

    def parse_hostname(self, checklist, project_list) -> str:
        """Takes a checklist location and a list of projects to look for in the path provided
        :param checklist: The location of the .ckl file to convert
        :param project_list: A list of projects to look for in the path provided
        :return: The project name if found in the path, else an empty string
        """

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
            if "/" in filename:
                splitpath = filename.split("/")
                newfile = splitpath[-1]
                name = newfile.split(".")[0]
                ext = newfile.split(".")[1]
                updated_filename = f"{name}-{current_date}.{ext}"
                return "/".join(splitpath[:-1]) + "/" + updated_filename

    def validate_filetype(self, file_in, out_type) -> bool:
        """Returns a list of valid outputs for the provided checklist type"""

        ext = file_in.split(".")[-1]
        valid_conversions = {
            "ckl": ["csv", "json"],
            "csv": ["json"],
            "json": ["ckl"],
        }
        if ext not in valid_conversions:
            print(f"Invalid input file type: {ext}")
            if out_type not in valid_conversions[ext]:
                print(f"Can't convert {ext} to file type {out_type}")
            return False
        print(f"[*] Valid conversion: {ext} to {out_type} [*]")
        return True

    def convert(self) -> None:
        """Takes in a checklist and converts it to the desired output type"""

        updatedname = self.update_filename(self.input_file)
        base_path, current_extension = os.path.splitext(updatedname)
        updated_file_path = base_path + "." + self.output_type
        self.output_file = updated_file_path

        #TODO Use os.path or pathlib to work with filepaths
        if self.validate_filetype(self.input_file, self.output_type):
            if self.input_file_ext == "ckl":
                if self.output_type == "csv":
                    convert_ckl_to_csv(self.input_file, self.output_dir)
                elif self.output_type == "json":
                    convert_ckl_to_json(self.input_file, self.output_dir)
            elif self.input_file_ext == "csv":
                if self.output_type == "json":
                    convert_csv_to_json(self.input_file, self.output_dir)
            elif self.input_file_ext == "json":
                if self.output_type == "ckl":
                    convert_json_to_ckl(self.input_file, self.output_dir)
            else:
                print("Conversion error")
        print(f"[*] Conversion complete: {self.output_file} [*]")


class Interface:
    """Command line interface for stig_converter.py"""

    def __init__(self) -> None:
        self.args = None
        self.input_file = None
        self.output_dir = None
        self.project_name = None
        self.output_type = None
        self.cli()

    def cli(self):
        """Starts the Command Line Interface for stig_converter.py"""

        # Create argparsers to take CLI inputs
        parser = argparse.ArgumentParser(
            description="Process input checklist and generate output checklist."
        )

        # Add CLI arguments
        parser.add_argument("-i", "--input", required=True, help="input file name")
        parser.add_argument(
            "-o", "--output", required=True, help="output file directory"
        )
        parser.add_argument("-t", "--type", required=True, help="output file type")
        parser.add_argument("-n", "--name", required=False, help="project name")

        try:
            # Parse arguments
            args = parser.parse_args()
        except argparse.ArgumentError as arg_error:
            parser.print_usage()
            print(arg_error)
            exit()
        self.args = args
        self.input_file = self.args.input
        self.output_dir = self.args.output
        self.output_type = self.args.type
        self.project_name = self.args.name
        print("Interface options:")
        print("Input file: ", self.input_file)
        print("Output directory: ", self.output_dir)
        print("Output type: ", self.output_type)
        print("Project name: ", self.project_name)


def main():
    """Main function to run the script"""

    # python stig_converter.py -i "../data/stig_checklist.ckl" -o "../data" -t "json" -n "project1"
    interface = Interface()
    converter = STIGConverter(project_name="project1", options=interface)
    converter.input_file_ext = converter.parse_extension(converter.input_file)
    converter.convert()


if __name__ == "__main__":
    main()
