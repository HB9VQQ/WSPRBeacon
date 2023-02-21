## Python Script to parse Master list from Kin EA3CV and create set_badnode and unset_badnode
## Version < 250 will go to set_badnode, version ≥ 250 will go to unset_badnode
## Author HB9VQQ
#
from base64 import decode
import urllib.request
import logging
import re


#fileset="/spider/cmd_import/set_badnode"
#fileunset="/spider/cmd_import/unset_badnode"
#auditlog="/spider/badnodeparser/badnode_audit.log"
#applog="/spider/badnodeparser/badnode.log"

fileset="set_badnode"
fileunset="unset_badnode"
auditlog="badnode_audit.log"
applog="badnode.log"

URL='https://raw.githubusercontent.com/EA3CV/dxspider_info/main/Node_version/Master-latest.txt'

logging.basicConfig(filename=applog,  level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
try:
    logging.info(f'Retrieving: {URL}' )
    data= urllib.request.urlopen(URL)
    
    
except Exception as E:
    logging.error(E)
    exit(1)

set_badnode=[]
unset_badnode=[]
total=0

logging.info('Parsing content')
for line in data:
    line = line.decode()
    line = re.split('\s+', line)
    if line[0] =='':
        continue
    elif len(line) > 4:
        logging.info("file downladed: " + " ".join(line))
        continue
    elif line[0].startswith("Total:"):
        total = line[1]
    else:
        if line[2]=='No':
            unset_badnode.append(line[0])
        elif int(line[2])<250:
            set_badnode.append(line[0])
        else:
            unset_badnode.append(line[0])
logging.info(f'Numbers of entries in file={total}') 
with open(fileset,'w') as sbn:
    sbn.write("set/badnode "+" ".join(set_badnode))
logging.info("number of set badnodes="+str(len(set_badnode)))
with open(fileunset,'w') as ubn:
    ubn.write("unset/badnode "+" ".join(unset_badnode))
logging.info("number of unset badnodes="+str(len(unset_badnode)))
with open(auditlog,'w') as alog:
    alog.write("Set Badnode:\n")
    alog.write("set/badnode "+" ".join(set_badnode) +"\n")
    alog.write("\n")
    alog.write("Unset Badnode:\n")
    alog.write("unset/badnode "+" ".join(unset_badnode)+"\n")
