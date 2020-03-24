#!/bin/bash
source cookie.sh
echo 'content-type: text/plain'
echo ""
if [ "$User" == "admin@admin" ]
then
echo 'Cookies entfernt'
rm -f /tmp/mcc*
rm -f /tmp/mmc*
fi
