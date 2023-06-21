"""
Name: stig_converter.py
Converts STIG Checklists to/from various file formats
Author: Allen Montgomery, IO Security 6/2023
Version 2.0
"""

from datetime import datetime
import re
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

    def parse_extension(self, checklist) -> str:
        """Takes in a checklist location and returns the extension
        :param checklist: The location of the .ckl file to convert
        :return: The extension of the file"""

        extension = checklist.split(".")[-1]
        if extension not in ["ckl", "csv", "json"]:
            print("Invalid file type. Please provide a .ckl, .csv, or .json file.")
            exit()
        return extension

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

    def update_timestamp(self, filename):
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

    def convert(self):
        """Takes in a checklist and converts it to the desired output type"""

        cant_convert = f"Can't convert {self.input_file_ext} to {self.output_type}"

        if self.input_file_ext == "ckl":
            if self.output_type == "csv":
                convert_ckl_to_csv(self.input_file, self.output_dir)
            elif self.output_type == "json":
                convert_ckl_to_json(self.input_file, self.output_dir)

        elif self.input_file_ext == "csv":
            convert_csv_to_json(self.input_file, self.output_dir)

        elif self.input_file_ext == "json":
            convert_json_to_ckl(json_data=self.input_file, ckl_path=self.output_dir)

        else:
            print(cant_convert)
            exit()


def main():
    """Main function to run the script"""

    in_file = r"data/stig_checklist.ckl"
    out_dir = r"data/"

    stig = STIGConverter(
        project_name="Test Project",
        input_file=in_file,
        output_type="csv",
        output_dir=out_dir,
    )
    stig.convert()


if __name__ == "__main__":
    main()
