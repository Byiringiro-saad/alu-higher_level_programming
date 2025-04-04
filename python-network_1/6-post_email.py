#!/usr/bin/python3
"""
This script takes in a URL and an email
with the email as a parameter, and
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
