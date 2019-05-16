#!/usr/bin/python3
# -*- encoding: utf-8 -*-

def sortedArr(search):
    l = [i for i in range(100)]
    start = 0
    end = len(l)-1
    found = False

    while start<=end and not found:
        mid = (start + end) // 2
        if l[mid] is search:
            found = True
        else:
            if search < l[mid]:
                end=mid-1
            else:
                start=mid+1
    print("{} is on {}".format(search, mid))

if __name__ == "__main__":
    search = int(input("Search? (1, 100)\n"))
    sortedArr(search)