#!/usr/bin/python3
"""
Base module for managing the id attribute.
This module contains the Base class which is responsible
for handling the management of the id attribute in the 
future classes.
"""

import json


class Base:
    """
    Base class for managing the 'id' attribute in future

    Attributes:
        __nb_objects (int): Private class attribute to

    Methods:
        __init__(self, id=None): Constructor to initialize
        to_json_string(list_dictionaries): Serialize list
        from_json_string(json_string): Deserialize JSON
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base instance with an id.

        If the 'id' argument is provided, assigns i.
        Otherwise, increments the class attribute ''
        the new value as the 'id'.

        Args:
            id (int, optional): The id value to assign to.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by a JSON string.

        Args:
            json_string (str): A string representing.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)