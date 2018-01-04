
<h1><b><i>webdevbox:</i><br/>Setup Scripts for a Web Application Development Server</b></h1>

Building web applications on a home server is one thing. Making  
them available on the public internet is something else.
  
Dealing with dynamic IP's, controlling
and securing what's visible externally, certificates and 
encryption... it's not exactly rocket science, but it can be
a pain to get it all to play nicely together.

If you're trying to do something similar, and these scripts
can take away that pain for you, terrific.

--------

Starting point:
 *  You have an Ubuntu machine on a home network with a
    broadband connection through some router/hub
 *  You have set up an URL where you want your
    server to appear on the public internet... either
     *  a domain from GoDaddy, or 
     *  a dynamic IP forwarding URL from no-ip.com (free). 
     *  *I'm not promoting either of these;  these are 
        just the ones I've successfully used and scripted.*

Ending point:
 *  Your URL is connected to your Ubuntu machine.
 *  That URL remains connected through your home broadband
    dynamic IP address through a DNS updater which runs 
    automatically and transparently (systemd service).
 *  Inbound web traffic is routed first to a (reverse)
    proxy server (nginx) which acts as a secure gatekeeper
     *  All interactions are through a certified, encrypted
        connection
     *  You can choose which content you wish to expose
        externally, without losing local access to other
        content (e.g. administrative stuff, test/dev stuff)
 *  Multiple back end web servers assumed.  Currently
    Tomcat for servlet/JSP webapps;  nginx for pure
    HTML5.  Planned:  node.js, Jenkins (for CD/CI)
 *  These simply appear on the public internet as different
    paths from your public URL   
 
--------

<h2>Quick Start</h2>

Everything here is quick, so we are almost done.

Let's say you have set up a dynamic IP on no-ip.com
which is xyz.ddns.net.  (I apologize to anybody who
might own that;  no offense intended.)

If you have a place where you normally put git repos,
cd to that.  But if you don't have such a place, no 
worries... this will all work.

Enter the following commands:

    git clone https://github.com/danholle/webdevbox
    cd webdevbox
    base/install
    dnsnoip/install
    certificate/install xyz.ddns.net
    
After those 5 commands, you should be able to go to 
your URL (like xyz.ddns.net) and you should see a
Hello World page from your home machine.

If you are using a GoDaddy domain, say xyz.com,
replace the dnsnoip step above with 

    dnsgodaddy/install "xyz.com" "TheG00FyLongPublicKey" "TheG00fyLongPrivate"

where the 2 keys above emerge when you go to developer.godaddy.com, 
click on the Keys link, and create a Production key (+).

I have to go now.  But I hope you are on your way.  If this works for you,
let me know at webdevbox@danholle.com.  If it does NOT work for you, then
ESPECIALLY let me know.  

Thanks a bunch.
 

