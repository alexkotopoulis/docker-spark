#!/bin/bash
set -x

FILE=/app/init.sh
if test -f "$FILE"; then
    . $FILE
fi

sh /submit.sh
