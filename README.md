# ckl_to_csv.py

## Overview

This is a Python script to convert a DISA STIG Checklist `.ckl` file to `.csv` file.

## Usage

```python
python3 ckl_to_csv.py
```

```python
def check_connection(url, timeout=5) -> bool:
#Check connection to the URL provided, returns bool. Can provide a timeout limit

def get_checklists(checklist_location) -> list:
#Takes a location as a "glob" and returns a list of .ckl files detected. A glob in this case is an absolute path that can take wildcards (eg /var/log/*.log)

def parse_hostname(checklist, project_list) -> str:
#Takes a checklist location and a list of projects. Will look for any names in the list in the path and if it finds one, return that value.

def convert_to_csv(checklists) -> None:
#Takes in a list of absolute filepaths and writes them from .ckl to .csv.
```

## TODO

- Implement command line argument parsing

## Credits

Inspired from "a Python script to extract data out of a DISA STIG Viewer xccdf file to a CSV" @author Michael Joseph Walsh <github.com@nemonik.com> and the original [Github link](https://gist.github.com/nemonik/951a0e55436e0708222b)

> Note: (This was a Python2 implementation that I changed to Python3 and incorporated into `ckl_to_csv.py`)

## Legal

Department of Defense and Defense Information Systems Agency (DISA) are the owners of the STIGs and the associated documentation. The STIGs are provided as a public service. You are free to use the STIGs in any way you see fit provided that you give credit to the DoD and DISA. The STIGs are provided "as is" without any warranty of any kind.

![DoD and DISA](./DoD-DISA-logos-as-JPEG.jpg)
