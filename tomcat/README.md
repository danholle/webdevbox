## ***webdevbox/tomcat:***
# **Setting Up Apache Tomcat Web Server**

--------

In this step, we'll set up the Apache Tomcat web server.  Tomcat
is more or less the default platform for doing Java servlet or JSP
based web application development.  Alternatives include Jetty.

By default, Tomcat listens on port 8080.  Good choice;  lots of 
servers do the same.  Which presents a problem:  the next thing
we install might clash with Tomcat.  So I give you a way to 
have Tomcat listen at a different port.

I also let you set up a Tomcat user to use the Tomcat manager
application running on Tomcat.

## **What do I need to do?**

One command.  For example, you might say

    tomcat/install 8081 admin s3cr3t

You can probably guess what this command does, but to remove
the mystery:
 -  It installs a stable version of Tomcat 8.0.  
 -  Tomcat will listen on port 8081, rather than 8080, to 
    avoid the problems mentioned above.
 -  Open up port 8081 on the webdevbox's firewall so that
    you can get to Tomcat from other machines on your
    home network (but not from the public internet just yet)
 -  To get to the Tomcat Manager on this box, you'll use
    the username admin and the password s3cr3t.
 -  Tomcat is started;  and 
 -  It's set to restart whenever your webdevbox does.


## **Did that work?  (Is Tomcat running?)**

Well, probably.  Just say:  

    systemctl status tomcat

and it should say "active" plus a lot of gibberish that I don't understand, and something inside me feels you shouldn't understand it either.  You might need to type q to get out of this command.


## **Tomcat is running, but does it actually work?**

Well, probably.  If you can fire up a browser on your webdevbox, do so and go to

    http://localhost:8081

and you should get the Tomcat welcome page.  Or, if your 
webdevbox is headless and you have another machine, with a browser, 
on your local network... and your webdevbox has a
hostname of (say) george... then you ought to be able to go to 

    http://george:8081

from that other machine and see the same page.  You could try to log on to 
Tomcat Manager:

    http://localhost:8081/manager/html

...at which point it will ask you to log on.  Provide the username and password
you provided at installation time, and you should be rewarded with a page
showing what's going on with your shiny new Tomcat server.


## **What do I do next?**

Next we are going to get a certificate and wire things up
so you can access both Tomcat and static HTML content on your
webdevbox from the public internet, through a secure (encrypted, 
certified) connection.

It's all covered in the [certify](../certify/README.md) step.

