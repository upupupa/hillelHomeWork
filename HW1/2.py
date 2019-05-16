#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
2. даны два словаря
a = {'a': 1, 'b': 4, 't': 67}
b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
    2.1 найти ключи которые есть в обоих словарях
    2.2 найти ключи которые есть только во 2м словаре, но нет в 1м
    2.3 объединить словари в один, так чтоб числа при одинаковых ключах суммировались
"""

def dictswork():
    a = {'a': 1, 'b': 4, 't': 67}
    b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
    
    #2.1
    output = []
    aKeys = a.keys()
    for i in aKeys:
        if i in b.keys():
            output.append(i)
    print("Keys that repeat: {}".format(output))

    #2.2
    output = []
    bKeys = b.keys()
    for i in bKeys:
        if i not in a.keys():
            output.append(i)
    print("Unique keys in dict b: {}".format(output))

    #2.3
    output = {}
    for i in aKeys:
        if i in b.keys():
            output[i] = a[i] + b[i]
        else:
            output[i] = a[i]
    for i in bKeys:
        if i not in a.keys():
            output[i] = b[i]
    print("Joined dictionary: {}".format(output))

if __name__ == "__main__":
    dictswork()