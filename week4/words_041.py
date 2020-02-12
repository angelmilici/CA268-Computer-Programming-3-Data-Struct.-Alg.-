import sys
import string

def main():
    word = {}
    for line in sys.stdin.read().split():
        line = line.lower().strip(string.punctuation)
        word[line] = word[line] + 1 if line in word else 1

    for line, freq in sorted(word.items()):
        print(line + ' : ' + str(freq))

if __name__ == '__main__':
    main()
