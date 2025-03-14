#!/usr/bin/python3

"""
Module that contains a function to read a its content.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints to stdout.

    Args:
        filename (str): The name of the file to read string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
