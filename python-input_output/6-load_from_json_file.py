#!/usr/bin/python3

"""
A function to create object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename: The name of the file to read.

    Returns:
        object: The object created from the JSON.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
