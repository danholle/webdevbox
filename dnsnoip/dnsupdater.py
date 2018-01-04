#!/usr/bin/env python3

import pif
import godaddypy
import time
import logging

# GoDaddy domain & authentication
domain="GODADDYDOMAIN"
publickey="GODADDYPUBLICKEY"
privatekey="GODADDYPRIVATEKEY"

logging.basicConfig(filename="dnsupdater.log",filemode='a',
    level=logging.INFO, format='%(asctime)s: %(message)s',
    datefmt='%Y/%m/%d %I:%M/%S %p')
logging.info("Updating IP address for "+domain+" on GoDaddy.")
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
      print("Initial IP address is "+currip+".")
    else:
      print("IP changed from "+previp+" to "+currip+".")
    client=godaddypy.Client(acct)
    logging.info("Logged into godaddy.")
    client.update_ip(currip,domains=[domain])
    logging.info("Set the address for "+domain+" to "+currip+".")
    previp=currip
    client=None
