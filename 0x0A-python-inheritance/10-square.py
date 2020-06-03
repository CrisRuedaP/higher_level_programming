#!/usr/bin/python3
"""
Import Rectangle and define a square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """initialize the method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
