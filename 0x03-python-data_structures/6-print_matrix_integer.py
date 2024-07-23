#!/usr/bin/python3
"""
prints a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for ele in row:
            print("{:d}".format(ele), end=' ' if ele != row[-1] else "")
        print()
