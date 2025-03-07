#!/usr/bin/python3

"""
This module defines a class called Square. The class has a private
instance attribute `size` that represents the size of the square.
This implementation does not perform any type or value verification.
"""


class Square:
    """
    A class that represents a square.

    The class has a private instance attribute `size` which defines
    the size of the square. There is no type or value verification 
    implemented for the size attribute.
    """

    def __init__(self, size):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
