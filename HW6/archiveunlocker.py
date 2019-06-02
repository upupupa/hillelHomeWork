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

def extractor(path, passwords):
    with zipfile.ZipFile(path, "r") as zipf:
        for i in passwords:
            password = "".join(i)
            passwordbytes = password.encode('utf-8')
            try:
                os.system("clear")
                print("trying {}".format(password))
                zipf.extractall("./", pwd=passwordbytes)
                #if password is incorrect throws an exception
                #so after this point i can get right password?
                right_password = password
                print("correct password is {}".format(right_password))
                break
            except Exception:
                print("{} didnt work".format(password))
                continue

def brutepass(length):
    comb = itertools.product(string.ascii_lowercase, repeat=length)
    return comb

if __name__ == "__main__":
    passwords = brutepass(3)
    extractor("./lesson6.zip", passwords)