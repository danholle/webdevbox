WARNING:  This is not quite ready to consume!  Published because I'm testing.

<h1><b><i>webdevbox/base:</i><br/>Base Setup Scripts for a Web Application Development Server</b></h1>

*Compilers, Build Tools, Proxy, Firewall, Port Forwarding...*

--------

Have a look at the base install script:
  
    vim base/install

If you're not familiar with the vim editor, here is a minimal 
cheat sheet that should be sufficient to get you going.  
 *  vim should work fine over an SSH connection.
 *  Use up, down, left, right arrows to move around.
 *  If you want to add or delete characters, press "i" to go into 
    insert mode.  It will say -- INSERT -- at the bottom.
 *  To exit without changing anything, type <esc> :q! <enter>
 *  To save and exit, type <esc> :wq <enter>

Where were we?  Ah, yes, base/install.  Have a look;  there
are plenty of comments.  If some of the stuff is wrong for
you, change it using the above instructions.  Otherwise,
just run it:

    base/install

We've installed nginx, the web server / (reverse) proxy that 
will securely direct traffic to your back end web servers 
such as Tomcat, node.js, or Jenkins.  To test that nginx 
installed correctly, hit your webdevbox from a browser.  
For example, if you've got a browser running directly on
the webdevbox, go to

    http://localhost

or, if your webdevbox is headless, and its hostname is 
george, you should be able to go to 

    http://george

from another machine on your local network.  In response,
you should get an nginx page congratulating you for being 
smart enough to install nginx.


<h2>Port Forwarding on your Local Network</h2>

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
               Ports:  Map To:
         TCP   22-22   22-22      This forwards your SSH traffic
         TCP   80-80   80-80      This forwards your HTTP traffic
         TCP   443-443 443-443    This forwards your HTTPS traffic
     Click apply.
 5.  Click Return to Port Forwarding.
 6.  Under "Select game or application", choose "httphttps".  Under 
     "Select Device", select george.  Click Add.  Click Apply.

<h2>Test your Public Access</h2>

On any machine with a browswer on your home network, go to

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
same "Welcome to nginx" page you saw minutes ago.

Now you're almost ready to set up your 
[domain name and DNS](../dnsgodaddy/README.md)
so you can get to your box using your domain name...




