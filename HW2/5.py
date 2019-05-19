#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
Напишите генератор случайных паролей. После запуска программа должна ждать ввода 
числа - длины пароля и нажатия Enter. Завершить программу нужно если будет введен 0. 
Также нужно проверять является ли введенная строка числом. 
Допустимые символы - цифры, большие и маленькие латинские буквы.
"""
import random
import string

def passGen(length):
    password = []
    letters = string.ascii_letters + "0123456789"
    for i in range(0, length):
        flag = random.randint(0, len(letters)-1)
        password.append(letters[flag])
    output = "".join(password)
    return output

if __name__ == "__main__":
    length = int(input("Input pass len: "))
    if length == 0:
        exit()
    password = passGen(length)
    print(password)