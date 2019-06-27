#!/bin/usr/python3
# -*- coding: utf-8 -*-

"""
Написать декоратор который будет подавлять ошибки возникающие в теле вашей функции.
"""

def execptiondeco(func):
    def wrapper(a, b):
        try:
            a = func(a, b)
        except ZeroDivisionError as e:
            return e
        except TypeError as e:
            return e
        return a
    return wrapper

@execptiondeco
def divide(a, b):
    return a / b

if __name__ == "__main__":
    print(divide(2, 0))
    print(divide(2, "a"))
    print(divide(10, 2))