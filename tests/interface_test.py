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
            self.args = parser.parse_args()
        except argparse.ArgumentError as arg_error:
            parser.print_usage()
            print(arg_error)
            sys.exit(1)

        try:
            # Validate the command line input file and path
            self.validate_input(self.args.input)
            # Validate the command line output file and path
            self.validate_output(self.args.output)
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
            print("[*] Interface ready to run... [*]")
            self.run_script()

    def validate_files(self, input_file, output_file):
        # Validate input file and output file

        abs_ifp = Path.absolute(input_file)
        abs_ofp = Path.absolute(output_file)
        filetypes = [".ckl", ".csv", ".json"]
        if abs_ifp.exists():
            if abs_ifp.is_file():
                if abs_ifp.suffix in filetypes:
                    self.input_file = abs_ifp
                    self.input_file_path = abs_ifp.parent
                    self.input_file_type = abs_ifp.suffix
                else:
                    print(f"[-] Error: {self.input_file} is not a valid input file")
                    sys.exit(1)
            else:
                print(f"[-] Error: {abs_ifp} is not a file")
        else:
            print(f"[-] Error: {abs_ifp} does not exist")
            sys.exit(1)
        # Validate Output File
        if abs_ofp.exists():
            if abs_ofp.is_file():
                if abs_ofp.suffix in filetypes:
                    self.output_file = abs_ofp
                    self.output_file_path = abs_ofp.parent
                    self.output_file_type = abs_ofp.suffix
                else:
                    print(f"[-] Error: {self.output_file} is not a valid output file")
                    sys.exit(1)
            else:
                print(f"[-] Error: {abs_ofp} is not a file")
                sys.exit(1)
        else:
            print(f"[-] Error: {abs_ofp} does not exist")
            sys.exit(1)

    def is_valid_conversion(self, input_type, output_type):
        # Checks a dictionary of valid conversions

        conversions = {
            "ckl": ["csv", "json"],
            "csv": ["json"],
            "json": ["ckl"],
        }
        try:
            # check to see if the input type is a key in the dictionary
            if input_type in conversions.keys():
                # check to see if the output type is a value in the dictionary
                if output_type in conversions[input_type]:
                    return True
            else:
                return False
        except KeyError as e:
            print(f"[-] File Error: {e}")
            sys.exit(1)

    def run_script(self):
        # Runs the script with the provided arguments
        print("[*] Running STIG Conversion... [*]")
        print(f"[*] Input file: {self.input_file}")
        print(f"[*] Output file: {self.output_file}")
        print(f"[*] Project name: {self.project_name}")
        print("[*] Conversion complete... [*]")


if __name__ == "__main__":
    try:
        interface = Interface()
    except Exception as e:
        print(f"[-] Error: {e}")
        exit()
    print("[*] Interface created...")
