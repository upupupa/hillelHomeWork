#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
Дана строка "English = 78 Science = 83 Math = 68 History = 65". Вычислить сумму всех чисел в строке
"""
import re

def sumInStr(inputString):
    regexp = r"[0-9]{2}"
    result = 0
    flag = re.findall(regexp, inputString)
    for i in flag:
        result += int(i)
    print(result)

if __name__ == "__main__":
    inputString = "English = 78 Science = 83 Math = 68 History = 65"
    sumInStr(inputString)    
