#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Create a new List to hold the modified element"""
    result = []

    """Iterate over the original list and replace elements necessary"""
    for ele in my_list:
        if ele == search:
            result.append(replace)
        else:
            result.append(ele)
    return result
