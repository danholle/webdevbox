## ***webdevbox/commonbase:***
# **Setting Up a Common Base of Compilers, Tools, and Libraries**

--------

This is where we establish a common base of software tools 
that are used by one or more of the install steps which follow.  In many cases, these
things may already be installed.  But if they're not, they're the sort of thing where
you'd probably regret not having.

The process starts by doing an update/upgrade to make sure that you're dealing with
current, complete, and stable software.  Then we set about installing
 *  Tools that you may need during the rest of the install process (vim, git, curl, wget)
 *  SSH to give you remote command access to this box (openssh-server)
 *  Firewall which I'll configure in subsequent install steps (ufw)
 *  Compilers and build tools for c, c++, Java 1.8, Python 3
     *  build-essential, openjdk-8-jdk, python3-dev
     *  pip3, maven, Python libraries 

<h2>What do I need to do?</h2>

Your job is easy.  Assuming you've cd'd to webdevbox, just say

    commonbase/install

and kick back.  No input, no actions, just wait.  And you won't wait long.


<h2>I'm done.  Did it work?</h2>

Well, normally I'd give you a few things you can do to check it out.  In this case,
that seems a bit heavy-handed.  Let's pretend it just worked.


<h2>What do I do next?</h2>

Next we will set up nginx as a secure [gateway](../gateway/README.md) 
between the public internet and our web server(s) and content.

