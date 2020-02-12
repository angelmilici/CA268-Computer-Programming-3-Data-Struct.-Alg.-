import sys
import math

def roots(a, b, c):
    try:
        r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        r2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return r1, r2
    except ValueError:
        return None

def main():
    for line in sys.stdin:
        try:
            line = line.strip().split()
            a_b_c = [int(i) for i in line]
            root = roots(a_b_c[0], a_b_c[1], a_b_c[2])
            print('r1 = {}, r2 = {}'.format(root[0], root[1]))
        except TypeError:
            print(None)

if __name__ == '__main__':
    main()
