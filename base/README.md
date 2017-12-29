WARNING:  This is not quite ready to consume!  Published because I'm testing.

# ***webdevbox:***

# **Ubuntu Setup Scripts for a**
# **Web Application Development Server**

*Compilers, Tomcat, nginx, node.js, Jenkins, etc.*

--------

I used these scripts to set up a home server for doing web 
application development.  If they are useful to you in doing
something the same or similar, great.

There's nothing profound or innovative here.  It's just that 
it took a bit of hacking to get these parts to play nicely...
time that hopefully I can save for you.

--------

My objectives for this web development box:
 *  I wanted an environment where I could develop and test
    web applications, and make them available on the 
    public internet
 *  Web content might be static HTML, or Java servlet / JSP,
    or node.js
 *  I'm planning to add a Continuous Integration setup
    using Jenkins (also accessible remotely)
 *  Since the above can be challenging to make secure on
    the public internet, front-end this stuff with a
    (reverse) proxy which only exposes what I want to
    expose, without limiting the server-local environment
 *  All remote access is via https (encrypted)

--------

I'm assuming you are installing on an Ubuntu machine.  We will
get the scripts onto your machine by pulling them from git;
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

1.  [base](base/README.md) 

    





These scripts are for setting up an Ubuntu development server
for building web applications.   Components installed include
 *  *basebox:*  Compilers and stuff
 *  *tomcat:*  Tomcat servlet container, along with a Hello World servlet
 *  *nodejs:*  Sets up node.js and associated tools
 *  *nginx:*  Sets up nginx as a reverse proxy in front of static HTML, Tomcat, and node.js with SSL and all that stuff.

 
 

## Installing Tomcat

blah blah

   tomcat/install 8080

blah blah






