#!/bin/bash 

QUERY="$1"

mkdir /tmp/klima
rm /tmp/klima/*
cd /tmp/klima/ 

read A ID location B Zeitraum C Art <<<"$QUERY"

curl -O https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/recent/tageswerte_KL_"$ID"_akt.zip; 
unzip tageswerte_KL_"$ID"_akt.zip >/dev/null;

cut -d ";" -f 2,$Art produkt_klima_tag_*_*"$ID".txt | tr ";" " " | tail -$Zeitraum  > $ID.$Art.dat; 

cat $ID.$Art.dat | while read Datum Wert
do
  if [ $Wert != "-999" ]
  then
    echo "$Datum $Wert" >> $ID.dat
  fi
done

if [ "$Art" == "7" ]; then  

  echo "set terminal svg size 1200,600

  set out '/tmp/klima/$ID-$Art-$Zeitraum.svg'
  set rmargin 8
  set title '$location'
  set xlabel 'Datum'
  set ylabel 'Niederschlag (mm)'
  set xdata time
  set timefmt '%Y%m%d'
  set format x '%d.%m.%Y'

  plot '$ID.dat' using 1:2 with lines" > $ID.$Art.gp

  gnuplot $ID.$Art.gp

  mv /tmp/klima/*.svg /var/www/html/docker11259/diagramme

elif [ "$Art" == "14" ]; then  

  echo "set terminal svg size 1200,600

  set out '/tmp/klima/$ID-$Art-$Zeitraum.svg'
  set rmargin 8
  set title '$location'
  set xlabel 'Datum'
  set ylabel 'Temperatur (°C)'
  set xdata time
  set timefmt '%Y%m%d'
  set format x '%d.%m.%Y'

  plot '$ID.dat' using 1:2 with lines" > $ID.$Art.gp

  gnuplot $ID.$Art.gp

  mv /tmp/klima/*.svg /var/www/html/docker11259/diagramme

elif [ "$Art" == "9" ]; then  

  echo "set terminal svg size 1200,600

  set out '/tmp/klima/$ID-$Art-$Zeitraum.svg'
  set title '$location'
  set xlabel 'Datum'
  set ylabel 'Sonnenstunden (h)'
  set xdata time
  set timefmt '%Y%m%d'
  set format x '%d.%m.%Y'

  plot '$ID.dat' using 1:2 with lines" > $ID.$Art.gp

  gnuplot $ID.$Art.gp

  mv /tmp/klima/*.svg /var/www/html/docker11259/diagramme

elif [ "$Art" == "5" ]; then  

  echo "set terminal svg size 1200,600

  set out '/tmp/klima/$ID-$Art-$Zeitraum.svg'
  set rmargin 8
  set title '$location'
  set xlabel 'Datum'
  set ylabel 'Windgeschwindigkeit (m/s)'
  set xdata time
  set timefmt '%Y%m%d'
  set format x '%d.%m.%Y'

  plot '$ID.dat' using 1:2 with lines" > $ID.$Art.gp

  gnuplot $ID.$Art.gp

  mv /tmp/klima/*.svg /var/www/html/docker11259/diagramme
fi

