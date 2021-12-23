#!/usr/bin/python 
import os 
from googlesearch import search 

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
os.system("clear")
print(logo)

query = str(input("\033[1;31m>> \033[1;32mEnter Dork To Scan : \033[1;36m"))
limit = int(input("\033[1;31m>> \033[1;32mHow Many Site You Want To Display : \033[1;36m"))
if query == "":
	exit()
if limit == "":
	exit()

print("")
count = 0 
for url in search(query,num=limit,start=0,stop=None,pause=2):
	print(f"\033[1;35m[+] \033[1;31m>> \033[1;32m{url}")
	if count == limit:
		exit()
	count = count + 1
