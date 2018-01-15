#!/usr/bin/env python3

import pif
import godaddypy
import time
import logging

# GoDaddy domain & authentication
domains="GODADDYDOMAINS".strip()
publickey="GODADDYPUBLICKEY"
privatekey="GODADDYPRIVATEKEY"

domainlist=domains.split(" ")

logging.basicConfig(filename="dnsupdater.log",filemode='a',
    level=logging.INFO, format='%(asctime)s: %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S')
logging.info("dnsupdater:  Updating IP address for "+domains+" on GoDaddy.")
acct=godaddypy.Account(api_key=publickey,api_secret=privatekey)
previp="none"
passno=0
sleepsecs=10
while True:
  passno+=1
  if (passno>10):
    sleepsecs=60
  time.sleep(sleepsecs)
  currip=pif.get_public_ip()
  if (previp!=currip):
    if (previp=="none"):
      logging.info("Initial IP address is "+currip+".")
    else:
      logging.info("IP changed from "+previp+" to "+currip+".")
    client=godaddypy.Client(acct)
    logging.info("Logged into godaddy.")
    client.update_ip(currip,domains=domainlist)
    logging.info("Set the address for "+domains+" to "+currip+".")
    previp=currip
    client=None
  # end if changed IP
# end while
