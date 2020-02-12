#!/usr/bin/env python

import sys

a = {}
list_of_lists = []
def l2d(l):
    for line in l.readlines():
        new_list = [c for c in line.strip().split()]
        list_of_lists.append(new_list)
    ls_1 = list_of_lists[0]
    ls_2 = list_of_lists[1]
    i = 0
    while i < len(ls_1):
        a[str(ls_1[i])] = int(ls_2[i])
        i += 1
    return a

def main():
    d = l2d(sys.stdin)
    for (k, v) in sorted(d.items()):
        print('{} : {}'.format(k, v))

if __name__ == '__main__':
    main()
