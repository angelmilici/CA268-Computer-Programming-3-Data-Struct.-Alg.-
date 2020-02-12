import sys

def sumFac(n):
    l = []
    for i in range(1, int(n / 2 + 1)):
        if n % i == 0:
            l.append(i)
    return sum(l)

def isPerfect(n):
    if n == sumFac(n):
        return True
    return False

def main():
    for line in sys.stdin:
        line = int(line.strip())
        print(isPerfect(line))

if __name__ == '__main__':
    main()
