#!/usr/bin/python3

"""
Module that contains a function to write to a file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 encoded text file written.

    Args:
        filename (str): The name of the
        text (str): The string to to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
