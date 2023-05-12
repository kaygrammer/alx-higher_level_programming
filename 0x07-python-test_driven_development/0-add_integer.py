#!/usr//bin/python3

"""Defines a function that adds two integer"""


def add_integer(a, b=98):
    """ Returns an integer: the addition of a and b

    a and b must first be cast to integers if they are float

    Raises:
        TypeError:if either a or b is a non-integer and non-float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
