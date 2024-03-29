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
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
