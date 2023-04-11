#!/usr/bin/python3
"""Module for Rectangle class"""


class Rectangle(BaseGeometry):
    """Class Rectangle inheriting from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height
        as private attributes"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
