

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

after sending we see the master key of the ADMIN_API_KEY = "CUPID_MASTER_KEY_XOXO", we save this for later. then below we see the data base file. knowing that it exists here

we try to find the data base directory by scrolling down

we find /api/admin/export_db

then we try to acces it but below we see a command that **if auth_header == Authenticaiton_key**, so we already have the key from earlier "CUPID_MASTER_KEY_XOXO"

now to find the auth_header, which we see above this command. **X-Valentine-Token**

so what we will encode to the request will be 

GET /api/admin/export_db

X-Valentine-Token:CUPID_MASTER_KEY_XOXO

after sending we find our key

so we also find the 
