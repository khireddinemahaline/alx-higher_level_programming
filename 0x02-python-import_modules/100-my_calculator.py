#!/usr/bin/python3
"""prograame"""


if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    n = len(sys.argv) - 1
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    ope = sys.argv[2]
    if n != 3:
        print("Usage: ./100-my_calculator.py {} {} {}".format(a, ope, b))
        sys.exit(1)
    else:
        if ope == "*":
            print("{} {} {} = {}".format(a, ope, b, mul(a, b)))
        if ope == "+":
            print("{} {} {} = {}".format(a, ope, b, add(a, b)))
        if ope == "-":
            print("{} {} {} = {}".format(a, ope, b, sub(a, b)))
        if ope == "/":
            print("{} {} {} = {}".format(a, ope, b, div(a, b)))
        sys.exit(1)
