<p style="font-size: large; font-weight: bold; font-style: italic">
  webdevbox/certify:
</p>
<p style="font-size: x-large; font-weight: bold">
  Creating Free SSL Certificates For Your Site
</p>

--------

The fine folks at the Electronic Frontier Foundation, through certbot,
have created a mechanism by which you can certify your webdevbox for
free, and in so doing protects your users with encrypted connections
to your server.  The scripts here will hopefully make it more or less
pushbutton to leverage their handiwork.

You have no idea how close you are to achieving greatness.


<h2>What do I need to do?</h2>

Let's say your domain/URL is blah.com.  Your next step would be to say

    certify/install blah.com

and sit back while it does all the heavy lifting for you.  It will
 -  Install certbot
 -  It will run a challenge to make sure you own that domain, by putting a 
    file out in /var/www/html which it will access from an external box
 -  Assuming that goes okay, you will get a signed certificate and an nginx
    config that allows you to test access HTML (nginx) or a servlet (Tomcat).


<h3>I did my bit.  Did it work?</h3>

Well, probably.  You can check it easy enough:  on any browser on the planet, 
go to 

    http://blah.com

and it should come back with our Hello World page.  By the way. look close at
your browser:  the URL should now be https://blah.com, which means that the 
HTTP request was quietly upgraded to an encrypted HTTPS connection for you.

Now, assuming you have Tomcat up and running, try

    http://blah.com/docs

and you should see Tomcat's documentation home page.  Note that, again, the
session was quietly upgraded to HTTPS.


<h2>What do I do next?</h2>

Well, you need to tailor up an nginx configuration file that matches your 
needs.  This may well take you out of your comfort zone and into somebody
else's TL;DR documentation  :)

Have a look at your current nginx configuration which you can find at

    /etc/nginx/sites-available/default

and you might get a good feel for what this configuration file is 
specifying. 
 
