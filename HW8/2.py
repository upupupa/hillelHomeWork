#!/bin/usr/python3
# -*- coding: utf-8 -*-

"""
2. Реализовать класс который будет:
- читать из ввода строку
- проверять, что строка состоит только из скобочек “{}[]()<>”
- проверять, что строка является правильной скобочной последовательностью - выводить вердикт
"""
from queue import LifoQueue as Queue

class Misha():
    def __init__(self):
        self.opencases = ("{", "[", "(", "<")
        self.closecases = ("}", "]", ")", ">")
        self.allcases = "{}[]()<>"
        
    def check(self, arg:str):
        for i in arg:
            if self.allcases.find(i) == -1:
                raise KeyError

    def findcase(self, case):
        for i in range(0, 4):
            if case is self.opencases[i] or case is self.closecases[i]:
                return i

    def checkforcorrect(self, arg):
        last_case = Queue()
        for i in range(0, len(arg)):
            if last_case.empty():
                if arg[i] in self.closecases:
                    raise KeyError
                last_case.put(arg[i])
                continue
            if arg[i] in self.opencases:
                last_case.put(arg[i])
                continue
            if arg[i] in self.closecases:
                bracket = last_case.get()
                print(bracket, self.findcase(bracket), arg[i], self.findcase(arg[i]))
                if self.findcase(arg[i]) == self.findcase(bracket):
                    continue
                else:
                    raise KeyError


if __name__ == "__main__":
    m = Misha()
    s = input("input: ")
    try:
        m.check(s)
    except KeyError:
        print("use only brackets")
        exit()
    try:
        m.checkforcorrect(s)
    except KeyError:
        print("bracket input incorrect")
        exit()
    print("correct string")