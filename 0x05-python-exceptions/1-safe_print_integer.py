#!/usr/bin/python3


def safe_print_integer(value):
    """type integer value
    Args:
        value (int): int number
    Return:
        true: if its int
        false: otherwise
    """
    try:
        print("{:d}".format(isinstance(value, int)))
        return True
    except:
        return False
