import sys
import string

def main():
    word = {}
    for line in sys.stdin.read().split():
        line = line.lower().strip(string.punctuation)
        word[line] = word[line] + 1 if line in word and len(line) > 3 else 1

    for line, freq in sorted(word.items()):
        if freq > 2:
            print('{:>{:d}s}'.format(line, 9) + ' : ' + '{:{:d}d}'.format(freq, 2))

if __name__ == '__main__':
    main()
