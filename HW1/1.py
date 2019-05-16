#!/usr/bin/python3/
# -*- encoding:utf-8 -*-

"""
1. дан список [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
    1.1 найти максимум, минимум и их индексы в массиве
    1.2 найти три самых часто встречаемых элемента массива
    1.3 преобразовать в список где каждое значение будет встречаться только 1 раз
        1.3.1 порядок не сохранялся
        1.3.2 порядок сохранялся
"""
def listswork():
    l = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]

    #1.1
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

    #1.2    
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

    #1.3    
    lx = [] 
    for i in l:
        if i in lx:
            continue
        else:
            lx.append(i)
    #1.3.1
    print("Unique list saved order {}".format(lx))
    #1.3.2
    lx.sort()
    print("Unique list sorted {}".format(lx))

if __name__ == "__main__":
    listswork()