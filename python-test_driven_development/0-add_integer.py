#!/usr/bin/python3
"""
The function takes two parameters, converts them to
floats, and returns their sum as an integer.
If either parameter is not an integer or float,
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Args:
        a (int, float): First number to be added.
        b (int, float): Second number to be added, defaults to 98.

    Returns:
        int: The addition of a and b after converting to integers.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if a is None:
        raise TypeError("a must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Handle special float cases before casting
    if isinstance(a, float):
        if a == float('inf') or a == -float('inf'):
            raise ValueError("cannot convert float infinity to integer")
        if a != a:  # Check for NaN
            raise ValueError("cannot convert float NaN to integer")

    if isinstance(b, float):
        if b == float('inf') or b == -float('inf'):
            raise ValueError("cannot convert float infinity to integer")
        if b != b:  # Check for NaN
            raise ValueError("cannot convert float NaN to integer")

    return int(a) + int(b)
