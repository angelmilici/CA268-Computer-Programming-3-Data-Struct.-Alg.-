import sys

a = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}

def main():
    for line in sys.stdin:
        b = []
        for i in line.strip().split():
            if i is int:
                b.append(a[int(i)])
            print(b)


if __name__ == '__main__':
    main()
