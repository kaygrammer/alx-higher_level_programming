#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """a function that deletes a key in a dictionary"""
    # check if the key exist
    if key in a_dictionary:
        # if it exist del it
        del a_dictionary[key]
    return a_dictionary
