#!/bin/bash
cookie="$HTTP_COOKIE"
if [ "$cookie" = "" ]; then
  cookie="mmc=$RANDOM-$RANDOM-$RANDOM"
  echo > "/tmp/$cookie"
  echo "set-cookie: $cookie"
else
  User=$(cat "/tmp/$cookie")
fi

