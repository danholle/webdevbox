<p style="font-size: large; font-weight: bold; font-style: italic">
  webdevbox/gateway:
</p>
<p style="font-size: x-large; font-weight: bold">
  Setting Up nginx as a Secure Gateway to the Public Internet
</p>

--------

You may have a number of different servers running on your webdevbox...
maybe Tomcat, node.js, Jenkins, Drupal... any or all.  You may have 
some of these running on other boxes on your internal network.  Naturally
you'll want to isolate your remote users from your internal architecture,
and you'll want to isolate your internal architecture from hack attacks
from the public internet.

This is done with a gateway layer, in the form of nginx.  If you're not
familiar with it, nginx has been the most popular engine for the world's biggest
websites for many years now. 

We use it to do a number of things, such as
 -  Dealing with HTTP/HTTPS and certificates in one place, rather than
    needing to deal with it separately for each server
     -  Back end servers all talk straight HTTP
     -  All external traffic is HTTPS (encrypted and certified)
 -  Forward inbound traffic directed to an URL/path to whatever 
    back end server/port/path, through nginx's symbolic config 
    language
     -  Outside users see a logical site structure you choose rather than
        the physical structure of your back end servers
     -  You can choose what resources you want to expose 
        externally and what resources you don't.  For example,
        you may want to only allow administrative access 
        locally
     -  You can change the routing on the fly without bringing
        down either nginx or your back end servers
 -  nginx can directly serve HTML content without needing a 
    back end server for that
 -  And so forth.

In the "gateway" step, we'll deal with 
 -  the initial installation and configuration of nginx
 -  Set up port forwarding on your router/hub so public internet 
    traffic flows to your webdevbox
 -  Set up and enable your webdevbox firewall so your webdevbox
    is secure even if your local network gets hacked
 -  We'll check from an external server to make sure there are
    no surprising ports open on your router/hub
 -  We'll make sure your webdevbox is accessible on the public
    internet via nginx

So that's enough idle talk.  Time to do some actual stuff.


<h2>What do I need to do?</h2>

For starters, let's install nginx, which is simple enough:

    gateway/install

This will not only install nginx, but also set up the firewall as described, and put an HTML page in place that
we will use to verify internal and external access.  It will set things up so nginx starts automatically when
your webdevbox starts.  It will start nginx so you can test access.


<h3>Is nginx running?</h3>

Well, probably.  You can check in a few ways;  for example

    ps -A | grep nginx

will probably show you some number of nginx threads running.  I think it's one master and one slave for each core nginx found on your webdevbox.  Alternatively, you could say

    sudo systemctl status nginx

and it should say "active" plus a lot of gibberish that I don't understand, and something inside me feels you shouldn't understand it either.  You might need to type q to get out of this command.


<h3>Does nginx work?</h3>

Well, probably.  If you can fire up a browser on your webdevbox, do so and go to

    http://localhost

and you should get a Hello World page which claims it was installed by gateway/install.  Or, if your 
webdevbox is headless and you have another machine on your local network, and your webdevbox has a
hostname of (say) george, then you ought to be able to go to 

    http://george

from that other machine and see the same page.


<h3>Port Forwarding on your Local Network</h3>

I'm assuming you're on some sort of home broadband network.
There is some network hub which connects you to the outside
world;  that hub will have some public IP address which is
probably assigned dynamically and changes from time to time.

By default your network hub will be set to reject any attempts
to connect to any port.  What we want to do now is to redirect
any HTTP (port 80) or HTTPS (port 443) traffic to your
webdevbox... specifically, to nginx, our gatekeeper/proxy.

I am a BT subscriber here in the UK, and will give detailed
instructions for that environment.  You probably are NOT using
BT;  but I'm hoping that my description will give you a 
flavour of what you need to do in your environment.

For this description, I am going to pretend your webdevbox has
a hostname of "george".  Substitute your actual hostname as 
required.

The steps to set port forwarding on a BT Home Hub 5 are as follows:
 1.  Fire up a browser on any machine in your home network.  Aim
     it at the IP address of the hub admin server.  That address
     will be present in your documentation;  for BT, you'd go to
  
         http://192.168.1.254

     Yours may be similar.
 2.  Click Advanced Settings, then Firewall.  You should have
     a page presenting any current port forwarding you may have
     already set up.
 3.  Now let's go create a forwarding rule.  Click "Manage games
     and applications".
 4.  Call your rule "httphttps".  Set up the following ports:
| Protocol | Port Range | Transfer To | Description |
|------|----------|-------------|-------------|
| TCP  | 22 - 22    | 22 - 22       | This forwards your SSH traffic |
| TCP  | 80 - 80    | 80 - 80       | This forwards your HTTP traffic |
| TCP  | 443 - 443  | 443 - 443     | This forwards your HTTPS traffic |
     Click apply.
 5.  Click Return to Port Forwarding.
 6.  Under "Select game or application", choose "webdevbox".  Under 
     "Select Device", select george.  Click Add.  Click Apply.

<h3>Test your Public Access</h3>

On any machine with a browser on your home network, go to

    https://www.yougetsignal.com/tools/open-ports

This tool will display the public IP address of your hub.  Click the
link at the bottom of the list on the right that says "Scan all 
Common Ports".  It should show 22 and 80 as open, and none others.
If you thought 443 would be open, that's a fair guess;  but in this
initial configuration for nginx, he's not listening on 443 just yet.
Soon!

See the Remote Address?  Mine's something like 86.198.144.205.  Make
note of yours.  Now go to a browser anywhere (on or off your
broadband network) and go to that address.  Like

    http://86.198.144.205

but supplying your Remote Address instead.  You should get the
same Hello World page you saw minutes ago.


<h3>How are we doing so far?</h3>

Well, probably pretty good.  So far we have
 -  Installed nginx as the secure gateway
 -  Set up a firewall around your webdevbox
 -  Done the port forwarding via your router/hub
 -  Verified that there aren't any surprising ports exposed externally
 -  Accessed a Hello World page from the public internet via nginx


<h2>What do I do next?</h2>

Next we are going to connect your webdevbox to an external URL 
on the public internet.  I've got scripts here for dealing with
two possible kinds of external URL:
 -  You got a domain name from GoDaddy.  Or
 -  You got a dynamic IP URL from No-IP

If one of those applies, click on the link above and keep on truckin'.  
If not... say, you have a static IP and some way of pointing your URL to it...
or if not, perhaps you can adapt my scripts to your use case... then you
should go do all that, and verify that you can access the Hello World page
via http://<your url>.  Then you can safely move on to the 
[certify](../certify/README.md) step.

Thanks for hanging in there;  we are almost home.

