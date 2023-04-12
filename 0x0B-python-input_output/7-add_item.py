#!/usr/bin/python3
"""Module for add_item method"""


import json
import sys
from os import path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

my_list = []

# Check if the file exists, and load the existing list if it does
filename = 'add_item.json'
if path.exists(filename):
    my_list = load_from_json_file(filename)

# Add all arguments to the list
for arg in sys.argv[1:]:
    my_list.append(arg)

# Save the updated list to the file
save_to_json_file(my_list, filename)
