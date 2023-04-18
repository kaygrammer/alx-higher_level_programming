#!/usr/bin/python3

"""an empty class that represent a square class"""


class Square:
    def __init__(self, size=0):
        """Args:
       Size: size of an integer
        """
        if type(size) is not int:
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
