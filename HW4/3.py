#!bin/usr/python3
# -*- encoding: utf-8 -*-

"""
3. Дается строка - нужно проверить является ли она валидным паролем: 
- длина больше 4 символов
- содержит только маленькие латинские буквы и цифры
- число букв должно быть нечетным, а цифр четным.
"""

import re

def lengthcheck(pw):
    if len(pw) > 4:
        return True
    else:
        return False

def isletterssmall(pw):
    regexp = r'[a-z]|[0-9]'
    for i in range(0, len(pw)):
        if re.match(regexp, pw[i]) is None:
            return False
    return True

def eL_uneD(pw): #even Letters - uneven Digits
    countL = 0
    countD = 0
    for i in range(0, len(pw)):
        if pw[i].isdigit():
            countD+=1
        else:
            countL+=1
    if countL % 2 == 0:
        if countD % 2 == 1:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    pw = input("Input password: ")
    if lengthcheck(pw):
        if isletterssmall(pw):
            if eL_uneD(pw):
                print("{} - good password".format(pw))
            else:
                print("Password must be with an even quantity of letters and uneven quantity of digits")
        else:
            print("All letters must be latin and small")
    else:
        print("Password must be greater than 4 symbols")