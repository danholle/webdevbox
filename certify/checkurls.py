#!/usr/bin/env python3

import sys
import pif
import socket
import time
import logging

def getip(u):
  try:
    ans=socket.gethostbyname(u)
  except InsecureRequestWarning: 
    print("tilt")
  # end try
  return ans
# end def getip

domains=sys.argv[1:]
print("There are "+str(len(domains))+" URLs in the list.")
currip=pif.get_public_ip()
print("Current IP is "+currip)

for url in domains:
  sleepsecs=2
  errors=0
  urlsip=getip(url)
  while (urlsip!=currip):
    print(url+"'s IP is "+urlsip)
    errors+=1
    if (errors>4):
      print("URL "+url+" does not seem to point to our IP.")
      exit(1)
    # end if too many errors
    time.sleep(sleepsecs)
    sleepsecs+=sleepsecs 
    urlsip=getip(url)
  # end while this url isn't ready
# end for all urls

