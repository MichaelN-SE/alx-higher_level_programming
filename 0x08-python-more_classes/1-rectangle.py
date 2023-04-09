#!/usr/bin/python3
"""
Define a class rectangle
"""



class rectangle
    """ Representation of a rectangle """
    def__init__(self, width=0, height=0):
        """ initialize the rectangle """
        self.height=height
        self.width=width


    def define width(self):

        """ getter for the private instance attribute width
    """
    return self.__width
    def width(self value
        """ setter for private instance attribute width """
        if type(value) is not int
        raise TypeError("width mudt be an integer")
    if value <0
    raise ValueError(width must be >=0)
self.__width = value
