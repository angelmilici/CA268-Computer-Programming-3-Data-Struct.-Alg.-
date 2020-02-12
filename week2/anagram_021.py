#!/usr/bin/env python

import sys

def anagram(x, y):
    if sorted(x) == sorted(y):
        return True
    else:
        return False

def main():
    for line in sys.stdin:
        line_one = line.strip().split()[0]
        line_two = line.strip().split()[1]
        print(anagram(line_one, line_two))

if __name__ == '__main__':
    main()
