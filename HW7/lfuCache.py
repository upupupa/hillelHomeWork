#!/bin/usr/python3
# -*- coding: utf-8 -*-
from time import time


def lfu_cachearg(cache_length):
    def lfu_cache(func):
        lfu_cache.cache = {}
        lfu_cache.CACHE_LENGTH = cache_length
        lfu_cache.lifetime = time()
        lfu_cache.func_usage = 0
        lfu_cache.cache_usage = 0
        def wrapper(a):
            if a in lfu_cache.cache.keys():
                print("from cache returning {}".format(a))
                counter  = lfu_cache.cache[a][1] + 1
                lfu_cache.cache[a] = (lfu_cache.cache[a][0], counter)
                lfu_cache.cache_usage += 1
                return lfu_cache.cache[a][0]
            if len(lfu_cache.cache.keys()) >= lfu_cache.CACHE_LENGTH:
                flag = None
                for i in lfu_cache.cache.keys():
                    if flag is None:
                        flag = (lfu_cache.cache[i][0], lfu_cache.cache[i][1], i)
                    if flag[1] > lfu_cache.cache[i][1]:
                        flag = (lfu_cache.cache[i][0], lfu_cache.cache[i][1], i)
                print("{} deleted".format(flag[2]))
                del lfu_cache.cache[flag[2]]
            result = func(a)
            lfu_cache.func_usage += 1
            lfu_cache.cache[a] = (result, 0)
            print("{} added to cache".format(a))
            return lfu_cache.cache[a]

        def cache_info():
            print("Function usage: {}".format(lfu_cache.func_usage))
            print("Cache usage: {}".format(lfu_cache.cache_usage))
            print("Space left in cache: {}".format(lfu_cache.CACHE_LENGTH-len(lfu_cache.cache.keys())))
            print("Cache lifetime: {}\n".format(int(time())-lfu_cache.lifetime))
        wrapper.cache_info = cache_info

        def cache_clear():
            lfu_cache.cache.clear()
            lfu_cache.func_usage = 0
            lfu_cache.cache_usage = 0
            lfu_cache.lifetime = time()
            print("Cache cleared")
        wrapper.cache_clear = cache_clear
        return wrapper
    return lfu_cache

@lfu_cachearg(3)
def simplefunc(a):
    return a*a

if __name__ == "__main__":
    while True:
        try:
            action = int(input("1.Use function\n2.Print cache info\n3.Clear cache\n"))
            if action == 1:
                a = int(input("Digit: "))
                simplefunc(a)
                action = 0
            elif action == 2:
                simplefunc.cache_info()
                action = 0
            elif action == 3:
                simplefunc.cache_clear()
                action = 0
            else:
                action = 0
        except KeyboardInterrupt:
            exit()