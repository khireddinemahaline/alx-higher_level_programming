#!/usr/bin/python3
""" caclulator function """


if __name__ == "__main__":
    from calculator_1 import calculator
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, calculator.add(a, b)))
    print("{} - {} = {}".format(a, b, calculator.substruct(a, b)))
    print("{} * {} = {}".format(a, b, calculator.multiply(a, b)))
    print("{} / {} = {}".format(a, b, calculator.devide(a, b)))
