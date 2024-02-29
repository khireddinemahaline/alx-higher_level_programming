#!/usr/bin/python3
"""write a programme that print the result of addint two integer"""


def add_integer(a, b=98):
    """
    Args:
        a: integer number
        b: integer number
    Return:
        should return the result of the tow integers
    Raises:
        TypeError: if a or b not an integer or a float
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, float) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
