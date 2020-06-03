#!/usr/bin/python3
"""
Import BaseGeometry and define a square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        initialize the square object
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        method that returns the area of the square
        """
        return self.__size * self.__size
