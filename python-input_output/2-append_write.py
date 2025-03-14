#!/usr/bin/python3

"""
Module that contains a function to to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of characters added.

    Args:
        filename (str): The name of the

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
