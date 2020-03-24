#!/bin/bash
cookie="$HTTP_COOKIE"
if [ "$cookie" = "" ]; then
  cookie="mcc=$RANDOM-$RANDOM-$RANDOM"
  echo > "/tmp/$cookie"
  echo "set-cookie: $cookie"
else
  anfragen=$(cat "/tmp/$cookie")
fi

