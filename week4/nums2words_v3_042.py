import sys

a = {}
d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}

def main():
    with open(sys.argv[1], 'r') as f:
        for i in f:
            a[i.strip().split()[0]] = i.strip().split()[1]

        for line in sys.stdin:
            b = []
            s = []
            for c in line.strip().split():
                b.append(d[int(c)])
            for n in b:
                s.append(a[str(n)])
            print(' '.join(s))

if __name__ == '__main__':
    main()
