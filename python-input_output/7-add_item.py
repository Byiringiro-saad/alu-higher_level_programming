#!/usr/bin/python3

"""
This script reads arguments from to a list stored in a
JSON file named 'add_item.json', list back to the file.

It uses two functions:
- load_from_json_file: Loads the list from the 'add_item.json' file.
- save_to_json_file: Saves th list back to the 'add_item.json' file.
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

items = load_from_json_file('add_item.json')

items.extend(sys.argv[1:])

save_to_json_file(items, 'add_item.json')
