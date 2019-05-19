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
    flag = 0
    factor = ""
    cleanOutput = []
    for j in range(0, len(output)):
        flag = output[j]
        if flag is "SKIP":
            continue
        counter = 1
        for k in range(j+1, len(output)):
            if flag == output[k]:
                counter+=1
                output[k] = "SKIP"
        if counter > 1:
            factor = "{}^{}".format(flag, counter)
        else:
            factor = "{}".format(flag)
        cleanOutput.append(factor)
    outString = " * ".join(str(i) for i in cleanOutput)    
    print("Answer: {}".format(outString))

if __name__ == "__main__":
    number = 0
    while number <= 1:
        number = int(input("Enter number: "))
    counter(number)