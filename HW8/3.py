#!/bin/usr/python3
# -*- coding: utf-8 -*-

"""
3. У вас несколько JSON файлов. В каждом из этих файлов есть произвольная структура данных. Вам необходимо написать класс который будет описывать работу с этими файлами, а именно:
- запись в файл
- чтение из файла
- объединение данных из файлов в новый файл
- получить относительный путь к файлу
- получить абсолютный путь к файлу
"""
import json
import os

class Jsonreader():
    def __init__(self, path):
        self.path = path
        self.jsonData = None

    def readjfile(self):
        try:
            with open(self.path, "r") as jf:
                self.jsonData = json.load(fp=jf)
        except Exception as e:
            print(e)
            return -1
        return self.jsonData
            
    def writejfile(self, data=None):
        if data is None:
            if self.jsonData is None:
                print("no data to write")
                return -1
            data = self.jsonData
        with open(self.path, "w", encoding="utf-8") as jf:
            json.dump(data, jf, indent=2, ensure_ascii=False)
            jf.close()
        return 0
    
    def combine(self, jObj1, jObj2):
        combined = []
        if jObj1 == -1 or jObj2 == -1:
            print("invalid json object")
            return -1
        combined.extend(jObj1)
        combined.extend(jObj2)
        return combined
    
    def getRelPath(self):
        try:
            relpath = os.path.relpath(self.path, start=os.curdir)
        except Exception:
            print("no such file")
            return -1
        return relpath

    def getAbsPath(self):
        try:
            abspath = os.path.abspath(self.path)
        except Exception:
            print("no such file")
            return -1
        return abspath

if __name__ == "__main__":
    a = Jsonreader("./jsons/a.json")
    b = Jsonreader("./jsons/b.json")
    c = Jsonreader("./jsons/c.json") #by default not exist
    ab = Jsonreader("./jsons/ab.json") #to combine a and b
    ab.jsonData = ab.combine(a.readjfile(), b.readjfile())
    ab.writejfile(ab.jsonData)