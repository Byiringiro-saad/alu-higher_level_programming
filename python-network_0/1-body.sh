#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response only if the status code is 200
curl -s -w "%{http_code}" -o response_body.txt "$1" && [ "$(tail -n 1 response_body.txt | awk '{print $1}')" -eq 200 ] && cat response_body.txt
