#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_ints = set()
    for num in my_list:
        if isinstance(num, int):
            unique_ints.add(num)
    sum_unique_ints = sum(unique_ints)
    return sum_unique_ints
