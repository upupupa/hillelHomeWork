#!/bin/usr/python3
# -*- encoding: utf-8 -*-

"""
1.4. единичный вызов - выполняет вызов функции только при первом обращении, затем выводит сообщение, что функция уже вызывалась
"""

def singleuse(func):
    singleuse.beenUsed = False
    def wrapper(l):
        if singleuse.beenUsed:
            print("Function can be called only one time")
        else:
            func(l)
            singleuse.beenUsed = True
    return wrapper

@singleuse
def simplefunc(l):
    print(l)

if __name__ == "__main__":
    while True:
        try:
            l = list(input("Input: "))
            simplefunc(l)
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt\nExiting..")
            exit()
