#!usr/bin/env python

import sys

def find(L, target):
    start = 0
    end = len(L) - 1
    while start <= end:
        middle = (start + end)// 2
        midpoint = L[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return midpoint

    L = sorted(L)

def main():
    linelist = []
    for line in sys.stdin:
        linelist.append(line.strip())

    for n in linelist:
        print(find(linelist, n[::-1]))

