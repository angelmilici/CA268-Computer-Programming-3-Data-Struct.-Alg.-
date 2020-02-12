import sys

def build_dictionary(filename):
    a = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip().split()
            a[str(line[0])] = int(line[1])
        return a

def extract_range(d, low, high):
    p = {}
    for k, v in d.items():
        if low <= int(v) and int(v) <= high:
            p[str(k)] = int(v)
    return p

def main():
    d = build_dictionary(sys.argv[1])
    nd = extract_range(d, 5, 15)
    for (k, v) in sorted(nd.items()):
        print('{} : {}'.format(k, v))

if __name__ == '__main__':
    main()
