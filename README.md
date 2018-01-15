## ***webdevbox:***
# **Setting Up a Web Application Development Server**

-------

Building web applications on a home server is one thing. 
Making them available on the public internet is something 
else.
  
Dealing with dynamic IP's, controlling and securing what's 
visible externally, certificates and encryption... it's 
not exactly rocket science, but it can be a pain to get it 
all to play nicely together.

If you're trying to do something similar, and these scripts 
can take away that pain for you, terrific.

--------

Starting point:
 *  You have an Ubuntu machine you want to use as a platform for
    developing and running web applications
 *  That machine is on a home network with a
    broadband connection through some router/hub
 *  You have set up an URL where you want your
    server to appear on the public internet... for example, 
     *  a domain from GoDaddy, or 
     *  a dynamic IP forwarding URL from no-ip.com (free). 
     *  Note:  *I'm not promoting either of these;  these are 
        just the ones I've successfully used and scripted.*

Ending point:
 *  Any internet browser who goes to your URL is connected 
    to your Ubuntu machine.
 *  That URL remains connected through your home broadband
    dynamic IP address through a DNS updater which runs 
    automatically and transparently (systemd service).
 *  Inbound web traffic is routed first to a (reverse)
    proxy server (nginx) which acts as a secure gatekeeper
     *  All interactions are through a certified, encrypted
        connection to protect you and your clients
     *  You have ultimate control on what resources you 
        expose externally and how... potentially delivering
        HTML, servlet/JSP, and/or node.js content 
     *  In particular, you can prevent access to content 
        you DON'T wish to expose externally, such as test/dev
        content or administrative tools
 *  Multiple back end web servers assumed.  Currently
    Tomcat for servlet/JSP webapps;  nginx for pure
    HTML5.  Planned:  node.js, Jenkins (for CD/CI)
 *  These simply appear on the public internet as different
    paths from your public URL   

--------

Setting up the webdevbox is broken into the following steps.  
Each step has a TL;DR writeup that takes you through the
process in some detail.
 *  [commonbase](commonbase/README.md) installs common prerequisites:  compilers, build tools, libraries.
 *  [gateway](gateway/README.md) installs a gateway server to manage secure inbound connections from the Web
 *  [url2box](url2box/README.md) sets up a link between your external URL and your webdevbox (dynamic IP).
 *  [tomcat](tomcat/README.md) sets up the Apache Tomcat web server
 *  [certify](certify/README.md) creates a security certificate and configures the gateway for it.

--------

## **Quick Start**

I'm going to assume you have this page up on a
browser, and that you've got command line access
to your webdevbox with sudo privileges.

First, let's grab the scripts and temporarily land
them on your webdevbox:

    git clone https://github.com/danholle/webdevbox
    cd webdevbox

Now let's install the common base (prerequisites):

    commonbase/install

Now let's install the secure gateway.  We use nginx for
this.  This step also includes things like setting
up port forwarding; see the [gateway](gateway/README.md)
TL;DR writeup first.  

    gateway/install

Now let's connect our external URL to the webdevbox.
If, for example, you have used No-IP.com to set up an
URL like mynoipurl.ddns.net, you would next say

    url2box/noip/install mynoipurl.ddns.net

or, if you have a GoDaddy URL like mygodaddyurl.com,

    url2box/godaddy/install mygodaddyurl.com "myL0n6Pub1icK3y" "pr1vat3k3y"

where the keys are from GoDaddy (see the [url2box](url2box/README.md)]
writeup for details).  Then we'll install Tomcat:

    tomcat/install 8081 admin s3cr3t

which, as described in the [tomcat writeup,](tomcat/README.md) will 
set up Tomcat listening on port 8081.  Now we'll set up our 
certified secure connection:

    certify/install mygodaddyurl.com

And you're up and running!



