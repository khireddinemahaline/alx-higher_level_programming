#!/usr/bin/python3
"""program that prints the number of and the list of its arguments"""


if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    count = n - 1
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i+1 ,sys.argv[i+1]))
