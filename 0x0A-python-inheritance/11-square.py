#!/usr/bin/python3
"""Inherit from rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class inherit from a class that inherited from another class to find
    area of a square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
