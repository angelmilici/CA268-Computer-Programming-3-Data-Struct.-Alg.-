#!/usr/bin/env python

import sys
from math import pi

def area(r):
    return 4 * pi * (r ** 2)

def volume(r):
    return (4 / 3) * pi * (r ** 3)

def main():
    start_r = float(sys.argv[1])
    inc_r = float(sys.argv[2])
    end_r = float(sys.argv[3])

    h1 = 'Radius (m)'
    h4 = '-' * len(h1)
    h2 = 'Area (m^2)'
    h5 = '-' * len(h2)
    h3 = 'Volume (m^3)'
    h6 = '-' * len(h3)

    print('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3))
    print('{:>s} {:>15s} {:>15s}'.format(h4, h5, h6))

    counter = float(start_r)
    while counter <= float(end_r):
        print('{:>10.1f}'.format(counter) + '{:>16.2f}'.format(area(counter)) + '{:>16.2f}'.format(volume(counter)))
        counter += float(inc_r)

if __name__ == '__main__':
    main()
