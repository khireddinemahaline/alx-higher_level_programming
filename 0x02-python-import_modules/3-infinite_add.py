#!/usr/bin/python3
"""program that prints the result of the addition of all arguments"""


if __name__ == "__main__":
    import sys
    result = 0
    n = len(sys.argv) - 1
    for i in range(n):
<<<<<<< HEAD
        result += int(sys.argv[i + 1])
=======
        result =+ int(sys.argv[i + 1])
>>>>>>> e8001e85bc0d55a26d9bb4b4c32c45d2c52221f8
    print(result)
