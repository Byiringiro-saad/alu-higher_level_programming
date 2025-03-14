#!/usr/bin/python3

"""
Module that contains a function to object.
"""

import json


def from_json_string(my_str):
    """
    Returns a Python object represented by string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python data structure JSON string.
    """
    return json.loads(my_str)
