import csv
import glob
from importlib import reload
import os
import requests
import sys
import xml.etree.ElementTree as ET


#SHARE = "//bamtech/public/IA/Projects"
#PROJECTS = ["/afaems","/slcms","/myvector","/seco","/msep","/aiportal"]

INPUT_CKL = "F:/Allen/python/ckl_to_csv/blank_checklist.ckl"
OUTPUT_CSV = "F:/Allen/python/ckl_to_csv/TestNewChecklist.csv"
CKL_GLOB = "F:/Allen/python/ckl_to_csv/*.ckl"

def check_connection(url, timeout=5):
    try:
        _ = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False


def parse_XML(input_file=INPUT_CKL):
    """
    # create element tree object using xml etrees parse function
    tree = ET.parse(cklfile)
    # get root element (ie <CHECKLIST> on line 3)
    root = tree.getroot()
    # Parse Asset Information
    
    for node in root.findall('./ASSET'):
        # empty asset dictionary
        asset = {}
        # iterate child elements of <ASSET> and put relevant info in the list
        for subnode in node:
            if subnode.tag == "ROLE":
                asset['role'] = subnode.text
            elif subnode.tag == "ASSET_TYPE":
                asset['asset_type'] = subnode.text
            elif subnode.tag == "MARKING":
                asset['marking'] = subnode.text
            elif subnode.tag == "HOST_NAME":
                asset['host_name'] = subnode.text

            else:
                continue
        # Add everything to the asset list
        findings.append(asset)

    # Parse Finding Information (ie. iterate <VULN> tags)
    for node in root.findall('./STIGS/iSTIG/VULN'):
        
        # empty finding dictionary
        findings = {}
        
        # iterate child elements of item
        for child in node:
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                findings['media'] = child.attrib['url']
            else:
                findings[child.tag] = child.text
  
        # append finding dictionary to findings list
        finding_list.append(findings)
      
    # return findings list
    return finding_list
    """
    return 1


def savetoCSV(input_file=INPUT_CKL,output_file=OUTPUT_CSV):

    fieldnames = ['HOST_NAME', 'HOST_IP', 'Vuln_Num', 'Severity', 'Group_Title', 'Rule_ID', 'Rule_Ver', 'Rule_Title', 'Fix_Text']

    # writing to csv file
    with open(output_file, 'w', newline='') as csvfile:
        # specifying the fields for csv file
        # fields = ['id','severity','title','description','iacontrols','ruleID','fixid','fixtext','checkid','checktext']
        # creating a csv DictWriter object to write to
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames = fieldnames)

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
                            finding[stig_data.find('VULN_ATTRIBUTE').text] = stig_data.find('ATTRIBUTE_DATA').text
        
                    writer.writerow(finding)

      
def main():

    #check_connection(SHARE)
    savetoCSV()


# RUN RUN RUN      
if __name__ == "__main__":
    main()