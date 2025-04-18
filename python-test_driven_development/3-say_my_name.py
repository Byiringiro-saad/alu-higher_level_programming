#!/usr/bin/python3
"""
This module contains a function that prints a name.

The function takes first name and last name parameters and prints them
in the format "My name is <first name> <last name>".
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): The first name to be printed.
        last_name (str): The last name to be printed, defaults to empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
