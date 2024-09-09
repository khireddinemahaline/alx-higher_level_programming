#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(lst):
    if not lst:
        return None

    n = len(lst)

    # Check if the first or last element is a peak
    if n == 1:
        return lst[0]
    if lst[0] >= lst[1]:
        return lst[0]
    if lst[-1] >= lst[-2]:
        return lst[-1]

    # Check the rest of the elements
    for i in range(1, n - 1):
        if lst[i] >= lst[i - 1] and lst[i] >= lst[i + 1]:
            return lst[i]

    return None
