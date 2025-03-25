#!/bin/bash
# This script sends a GET request to a URL and displays
curl -s -w "%{http_code}" -o response_body.txt "$1" | tail -n 1 | grep -q "200" && cat response_body.txt