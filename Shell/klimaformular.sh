#!/bin/bash   
source klimacookie.sh
echo "Content-type: text/html"
echo ''
echo '<!doctype html>'
echo '<html>'

echo '  <head>'
echo '    <meta charset='utf-8'>'
echo '    <title>Teampage</title>'
echo '    <link href="../styles.css" rel="stylesheet" type="text/css">'
echo '  </head>'

echo '  <body>'
echo '    <div id="navigation">'
echo '      <div id="banner">'
echo '        <h1>Team 10 Lion</h1>'
echo '        <hr>'
echo '      </div>'
echo '      <p id="menu">'
echo '        <a href="http://informatik.hs-bremerhaven.de/step2019team10/index.html">Home</a>'
echo '        <a href="http://informatik.hs-bremerhaven.de/step2019team10/ueber_uns.html">Über Uns</a>'
echo '        <a href="http://informatik.hs-bremerhaven.de/docker11259/cgi-bin/klimaformular.sh">Unser Projekt</a>'
echo '        <a href="http://informatik.hs-bremerhaven.de/step2019team10/team10poster.pdf">Teamposter</a>'
echo '        <a class="login" href="http://informatik.hs-bremerhaven.de/step2019team10/login.html">Login</a>'
echo '      </p>'
echo '    </div>'
echo '    <div id="inhalt">'
echo '    <div id="history" style="float:right;">'
echo '      <button class="button">Letzte Suchanfragen</button>'
echo '      <div class="history-content">'
echo "        $anfragen"
echo "      </div>"
echo '    </div>'
echo '    <div class="formular">'
echo '      <h1>Abruf von Klimadaten</h1> <br>'
echo '      <form>'
echo '        <select class="button" name="ID"> action="">'
echo '          <option>Stadt</option>'

cat stationen.txt | while read ID Startdatum Enddatum Stadt #erstellt ein Drop-down mit allen Staedtenamen 
do
  echo "        <option value="$ID"."$Stadt">$Stadt</option>"
done

echo '        </select>'
echo '        <select class="button" name="zeitraum"> action="">'    
echo '          <option>Zeitraum</option>'
echo '          <option value=7>7 Tage</option>'
echo '          <option value=30>30 Tage</option>'
echo '          <option value=90>90 Tage</option>'
echo '          <option value=365>365 Tage</option>'
echo '        </select>'
echo '        <select class="button" name="art"> action="">'
echo '          <option>Parameter</option>'
echo '          <option value=9>Sonnenstunden</option>'
echo '          <option value=14>Temperatur</option>'
echo '          <option value=7>Niederschlag</option>' 
echo '          <option value=5>Windgeschwindigkeit</option>' 
echo '        </select>'
echo '        <button class="button" type="submit">Formular abschicken</button>'
echo '      </form>'
echo '      <br>'

QUERY=$QUERY_STRING
QUERY=$(echo "$QUERY"|sed 's/+/ /g; s/%/\\x/g')
QUERY=$(echo -e "$QUERY")
QUERY=$(echo "$QUERY" | sed 's/\&/ /g'| tr "=" " " | tr "." " " )  

./create.sh "$QUERY"

if [ "$QUERY" != "" ]; then
  read A ID location B Zeitraum C Art <<<"$QUERY"
  echo "<img src='https://informatik.hs-bremerhaven.de/docker11259/diagramme/$ID-$Art-$Zeitraum.svg' alt='Abruf nicht möglich'>" 
  echo "<a href='https://informatik.hs-bremerhaven.de/docker11259/diagramme/$ID-$Art-$Zeitraum.svg'>$location</a>" >> /tmp/$cookie 
fi 

echo '      <h3>Quelle: Deutscher Wetterdienst</h3>'
echo '    </div>'
echo '    <div class="hinweis">'
echo '      <p>Hinweis: Die Rohdaten werden vom Deutschen Wetterdienst zur Verfügung gestellt und täglich etwa um 10:30 Uhr aktualisiert. Dadurch kann es zwischen 09:30 Uhr und 10:30 Uhr zu Fehlern beim Abruf der Daten kommen. Darüber hinaus erfassen nicht alle Wetterstationen alle die hier abrufbaren Parameter. Unsere Anwendung ist so konzipiert, dass sie diese Fehlerwerte (in den Daten des DWD angegeben mit -999) nicht ausgibt, daher ist es möglich, dass Standorte für einige Parameter keine Ausgabe produzieren. Dies betrifft insbesondere die Werte für Windgeschwindigkeit und Sonnenstunden.<br> It´s not a bug it´s a feature!</p>'
echo '      <hr>'
echo '      <p> Pro Datenabruf verbaucht unsere Anwendung ca. 0,053g CO2, inkl. der Darstellung durch die Webseite. Der einmal täglich stattfindende Abruf der Stationen verbraucht zusätzlich ca. 0,05g CO2 (1GB=13kWh; 1,2 Pfund CO2 je kWh) <br> Quellen: United States Environmental Protection Agency; Lawrence Berkeley National Laborator </p>'
echo '    </div>'
echo '    </div>'
echo '    <div id="footer">'
echo '      <p> Copyright © Team 10 Lion </p>'
echo '    </div>'
echo '  </body>'
echo '</html>'
