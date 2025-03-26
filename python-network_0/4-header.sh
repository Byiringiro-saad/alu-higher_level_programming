#!/bin/bash
# This script sends a GET request to a URL with a custom X-HolbertonSchool-User-Id header and displays the response body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$0"