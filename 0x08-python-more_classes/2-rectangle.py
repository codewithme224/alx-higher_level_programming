#!/usr/bin/python3
"""This module defines a Rectangle class"""


class Rectangle:
    """This class defines a Rectangle object"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle
        Args:
            value (int): the new width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle
        Args:
            value (int): the new height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
