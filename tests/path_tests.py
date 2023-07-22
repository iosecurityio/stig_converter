import os
from pathlib import Path

# if the current running directory isnt the same as the directory of the script
# change the current working directory to the directory of the script
if Path.cwd() != Path(__file__).parent:
    os.chdir(Path(__file__).parent)
    print("Changed directory to:")
    # check current running directory
    print(Path.cwd())


class PathTest:
    """Test the Path module"""

    def __init__(self):
        self.current_path = Path.cwd()
        self.parent_path = Path(__file__).parent
        print("PathTest object created")

    def print_current_path(self):
        print("Current path:")
        print(self.current_path)
        self.print_div()

    def print_parent_path(self):
        print("Parent path:")
        print(self.parent_path)
        self.print_div()

    def list_files(self):
        print("Files in current path:")
        print(os.listdir(self.current_path))
        self.print_div()

    def list_parent(self):
        print("Files in parent path:")
        print(os.listdir(self.parent_path))
        self.print_div()

    def print_div(self):
        print("-" * 30)


testing = PathTest()

testing.print_current_path()
testing.list_files()

testing.print_parent_path()
testing.list_parent()

# take in a string file path and check if a file exists at that path
# if it does, return the path
file_location = input("Enter a file path: ")
if Path(file_location).is_file():
    print("File exists at path")
else:
    print("File does not exist at path")