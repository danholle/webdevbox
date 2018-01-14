## ***webdevbox:***
# **Setting Up a Web Application Development Server**

TODO List:
 *  Do a security advice page:  https://help.ubuntu.com/community/SSH/OpenSSH/Configuring 
 *  Switch to pulling Tomcat from Apache archive
 *  ~~Get commonbase/gateway/url2box/certify to work end to end for GoDaddy~~
 *  Get them to work end to end for No-IP
 *  Rationalize purge for each unit:  we are removing a partially installed
    or somehow broken thing to a clean point, not a clean rollback
 *  Rationalize install scripts to be like gateway/install:  i.e.
     *  Check if already installed (offer purge if reinstall desired)
     *  Check if prereqs WE USE are in place
     *  Check parameter validity
     *  Actually do it
     *  Describe validation steps
     *  Describe what is next if validation works
 *  Rationalize writeups for each unit
     *  Common header format
     *  Describe what function we are fulfilling
     *  What do I need to do?
     *  Validation steps
     *  Next Steps with link to its .md
 *  Fix up this main writeup 
     *  Common header format
     *  Objective
     *  Assumptions
     *  Overview of solution / ground rules
         *  Links out to TL;DR pages
     *  Quick Start Example
         *  Just the script
 *  Do a once-over eyeballing .md files and links
 *  Do a dry run through GoDaddy and No-IP
 *  gitsave

-------

Building web applications on a home server is one thing. Making them available on the public internet is something else.
  
Dealing with dynamic IP's, controlling and securing what's visible externally, certificates and encryption... it's not exactly rocket science, but it can be a pain to get it all to play nicely together.

If you're trying to do something similar, and these scripts can take away that pain for you, terrific.

--------

Starting point:
 *  You have an Ubuntu machine on a home network with a
    broadband connection through some router/hub
 *  You have set up an URL where you want your
    server to appear on the public internet... either
     *  a domain from GoDaddy, or 
     *  a dynamic IP forwarding URL from no-ip.com (free). 
     *  Note:  *I'm not promoting either of these;  these are 
        just the ones I've successfully used and scripted.*

Ending point:
 *  Any internet browser who goes to your URL is connected to your Ubuntu machine.
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

<h2>Quick Start</h2>

Everything here is quick, so we are almost done.

Let's say you have set up a dynamic IP on no-ip.com
which is mynoipdomain.ddns.net.  (I apologize to anybody who
might own that;  no offense intended.)

Enter the following commands:

    git clone https://github.com/danholle/webdevbox
    cd webdevbox
    nginx/install
    tomcat/install 8081
    dnsnoip/install
    certificate/install mynoipdomain.ddns.net
    
After those 5 commands, you should be able to go to 
your URL (in the example, mynoipdomain.ddns.net) and you should see a
Hello World page from your home machine.  

If you are using a GoDaddy domain, the last two commands will change.  For the sake
of discussion, lets say your GoDaddy domain name is mygodaddydomain.com (again, the
same apologies apply.)  say xyz.com,
replace the dnsnoip step above with 

    dnsgodaddy/install "xyz.com" "TheG00FyLongPublicKey" "TheG00fyLongPrivate"

where the 2 keys above emerge when you go to developer.godaddy.com, 
click on the Keys link, and create a Production key (by clicking on the + sign).

I have to go now.  But I hope you are on your way.  If this works for you,
let me know at webdevbox@danholle.com.  If it does NOT work for you, then
ESPECIALLY let me know.  

Thanks a bunch.
 

