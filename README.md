# stig_converter.py

## Overview and Features

stig_converter converts DISA STIG Checklists into various file formats.
This project is the result of a collection of individual Python scripts used to convert STIGs and is currently being sewn back together into one main script.

Supported file formats:

- convert `.ckl` file to `.csv` file

- convert `.ckl` file to `.json` file

- convert `.csv` file to `.json` file

- convert `.json` file to `.ckl` file

- convert `.json` file to `.md` file

- get latest STIGs from [www.stigviewer.com](https://stigviewer.com) in `.json`

- get latest STIGs from DISA Cyber Exchange in `.zip`

## Security Features

This project implements multiple security controls to protect against common vulnerabilities:

- **XXE Protection**: Secure XML parsing using `defusedxml` library prevents XML External Entity attacks
- **Path Traversal Prevention**: All file operations validate paths against allowed directories
- **Zip Slip Protection**: Secure ZIP extraction prevents malicious archive extraction attacks
- **Input Validation**: URL parameters and file paths are sanitized to prevent injection attacks
- **File Size Limits**: Download operations include size restrictions (100MB limit)

## Usage

1. `git clone https://github.com/iosecurityio/stig_converter.git`

1. `cd stig_converter`

1. `python3 -m venv venv`

1. `source venv/bin/activate`

1. `pip install -r requirements.txt`

## Security Architecture

The security utilities are centralized in `scripts/security_utils.py` and provide:

- **Path Validation**: `validate_file_path()` ensures all file operations stay within allowed directories
- **Secure Output Handling**: `validate_output_path()` creates safe output paths with automatic directory creation
- **Default Security Boundaries**: Operations restricted to current directory, `data/`, and `output/` subdirectories

All conversion scripts now import and use these security functions to prevent:

- Directory traversal attacks (e.g., `../../../etc/passwd`)
- Arbitrary file writes outside project boundaries
- ZIP bomb and zip slip attacks
- XML External Entity (XXE) injection

## Development

Code formatting is enforced using `ruff`. After making changes, run:

```bash
ruff format scripts/
```

## TODO

- Fix `stig_converter.py`

---

## Credits

Inspired by "a Python script to extract data out of a DISA STIG Viewer xccdf file to a CSV" @author Michael Joseph Walsh <github.com@nemonik.com> and the original [Github link](https://gist.github.com/nemonik/951a0e55436e0708222b). Shout out.

> Note: (This was a Python2 implementation that I changed to Python3 and incorporated into `stig_converter.py`)

---

## License

**Allen Montgomery** - <allen@iosecurityio> - IO Security

Use responsibly at your leisure. Wear your helmet.

---

## Legal

Department of Defense and Defense Information Systems Agency (DISA) are the owners of the STIGs and the associated documentation. The STIGs are provided as a public service. You are free to use the STIGs in any way you see fit provided that you give credit to the DoD and DISA. The STIGs are provided "as is" without any warranty of any kind.

![DoD and DISA](static/DoD-DISA-logos-as-JPEG.jpg)
