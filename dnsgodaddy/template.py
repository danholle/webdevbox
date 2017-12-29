#!/usr/bin/env python3

import pif
import godaddypy
import time

# GoDaddy domain & authentication
domain="GODADDYDOMAINNAME"
publickey="GODADDYPUBLICKEY"
privatekey="GODADDYPRIVATEKEY"

acct=godaddypy.Account(api_key=publickey,api_secret=privatekey)
previp="none"
passno=0
sleepsecs=10
while True:
  passno+=1
  currip=pif.get_public_ip()
  if (previp==currip):
    print("Pass "+passno+":  IP address is still "+currip+".")
  else:
    if (previp=="none"):
      print("Initial IP address is "+currip+".")
    else:
      print("IP changed from "+previp+" to "+currip+".")
    client=godaddypy.Client(acct)
    print("Logged into godaddy.")
    client.update_ip(currip,domains=[domain])
    print("Set the address for "+domain+" to "+currip+".")
    previp=currip
    client=None
  if (passno>10):
    sleepsecs=60
  time.sleep(sleepsecs)
