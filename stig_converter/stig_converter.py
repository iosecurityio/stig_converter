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

    def __init__(self, project_name, input_file, output_type, output_dir) -> None:
        self.project_name = project_name
        self.input_file = input_file
        self.input_file_ext = self.parse_extension(input_file)
        self.output_type = output_type
        self.output_dir = output_dir
        self.output_file = None
        self.run()

    def parse_extension(self, filename) -> str:
        """Takes a file or filepath and returns the extension of the file"""

        # Check if the input filename is a valid file.ext combination
        pattern = r"^[^.]*\.[^.]*$"
        if re.match(pattern, filename):
            return filename.split(".")[-1]
        else:
            print(f"Invalid file: {filename}")
            sys.exit()

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

    def update_timestamp(self, filename) -> str:
        """Updates the timestamp of the checklist to the current date"""

        pattern = r"-(\d{8})"
        match = re.search(pattern, filename)
        current_date = datetime.now().strftime("%Y%m%d")

        if match:
            matched_sequence = match.group(1)
            updated_filename = filename.replace(matched_sequence, current_date)
        else:
            filename_split = filename.split(".")
            updated_filename = f"{filename_split[0]}-{current_date}.{filename_split[1]}"
        return updated_filename

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
            return False
        if out_type not in valid_conversions[ext]:
            print(f"Can't convert {ext} to file type {out_type}")
            return False
        print(f"[*] Valid conversion: {ext} to {out_type} [*]")
        return True

    def run(self) -> None:
        """Takes in a checklist and converts it to the desired output type"""

        cant_convert = f"Can't convert {self.input_file_ext} to {self.output_type}"

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
                print(cant_convert)


class Interface:
    """Command line interface for stig_converter.py"""

    def __init__(self) -> None:
        self.args = None
        self.input_file = None
        self.output_dir = None
        self.project_name = None
        self.cli()

    def check_file_extension(self, value):
        "Ensures the file extension matches a list of valid extensions"

        valid_extensions = [".csv", ".ckl", ".json"]
        _, extension = os.path.splitext(value)
        if extension.lower() not in valid_extensions:
            raise argparse.ArgumentTypeError(
                f"Invalid file extension. Allowed extensions are: {', '.join(valid_extensions)}"
            )
        return value

    def cli(self):
        """Runs the script with the provided arguments"""

        parser = argparse.ArgumentParser(
            description="Process input checklist and generate output checklist."
        )
        # Parse arguments
        parser.add_argument("-n", "--name", required=True, help="project name")
        parser.add_argument(
            "-o", "--output", required=True, help="output file directory"
        )
        parser.add_argument("-i", "--input", required=True, help="input file name")
        parser.add_argument("-t", "--type", required=False, help="output file type")
        parser.add_argument("-v", "--verbose", required=False, help="verbose output")
        # Validate arguments
        try:
            args = parser.parse_args()
            input_file = args.input
            output_dir = args.output
            project_name = args.name
            # TODO Check for type argument
            # TODO check for verbose argument

            print(f"Input file: {input_file}")
            print(f"Output file: {output_dir}")
            print(f"Project name: {project_name}")

        except argparse.ArgumentError as arg_error:
            parser.print_usage()
            print(f"Error: {arg_error}")
            exit()


def main():
    """Main function to run the script"""
    try:
        interface = Interface()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)


if __name__ == "__main__":
    main()
