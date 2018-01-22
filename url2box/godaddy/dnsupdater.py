#!/usr/bin/env python3

import pif
import godaddypy
import time
import logging

# GoDaddy domain & authentication
domains="GODADDYDOMAINS".strip()
publickey="GODADDYPUBLICKEY"
privatekey="GODADDYPRIVATEKEY"

logging.basicConfig(filename="dnsupdater.log",filemode='a',
    level=logging.INFO, format='%(asctime)s: %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S')

def say(s):
  logging.info(s)
  logging.getLogger().handlers[0].flush()

# Look at our domain list and log it.
domainlist=domains.split(" ")
domcnt=len(domainlist)

if domcnt==1:
  say("dnsupdater:  Updating IP address on GoDaddy for domain "+domains+".")
else:
  say("dnsupdater:  Updating IP address on GoDaddy for "+str(domcnt)+" domains:")
  say("    "+domains)

previp="none"
passno=0
sleepsecs=10
while True:
  passno+=1
  if (passno>10):
    sleepsecs=300
  time.sleep(sleepsecs)
  currip=pif.get_public_ip()

  # Did the IP address change since last time?
  if (previp!=currip):
    if (previp=="none"):
      say("Initial IP address is "+currip+".")
    else:
      say("IP changed from "+previp+" to "+currip+".")

    try:
      acct=godaddypy.Account(api_key=publickey,api_secret=privatekey)
      client=godaddypy.Client(acct)
      say("Logged into GoDaddy.")

      # Loop through domains to be updated
      for domain in domainlist:
        try:
          ok=client.update_record_ip(currip,domain,name='@',record_type='A')
          if ok:
            say(" ... successfully updated "+domain+".")
          else:
            say(" ... unable to update "+domain+"!!!")
        except:
          say("Error updating domain "+domain+":")
          say("  "+sys.exc_info()[1])
        # end try updating domain
      # end for each domain in the list

      previp=currip
      client=None
      acct=None
    except:
      say("Error updating IP:")
      say(sys.exc_info()[1])
    # end try
  # end if changed IP
# end while
