# stig_converter

## Overview

`stig_converter` converts DISA STIG checklists between file formats via a unified CLI.

**Supported conversions:**

| Input   | Output                          | Notes                                              |
| ------- | ------------------------------- | -------------------------------------------------- |
| `.ckl`  | `.csv`, `.json`, `.md`, `.cklb` |                                                    |
| `.cklb` | `.ckl`                          |                                                    |
| `.csv`  | `.json`                         |                                                    |
| `.json` | `.ckl`, `.md`                   | JSON → CKL requires `--template-ckl`               |
| `.xml`  | `.ckl`, `.cklb`                 | DISA XCCDF Benchmark; all findings → Not_Reviewed  |

CKL is the XML-based checklist format used by DISA STIG Viewer.
CKLB is the JSON-based checklist format used by DISA STIG Viewer 3+.
XML (XCCDF) is the DISA Benchmark definition file included in official STIG packages.

Additional utilities:

- Download the latest STIGs from [stigviewer.com](https://stigviewer.com) as `.json`
- Download the latest STIGs from DISA Cyber Exchange as `.zip`

## Usage

```bash
git clone https://github.com/iosecurityio/stig_converter.git
cd stig_converter
python3 -m venv venv
source venv/bin/activate
pip install -e .
stig_converter --help
```

### convert

Convert a checklist between file formats.

```bash
# CKL to CSV
stig_converter convert -i data/checklist.ckl -o data/report.csv

# CKL to JSON
stig_converter convert -i data/checklist.ckl -o data/findings.json

# CKL to Markdown
stig_converter convert -i data/checklist.ckl -o data/report.md

# CSV to JSON
stig_converter convert -i data/checklist.csv -o data/findings.json

# JSON to CKL (requires a template CKL)
stig_converter convert -i data/findings.json -o data/checklist.ckl --template-ckl data/template.ckl

# JSON to Markdown
stig_converter convert -i data/findings.json -o data/report.md

# CKL to CKLB
stig_converter convert -i data/checklist.ckl -o data/checklist.cklb

# CKLB to CKL
stig_converter convert -i data/checklist.cklb -o data/checklist.ckl

# XCCDF Benchmark to CKL (blank checklist, all findings Not_Reviewed)
stig_converter convert -i data/U_ASD_STIG_V6R4_Manual-xccdf.xml -o data/checklist.ckl

# XCCDF Benchmark to CKLB (blank checklist, all findings not_reviewed)
stig_converter convert -i data/U_ASD_STIG_V6R4_Manual-xccdf.xml -o data/checklist.cklb
```

### fetch

Download the latest STIG data from remote sources. Output files are written to the `data/` directory.

```bash
# Download ASD STIG checklist from stigviewer.com as JSON
stig_converter fetch --json data/latest_stigs.json

# Download official STIG package from DISA Cyber Exchange as ZIP (default: ASD V6R4)
stig_converter fetch --zip data/U_ASD_V6R4_STIG.zip

# Download a specific STIG version
stig_converter fetch --zip data/U_ASD_V6R3_STIG.zip --stig-sys ASD --stig-ver V6R3
```

## Security Features

This project implements multiple security controls to protect against common vulnerabilities:

- **XXE Protection**: Secure XML parsing using `defusedxml` prevents XML External Entity attacks
- **Path Traversal Prevention**: All file operations validate paths against allowed directories
- **Zip Slip Protection**: Secure ZIP extraction prevents malicious archive extraction attacks
- **Input Validation**: URL parameters and file paths are sanitized to prevent injection attacks
- **File Size Limits**: Download operations include a 100MB size cap

## Security Architecture

Security utilities are centralized in `stig_converter/security_utils.py` and provide:

- **Path Validation**: `validate_file_path()` ensures all file operations stay within allowed directories
- **Secure Output Handling**: `validate_output_path()` creates safe output paths with automatic directory creation
- **Default Security Boundaries**: Operations restricted to the project root, `data/`, and `output/` subdirectories — paths are resolved relative to the project root regardless of working directory

These functions are used throughout the converters to prevent:

- Directory traversal attacks (e.g., `../../../etc/passwd`)
- Arbitrary file writes outside project boundaries
- ZIP bomb and zip slip attacks
- XML External Entity (XXE) injection

## Development

Code formatting is enforced using `ruff`. After making changes, run:

```bash
ruff format stig_converter/
```

---

## Credits

Inspired by "a Python script to extract data out of a DISA STIG Viewer xccdf file to a CSV" @author Michael Joseph Walsh <github.com@nemonik.com> and the original [Github link](https://gist.github.com/nemonik/951a0e55436e0708222b). Shout out.

> Note: (This was a Python2 implementation that I changed to Python3 and incorporated into `stig_converter.py`)

## Legal

Department of Defense and Defense Information Systems Agency (DISA) are the owners of the STIGs and the associated documentation. The STIGs are provided as a public service. You are free to use the STIGs in any way you see fit provided that you give credit to the DoD and DISA. The STIGs are provided "as is" without any warranty of any kind.

![DoD and DISA](static/DoD-DISA-logos-as-JPEG.jpg)
