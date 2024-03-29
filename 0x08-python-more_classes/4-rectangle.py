#!/usr/bin/python3
"""Definition of a class Rectangle."""


class Rectangle:
    """Representation of a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): Width of new rectangle.
            height (int): Weight of new rectangle.
        """
        
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set width of Rectangle."""
        
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
            
        if value < 0:
            raise ValueError("width must be >= 0")
            
        self.__width = value

    @property
    def height(self):
       """Set height of Rectangle."""
       return self.__height
       
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
            
        if value < 0:
            raise ValueError("height must be >= 0")
            
        self.__height = value

    def area(self):
        """Returns area of Rectangle."""
        
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of Rectangle."""
        
        if self.__width == 0 or self.__height == 0:
            return (0)
            
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents rectangle with # character.
        """
        
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
                
        return ("".join(rect))

    def __repr__(self):
        """Returns string representation of Rectangle."""
        
        rect = "Rectangle(" + str(self.__width)
        
        rect += ", " + str(self.__height) + ")"
        
        return (rect)
