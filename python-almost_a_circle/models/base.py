#!/usr/bin/python3

"""Base class for all other classes in the project.
This class manages id attribute for all classes.
It also keeps track of the number of instances created.
"""


class Base:
    # Private class attribute to keep track of the number of instances

    """Private class attribute to keep track of the numberof instances"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        If id is provided, assigns it to the instance.
        Otherwise, increments __nb_objects and assigns the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
