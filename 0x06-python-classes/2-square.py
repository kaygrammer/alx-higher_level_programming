#!/usr/bin/python3

"""an empty class that represent a square class"""


class Square:
    """init size and check for errors"""
    def __init__(self, size=0):
        """
        Args:
        size: size of the integer
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
