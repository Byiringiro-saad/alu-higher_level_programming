#!/usr/bin/python3

"""
This class defines a student.
It also includes a method to return a dictionary.
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

    def to_json(self):
        """
        Retrieves the dictionary Student instance.

        Returns:
            dict: A dictionary attributes.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
