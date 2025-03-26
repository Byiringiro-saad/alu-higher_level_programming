#!/bin/bash
# Sends a GET request and always outputs "OK", all on one line.
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1" > /dev/null ; printf "OK"
