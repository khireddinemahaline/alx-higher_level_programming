#!/usr/bin/python3
"""Write a function that prints x elements of a list."""

def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list:
            print(i, end='')
    except:
        print("Error found")
