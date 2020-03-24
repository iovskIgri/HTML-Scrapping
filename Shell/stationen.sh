#!/bin/bash

curl http://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/recent/KL_Tageswerte_Beschreibung_Stationen.txt | dos2unix > stationen.txt 
iconv -f ISO-8859-15 -t utf-8 stationen.txt > stationen2.txt 
rm stationen.txt
sed 's/ \+ / /g' stationen2.txt > stationen.txt
rm stationen2.txt
cut -d " " -f 1,2,3,7,8,9,10 stationen.txt > stationen2.txt
sort -k3 -n -k1 stationen2.txt > stationen.txt #Sortierung nach Datum nicht mehr relevant
rm stationen2.txt

cat stationen.txt |  while read ID Startdatum Enddatum Stationsname Bundesland
do
  if [ $Enddatum == $(date -d "1 day ago" '+%Y%m%d') ]
  then
   echo " $ID $Startdatum $Enddatum $Stationsname $Bundesland " >> stationenfinal.txt 
   fi
done

rm stationen.txt

sort -k4 stationenfinal.txt > stationen.txt

scp stationen.txt mydocker:/usr/lib/cgi-bin/
ssh mydocker chmod o+w /usr/lib/cgi-bin/stationen.txt

rm stationenfinal.txt
rm stationen.txt
