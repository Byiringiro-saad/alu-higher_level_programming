#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits.
"""

from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle, inherits from Base.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X coordinate.
        y (int): Y coordinate.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X coordinate (default 0).
            y (int): Y coordinate (default 0).
            id (int, optional): ID (default None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns the string representation of
        Format: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width with validation"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with validation"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x with validation"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y with validation"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
        Prints the Rectangle instance to stdout
        taking into account the x and y offsets.
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def display(self):
        """
        Prints the Rectangle instance with
        """
        for _ in range(self.height):
            print("#" * self.width)

    def display(self):
        """
        Prints in stdout the Rectangle instance with
        considering x and y offsets.
        """
        # Print vertical offset (y) first
        for _ in range(self.y):
            print()
        # Then print the rectangle rows
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args):
        """
        Assigns arguments to attributes in the following order:
        1st: id, 2nd: width, 3rd: height, 4th: x, 5th: y
        """
        attrs = ["id", "width", "height", "x", "y"]

        for i, arg in enumerate(args):
            if i < len(attrs):
                setattr(self, attrs[i], arg)

    def update(self, *args, **kwargs):
        """
        Assigns arguments to attributes:
        - If *args is provided and not empty, assigns
        id, width, height, x, y.
        - Otherwise, assigns using **kwargs where keys
        """
        attrs = ["id", "width", "height", "x", "y"]

        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
