# stig_converter.py

## Overview and Features

This is a Python script to convert DISA STIG Checklists into various formats.

- convert `.ckl` file to `.csv` file

- convert `.csv` file to `.json` file

- convert `.ckl` file to `.json` file

- convert `.json` file to `.ckl` file

- pull down latest STIGs from www.stigviewer.com and convert them to a markdown format

## Usage

1. `git clone https://github.com/iosecurityio/stig_converter.git`

1. `cd stig_converter`

1. `pip install -r requirements.txt`

```python
usage: stig_converter.py [-h] -n NAME -i INPUT -o OUTPUT
                         [-t TYPE] [-v VERBOSE]
```

## TODO

- Refactor basically every script (:
- Finish argparse and CLI

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

![DoD and DISA](./docs/DoD-DISA-logos-as-JPEG.jpg)
