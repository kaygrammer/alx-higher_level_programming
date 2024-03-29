#!/usr/bin/python3

"""class that explains private and public instance"""


class Square:
    """Repesent a Square"""
    def __init__(self, size=0):
        """Initialize the square.
        Args:
        size(int): The size of the new square
        """
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current Area"""
        return (self.__size * self.__size)
