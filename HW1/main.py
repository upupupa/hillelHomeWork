#!/usr/bin/python3/
# -*- encoding:utf-8 -*-

"""
Основное задание:
    Познакомиться с LMS
    Завести аккаунт в Git
    Установить PyCharm(или другую IDE)
    Создать репозиторий в Git, познакомиться с основными командами.
Дополнительные задания:
1. дан список [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
    1.1 найти максимум, минимум и их индексы в массиве
    1.2 найти три самых часто встречаемых элемента массива
    1.3 преобразовать в список где каждое значение будет встречаться только 1 раз
        1.3.1 порядок не сохранялся
        1.3.2 порядок сохранялся
2. даны два словаря
a = {'a': 1, 'b': 4, 't': 67}
b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
    2.1 найти ключи которые есть в обоих словарях
    2.2 найти ключи которые есть только во 2м словаре, но нет в 1м
    2.3 объединить словари в один, так чтоб числа при одинаковых ключах суммировались
3. реализовать разложение числа на степени простых множителей (ввод через input, выход по 0)
(простое число - делится только на себя и 1)
вход:
456
0
вывод:
2^3 * 3 * 19
"""

def listswork():
    l = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
    flag = l[0]
    indexList = []
    for i in l:
        if flag < i:
            flag = i
    for i in range(0, len(l)):
        if flag == l[i]:
            indexList.append(i)
    print("Max {} with index {}".format(flag, indexList))

    flag = l[0]
    indexList = []
    for i in l:
        if flag > i:
            flag = i
    for i in range(0, len(l)):
        if flag == l[i]:
            indexList.append(i)
    print("Min {} with index {}".format(flag, indexList))
    
    output = {1:(), 2:(), 3:()}
    for i in l:
        flag = i
        freq = 0
        for j in range(0, len(l)):
            if flag == l[j]:
                freq+=1
        cand = (i, freq)
        try:
            if cand[1] >= output[1][1] and cand[0] != output[1][0]:
                output[3] = output[2]
                output[2] = output[1]
                output[1] = cand
        except:
            output[1] = cand 
    print("3 most frequent elements: ")
    print(output)
        
    lx = [] 
    for i in l:
        if i in lx:
            continue
        else:
            lx.append(i)
    lx.sort()
    print("Unique list sorted {}".format(lx))

    lx = []
    for i in l:
        if i in lx:
            continue
        else:
            lx.append(i)
    print("Unique list saved order {}".format(lx))

if __name__ == "__main__":
    listswork()