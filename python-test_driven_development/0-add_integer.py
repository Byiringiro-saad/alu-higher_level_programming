#!/usr/bin/python3
"""
This module contains a function that adds two integers.
The function checks that the inputs are either integers
If the inputs are not valid, a TypeError is raised with
"""

def add_integer(a, b=98):
    """
    Adds two integers, where the second integer has

    Parameters:
    a (int or float): The first value to add.
    b (int or float, optional): The second value to

    Returns:
    int: The sum of the two integers.

    Raises:
    TypeError: If either a or b is not an integer

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
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
