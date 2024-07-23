#!/usr/bin/python3
"""a function that removes all characters c and C
from a string
"""


def no_c(my_string):
    new_str = my_string.translate({ord(i): None for i in 'cC'})
    return new_str
