## ***webdevbox/url2box:***
# **Connect an external URL to our webdevbox**

--------

If you want to present content on the public internet, then
you need to have an external URL.  You can get such a URL
from domain name providers like GoDaddy, or dynamic IP 
services from outfits like No-IP.

This step is about connecting this external URL to your webdevbox.


## **What do I need to do?**

That depends.  Perhaps you have a domain, and already have some way
of connecting that domain to your home IP address.  If so, great...
we're done and you can move on to the next thing.

But if you don't, I've put together tools for the two services I 
mentioned above... GoDaddy and No-IP.  I'm not advocating or pushing
either of these;  it's just that I've used both, and if my scripts
are helpful to you, fine.  

If you are using some other service, you
may find that you can adapt these scripts to do your bidding.

### If you have a [noip](noip/README.md) URL...

There are a number of companies which do dynamic IP forwarding for
free.  The largest of these is No-IP.

A URL from www.noip.com consists of a name you come up with (let's say
mynoipprefix) followed by a domain that No-IP owns (like ddns.net).  
Their service is to let you route requests to the composite name 
(in this case, mynoipprefix.ddns.net) to your IP address.

First, go to www.noip.com and lay claim to your shiny new URL.

To set up a DNS updater that keeps your URL pointing at your webdevbox,
just say
  
    url2box/noip/install mynoipprefix.ddns.net

Once that's all done, you will be able to fire up a browser anywhere 
and go to 

    http://mynoipprefix.ddns.net

and you should see the Hello World page, faithfully rendered by your 
friendly neighbourhood webdevbox.  


### If you have a [godaddy](godaddy/README.md) URL...

GoDaddy is the biggest domain registrar in the world, so maybe you 
have a domain with them.  Let's say you're the proud owner of
mygodaddydomain.com, and want to make that name forward to your 
webdevbox.

To set this up, you need to first go to GoDaddy and get some API
keys which will be used in updating your IP.  Go to 

    developer.godaddy.com

and click on Keys.  Create a new PRODUCTION key pair.  Now you are
ready to set up your DNS updater:

    url2box/godaddy/install "G0ofyV3ryL0ngK3y" "5h0rt3rPr1vat3K3y" mygodaddydomain.com

This will create a DNS updater on your webdevbox which will update
mygodaddydomain.com's IP address when it starts, then again whenever
your home IP changes.  The updater starts as a daemon every time
your webdevbox starts.

Now you should be able to go to 

    http://mygodaddydomain.com

and be rewarded with our Hello World page brought to you by your 
webdevbox, with a little help from nginx.


## **What do I do next?**

We'll now set up back end web servers.  At the moment I only have
one scripted, and that's [tomcat](../tomcat/README.md).

