#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        res = a / b
        print("{} / {} = {}".format(a, b, res))
    except:
        res = None
    finally:
        print("Inside result: {}".format(res))
