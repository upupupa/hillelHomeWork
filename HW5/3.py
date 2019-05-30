#!/bin/usr/python3
# -*- coding: utf-8 -*-

"""
LRU (least recently used) — это алгоритм, при котором вытесняются значения, которые дольше всего не запрашивались. 
Соответственно, необходимо хранить время последнего запроса к значению. И как только число закэшированных 
значений превосходит N необходимо вытеснить из кеша значение, которое дольше всего не запрашивалось.
Задача - 1
Создать декоратор lru_cache (подобный тому который реализован в Python).
Задача - 2
Ваш lru_cache декоратор должен иметь служебный метод cache_info  - статистика использования вашего кеша 
(например: сколько раз вычислялась ваша функция, а сколько раз значение было взято из кеша, сколько места свободно в кэше, время жизни кэша)
Задача - 3
Ваш lru_cache декоратор должен иметь служебный метод cache_clear - очищает кэш
Пример обращения к служебному методу декоратора
"""
from time import time
def lru_cache(func):
    lru_cache.func_usage = 0
    lru_cache.cache_usage = 0
    lru_cache.lifetime = 0
    lru_cache.cache = {}
    lru_cache.CACHE_LENGTH = 10
    def wrapper(a):
        if a in lru_cache.cache.keys():
            print("from cache: {}".format(lru_cache.cache[a][0]))
            lru_cache.cache_usage+=1
        else:
            result = func(a)
            print("result of function: {}".format(result))
            lru_cache.cache[a] = (result, time())
            lru_cache.func_usage+=1
        if len(lru_cache.cache.keys()) > lru_cache.CACHE_LENGTH:
            flag = (a, lru_cache.cache[a])
            for i in lru_cache.cache.keys():
                if flag[1][1] > lru_cache.cache[i][1]:
                    flag = (i, lru_cache.cache[i])
            del lru_cache.cache[flag[0]]
        if lru_cache.lifetime == 0:
            lru_cache.lifetime = time()

    def cache_info():
        print("Function usage: {}".format(lru_cache.func_usage))
        print("Cache usage: {}".format(lru_cache.cache_usage))
        print("Space left in cache: {}".format(lru_cache.CACHE_LENGTH-len(lru_cache.cache.keys())))
        print("Cache lifetime: {}\n".format(int(time())-lru_cache.lifetime))
    wrapper.cache_info = cache_info
    
    def cache_clear():
        lru_cache.cache.clear()
        lru_cache.func_usage = 0
        lru_cache.cache_usage = 0
        lru_cache.lifetime = time()
        print("Cache cleared")
    wrapper.cache_clear = cache_clear
    return wrapper

@lru_cache
def func(a):
    return a**a

if __name__ == "__main__":
    while True:
        try:
            action = int(input("1.Use function\n2.Print cache info\n3.Clear cache\n"))
            if action == 1:
                a = int(input("Digit: "))
                func(a)
                action = 0
            elif action == 2:
                func.cache_info()
                action = 0
            elif action == 3:
                func.cache_clear()
                action = 0
            else:
                action = 0
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt\nExiting..")
            exit()