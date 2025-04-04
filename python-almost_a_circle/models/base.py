#!/usr/bin/python3
"""
Base module for managing the id attribute.
This module contains the Base class which is responsible
for handling the management of the id attribute in the 
future classes.
"""


class Base:
    """
    Base class for managing the 'id' attribute in future

    Attributes:
        __nb_objects (int): Private class attribute to keep

    Methods:
        __init__(self, id=None): Constructor to initialize
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base instance with an id.

        If the 'id' argument is provided, assigns it to the instance.
        Otherwise, increments the class attribute '__nb_objects'
        the new value as the 'id'.

        Args:
            id (int, optional): The id value to assign to the.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects