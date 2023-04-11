#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    1. create an empty list
    2. iterate from zero to the length of the list
    perform division on the each items of the list
    3. check if TypeError
    4. ZeroDivisionError
    5. IndexError
    6, add the result to the new_list by appending
    """
    new_list = []

    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return (new_list)
