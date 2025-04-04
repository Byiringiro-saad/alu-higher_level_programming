#!/usr/bin/python3
"""
This module contains a function that adds two integers
casting them to integers and checking for valid input.
The function raises a TypeError if either of the inputs
or if there are invalid floating point values like NaN.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting

    Parameters:
    a (int or float): The first value to add.
    b (int or float, optional): The second value to add,

    Returns:
    int: The sum of the two numbers after casting them to integers.

    Raises:
    TypeError: If a or b is not an integer or float.
    ValueError: If a or b is a float that cannot

    Example:
    >>> add_integer(2, 3)
    5
    >>> add_integer(2.5, 3.5)
    5
    >>> add_integer(2.5)
    100
    >>> add_integer("2", 3)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    """
    # Check type of 'a'
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    # Check type of 'b'
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    # Handle NaN or infinity floats
    if isinstance(a, float) and (
        a != a or a == float('inf') or a == float('-inf')
    ):
        raise ValueError("a cannot be converted to an integer")

    if isinstance(b, float) and (
        b != b or b == float('inf') or b == float('-inf')
    ):
        raise ValueError("b cannot be converted to an integer")

    # Cast floats to integers
    a = int(a)
    b = int(b)

    return a + b
