import sys

def cal_dict(filename):
    d = {}
    with open(filename, 'r') as f:
        for line in f:
            food = line.strip().split()[:-1]
            cal = line.strip().split()[-1]
            d[str(' '.join(food))] = int(cal)
        return d

def diet_dict(p, d):
    name_cal = {}
    for line in p.readlines():
        cal = []
        name = line.strip().split(',')[0]
        food = line.strip().split(',')[1:]
        for i in food:
            if i not in d:
                cal.append(100)
            else:
                cal.append(d[i])
        name_cal[name] = sum(cal)
    return name_cal

def main():
    s = sys.argv[1]
    p = sys.stdin
    d = cal_dict(s)
    nd = diet_dict(p, d)
    z = [k for k, v in nd.items()]
    q = [str(v) for k, v in nd.items()]
    for k, v in sorted(nd.items(), key=lambda x: x[1]):
        max_1 = max(z, key=len)
        max_2 = max(q, key=len)
        print('{:>{:d}s}'.format(k, int(len(max_1))) + ' : ' + '{:{:d}d}'.format(v, int(len(max_2))))

if __name__ == '__main__':
    main()
