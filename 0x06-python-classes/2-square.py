#!/usr/bin/python3

"""an empty class that represent a square class"""


class Square:
    """this inititalize size and check for value and type error"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
