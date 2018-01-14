## ***webdevbox/url2box:***
# **Connect an external URL to our webdevbox**

--------

If you want to present content on the public internet, then
you need to have an external URL.  You can get such a URL
from domain name providers like GoDaddy, or dynamic IP 
services from outfits like No-IP.

This step is about connecting this external URL to your webdevbox.

blah blah blah


## **What do I need to do?**

I've put together tools for the two services I mentioned above...
GoDaddy and No-IP. blah blah blah

    url2box/noip/install webdevboxexample.ddns.net

blah blah blah

    url2box/godaddy/install webdevboxexample.com "G0ofyV3ryL0ngK3y" "5h0rt3rPr1vat3K3y"

blah blah blah


## **I'm done.  Did it work?**

Well, probably.  But if you'd like to make sure, and you should, you can now test 
the IP forwarding by trying out your URL.  In a browser on a web-connected client
machine, go to your URL... if you're using a domain provider like GoDaddy, something
like

    http://webdevboxexample.com

or if you're using a dynamic IP provider like No-IP, maybe
    
    http://webdevboxexample.ddns.net

or whatever.  For your efforts, you should see a Hello World page we installed on
a previous step.


## **What do I do next?**

We'll now set up back end web servers.  At the moment I only have
one scripted, and that's [tomcat](../tomcat/README.md).

