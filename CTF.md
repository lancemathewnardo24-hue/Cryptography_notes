We are given a site url, when opened it gives us a site ValenFind, letting us log in and we see diferent users.

One user named cupid has a description not like anyother speaking of data base. then we open our burp to intercept the proxy in the site.

as we forward the cupid site and check the history, we find a response. scrolling down we find a //vunrability stating that layout 'parameter' allows LFI

Then we change the layout of the profile cupid then turning on intercept again

using the xyz = /../../etc/passwd  which is the Local File Inclusion
