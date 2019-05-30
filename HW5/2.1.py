#!/bin/usr/python3
# -*- coding: utf-8 -*-

"""
2. Реализовать примеры с functools - wraps и singledispatch
"""
#singledispatch
import functools

@functools.singledispatch
def funfunc(arg):
    print("use string or list")
    pass

@funfunc.register(str)
def _(arg:str):
    arg1 = arg[::-1]
    print(arg1, arg)
    pass

@funfunc.register(list)
def _(arg:list):
    arg.sort()
    print(arg)
    pass

if __name__ == "__main__":
    funfunc(15)
    funfunc("hewwwoo")
    funfunc([15, 3, 55, 2, 7])