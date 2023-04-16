#!/usr/bin/python3
"""

Real definition of a class Rectangle

"""

class my_rectangle:
    
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def width(self):
        return self.__width

    def width(self, value):
        
        if type(value) is not int:
            raise TypeError 
            
        if value < 0:
            raise ValueError
            
        self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        
        if type(value) is not int:
            raise TypeError
            
        if value < 0:
            raise ValueError
            
        self.__height = value
