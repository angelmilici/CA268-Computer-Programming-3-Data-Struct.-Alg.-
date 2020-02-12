#!usr/bin/env python

import sys

def main():
    f = open(sys.argv[1], 'r')
    a = []
    for line in f:
        line = line.strip()
        a.append(line)
    f.close()

    linelist = []
    for line in sys.stdin:
        linelist.append(line.strip())

    for n in linelist:
        i = 0
        while i < len(a):
            if a[i] in n:
                n.replace(a[i], '@')
            i += 1
        print(n)




if __name__ == '__main__':
    main()
