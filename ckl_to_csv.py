import csv
import glob
import requests
import xml.etree.ElementTree as ET

# CKL/ckl always stands for STIG CHECKLIST, always.
# GLOB is basically a directory path
#PROJECTS = ["/afaems","/slcms","/myvector","/seco","/msep","/aiportal"]
BAM_ROOT = "//bamtech/public/IA/Projects/"
CKL_SHARE_GLOB = f"{BAM_ROOT}['afaems','slcms','myvector','seco','msep','aiportal']/STIGs/*.ckl"
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


def convert_to_csv(checklists, output_file=OUTPUT_CSV):
    ### Function that takes in a directory path, and converts .CKL to .CSV as an output_file(s)
    # Define your table headers as fieldnames
    fieldnames = ['HOST_NAME', 'HOST_IP', 'Vuln_Num', 'Severity', 'STATUS', 'Group_Title', 'Rule_ID', 'Rule_Ver', 'Rule_Title', 'Fix_Text', 'FINDING_DETAILS', 'COMMENTS']

    # Open a new CSV file to write to
    with open(output_file, 'w', newline='') as csvfile:

        # creates a CSV DictWriter to write dictionaries
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # writes fieldnames as the table headers
        writer.writeheader()
  
        # Grabs every checklist in the checklist_location
        for checklist in checklists:
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
                    
                    
def get_checklists(checklist_location):
    # just pass this a path and it will get checklists, regex syntax included
    # returns list of every checklist detected in the path(s)
    return [ckl for ckl in glob.glob(checklist_location, recursive=True)]


def main():

    # 1. Check Connection at the beginning
    # if check_connection(BAM_ROOT):

    #2. Get list of checklists that exist, look at them
    # get_checklists(location)
    stig_checklists = get_checklists(CKL_GLOB)
    print(f"Checklists detected: {stig_checklists}")

    #3. convert them to csv files
    # convert_to_csv(get_checklists(CKL_GLOB))
    print(f"Converting {stig_checklists} to .csv")
    convert_to_csv(stig_checklists, OUTPUT_CSV)


# RUN RUN RUN      
if __name__ == "__main__":
    main()