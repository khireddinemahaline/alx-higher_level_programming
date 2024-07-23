#!/usr/bin/python3
"""a function that removes all characters c and C
from a string
"""
def no_c(my_string):
    new_str = list(my_string)
    for i in range(len(new_str)):
        if new_str[i] == 'c' or new_str[i] == 'C':
            new_str[i] = ''
    new_str = ''.join(new_str)
    return new_str