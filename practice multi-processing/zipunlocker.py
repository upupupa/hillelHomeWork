#!/bin/usr/python3
# -*- coding: utf-8 -*-

"""
2. Подобрать пароль (3 строчных латинских буквы). Для работы с архивами можно использовать модуль zipfile. Для подбора паролей - itertools.
3. Распаковать (в итоге получится группа папок с файлами логов в таком формате
 “device\tage\tsex\tcity\tuser_id\tsearch_keyword\tdomain\turl\ttype”
"""

import zipfile
import itertools
import string
import os
import multiprocessing as mp
from queue import Queue
from time import time
import math

def extractor(path, passwords, start, end):
    start = time()
    for i in range(int(start)):
        passwords.next()
    flag = 0
    with zipfile.ZipFile(path, "r") as zipf:
        for i in passwords:
            if flag > end:
                break
            password = "".join(i)
            passwordbytes = password.encode('utf-8')
            try:
                # os.system("clear")
                # print("trying {}".format(password))
                zipf.extractall("./", pwd=passwordbytes)
                #if password is incorrect throws an exception
                #so after this point i can get right password?
            except Exception:
                # print("{} didnt work".format(password))
                flag+=1
                continue
            else:
                right_password = password
                print("correct password is {}, time: {}".format(right_password, time()-start))
                break

def brutepass(*args):
    length, combine, start, end = args
    comb = itertools.product(combine, repeat=length)
    extractor("./lesson6.zip", comb, start, end)

def makeprocess(length, proc=1):
    combine = string.ascii_lowercase
    print(combine, len(combine))
    maxcombinations = math.factorial(length)
    start = 0
    end = maxcombinations//proc
    for i in range(proc):
        mp.Process(target=brutepass, args=(length, combine, start, end)).start()
        end += end
        start = start + end + 1

if __name__ == "__main__":
    makeprocess(3, 4)