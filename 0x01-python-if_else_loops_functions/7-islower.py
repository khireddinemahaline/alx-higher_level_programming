#!/usr/bin/python3
""" function that checks for lowercase character"""


def islower(c):
    if (c in range(ord('a'), ord('z')+1)):
        return True
    else:
        return False
