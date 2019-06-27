#!/bin/usr/python3
# -*- coding: utf-8 -*-

"""
Написать декоратор с аргументом который будет подавлять определенные ошибки возникающие в теле вашей функции. 
Ошибки которые должен будет подавить ваш декоратор, вы должны передать ему в качестве аргумента
"""

def decoargs(*exceptions):
    def exceprionhandler(func):
        def wrapper(a, b):
            try:
                a = func(a, b)
            except exceptions as e:
                return e
            return a
        return wrapper
    return exceprionhandler

@decoargs(ZeroDivisionError, TypeError)
def divide(a, b):
    return a/b

if __name__ == "__main__":
    print(divide(2, 0))
    print(divide(2, 10))
    print(divide(2, "a"))
    print(divide(10, 2))