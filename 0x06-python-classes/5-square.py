#!/usr/bin/python3

"""a class Square that defines a square"""


class Square:
    """"initialize the new square
    Args:
        size(int): The size of the square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """retrieve size"""
        return (self._size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            return TypeError("size must be an integer")
        elif value < 0:
            return ValueError("size must be >= 0")
        self._size = value

    def area(self):
        return (self._size * self._size)

    def my_print(self):
        """Print the square with the # character"""
        for i in range(0, self._size):
            [print("#", end="") for j in range(self._size)]
            print("")
        if self._size == 0:
            print("")
