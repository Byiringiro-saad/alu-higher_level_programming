#!/usr/bin/python3

"""
This script reads arguments from the list stored in a
JSON file named 'add_item.json'. The uck to the file.

It uses two functions:
- load_from_json_file: the 'add_item.json' file.
- save_to_json_file: Saves the d_item.json' file.
"""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if not os.path.exists('add_item.json'):
    items = []
else:
    items = load_from_json_file('add_item.json')

items.extend(sys.argv[1:])

save_to_json_file(items, 'add_item.json')
