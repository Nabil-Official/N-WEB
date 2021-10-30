# -*- coding: utf-8 -*-
#!/usr/bin/python2
# Author : Nabil-Rahman 
# Team : DarkWeb T-D

try:
  import os
  import sys
  import time
  import requests as nabil
  import bs4 
  import json 
  import urllib2 
except Exception as e:
  print ('[+] ERROR : '+str(e))

# COLOR VALUES 

blue= '\33[94m'
lightblue = '\033[94m'            
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'

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

def logop(z):
    for word in z + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)


## Menu
def intro():
    os.system('clear')
    logop(logo)
   # os.system('xdg-open https://facebook.com/groups/368007073698875')
    print
    print blue+"[\033[1;31m01\033[1;94m] \033[1;35m>>\033[1;32m Admin-Finder"
    print blue+"[\033[1;31m02\033[1;94m] \033[1;35m>>\033[1;32m Admin-Scanner"
    print blue+"[\033[1;31m03\033[1;94m] \033[1;35m>>\033[1;32m Dork-Generator"
    print blue+"[\033[1;31m04\033[1;94m] \033[1;35m>>\033[1;32m Advance-Dork-Finder"
    print blue+"[\033[1;31m05\033[1;94m] \033[1;35m>>\033[1;32m Extract-Links"
    print blue+"[\033[1;31m06\033[1;94m] \033[1;35m>>\033[1;32m No-Redirect"
    print blue+"[\033[1;31m07\033[1;94m] \033[1;35m>>\033[1;32m Hash-Crack \033[1;31m(Online-DataBase)"
    print blue+"[\033[1;31m08\033[1;94m] \033[1;35m>>\033[1;32m Hash-Crack \033[1;31m(Word-List)"
    print blue+"[\033[1;31m09\033[1;94m] \033[1;35m>>\033[1;32m Whois-Lookup"
    print blue+"[\033[1;31m10\033[1;94m] \033[1;35m>>\033[1;32m Subdomain-Finder"
    print blue+"[\033[1;31m11\033[1;94m] \033[1;35m>>\033[1;32m Tcp-Port-Scan"
    print blue+"[\033[1;31m12\033[1;94m] \033[1;35m>>\033[1;32m Geo-Ip-Lookup"
    print blue+"[\033[1;31m13\033[1;94m] \033[1;35m>>\033[1;32m Reserve-Analysts-Search"
    print blue+"[\033[1;31m14\033[1;94m] \033[1;35m>>\033[1;32m Csrf-Vernability-Checker"
    print blue+"[\033[1;31m15\033[1;94m] \033[1;35m>>\033[1;32m Dns-Lookup,Zone-Transfer,Reserve-Ip-Lookup,Http-Headers,Subnet-Lookup"
    print blue+"[\033[1;31m16\033[1;94m] \033[1;35m>>\033[1;32m WordPress-Username-Finder"
    print blue+"[\033[1;31m17\033[1;94m] \033[1;35m>>\033[1;32m WP Scan"
    print blue+"[\033[1;31m18\033[1;94m] \033[1;35m>>\033[1;32m Wp BruteForce"
    print blue+"[\033[1;31m19\033[1;94m] \033[1;35m>>\033[1;32m Sqli Scanner"
    print blue+"[\033[1;31m20\033[1;94m] \033[1;35m>>\033[1;32m Directory BruteForce"
    print blue+"[\033[1;31m21\033[1;94m] \033[1;35m>>\033[1;32m Help?"
    print blue+"[\033[1;31m22\033[1;94m] \033[1;35m>>\033[1;32m About"
    print blue+"[\033[1;31m00\033[1;94m] \033[1;35m>>\033[1;32m Exit"
    
    # choise inputb
    print
    user_choise = raw_input(red+">> "+blue+'Enter Your Choice : \033[1;32m')
   # choise condition
    if user_choise == "1":
       os.system('cd files && python3 xc.py')
    elif user_choise == "2":
         os.system('cd files && python2 admin-scanner.py')
    elif user_choise == "3":
         os.system('cd files && python2 dork-genaretor.py')
    elif user_choise == "4":
         os.system('cd files && bash dork.sh')
    elif user_choise == "5":
         os.system('cd files && python2 extract.py')
         
    elif user_choise == "6":
         os.system('cd files && bash no-re.sh')
    elif user_choise == "7":
         os.system('cd files && python2 hashcrack.py')
    elif user_choise == "8":
         os.system('cd files && python hashcrack-word.py')  
    elif user_choise == "9":
         os.system('cd files && python2 whois.py')
    elif user_choise == "10":
         os.system('cd files && python2 subdomain-api.py')
    elif user_choise == "11":
         os.system('cd files && python2 tcp-port-scan.py')
    elif user_choise == "12":
         os.system('cd files && python2 geo-ip.py')
    elif user_choise == "13":
         os.system('cd files && python2 analytich.py ')
    elif user_choise == "14":
         os.system('cd files && python2 csrf.py')
    elif user_choise == "15":
         os.system('cd files && python2 dns-lookup.py')
    elif user_choise == "16":
         os.system('cd files && python2 user.py')
    elif user_choise == "17":
         os.system('cd files && python3 wp-scan.py')
    elif user_choise == "18":
         os.system('cd files && python2 wordpress-brute.py')
    elif user_choise == "19":                  
         os.system('cd files && python2 sqli.py')
    elif user_choise == "20": 
         os.system('cd files && python3 dir-brute.py')
    elif user_choise == "21":
         os.system('xdg-open https://m.facebook.com/nabil.404')
         
    elif user_choise == "22":
         os.system('cd .. && python2 about.py')
         
    elif user_choise == "00":
         exit()
         print (yellow+'   << Thanks For Using >>')
    else:
       print
       
       print (yellow+'   << Thanks For Using >>')
      
def up_chker():
    os.system('clear')
    url = "https://pastebin.com/raw/kxUhLgKT"
    ver = "1.2.2"
    res = nabil.get(url)
    r = res.text
    ### Not Updated Funtion
    if r != ver:
       print (logo)
       
       print 
       print (red+'[!]''\033[1;35m WAIT CHECKING FOR UPDATES'+red+' [!]')
        
       time.sleep(0.7)
        
       print (red+'[+]''\033[1;35m UPDATE-STATUS : '+ red+'NOT UPDATED')
       os.system('xdg-open https://github.com/Nabil-Official')
       exit()
       
    else:
        print (logo)
       
        print 
        print (red+'[!]''\033[1;35m WAIT CHECKING FOR UPDATES'+red+' [!]')
        
        time.sleep(0.2)
        
        print (red+'[+]''\033[1;35m UPDATE-STATUS : '+ green+'OK ')
        time.sleep(2)
        os.system('clear')
#        time.sleep(0.1)
        intro()
up_chker()

