#!/usr/bin/python3
""" function that checks for lowercase character"""


def islower(c):
    if (c in range(ord(c) >= 97 , ord(c) <= 122)):
        return True
    else:
        return False
