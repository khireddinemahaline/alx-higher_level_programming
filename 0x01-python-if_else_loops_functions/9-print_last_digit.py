#!/usr/bin/python3
"""print the last digit """


def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
