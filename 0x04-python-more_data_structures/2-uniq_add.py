#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()
    number = 0
    for i in my_list:
        if i not in unique_integers:
            unique_integers.add(i)
            number += i
