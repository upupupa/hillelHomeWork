#!/bin/usr/python3
# -*- coding: utf-8 -*-

"""
2. Реализовать примеры с functools - wraps и singledispatch
"""
#wraps
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(a):
        func(a)
        print("printing cool documentation")
        print(func.__doc__)
        print("end of cool documentation")
    return wrapper


@decorator
def funcwithdoc(a):
    """
    Super function with super docstring

    a - means nothing
    """
    print(a)

if __name__ == "__main__":
    funcwithdoc("wow such function")