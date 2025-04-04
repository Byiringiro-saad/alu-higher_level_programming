#!/usr/bin/python3
"""
This is the "models/rectangle.py" file for the.
The Rectangle class inherits from Base and represents
specific attributes: width, height, x, and y. This class
and setter methods to protect and validate these attributes.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base and represents.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x coordinate for the position.
        __y (int): The y coordinate for the position.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
        width (int): Getter for the width attribute.
        width (int): Setter for the width attribute.
        height (int): Getter for the height attribute.
        height (int): Setter for the height attribute.
        x (int): Getter for the x attribute.
        x (int): Setter for the x attribute.
        y (int): Getter for the y attribute.
        y (int): Setter for the y attribute.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate for the position (default 0).
            y (int): The y coordinate for the position (default 0).
            id (int): The id for the instance (default None).

        Calls the super class constructor to handle the id.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        if type(value) is not int:
            raise ValueError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if type(value) is not int:
            raise ValueError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        if type(value) is not int:
            raise ValueError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        if type(value) is not int:
            raise ValueError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
