#!/usr/bin/python3
"""Module for add_item method"""


import sys
import json
import os.path
from sys import argv

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

for i in argv[1:]:
    my_list.append(i)

save_to_json_file(my_list, filename)
