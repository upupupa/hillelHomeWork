#!/bin/usr/python3
# -*- encoding: utf-8 -*-
import time
import string
import random

def timer(func):
    def wrapper(listLength):
        start = float(time.time())
        func(listLength)
        print(float(time.time() - start))
    return wrapper

@timer
def listGenerator(listLength):
    l = []
    letters = string.ascii_letters + "0123456789"
    for i in range(0, listLength):
        l.append(letters[random.randint(0, len(letters)-1)])
    print(l)

if __name__ == "__main__":
    lLen = int(input("Input length: "))
    listGenerator(lLen)
