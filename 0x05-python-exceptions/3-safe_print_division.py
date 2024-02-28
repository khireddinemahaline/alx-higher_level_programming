#!/usr/bin/python3
"""write print division function"""

def safe_print_division(a, b):
    try:
        res = a / b
    except (TypeError, ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
