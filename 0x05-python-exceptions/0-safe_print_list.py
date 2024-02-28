#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Write a function that prints x elements of a list.

    Args:
        my_list (list): the list of elements
        x (int): number of elements

    Return:
        number of elemnts printed
    
    """
    try:
        for i in my_list[:x]:
            print(i, end='')
        return x
    except IndexError: 
        break
