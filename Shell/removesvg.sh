#!/bin/bash
source cookie.sh
echo 'content-type: text/plain'
echo ""
if [ "$User" == "admin@admin" ]
then
echo 'svg Dateien entfernt'
rm -f /var/www/html/docker11259/diagramme/*
fi

