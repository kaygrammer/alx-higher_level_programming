#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for ele in matrix:
        for num in ele:
            if num == ele[-1]:
                print("{}".format(num), end=" ")
            else:
                print("{}".format(num), end=" ")
        print()
