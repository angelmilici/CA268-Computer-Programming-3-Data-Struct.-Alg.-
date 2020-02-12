#!/usr/bin/env python

import sys

def cen(s):
    for i in range(len(s)):
        return i



def main():
    for lines in sys.stdin.readlines():
        l = len(lines.strip())
        print(cen(lines.strip()))


if __name__ == '__main__':
    main()
