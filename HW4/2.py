#!bin/usr/python3
# -*- encoding: utf-8 -*-

"""
Дан массив целых чисел. Нужно найти сумму элементов с индексами у которых
сумма бит двоичного представления четна, затем перемножить эту сумму и предпоследний элемент исходного массива.
"""

def evenbin(l):
    binl = bin(l)
    count = 0
    for i in range(len(binl)):
        if binl[i] is "1":
            count+=1
    if count % 2 == 0:
        return l
    else:
        return 0

def multiply(l, sumofl):
    return l[-2]*sumofl

if __name__ == "__main__":
    lstr = input("List: ")
    l = lstr.split(" ")
    lint = [int(i) for i in l]
    evenl = list(map(evenbin, lint))
    sumofl = sum(evenl)
    answer = multiply(lint, sumofl)
    print("Sum of even numbers (bin) = {}\n{} * {} = {}\nAnswer is: {}".format(sumofl, sumofl, lint[-2], answer, answer))