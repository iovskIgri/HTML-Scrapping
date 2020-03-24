#!/bin/bash

source cookie.sh 

if [ "$User" == "admin@admin" ];
then
  echo "content-type: text/html"
  echo ""
  echo '<!doctype html>'
  echo '<html>'

  echo  '<head>'
  echo  '<meta charset='utf-8'>'
  echo  '<title>Admin Bereich</title>'
  echo  '</head>'
  echo  '<body>'
  echo  '<h1> Login erfolgreich</h>'
  echo  "<h2>Hallo $User </h2>"
  echo  ' <ul id="menu">'
  echo  ' <li> <a class="link" href="removesvg.sh"> SVG Dateien löschen</a> </li>'
  echo  ' <li> <a class="link" href="removecookie.sh"> Cookies löschen</a> </li>'
  echo  '</ul>'

  echo  '<form action="/docker11259/cgi-bin/logout.sh">
         <button  type="submit">Logout</button>'
  echo  '</body>'
  echo  '</html>'
else
  echo 'content-type: text/plain'
  echo "Status: 303"
  echo "Location: https://informatik.hs-bremerhaven.de/step2019team10/login.html"
  echo  ''
fi 
