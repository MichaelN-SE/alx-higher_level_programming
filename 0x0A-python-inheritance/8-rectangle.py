#!/usr/bin/python3
"""Contains the class BaseGeometry and subclass Rectangle"""

BaseGeometry  =  __import__('7-base_geometry').BaseGeometry
"""importing module with class to inherit"""


class Rectangle(BaseGeometry):
    """using class base to validate integer errors"""

    def  __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
