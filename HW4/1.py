#!bin/usr/python3
# -*- encoding: utf-8 -*-

"""
Дан массив. Реализовать функцию которая будет переставлять 2 выбранных элемента списка местами. 
Функция должна иметь вид: def swap(target_list, item_index1, item_index2).
"""

def swap(l, ind1, ind2):
    a = l[ind1]
    b = l[ind2]
    l[ind1] = b
    l[ind2] = a
    return l

if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9]
    sl = swap(l, 0, 8)
    print(sl)