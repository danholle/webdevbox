WARNING:  This is not quite ready to consume!  Published because I'm testing.

<h1><b><i>webdevbox:</i><br/>Setup Scripts for a Web Application Development Server</b></h1>

*Compilers, Tomcat, nginx, node.js, Jenkins, etc.*

--------

I used these scripts to set up a home server for doing web 
application development.  If they are useful to you in doing
something the same or similar, great.

There's nothing profound or innovative here.  It's just that 
it took a bit of hacking to get these parts to play nicely...
time that hopefully I can save for you.
I've made it easy for you to grab the scripts, and help walk
you through the process so you can modify the steps to suit
your needs along the way.

This stuff assumes you have an Ubuntu server up and running,
with an internet connection and command-line access to the
box... either through Terminal or via SSH.

--------

At the end of this exercise, you will have
 *  An environment where you could develop and test
    web content, be it in the form of HTML5, Java 
    servlets / JSP, node.js apps, etc.
 *  A platform which can present such content securely
    on the public Internet, through a gateway server
    (reverse proxy) which acts as a secure gatekeeper
 *  Your public internet location is either a domain
    you own, or a dynamic DNS location you've set up.
    We'll set up DNS updating for your home network. 
 *  COMING SOON:  I'm planning to add a CI/CD setup
    using Jenkins (also accessible remotely)

--------

Let's get started.  To keep things simple, we will 
get my scripts onto your machine by pulling them from git;
we will view / modify them with vim.  Everything here can be 
done on an ssh connection, and each step will be described in
TL;DR detail so don't get stressed just yet.

To get started, type these two commands to grab git and vim (in
case you don't already have them), and pull down the scripts:

    sudo apt-get install vim git
    git clone https://github.com/danholle/webdevbox

Upon completing these commands, you will have a webdevbox 
directory in your home directory.  Let's get closer:
  
    cd webdevbox
    ls

You'll see this README and a set of directories, one for
each of the following steps, which I'm assuming you will
carry out in the following order:

1.  [base](base/README.md) installs compilers, build tools,
    our gatekeeper/proxy (nginx), and some common prerequisites.
    When this is done, you will be able to hit a static "hello 
    world" HTML5 page from the public internet.  (If you click 
    the *base* link, it will take you to the TL;DR
    description of this step.)
2.  [dnsgodaddy](dnsgodaddy/README.md) is used to connect your
    webdevbox to a GoDaddy domain you own.  DNS updating will
    be set up to keep this domain pointed at your webdevbox.
    Once this is done, you'll be able to get at that same
    "Hello World" page via your domain from anywhere.
3.  [dnsselfsigned](dnsselfsigned/README.md) is an alternative
    to the above if you want to set up forwarding using No-IP
    and a self-signed certificate.  Your site will still be 
    secure and encrypted, but users may get some
    scary messages upon their first visit.
4.  [tomcat](tomcat/README.md) installs the Tomcat web server
    (servlet container) as a service which will start 
    whenever your machine restarts.

That should do it for now.  Good luck... and may the Force
be with you!


