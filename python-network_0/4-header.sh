#!/bin/bash
# Sends a GET request with a custom header and displays the response body
curl -s -v -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
