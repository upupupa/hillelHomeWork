#!/bin/usr/python3
# -*- coding: utf-8 -*-

def countCalls(func):
    count = 1
    def wrapper():
        nonlocal count
        func()
        print("function called {} times".format(count))
        count+=1
    return wrapper

@countCalls
def simpleFunc():
    print("function was called")

if __name__ == "__main__":
    how_many = int(input("How many times function will be called?: "))
    for i in range(0, how_many):
        simpleFunc()