#!usr/bin/env python

import sys

def p(s):
    num = int(s[0])
    b = int(s[1])
    i = 0
    while b ** i < num:
        i += 1
    return i - 1

def num(n, s):
    num = int(s[0])
    b = int(s[1])
    d = []
    i = 0
    while i <= n:
        knum = (num // (b ** (n - i)))
        d.append(int(knum))
        num = (num - ((b ** (n - i)) * knum))
        i += 1
    return d

def c(n):
    fnum = 0
    for c in n:
        fnum = fnum + c ** 2
    return fnum

def main():
    lines = sys.stdin.readlines()
    try:
        d = []
        i = 0
        for l in lines:
            try:
                l = lines[i].strip().split()
                n = p(l)
                knumlist = num(n, l)
                print(c(knumlist))
            except ValueError:
                d.append(i)
            i += 1
    finally:
        if len(d) > 0:
            a = []
            i = 0
            while i < len(d):
                a.append(str(d[i] + 1))
                i += 1
            print('Failed to convert line(s): ' + ', '.join(a) + ' ')

if __name__ == '__main__':
    main()
