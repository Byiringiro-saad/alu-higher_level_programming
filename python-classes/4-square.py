#!/usr/bin/python3

"""
This module defines a class called Square. The class has a private
instance attribute `size` and a public instance method `area` to
calculate the area of the square. The `size` must be an integer
and greater than or equal to 0. A property is used to manage the
`size` attribute.
"""

class Square:
    """
    A class that represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2
