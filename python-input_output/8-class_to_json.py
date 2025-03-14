#!/usr/bin/python3

"""
This function returns a dictionary
serialization. The function is designed
list, dictionary, string, integer, and boolean.

Prototype: def class_to_json(obj):
- obj is an instance of a Class
- All attributes of the obj Class are serializable
"""


def class_to_json(obj):
    """
    Returns the dictionary description serialization.

    Args:
        obj (object): The object instance to.

    Returns:
        dict: A dictionary containing the.
    """
    return vars(obj)
