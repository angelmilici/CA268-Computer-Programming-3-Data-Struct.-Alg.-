import sys

def rotate(s, n):
    for i in range(int(n)):
        s = s[-1] + s[:-1]
    return s

def main():
    s = sys.argv[1]
    n = int(sys.argv[2])
    print(rotate(s, n))

if __name__ == '__main__':
    main()
