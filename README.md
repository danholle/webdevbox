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
    web applications, and make them available on the 
    public internet
 *  Web content might be static HTML, or Java servlet / JSP,
    or node.js;  they all appear as one site from the Web
 *  COMING SOON:  I'm planning to add a CI/CD setup
    using Jenkins (also accessible remotely)
 *  Since the above can be challenging to make secure on
    the public internet, the above is front-ended with a
    (reverse) proxy which only exposes what I want to
    expose, without limiting the server-local dev environment
 *  All remote (public internet) access is certified
    and encrypted (no changes required for your web content)

--------

Let's get started.  We will
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

1.  [base](base/README.md) installs some common prerequisites.
    If you click on the link, it will take you to the TL;DR
    description of this step.
2.  [dnsgodaddy](dnsgodaddy/README.md) sets up the web proxy
    if you are coming in via a GoDaddy domain.  In the 
    process we set up a (free) certificate to certify your
    site as legit.  Or, if you don't like GoDaddy,
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


