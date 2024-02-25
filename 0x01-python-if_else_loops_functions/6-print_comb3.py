#!/usr/bin/python3
"""rogram that prints all possible different combinations of two digits"""


def comb_num():
    for i in range(0, 10, 1):
        for j in range(1, 10, 1):
            if (j >= i):
                print("{}{}, ".format(i, j), end = " ")

 
comb_num()
