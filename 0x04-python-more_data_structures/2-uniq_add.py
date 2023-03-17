#!/usr/bin/python3


def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)."""
    sum = 0
    uniques = set(my_list)
    for i in uniques:
        sum += i
    return sum
