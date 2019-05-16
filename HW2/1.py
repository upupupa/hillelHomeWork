#!/usr/bin/python3
# -*- encoding: utf-8 -*-

def countsymbol():
    s = "spam and eggs or eggs with spam"
    sL = list(s)
    sD = {}
    freq = 0
    for i in range(0, len(sL)):
        sD[sL[i]] = 0
    for i in range(0, len(sL)):
        if sL[i] in sL:
            freq = sD[sL[i]] + 1
        sD[sL[i]] = freq
    print(sD)

if __name__ == "__main__":
    countsymbol()
