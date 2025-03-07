#!/usr/bin/python3

"""
This module defines a class called Square. The class has private
instance attributes `size` and `position`, with appropriate getters
and setters. It also provides methods to calculate the area of the
square and to print the square to the screen, considering the position.
"""

class Square:
    """
    A class that represents a square.
    """
    
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a given size and position.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character.
        """
        if self.__size == 0:
            print("")
            return
        
        # Print leading spaces according to the position
        for i in range(self.__position[1]):
            print("")
        
        # Print the square row by row with leading spaces for each row
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
