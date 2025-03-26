#!/bin/bash
# Sends a GET request to a URL with a custom header and displays the body, checking for errors.
response=$(curl -s -H "X-HolbertonSchool-User-Id: 98" "$1")
echo "$response"