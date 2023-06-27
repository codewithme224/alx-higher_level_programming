#!/usr/bin/python3
""" finds a peak in a list of unsorted integers. """


def find_peak_rec(list_of_integers, low, high):
    """recursive function to find peak"""
    if low == high:
        return list_of_integers[low]
    mid = (low + high) // 2
    if list_of_integers[mid] > list_of_integers[mid + 1]:
        return find_peak_rec(list_of_integers, low, mid)
    return find_peak_rec(list_of_integers, mid + 1, high)


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if len(list_of_integers) == 0:
        return None
    return find_peak_rec(list_of_integers, 0, len(list_of_integers) - 1)
