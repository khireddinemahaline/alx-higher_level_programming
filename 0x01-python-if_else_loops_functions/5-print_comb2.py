#!/usr/bin/python3
"""program that prints numbers from 0 to 99."""
def print_num():
    for i in range(0, 100, 1):
        if i < 98:
            print("{02d},".format(i), end=" ")
        else:
            print("{}\n".format(i))
print_num();
