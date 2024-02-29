#!/usr/bin/python3
"""program that prints the number of and the list of its arguments"""


if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    count = n - 1
    if n == 0:
        print("{} arguments.".format(n))
    elif n == 1:
        print("{} argument:".format(x))
    else:
        print("{} arguments:".format(n))
    for i in range(count):
        print("{}: {}".format(i+1 ,sys.argv[i+1]))
