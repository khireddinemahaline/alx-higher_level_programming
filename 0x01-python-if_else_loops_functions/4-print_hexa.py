#!/usr/bin/python3
"""prints all numbers from 0 to 98 in decimal and in hexadecimal"""
for i in range(0, 98, 1):
    print("{} : {}\n".format(i, hex(i)))
