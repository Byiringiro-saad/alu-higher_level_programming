#!/usr/bin/python3
"""Fetches http://0.0.0.0:5050/status and display body."""
import urllib.request


if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        decoded_body = body.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(decoded_body))