#!/usr/bin/python3

"""
This class defines a student.
It also includes a method to return.
If an optional list of attribute names is provided.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance.

        Args:
            first_name: The student's first name.
            last_name: The student's last name.
            age: The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves the dictionary of the Student.

        Args:
            attrs (list): A list of attribute in dictionary.

        Returns:
            dict: A dictionary containing the selected.
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
