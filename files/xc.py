# -*- coding: utf-8 -*-
import time
import os
import concurrent.futures
import requests
try:
        from colorama import *
except ImportError:
        os.system("clear")
        os.system("pip install colorama")
import time
### LOGO
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
print (logo)
print(Style.BRIGHT)
site = input('\033[1;31m>>\033[1;32m Enter Your Url : \033[1;36m')
print()
try:
        opn = open("paths.txt","r").readlines()
except:
        print("[+] File Not Found")
        quit()
def scan(x):
        try:
                st = x.strip()
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                r = requests.get(site+st,timeout=10,headers=headers)
                code = int(r.status_code)
                if code < 400:
                        print(Fore.GREEN+" [✔] FOUND : "+site+st)
                else:
                        print(Fore.RED+" [❌] NOT FOUND : "+site+st)
        except Exception as e:
                b = 2
try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(scan,opn)
except:
        print(Fore.RED+" [!] Check Your Internet ! ")

