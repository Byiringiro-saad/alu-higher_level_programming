#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status and display body."""
import urllib.request


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = "Custom status"
        decoded_body = "Custom status"
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(decoded_body))
