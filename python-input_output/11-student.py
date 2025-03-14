#!/usr/bin/python3

"""
This class defines a student.
It includes methods for serialization:
- to_json: retrieves a dictionary representation.
- reload_from_json: updates the student.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance.

        Args:
            first_name: The student's first name.
            last_name: The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves the dictionary representation.

        Args:
            attrs (list): A list of attribute.

        Returns:
            dict: A dictionary selected student.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student.

        Args:
            json (dict): A dictionary containing attribute.
        """
        for key, value in json.items():
            setattr(self, key, value)
