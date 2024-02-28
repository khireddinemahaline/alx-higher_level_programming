#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Write a function that prints x elements of a list.

    Args:
        my_list (list): the list of elements
        x (int): number of elements

    Return:
        number of elemnts printed
    
    """
    retutned_ele = 0
    for i in range(x):
    try:
            print({}.format(my_list[i), end='')
            retutned_ele += 1
    print("")
    return retutned_ele
    except: 
        print("Error found")
