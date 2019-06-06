#!/bin/usr/python3
# -*- coding: utf-8 -*-
def lfu_cachearg(cache_length):
    def lfu_cache(func):
        lfu_cache.cache = {}
        lfu_cache.CACHE_LENGTH = cache_length
        def wrapper(a):
            if a in lfu_cache.cache.keys():
                print("from cache returning {}".format(a))
                counter  = lfu_cache.cache[a][1] + 1
                lfu_cache.cache[a] = (lfu_cache.cache[a][0], counter)
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
            lfu_cache.cache[a] = (result, 0)
            print("{} added to cache".format(a))
            return lfu_cache.cache[a]
        return wrapper
    return lfu_cache

@lfu_cachearg(3)
def simplefunc(a):
    return a*a

if __name__ == "__main__":
    while True:
        try:
            a = int(input("Digit: "))
            simplefunc(a)
        except KeyboardInterrupt:
            exit()