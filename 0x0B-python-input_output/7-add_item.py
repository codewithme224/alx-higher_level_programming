#!/usr/bin/python3
"""Module for add_item method"""


import sys
import json
from os import path
from sys import argv


from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


filename = "add_item.json"
my_list = []

if path.exists(filename):
    my_list = load_from_json_file(filename)

for i in argv[1:]:
    my_list.append(i)

save_to_json_file(my_list, filename)
