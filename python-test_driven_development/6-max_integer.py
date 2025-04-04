#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """
    Function to find and return the max integer
    If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    max_value = list[0]
    for i in range(len(list)):
        if list[i] > max_value:
            max_value = list[i]
    return max_value
