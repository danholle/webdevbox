## ***webdevbox/metadb:***
# **Setting Up a Metadata Database**

--------

Some of the tools we install need a database.  So here we are.

We'll use MariaDB, which is more or less the non-Oracle version of
MySQL.  We just need something that works, not something that is 
scalable or mega-efficient... and something that tools like Drupal
can use without missing a beat.


## **What do I need to do?**

For starters, let's install MariaDB, which is simple enough:

    metadb/install


## **Did that work?  (Is MariaDB running?)**

Well, probably.  You can check in a few ways;  for example

    ps -A | grep nginx

will probably show you some number of nginx threads running.  I think it's one master and one slave for each core nginx found on your webdevbox.  Alternatively, you could say

    sudo systemctl status nginx

and it should say "active" plus a lot of gibberish that I don't understand, and something inside me feels you shouldn't understand it either.  You might need to type q to get out of this command.


## **MariaDB is running, but does it actually work?**

Well, probably.  If you can fire up a browser on your webdevbox, do so and go to

    http://localhost

and you should get a Hello World page which claims it was installed by gateway/install.  Or, if your 
webdevbox is headless and you have another machine on your local network, and your webdevbox has a
hostname of (say) george, then you ought to be able to go to 

    http://george

from that other machine and see the same page.


## **What do I do next?**

Next we are going to push the PHP button:  installing the PHP FastCGI Process Manager.
TODO stay tuned: [php](../php/README.md).

