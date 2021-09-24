#GOT FROM DARK-HUNTER-141
clear
echo -en "
\033[34m
    _   __    _       ____________ 
   / | / /   | |     / / ____/ __ )
  /  |/ /____| | /| / / __/ / __  |
 / /|  /_____/ |/ |/ / /___/ /_/ / 
/_/ |_/      |__/|__/_____/_____/  

Created By : \033[96mNabil-Rahman |\033[0m [V 1.2.2]

\033[32m------------------------------------------
\033[93m AUTHOR  : Team DarkWeb T-D
\033[93m GITHUB  : github.com/Nabil-Official
\033[93m FB      : nabil.404
\033[32m------------------------------------------

\033[35m[1]\033[31m >> \033[92mDORK SEARCHER
\033[35m[2]\033[31m >> \033[92mRANDOM DORKS 
\033[35m[3]\033[31m >> \033[92mDORKING 

 \033[96m>> Enter Your Optionn : "

read menu
dorking() {
  echo -e "use ctrl-c to skip to the next process  ${N} please wait make sure the connection is fast and stable .." | tr "+" " ";rm -rf .result_dork .not
    COUNT="$hitung"
         echo -e "${G}Result from bing page $COUNT${N}"
         curl -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" --max-time $time_out -sL "http://www.bing.com/search?q=$dork&qs=n&pq=$dork&sc=8-5&sp=-1&sk=&first=$COUNT&FORM=PORE" | grep -Po '_blank" href="[^"]*' | sort -u | uniq -i | cut -d '"' -f3 | sed '/facebook/d' | sed '/google/d' | sed '/twitter/d' | sed '/microsoft/d' | sed '/youtube/d' | sed '/&amp/d' | sed "/amp;/d" >> .result_dork
         cat .result_dork 2>/dev/null | while read ress; do
         echo -e "Result => ${O}$ress${N}";done
         echo -e "${G}Result from google page $COUNT${N}"
         dork2=$(echo "$dork" | sed "s,inurl:,+,g")
         curl -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" --max-time $time_out -s "https://www.google.com/search?q=${dork2}=&start=${COUNT}" -L | grep -Po '<a href="\K.*?(?=".*)' | egrep -o "(http(s)?://){1}[^'\"]+" | sed '/facebook/d' | sed '/google/d' | sed '/twitter/d' | sed '/instagram/d' | sed '/youtube/d' | sed '/google/d' | sed "/amp;/d" >> .result_dork
         cat .result_dork 2>/dev/null | while read ress; do
         echo -e "Result => ${O}$ress${N}";done
         echo -e "${G}Result from ask.com page $COUNT${N}"
         curl -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" --max-time $time_out "uk.ask.com/web?q=$dork&page=${COUNT}" -sL | grep -Po "blank\" href='[^']*'" | cut -d "'" -f2 | sed "/amp;/d" >> .result_dork
         cat .result_dork 2>/dev/null | while read ress; do
         echo -e "Result => ${O}$ress${N}";done
         echo -e "${G}Result from yahoo page $COUNT${N}"
         curl -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" --max-time $time_out "https://search.yahoo.com/search?ei=UTF-8&gprid=&fr2=sb-top&p=$dork&b=${COUNT}" -sL | grep -Po 'lh-24\" href="[^"]*"' | cut -d '"' -f3 | sed "/amp;/d" >> .result_dork
         cat .result_dork 2>/dev/null | while read ress; do
         echo -e "Result => ${O}$ress${N}";done
}

if [ "$menu" = "3" ]
then
echo -ne "${G}Dork: ${O}"
read dork
echo -ne "${G}Page: ${O}"
read page
for hitung in $(seq $page)
do
  dorking
done
fi
if [ "$menu" = "1" ]
then
echo -ne "${G}POC : ${O}"
read poc
pocna=$(echo "$poc" | sed "s| |+|g")
poci=$(echo "$poc" | sed "s| |_|g")
trap break INT
echo -e "\nGETTING FROM DATABASE"
echo "+++++++++++++[ $(date) ]++++++++++++++++" >> Dork~$poci.txt
for hitung in $(seq 1 30)
do
   link=$(curl -sL "https://cxsecurity.com/search/wlb/DESC/AND/2020.10.14.1999.1.1/$hitung/30/$pocna/" | grep -Po "https://cxsecurity.com/issue/WLB-[^\"]*")
   if [ -z "$link" ]
   then
      echo -e "Check the connection or something went wrong"
   fi
   for url in $(echo "$link")
   do
     if [ -z "$url" ]
     then
         echo -e "Check the connection or something went wrong"
     fi
     url=$(echo "$url" | sed "s/issue/ascii/g")
     result0=$(curl -sL "$url")
     result1=$(echo "$result0" | grep -Po "<CENTER><h4><B>[^<]*|Dork:</abbr></b>[^<]*" | sed "s|<CENTER><h4><B>|Poc : |g" | sed "s|</abbr></b>||g" | sed "s|&quot;|'|g")
     result2=$(echo "$result0" | sed '/="/d' | grep -Po "http[s]://[^\n]*|http://[^\n]*|www.[^\n]*|: [^ ]*" | sed "/</d" | sed "/>/d" | sed "/'/d" | grep "/.[[:alnum:]*/]*" | tr -d ":" | sed 's|&#39;&#39;|"|g' | sed "s|&quot;|'|g" | sed "s|&quot;||g" | sed "s|&nbsp;| |g" | sed "s|^|Demo site: |g")
     result3=$(echo "$result0" | sed '/="/d' | grep -Po "http[s]://[^\n]*|http://[^\n]*|www.[^\n]*" | sed "/</d" | sed "/>/d" | sed "/'/d" | sed 's|&#39;&#39;|"|g' | sed "s|&quot;|'|g" | sed "s|&quot;||g" | sed "s|&nbsp;| |g" | sed "s|^|Demo site: |g" | echo "$result2" | sed "s|https//|https://|g" | sed "s|http//|http://|g" | sed "s|&[^;]*;||g" | grep "." | sort -u)
     result4=$(echo "$result0" | tr ">" "\n" | sed "/</d")
     echo -e "${P}$result4\n$url\n${BL}$result1"
     echo -e "${N}${P}$result3${N}\n"
     echo -e "$result4\n$result1\n$result3" | sort -u | uniq -i >> Dork~$poci.txt
   done 
done
trap - INT
trap break INT
echo -e "${P}Get dork via Article & Blogsite"
echo -e "${N}[${R}?${N}] page: "
read page
if [[ "$page" = "" ]];then
    echo -e "${R}input kosong"
else
for hitung in $(seq 1 $page)
do
   echo -e "${G}get dork from google"
   dork=$(echo "deface+$pocna")
   dorking
done
trap - INT
for site in $(cat .result_dork | sort -u)
do
  result2=$(curl -sL --max-time 20 "$site" | grep -Po "inurl:[^ ]*|inurl:[^<]*" | sed "s|&quot;|'|g" | sed 's|&#39;&#39;|"|g' | cut -d "<" -f1)
 if [ -z "$result2" ]
  then
    tidak="ada"
 else
     echo -e "${BL}$result2"
  fi
  echo "$result2" >> Dork
done
fi
echo -e "\n${N}${P}Stored on Dork~$poci.txt"
fi
if [ "$menu" = "2" ]
then
  echo -e "\n${N}${P}Fetch dork from database"
  for set in $(seq 22)
  do
     ngecurl=$(curl --max-time 60 -sL "https://cxsecurity.com/dorks/$set/" | grep -Po '(Dork:<=?)(.*?)(?=<)|" title="[^"]*|label label-default">[^<]*<' | sed "s|</B>&nbsp;&quot;| intext:|g" | sed "s|&quot;||g" | sed "s|</B>&nbsp;| |g" | sed 's| title="|Poc: |g' | tr '"' "\n" | sed "s|label label-default||g" | sed "s|><||" | tr -d "<" | sed "s|>|Date: |" | grep ":" | sed "s\Poc\%Poc \g" | tr "%" "\n" | sed "s|amp;||g" | sed "s|&#039;|'|g")
     if [ -z "$ngecurl" ]
     then
        echo -e "${R}Check the connection or something went wrong"
     fi
     echo -e "\033[0;96m$ngecurl"
     echo "$ngecurl" >> auto-gen.txt
     if [ "$set" = "20" ]
     then
        echo -en "${G}the process is complete want to add dork ?? y/n: ${O}"
        read pros
        if [ "$pros" = "y" ]
        then
           for set in $(seq 21 200)
           do
              ngecurl=$(curl --max-time 60 -sL "https://cxsecurity.com/dorks/$set/" | grep -Po '(Dork:<=?)(.*?)(?=<)|" title="[^"]*|label label-default">[^<]*<' | sed "s|</B>&nbsp;&quot;| intext:|g" | sed "s|&quot;||g" | sed "s|</B>&nbsp;| |g" | sed 's| title="|Poc: |g' | tr '"' "\n" | sed "s|label label-default||g" | sed "s|><||" | tr -d "<" | sed "s|>|Date: |" | grep ":" | sed "s\Poc\%Poc \g" | tr "%" "\n" | sed "s|amp;||g" | sed "s|&#039;||g")
              if [ -z "$ngecurl" ]
              then
                 echo -e "${R}Check the connection or something went wrong"
              fi
              echo -e "\033[0;96m$ngecurl"
              echo "$ngecurl" >> auto-gen.txt
           done
           echo -e "\n${N}${P}Stored on auto-gen.txt"
        else
           echo -e "\n${N}${P}Stored on auto-gen.txt"
           break
        fi
     fi
   done
   echo -e "\n${N}${P}Stored on auto-gen.txt"
fi
}
