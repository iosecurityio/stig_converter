###
# A Python script to extract data out of a DISA STIG Viewer xccdf file to a CSV
# @author Michael Joseph Walsh <github.com@nemonik.com>
##
import csv
import glob
import os
import sys
import xml.etree.ElementTree as ET

# Original github here:
# https://gist.github.com/nemonik/951a0e55436e0708222b
# Note this is Python2 implementation
# changed to Python3 and incorporated into ckl_to_csv.py

reload(sys)
sys.setdefaultencoding('utf-8')

with open('tmp.csv', 'ab+') as csvfile:
        fieldnames = ['HOST_NAME', 'HOST_IP', 'Vuln_Num', 'Severity', 'Group_Title', 'Rule_ID', 'Rule_Ver', 'Rule_Title', 'Fix_Text']
        output = csv.DictWriter(csvfile, fieldnames=fieldnames)

        output.writeheader()

        for filename in glob.glob("*.xml"):
                print "processing: " + filename
                tree = ET.parse(filename)
                root = tree.getroot()
                row = {}

                for asset in root.iter('ASSET'):
                        row['HOST_NAME'] = asset.find('HOST_NAME').text
                        row['HOST_IP'] = asset.find('HOST_IP').text

                for vuln in root.iter('VULN'):
                        for stig_data in vuln.findall('STIG_DATA'):
                                if (stig_data.find('VULN_ATTRIBUTE').text in ['Vuln_Num', 'Severity', 'Group_Title', 'Rule_ID', 'Rule_Ver', 'Rule_Title', 'Fix_Text']):
                                        row[stig_data.find('VULN_ATTRIBUTE').text] = stig_data.find('ATTRIBUTE_DATA').text

                output.writerow(row)