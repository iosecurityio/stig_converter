import csv
import datetime
import glob
import os
import requests
import xml.etree.ElementTree as ET

# CKL always stands for STIG CHECKLIST, always.
# GLOB is an absolute filepath that can use wildcards

# List of projects with STIG checklists
PROJECTS = ["project-1","project-2","project3"]
# Root path of file directory (Windows else /etc/dir/)
PROJ_ROOT = "\\\\share\\home\\group\\project\\"
# Glob from the root path
PROJ_GLOB = f"{PROJ_ROOT}**\\STIGs\\*.ckl"
# Todays date to append to new CSVs
CUR_DATE = datetime.datetime.now().strftime('%Y%m%d')


def check_connection(url, timeout=5):
    '''Check connection to the URL provided, returns bool'''
    try:
        _ = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No connection to share available.")
    return False


def convert_to_csv(checklists=[]):
    '''Takes in a list of absolute filepaths to checklists and converts .ckl to .csv'''

    # Define your table headers as fieldnames
    fieldnames = ['HOST_NAME', 'HOST_IP', 'Vuln_Num', 'Severity', 'STATUS', 'Group_Title', 'Rule_ID', 'Rule_Ver', 'Rule_Title', 'Fix_Text', 'FINDING_DETAILS', 'COMMENTS']

    # For every Checklist in our list from get_checklists()
    for checklist in checklists:

        print("Processing: " + checklist)

        # Get the path to the checklist
        path = os.path.dirname(checklist)

        # Parse checklist path for a host_name in case checklist has no HOST_NAME
        host_name = parse_hostname(checklist)

        # extract the filename + extension
        filename = os.path.basename(checklist)

        # strip the name from the extension
        new_name = os.path.splitext(filename)

        # create a new filepath/name with the date and extension, replace spaces with underscores
        new_csv = path + new_name[0].replace(" ", "_") + f"-{CUR_DATE}.csv"

        # Open a new CSV file to write to
        with open(new_csv, 'w', newline='') as csvfile:

            # creates a CSV DictWriter to write dictionaries
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # writes fieldnames as the table headers
            writer.writeheader()

            # Creates an XML elementtree from a checklist
            tree = ET.parse(checklist)

            # get the root node of the XML tree
            root = tree.getroot()

            # each finding is one row in the CSV, writing with dictwriter
            finding = {}

            # Parse the ASSET node for asset details
            for asset in root.iter('ASSET'):
                if asset.find('HOST_NAME').text == False:
                    finding['HOST_NAME'] = host_name
                else:
                    finding['HOST_NAME'] = asset.find('HOST_NAME').text
                finding['HOST_IP'] = asset.find('HOST_IP').text

            # Recursively get all of the finding details for all stig data in each vuln
            for vuln in root.iter('VULN'):
                for stig_data in vuln.findall('./STIG_DATA'):
                    if (stig_data.find('VULN_ATTRIBUTE').text in ['Vuln_Num', 'Severity', 'Group_Title', 'Rule_ID', 'Rule_Ver', 'Rule_Title', 'Fix_Text']):
                        finding[stig_data.find('VULN_ATTRIBUTE').text] = stig_data.find('ATTRIBUTE_DATA').text.replace('\n', '')

                # Get the other nodes that arent STIG data
                finding['STATUS'] = vuln.find('./STATUS').text
                finding['FINDING_DETAILS'] = vuln.find('./FINDING_DETAILS').text
                finding['COMMENTS'] = vuln.find('./COMMENTS').text

                # Write the finding row from the dict
                writer.writerow(finding)

            print("Created: " + new_csv)


def get_checklists(checklist_location):
    '''Takes a location "glob" and returns a list of .ckl files detected'''
    return [ckl for ckl in glob.glob(checklist_location)]


def parse_hostname(checklist, project_list=PROJECTS):
    '''Parse a hostname out of an absolute path and return the hostname if its in the project_list'''
    project_path = checklist.split("\\")

    for item in project_path:
        if item.lower() in project_list:
            return item
    return ''


def main():

    # 1. Check Connection at the beginning
    #if check_connection(PROJ_ROOT):

    #2. Get list of checklists that exist and look at them
    stig_checklists = get_checklists(PROJ_GLOB)
    for checklist in stig_checklists:
        print(f"Checklist detected: {checklist}")
        print(f"Hostname detected: {parse_hostname(checklist)}")

    #3. convert them to csv files
    #print(f"Converting {stig_checklists} to .csv files")
    #convert_to_csv(stig_checklists)


# RUN MAIN
if __name__ == "__main__":
    main()