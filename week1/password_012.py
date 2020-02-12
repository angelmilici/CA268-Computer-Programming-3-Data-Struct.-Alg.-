#!/usr/bin/env python

import sys

def counter(s):
    t = [0, 0, 0, 0]
    for c in s:
        if c.isdigit() == True:
            t[0] = 1

        elif c.isupper() == True:
            t[1] = 1

        elif c.islower() == True:
            t[2] = 1

        elif c.isalnum() != True:
            t[3] = 1

    return t
def main():
    for chars in sys.stdin:
        count = sum(counter(chars.strip()))
        print(count)

if __name__ == '__main__':
    main()
