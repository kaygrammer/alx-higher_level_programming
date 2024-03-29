#!/usr/bin/python3

"""class that defines a rectangle"""


class Rectangle():
    """initiate a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the rectangle.
        Args:
        size(int): The size of the new square
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return (2*(self.height + self.width))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
