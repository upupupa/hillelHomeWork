#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
3. реализовать разложение числа на степени простых множителей (ввод через input, выход по 0)
(простое число - делится только на себя и 1)
вход:
456
0
вывод:
2^3 * 3 * 19
"""
def counter(number):
    i = 2
    end = 0
    output = []
    while i * i <= number:
        while number % i == end:
            output.append(i)
            number = number / i
        i += 1
    if number > 1:
        output.append(int(number))
    outString = " * ".join(str(i) for i in output)
    print("Answer: {}".format(outString))

if __name__ == "__main__":
    number = 0
    while number <= 1:
        number = int(input("Enter number: "))
    counter(number)