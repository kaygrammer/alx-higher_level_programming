#!/usr/bin/python3

if __name__ == "__main__":
    """A simple calculator"""
    from calculator_1 import add, mul, sub, div
    '''Define variable A and B'''
    a = 10
    b = 5

    """perform some basic arithmetic"""
    addition = add(a, b)
    multiple = mul(a, b)
    substraction = sub(a, b)
    division = div(a, b)

    """Print the result"""
    print("{} + {} = {}".format(a, b, addition))
    print("{} - {} = {}".format(a, b, substraction))
    print("{} * {} = {}".format(a, b, multiple))
    print("{} / {} = {}".format(a, b, division))
