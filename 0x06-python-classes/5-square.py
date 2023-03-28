#!/usr/bin/python3

"""Class Square that defines a square"""


class Square:
    """Private instance attribute: size"""
    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.size = size

    """Public instance method: that returns the current square area"""
    def area(self):
        return self.__size ** 2

    """that prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
