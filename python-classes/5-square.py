#!/usr/bin/python3

"""
This module defines a class called Square. The class has a private
instance attribute `size` with appropriate getter and setter, a method
to calculate the area of the square, and a method to print the square
using the '#' character. The size of the square must be an integer
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
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square to set.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character.

        If the size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
