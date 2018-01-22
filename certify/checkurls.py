#!/usr/bin/env python3

import sys
import pif
import socket
import time
import logging

def getip(u):
  ans="unknown"
  try:
    # print("About to check "+u+"...")
    ans=socket.gethostbyname(u)
  except socket.gaierror:
    pass
  # end try
  return ans
# end def getip

domains=sys.argv[1:]
print("There are "+str(len(domains))+" URLs in the list.")

currip=pif.get_public_ip()
print("Our current IP is "+currip)

errors=0
notready=None
for url in domains:
  urlsip=getip(url)
  msg=url+" resolves to "+urlsip
  if urlsip==currip:
    print(msg+":  success!")
  else:
    print(msg+":  fail!")
    if notready==None:
      notready=url
    else:
      notready+=" "+url
    errors+=1
  # end if ip matches our own
# end for each domain

if errors>0:
  print("URLs which are not ready:  "+notready)
  exit(1)
else:
  print("Looking good!")
  exit(0)
# end if too many errors

