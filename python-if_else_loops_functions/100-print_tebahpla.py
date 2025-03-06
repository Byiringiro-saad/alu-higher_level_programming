#!/usr/bin/python3
def print_alphabet():
    for i in range(26):
        char = chr(122 - i)
        if i % 2 == 0:
            print("{}".format(char), end="")
        else:
            print("{}".format(char.upper()), end="")
