import sys

def dict(s):
    d = {}
    l = []
    for line in s:
        try:
            line = line.strip().split(':')
            name = line[0]
            result = sum([int(c) for c in line[1].split(',')])
            d[name] = int(result)
        except ValueError:
            l.append(name)

    return d, l

def main():
    d = dict(sys.stdin)
    for k, v in sorted(d[0].items(), key=lambda x: x[1], reverse=True):
        print('{} : {}'.format(k, v))

    print('Skipped:')
    for i in d[1]:
        print(i)

if __name__ == '__main__':
    main()
