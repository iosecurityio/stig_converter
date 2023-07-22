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
        self.output_dir = None
        self.project_name = None
        self.type = None
        self.cli()

    def cli(self):
        """Runs the script with the provided arguments"""

        parser = argparse.ArgumentParser(
            description="Process input checklist and generate output checklist."
        )
        # Parse arguments

        parser.add_argument("-i", "--input", required=True, help="input file name")
        parser.add_argument("-t", "--type", required=True, help="output file type")
        parser.add_argument(
            "-o", "--output", required=False, help="output file directory"
        )
        parser.add_argument("-n", "--name", required=False, help="project name")

        # parser.add_argument("-v", "--verbose", required=False, help="verbose output")

        # Validate arguments
        try:
            self.args = parser.parse_args()
            self.input_file = Path.absolute(self.args.input)
            self.output_dir = Path.absolute(self.args.output)
            self.project_name = self.args.name
            self.output_type = self.args.type if self.args.type else "ckl"            
        except argparse.ArgumentError as arg_error:
            parser.print_usage()
            print(arg_error)
            sys.exit(1)

        print("[*] Interface Created...")
        print(f"Arguments: {self.args}")
        print(f"Input file: {self.input_file}")
        print(f"Output Directory: {self.output_dir}")
        print(f"Output type: {self.output_type}")
        print(f"Project name: {self.project_name}")


if __name__ == "__main__":
    try:
        interface = Interface()
    except Exception as e:
        print(f"[-] Error: {e}")
        exit()
    print("[*] Interface created...")
