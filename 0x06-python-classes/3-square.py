#!/usr/bin/python3

"""an empty class that represent a square class"""


class Square:
    """initialize a private instance and public method"""
    def __init__(self, size=0):
        """
        Args:
        size: size of the integer
        Area: Area of a square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """public instance"""
    def area(self):
        return self.__size ** 2
