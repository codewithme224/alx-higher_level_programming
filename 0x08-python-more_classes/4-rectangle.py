#!/usr/bin/python3
"""Module for Rectangle class"""


class Rectangle:
    """Class that defines a rectangle"""
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for i in range(self.__height)])

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
