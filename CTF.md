

We are given a site url, when opened it gives us a site ValenFind, letting us log in and we see diferent users.

One user named cupid has a description not like anyother speaking of data base. then we open our burp to intercept the proxy in the site.

as we forward the cupid site and check the history, we find a response. scrolling down we find a //vunrability stating that layout 'parameter' allows LFI



Then we change the layout of the profile cupid then turning on intercept again then putting it to the repeater

using the xyz = /../../etc/passwd  which is the Local File Inclusion

we use this LFI to change the layout=theme_modern.html to layout=/../../etc/passwd

this will give us an error ther is not fiel ....../../../etc/passwd and before that we are given a directory.

/opt/Valenfind/templates/components/app.py

as we take down each folder from the right we are directed to a file in 

/opt/Valenfind/app.py
