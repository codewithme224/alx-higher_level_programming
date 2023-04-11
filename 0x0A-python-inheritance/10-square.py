#!/usr/bin/python3
"""Module for Square class"""


class Square(Rectangle):
    """Class Square inheriting from Rectangle"""
    def __init__(self, size):
        """Instantiation with size as private attribute"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
