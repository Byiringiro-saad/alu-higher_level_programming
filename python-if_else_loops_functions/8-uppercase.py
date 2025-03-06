#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is lowercase (between 'a' and 'z')
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase by subtracting the difference in ASCII values
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()  # Print a new line after the string
