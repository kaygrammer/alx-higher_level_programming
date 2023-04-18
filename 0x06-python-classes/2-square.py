#!/usr/bin/python3

"""an empty class that represent a square class"""


class Square:
    """init size and check for errors"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise("size must be an integer")
        elif(size < 0):
            raise("size must be >= 0")
        self.__size = size
