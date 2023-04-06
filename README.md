# stig_converter.py

## Overview and Features

This is a Python script to convert DISA STIG Checklists into various formats.

- convert `.ckl` file to `.csv` file

- convert `.csv` file to `.json` file

- can also find your most recent checklists in a file share

## Usage and Examples

Will convert the .CKL checklist that is in ./data/ and convert to both a csv and a json file in the same ./data/ directory

1. Drop your `.ckl` file in the `data` directory
2. Add your project name to `PROJECTS = ["project_name"]` in `stig_converter.py`
3. `python3 ./src/stig_converter.py`

```python
> python3 ./src/stig_converter.py

# Example JSON output of a STIG finding:
[
    {
        "DATE": "20230406",
        "HOST_NAME": "Test Hostname",
        "HOST_IP": "192.168.1.256",
        "Vuln_Num": "V-222387",
        "Severity": "medium",
        "Group_Title": "SRG-APP-000001",
        "Rule_ID": "SV-222387r508029_rule",
        "Rule_Ver": "APSC-DV-000010",
        "Rule_Title": "The application must provide a capability to limit the number of logon sessions per user.",
        "Fix_Text": "Design and configure the application to specify the number of logon sessions that are allowed per user.",
        "STATUS": "Not_Reviewed",
        "FINDING_DETAILS": "",
        "COMMENTS": "",
        "Unique_ID": "undefined_host-SV-222387r508029_rule-20230406"
    },
]
```

## TODO

- Implement command line argument parsing

- Interface?

---

## Credits

Inspired by "a Python script to extract data out of a DISA STIG Viewer xccdf file to a CSV" @author Michael Joseph Walsh <github.com@nemonik.com> and the original [Github link](https://gist.github.com/nemonik/951a0e55436e0708222b). Shout out.

> Note: (This was a Python2 implementation that I changed to Python3 and incorporated into `stig_converter.py`)

---

## License

**Allen Montgomery** - <allen@iosecurityio> - IO Security

Use responsibly at your leisure.

---

## Legal

Department of Defense and Defense Information Systems Agency (DISA) are the owners of the STIGs and the associated documentation. The STIGs are provided as a public service. You are free to use the STIGs in any way you see fit provided that you give credit to the DoD and DISA. The STIGs are provided "as is" without any warranty of any kind.

![DoD and DISA](./DoD-DISA-logos-as-JPEG.jpg)
