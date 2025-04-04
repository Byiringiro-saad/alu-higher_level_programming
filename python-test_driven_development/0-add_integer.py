#!/usr/bin/python3
"""
This module contains a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Args:
        a (int, float): First number to be added.
        b (int, float): Second number to be added

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
