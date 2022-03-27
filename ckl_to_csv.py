import csv
import glob
from importlib import reload
import os
import requests
import sys
import xml.etree.ElementTree as ET


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
        print("No internet connection available.")
    return False


def savetoCSV(checklist_location=CKL_GLOB, output_file=OUTPUT_CSV):

    fieldnames = ['HOST_NAME', 'HOST_IP', 'Vuln_Num', 'Severity', 'Group_Title', 'Rule_ID', 'Rule_Ver', 'Rule_Title', 'Fix_Text']

    # writing to csv file
    with open(output_file, 'w', newline='') as csvfile:
        # specifying the fields for csv file
        # fields = ['id','severity','title','description','iacontrols','ruleID','fixid','fixtext','checkid','checktext']
        # creating a csv DictWriter object to write to
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

        # writing headers aka field names
        writer.writeheader()
  
        for checklist in glob.glob(CKL_GLOB):
                print("Processing: " + checklist)
                tree = ET.parse(checklist)
                root = tree.getroot()
                finding = {}

                for asset in root.iter('ASSET'):
                    finding['HOST_NAME'] = asset.find('HOST_NAME').text
                    finding['HOST_IP'] = asset.find('HOST_IP').text

                for vuln in root.iter('VULN'):
                    for stig_data in vuln.findall('./STIG_DATA'):
                        if (stig_data.find('VULN_ATTRIBUTE').text in ['Vuln_Num', 'Severity', 'Group_Title', 'Rule_ID', 'Rule_Ver', 'Rule_Title', 'Fix_Text']):
                            finding[stig_data.find('VULN_ATTRIBUTE').text] = stig_data.find('ATTRIBUTE_DATA').text.replace('\n', '')
        
                    writer.writerow(finding)

      
def main():

    #check_connection(SHARE)
    savetoCSV()


# RUN RUN RUN      
if __name__ == "__main__":
    main()