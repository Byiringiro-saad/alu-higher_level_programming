#!/usr/bin/python3
"""
This module contains a function that prints
The function prints a text with 2 new lines
'.', '?' and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of the characters:

    Args:
        text (str): The text to print with indentation.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n\n", end="")
            i += 1
            # Skip spaces after special characters
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
