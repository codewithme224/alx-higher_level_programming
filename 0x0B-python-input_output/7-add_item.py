#!/usr/bin/python3
"""Module for add_item method"""


import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


filename = "add_item.json"
if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []
my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
