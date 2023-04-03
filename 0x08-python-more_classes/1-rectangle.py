#!/usr/bin/python3
"""Module for Rectangle class"""


class Rectangle:
    """Class that defines a rectangle

    Args:
        width: the width of the rectangle
        height: height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes the data"""
        self.width = width
        self.height = height

        @property
        def width(self):
            """Retrieves the width"""
            return self.__width

        @width.setter
        def width(self, value):
            """Sets the width"""
            if isinstance(value, int) is False:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self, value):
            """Retrieves the height"""
            return self.__height

        @height.setter
        def height(self, value):
            """Sets the height"""
            if isinstance(value, int) is False:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
