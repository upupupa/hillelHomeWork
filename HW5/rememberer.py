#!/bin/usr/python3
# -*- encoding: utf-8 -*-

def rememberer(func):
    d = {}
    def wrapper(p):
        nonlocal d
        if p not in d.keys():
            d[p]=func(p)
            print(d[p])
        else:
            print("saved result {}".format(d[p]))
    return wrapper

@rememberer
def degree(p):
    return p**p

if __name__ == "__main__":
    while True:
        try:
            param = int(input("Digit: "))
            degree(param)
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt\nExiting..")
            exit()