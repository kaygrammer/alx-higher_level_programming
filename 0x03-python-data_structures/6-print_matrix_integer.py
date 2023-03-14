#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for ele in matrix:
        for num in ele:
            print("{}".format(num), end=" ")
        print()
