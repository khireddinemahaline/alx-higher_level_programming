#!/usr/bin/python3
"""program that prints the result of the addition of all arguments"""


if __name__ == "__main__":
    import sys
    result = 0
    n = len(sys.argv) - 1
    for i in range(n):
        result += int(sys.argv[i + 1])
    return result
