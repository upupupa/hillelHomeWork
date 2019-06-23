#!/bin/usr/python3
# -*- coding: utf-8 -*-

"""
2. Реализовать класс singleton (использовать декоратор)
"""
import functools

def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def wrapper(ussid, password):
        if cls not in instances:
            instances[cls] = cls(ussid, password)
        return instances[cls]
    return wrapper

@singleton
class AccessPoint:
    def __init__(self, ussid, password):
        self.ussid = ussid
        self.password = password
    
if __name__ == "__main__":
    ap = AccessPoint("test", "qwerty01")
    print(ap)
    ap1 = AccessPoint("tset", "10ytrewq")
    print(ap1)