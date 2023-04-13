#!/usr/bin/python3
"""Module for add_item method"""

import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
if __name__ == "__main__":
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []
    for i, arg in enumerate(sys.argv):
        if i > 0:
            my_list.append(arg)
    save_to_json_file(my_list, filename)
