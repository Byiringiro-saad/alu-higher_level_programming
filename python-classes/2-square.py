#!/usr/bin/python3

"""
This module defines a class called Square with a private instance
attribute `size`. The class ensures that `size` is an integer and
greater than or equal to 0.
"""


class Square:
    """
    A class that represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square.
        
        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
