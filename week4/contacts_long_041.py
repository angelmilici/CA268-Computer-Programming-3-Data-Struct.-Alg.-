#!/usr/bin/env python

import sys

a = {}
b = {}
def dict():
    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = line.strip().split()
            a[line[0]] = line[1]
            b[line[0]] = line[2]

    for line in sys.stdin:
        try:
            print('Name: {:s}'.format(line.strip()))
            print('Phone: {:s}'.format(a[line.strip()]))
            print('Email: {:s}'.format(b[line.strip()]))
        except KeyError:
            print('No such contact')

def main():
    dict()

if __name__ == '__main__':
    main()
