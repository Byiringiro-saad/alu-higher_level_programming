#!/bin/bash
# Sends a GET request, follows redirects, and displays body if status is 200
curl -sL -o response.txt -w "%{http_code}" "$1" | grep -q "200" && cat response.txt
