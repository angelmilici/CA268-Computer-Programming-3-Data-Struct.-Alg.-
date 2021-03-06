#!/usr/bin/env python

import sys

def main():

    h1 = 'POS'
    h2 = 'CLUB'
    h3 = 'P'
    h4 = 'W'
    h5 = 'D'
    h6 = 'L'
    h7 = 'GF'
    h8 = 'GA'
    h9 = 'GD'
    h10 = 'PTS'

    print('{:>3s} {:20s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(h1, h2, h3, h4, h5, h6, h7, h8, h9, h10))

    for line in sys.stdin:

        
        print(line.strip().split()[1:-8])

if __name__ == '__main__':
    main()
