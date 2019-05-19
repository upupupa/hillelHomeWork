#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
На ввод дается строка. Нужно каждое слово развернуть наоборот. Порядок слов не должен меняться.
"""

def reverseWords(inputString):
    l = inputString.split(" ")
    for i in range(0, len(l)):
        l[i] = l[i][::-1]
    reversedWords = " ".join(l)
    return reversedWords

if __name__ == "__main__":
    inputSrting = input("String to reverse: ")
    rW = reverseWords(inputSrting)
    print(rW)