"""For testing the interface of the stig_converter.py script"""
import argparse
from pathlib import Path
import sys
import os


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
        self.ready = None
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

        if self.ready:
            print("[*] Conversion ready to run... [*]")
            self.run_script()
        else:
            print("[-] Error: Conversion not ready... [-]")
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

    def run_script(self):
        # Runs the script with the provided arguments
        print("[*] Running STIG Conversion script... [*]")
        print(f"[*] Input file: {self.input_file}")
        print(f"[*] Output file: {self.output_file}")
        print(f"[*] Project name: {self.project_name}")


if __name__ == "__main__":
    div = "-" * 30
    try:
        print("STIG Conversion Interface Test")
        print(div)
        interface = Interface()
    except Exception as e:
        print(f"[-] Error: {e}")
        exit()
    print(div)
    print("[*] Interface test successful [*]")
