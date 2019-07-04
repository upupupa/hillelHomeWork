#!/bin/usr/python3
# -*- coding: utf-8 -*-

"""
Реализовать свой класс исключения. Добавить метод записи в файл. Вызвать
своё исключение и записать ошибку в файл.
"""

class CyrillicException(Exception):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return "cant write cyrrilic symbols in file"

    def writeInFile(self, s):
        with open(self.path, "w") as f:
            f.write(s)
    
def checkCyrilic(s, path):
    cyrrilic = "АБВГДИЙКЛМНОПРСТУФХЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    for i in s:
        if i in cyrrilic:
            raise CyrillicException(path)


if __name__ == "__main__":
    s = input("Write in file: ")
    cyr = CyrillicException("crlcException.txt")
    try:
        checkCyrilic(s, "crlcException.txt")
        cyr.writeInFile(s)
    except CyrillicException as e:
        print(e)
        cyr.writeInFile(e.__str__())
    finally:
        print("print ended")