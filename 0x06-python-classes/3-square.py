#!/usr/bin/python3

"""Class Square that defines a square"""


class Square:
    """Private instance attribute: size"""
    def __init__(self, size=0):
        """Instantiation with optional size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """Public instance method: that returns the current square area"""
    def area(self):
        return self.__size ** 2
