#!/usr/bin/python3
"""Definition of Rectangle class."""


class Rectangle:
    """Representation of rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes new Rectangle.

        Args:
            width(int): Width of new rectangle.
            height(int): Height of new rectangle.
        """
        
        self.width = width
        self.height = height

    @property
    def width(self):
        """width of Rectangle is set."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError ("width must be an integer")
            
        if value < 0:
            raise ValueError ("width must be >= 0")
            
        self.__width = value

    @property
    def height(self):
        """height of the Rectangle is set."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError ("height must be an integer")
            
        if value < 0:
            raise ValueError ("height must be >= 0")
            
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
        """Returns printable representation of Rectangle.

        Represents rectangle with  # character.
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
        """Returns string representation of the Rectangle."""
        
        rect = "Rectangle(" + str(self.__width)
        
        rect += ", " + str(self.__height) + ")"
        
        return (rect)

    def __del__(self):
        """Prints message for every deletion of Rectangle."""
        print("Bye rectangle...")
