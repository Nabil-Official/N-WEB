#!/usr/bin/bash

main() {
clear

echo -en "
\033[34m
    _   __    _       ____________
   / | / /   | |     / / ____/ __ )
  /  |/ /____| | /| / / __/ / __  |
 / /|  /_____/ |/ |/ / /___/ /_/ /
/_/ |_/      |__/|__/_____/_____/

Created By : \033[96mNabil-Rahman |\033[0m [V 1.1.1]

\033[32m------------------------------------------
\033[93m AUTHOR  : Cyber_Sixteen
\033[93m GITHUB  : github.com/Nabil-Official
\033[93m FB      : nabil.404
\033[32m------------------------------------------ "
echo -e "\e[32m"

echo 
echo -e "\e[31m[+]\e[32m STARTING SERVER..."
sleep 2
php -S 127.0.0.1:5555 > /dev/null 2>&1 &
echo -e "\e[31m[+]\e[32m SERVER HOSTED SUCCESFULLY : 127.0.0.1:5555"
sleep 1
xdg-open http://127.0.0.1:5555 
echo 
read -p "PRESS ENTER TO GO BACK MENU" user 
if [ user = "" ]
then
python2 n-web.py 
fi
}
main

