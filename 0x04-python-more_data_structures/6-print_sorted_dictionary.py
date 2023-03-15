#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        value = a_dictionary.get(key)
        if isinstance(value, dict):
            print("{}:".format(key))
            print_sorted_dictionary(value)
        else:
            print("{}: {}".format(key, value))
