#!/usr/bin/python3
"""ValueError or TypeError raised by a class"""


class BaseGeometry():
    
    """Raise an Exceptions"""

    def area(self):
        """raise Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        
        """Raise ValueError and TypeError"""

        if type(value) !=  int:
            raise TypeError("{} must be  integer".format(name))
        if value <= 0:
            
            raise ValueError("{} must be greater than 0".format(name))
