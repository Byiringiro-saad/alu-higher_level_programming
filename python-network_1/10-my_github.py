#!/usr/bin/python3
"""
This script uses GitHub credentials
to access the GitHub API and display
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    try:
        json_data = response.json()
        print(json_data.get("id"))
    except ValueError:
        print("Not a valid JSON")
