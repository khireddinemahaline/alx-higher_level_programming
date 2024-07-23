#!/usr/bin/python3
"""
prints a matrix of integers.
"""
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for ele in range(len(matrix[row])):
            print(matrix[row][ele], end=' ')
        print()