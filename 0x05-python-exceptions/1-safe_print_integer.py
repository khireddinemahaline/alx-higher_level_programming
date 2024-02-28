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
        print("{:d}".format(int(value)))
        return True
    except:
        return False
