#!/bin/bash
# This script sends a request to a URL and displays the
curl -s -I "$1" | grep -i "Content-Length" | awk '{print $2}'
