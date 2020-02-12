import sys
import string

def main():
    word = {}
    for line in sys.stdin.read():
        line = line.lower()

        if line in 'aeiou':
            word[line] = word[line] + 1 if line in word else 1

    largest = None
    for line, freq in sorted(word.items(), key=lambda x: x[1], reverse=True):
        if largest is None:
            largest = len(str(freq))

        print('{} : {:{:d}d}'.format(line, freq, largest))

if __name__ == '__main__':
    main()
