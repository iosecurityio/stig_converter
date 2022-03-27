import csv
import requests
import xml.etree.ElementTree as ET
import os

# shared drive location - string
SHARE = "//bamtech/public/IA/Projects"
#projects in the projects folder - list
PROJECTS = ["/afaems","/slcms","/myvector","/seco","/msep","/aiportal"]
#location of checklist - string
CHECKLIST = "F:/Allen/python/STIGs/blank_checklist.ckl"

def check_connection(url, timeout=5):
    try:
        _ = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False


def parse_XML(cklfile=CHECKLIST):
    # create element tree object using xml etrees parse function
    tree = ET.parse(cklfile)
    # get root element (ie <CHECKLIST> on line 3)
    root = tree.getroot()
    # create empty lists for the asset and findings   
    findings = []
    # Parse Asset Information
    for node in root.findall('./ASSET'):
        # empty asset dictionary
        asset = {}
        # iterate child elements of <ASSET> 
        for subnode in node:
            if subnode.tag == "ROLE":
                asset['role'] = subnode.text.encode('utf8')
            elif subnode.tag == "ASSET_TYPE":
                asset['asset_type'] = subnode.text.encode('utf8')
            elif subnode.tag == "MARKING":
                asset['marking'] = subnode.text.encode('utf8')
            elif subnode.tag == "HOST_NAME":
                asset['host_name'] = subnode.text.encode('utf8')
            elif subnode.tag == "HOST_IP":
                asset['host_ip'] = subnode.text.encode('utf8')
            elif subnode.tag == "HOST_MAC":
                asset['host_mac'] = subnode.text.encode('utf8')
            elif subnode.tag == "HOST_FQDN":
                asset['host_fqdn'] = subnode.text.encode('utf8')
            elif subnode.tag == "TARGET_COMMENT":
                asset['target_comment'] = subnode.text.encode('utf8')
            elif subnode.tag == "TECH_AREA":
                asset['tech_area'] = subnode.text.encode('utf8')                
            elif subnode.tag == "TARGET_KEY":
                asset['target_key'] = subnode.text.encode('utf8')
            elif subnode.tag == "WEB_OR_DATABASE":
                asset['web_or_database'] = subnode.text.encode('utf8')
            elif subnode.tag == "WEB_DB_SITE":
                asset['web_db_site'] = subnode.text.encode('utf8')
            elif subnode.tag == "WEB_DB_INSTANCE":
                asset['web_db_instance'] = subnode.text.encode('utf8')
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
                findings[child.tag] = child.text.encode('utf8')
  
        # append finding dictionary to findings list
        finding_list.append(findings)
      
    # return findings list
    return finding_list
  
  
def savetoCSV(newsitems, filename):
    # specifying the fields for csv file
    fields = ['id','severity','title','description','iacontrols','ruleID','fixid','fixtext','checkid','checktext']
    
    # writing to csv file
    with open(filename, 'w') as csvfile:
  
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields)
  
        # writing headers (field names)
        writer.writeheader()
  
        # writing data rows
        writer.writerows(newsitems)
  
      
def main():
    #check access to shared drive
    #check_connection(SHARE)

    # parse xml file
    newsitems = parse_XML()

    # store news items in a csv file
    #savetoCSV(newsitems, 'topnews.csv')

      
if __name__ == "__main__":
    main()