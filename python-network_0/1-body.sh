#!/bin/bash  
# Sends a GET request to the URL and displays the body if status is 200  
curl -s -o response.txt -w "%{http_code}" "$1" | grep -q "200" && cat response.txt
