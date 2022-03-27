import csv
import glob
from importlib import reload
import os
import requests
import xml.etree.ElementTree as ET

# BAM Global vars
#SHARE = "//bamtech/public/IA/Projects"
#PROJECTS = ["/afaems","/slcms","/myvector","/seco","/msep","/aiportal"]

OUTPUT_CSV = "F:/Allen/python/ckl_to_csv/TestNewChecklist.csv"
CKL_GLOB = "F:/Allen/python/ckl_to_csv/*.ckl"

def check_connection(url, timeout=5):
    ## Check connection to the URL
    try:
        _ = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No connection to share available.")
    return False


def convert_to_csv(checklist_location=CKL_GLOB, output_file=OUTPUT_CSV):

    fieldnames = ['HOST_NAME', 'HOST_IP', 'Vuln_Num', 'Severity', 'STATUS', 'Group_Title', 'Rule_ID', 'Rule_Ver', 'Rule_Title', 'Fix_Text', 'FINDING_DETAILS', 'COMMENTS']

    # Open a CSV file to write to
    with open(output_file, 'w', newline='') as csvfile:

        # creates a CSV DictWriter to write dictionaries
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # writes fieldnames aka table headers if fieldnames is set
        writer.writeheader()
  
        # Grabs every checklist in the checklist_location
        for checklist in glob.glob(checklist_location):
                print("Processing: " + checklist)
                
                # Creates an XML elementtree from a checklist
                tree = ET.parse(checklist)

                # get the root node of the XML tree
                root = tree.getroot()

                # each finding is one row in the CSV, writing with dictwriter
                finding = {}

                # Parse the ASSET node for asset details
                for asset in root.iter('ASSET'):
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
                    
                    
      
def main():

    #check_connection(SHARE)
    convert_to_csv()


# RUN RUN RUN      
if __name__ == "__main__":
    main()