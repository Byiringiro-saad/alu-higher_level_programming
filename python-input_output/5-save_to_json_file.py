#!/usr/bin/python3

"""
Module that contains a function to write an.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON.

    Args:
        my_obj: The object to serialize and write to file.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
