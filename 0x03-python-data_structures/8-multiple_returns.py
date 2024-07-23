#!/usr/bin/python3
"""
multiple return
"""


def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple_sen = 0, None
    else:
        tuple_sen = len(sentence), sentence[0]
    return tuple(tuple_sen)
