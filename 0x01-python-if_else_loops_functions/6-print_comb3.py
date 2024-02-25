#!/usr/bin/python3
"""rogram that prints all possible different combinations of two digits"""


def comb_num():
    for i in range(0, 10, 1):
        for j in range(1, 10, 1):
            if (j > i or i < 9):
                print("{}{},".format(i, j), end = " ")
            else:
                print("{}{}".format(i, j))

 
comb_num()
