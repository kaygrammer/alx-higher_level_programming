#!/usr/bin/python3


def max_integer(my_list=[]):
    """Find the maximum integer in a list

    if the list is empty, returns None.

    Args:
        my_list(list of int): A list of integers

    Returns:
        The maximun integer in the list or None if list is empty
    """
    if not my_list:
        return None

    max_num = my_list[0]
    for num in my_list:
        if num > max_num:
            max_num = num

    return max_num
