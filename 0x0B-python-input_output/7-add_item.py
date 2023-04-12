#!/usr/bin/python3
"""Module for add_item method"""


import sys
import json
import os.path
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

json_file = "add_item.json"
my_list = []
if os.path.exists(json_file):
    my_list = load_from_json_file(json_file)

for i in argv[1:]:
    my_list.append(i)

save_to_json_file(my_list, json_file)
