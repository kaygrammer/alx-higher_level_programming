#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """print sorted dictionary"""
    for key, i in sorted(a_dictionary):
        print("{}: {}".format(key, i))
