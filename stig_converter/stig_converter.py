"""
Name: stig_converter.py
TLDR: Converts STIG Checklists to other various file formats
Author: Allen Montgomery, IO Security
Version: 2.3
Date: Apr 2025
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path


class STIGConverter:
    """
    Converts STIG Checklists to/from various file formats (CSV, JSON, CKL)
    """

    def __init__(self, interface_opts) -> None:
        self.config = interface_opts
        self.input_file = interface_opts.input_file
        self.output_file = interface_opts.output_file
        self.encoding = "utf-8"
        self.date = datetime.now().strftime("%Y%m%d")

    def update_filename(self, filename) -> str:
        """
        Updates the timestamp of the checklist to the current date
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


class Interface:
    """
    Command line interface for stig_converter.py
    """

    def __init__(self) -> None:
        self.args = None
        self.event = False
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
        """
        Runs the script with the provided arguments
        """

        # Create an argument parser to handle the CLI arguments
        parser = argparse.ArgumentParser(
            description="Process input checklist and generate output checklist."
        )
        parser.add_argument(
            "-i", "--input", required=True, help="input file name"
        )
        parser.add_argument(
            "-o", "--output", required=True, help="output file directory"
        )

        try:
            # Parse arguments from the command line
            self.args = parser.parse_args()

            # Validate input file and output file
            self.register_files(self.args.input, self.args.output)

            # Set the project name (optional)
            if self.args.name:
                self.project_name = self.args.name

            # Set the event flag (optional)
            if self.args.event:
                self.event = True

            # if self.ready is true, then the script is ready to run
            self.ready = True

        except argparse.ArgumentError as arg_error:
            print(f"[X] Argument Error: {arg_error}")
            parser.print_usage()

        except Exception as e:
            print(f"[X] Interface Error: {e}")
            parser.print_usage()

    def register_files(self, input_file, output_file):
        """
        Validate input file and output file
        """

        try:
            # Resolve the absolute path of the input and output files
            abs_input_file = Path(input_file).resolve()
            abs_output_file = Path(output_file).resolve()

            if abs_input_file == abs_output_file:
                print(
                    f"[X] Error: Input file: {input_file} and output file: {output_file} cannot be the same"
                )
                sys.exit(1)

            # Ensures the input file extension is valid
            if abs_input_file.suffix[1:] in self._conversions.keys():
                # Ensure your input file exists
                if abs_input_file.is_file():
                    self.input_file_path = abs_input_file
                    self.input_file_type = abs_input_file.suffix[1:]
                    self.input_file = abs_input_file.name
                else:
                    print(f"[X] Error: Input file: {input_file} does not exist")
                    sys.exit(1)
            else:
                print(f"[X] Error: {input_file} is not a valid input file")
                sys.exit(1)

            self.output_file_path = abs_output_file
            self.output_file_type = abs_output_file.suffix[1:]
            self.output_file = abs_output_file.name

            # Check if its a valid conversion
            if self.output_file_type in self._conversions[self.input_file_type]:
                self.ready = True
            else:
                print(
                    f"[X] Error: {self.output_file_type} is not a valid output file type"
                )
                sys.exit(1)

        except KeyError as ke:
            print(f"[X] Key Error: {ke}")
            sys.exit(1)
        except FileNotFoundError as fnf:
            print(f"[X] File Not Found Error: {fnf}")
            sys.exit(1)
        except Exception as ge:
            print(f"[X] General Error: {ge}")
            sys.exit(1)


if __name__ == "__main__":
    try:
        # Create the CLI and take arguments
        config = Interface()

        # Pass the CLI arguments to the STIGConverter class
        converter = STIGConverter(config)

        # TODO: Consolidate named conversion scripts into a convert method

        # Execute the conversions:
        converter.convert_ckl_to_json(
            config.input_file_path, config.output_file_path
        )
        converter.convert_ckl_to_csv(
            config.input_file_path, "../data/test_checklist.csv"
        )
        converter.convert_csv_to_json(
            "../data/test_checklist.csv", "../data/test_checklist_from_csv.json"
        )
        converter.convert_json_to_ckl(
            "../data/test_checklist.json", "../data/test_checklist_from_json.ckl"
        )

    except Exception as e:
        # TODO: Handle what happens when the output file already exists
        print("[X] Error: Unable to run STIG conversion [-]")
        print(e)
