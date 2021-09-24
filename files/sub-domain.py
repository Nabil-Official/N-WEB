import requests
import os,sys,time
os.system('clear')
# coding : utf-8
logo = """ \033[1;94m
    _   __    _       ____________
   / | / /   | |     / / ____/ __ )
  /  |/ /____| | /| / / __/ / __  |
 / /|  /_____/ |/ |/ / /___/ /_/ /
/_/ |_/      |__/|__/_____/_____/

Created By : \033[1;96mNabil-Rahman |\033[1;0m [V 1.2.2]

\033[1;32m------------------------------------------
\33[93m AUTHOR  : Team Dark T-D
\33[93m GITHUB  : github.com/Nabil-OfficiaL
\33[93m FB      : nabil.404
\033[1;32m------------------------------------------
"""
print (logo)
print 
# the domain to scan for subdomains
domain = str(input('Enter Url : '))
# read all subdomains
print 
file = open("subdomains.txt")
# read all content
content = file.read()
# split by new lines
subdomains = content.splitlines()
# a list of discovered subdomains
discovered_subdomains = []
for subdomain in subdomains:
    # construct the url
    url = f"http://{subdomain}.{domain}"
    try:
        # if this raises an ERROR, that means the subdomain does not exist
        requests.get(url)
    except requests.ConnectionError:
        # if the subdomain does not exist, just pass, print nothing
        pass
    else:
        print 
        print("\033[1;31m[+] \033[1;32mFOUND : \033[1;33m", url)
        # append the discovered subdomain to our list
        discovered_subdomains.append(url)

# save the discovered subdomains into a file
with open("discovered_subdomains.txt", "w") as f:
    for subdomain in discovered_subdomains:
        print 
        print(subdomain, file=f)

