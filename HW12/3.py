#!/bin/usr/python3
# -*- coding: utf-8 -*-

"""
Реализовать класс который можно использовать и как декоратор и как менеджер контекста
Пусть он тоже замеряте время выполнения. Проверить что работает быстрее - вызвать и обработать
исключение или использовать условный оператор
"""
from time import time

class TimeFunc(object):
    def __call__(self, func):
        def wrapper(s):
            start = time()
            func(s)
            result = time() - start
            print("{:.2f}".format(result))
        return wrapper

    def __enter__(self):
        self.start = time()
        return ""

    def __exit__(self, type, value, traceback):
        self.result = time() - self.start
        print("{:.2f}".format(self.result))

def listgenerator(a):
    l = [l for l in range(a)]
    return l

@TimeFunc()
def listgeneratorDeco(a):
    l = [l for l in range(a)]
    return l

if __name__ == "__main__":
    print("decorator")
    listgeneratorDeco(100000000)
    print("context manager")
    with TimeFunc() as t:
        listgenerator(100000000)