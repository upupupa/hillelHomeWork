#!/bin/usr/python3
# -*- coding: utf-8 -*-

"""
Создать класс Person, в котором будут атрибуты: имя, должность, з\п
Manager - наследуется от Person, атрибут процент от з\п
"""

class Person():
    def __init__(self, name="poly", position="programmer", salary=1000):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self, a):
        r = "'{}'".format(a)
        print("this is reloaded str func in class {}".format(__class__))
        return r

        
class Manager(Person):
    def __init__(self, name="andrew", position="manager", salary=1000, percent="10%"):
        self.percent = percent
        super().__init__(name, position, salary)

if __name__ == "__main__":
    p = Person()
    m = Manager()
    l = ["h", "e", "l", "l", "o"]
    print(p.__str__(l))