#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
    На ввод подается строка. Нужно узнать является ли строка палиндромом. (Палиндром - строка которая читается одинаково с начала и с конца.)
"""

def polyndrome(inputString):
    l = inputString
    middle = len(l) // 2
    backi = 0
    isPoly = False
    for i in range(0, middle):
        backi-=1
        if l[i] == l[backi]:
            if (i+1) == middle:
                isPoly = True
            continue
        else:
            break
    return isPoly

if __name__ == "__main__":
    inputString = input("String to check: ")
    isPoly = polyndrome(inputString)
    print("Is {} polyndrome? {}".format(inputString, isPoly))
#вау, с первого трая работает правильно