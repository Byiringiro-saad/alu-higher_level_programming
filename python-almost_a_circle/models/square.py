#!/usr/bin/python3
"""
This module defines the Square class that inherits
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, inherits from Rectangle.

    Attributes:
        size (int): Size of the square (width and height
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): Size of the square.
            x (int): X coordinate (default 0).
            y (int): Y coordinate (default 0).
            id (int, optional): ID (default None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return the string representation of the Square

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """
        Getter for size.

        Returns:
            int: The size (width) of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size, updates both width

        Args:
            value (int): New size for the square.
        """
        self.width = value
        self.height = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.size ** 2