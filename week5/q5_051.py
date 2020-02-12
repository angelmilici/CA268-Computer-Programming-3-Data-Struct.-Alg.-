import sys

def seconds(s):
    [mins, secs] = s.split(':')
    total = int(mins) * 60 + int(secs)
    return total

def sorter(s):
    return seconds(s[1])

def main():
    d = {}
    for line in sys.stdin:
        try:
            tokens = line.split()
            d[tokens[0]] = min(tokens[1:], key=seconds)
        except ValueError:
            print('{:s} was disqualified for an invalid time.'.format(tokens[0]))

    best_result = min(d.items(), key=sorter)
    print('{:s} is the fastest runner with a time of {}.'.format(best_result[0], best_result[1]))

if __name__ == '__main__':
    main()
