#!/usr/bin/env python

import sys

def mark(filename):
    a = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                words = line.strip().split()
                mark = int(words[0])
                name = ' '.join(words[1:])
                if mark not in a:
                    a[mark] = name

            max_mark = max(a)
            best_student = a[max_mark]

            print('Best student: {:s}'.format(best_student))
            print('Best mark: {:d}'.format(max_mark))

    except FileNotFoundError:
        print('The file {:s} could not be opened.'.format(filename))

def main():
    args = sys.argv[1]
    mark(args)

if __name__ == '__main__':
    main()
    