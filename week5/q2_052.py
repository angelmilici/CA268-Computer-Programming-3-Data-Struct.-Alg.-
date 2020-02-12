import sys

def matches(w, str_aeiou):
    return [c for c in w if c in str_aeiou] == list(str_aeiou)

def main():
    words = [line.strip() for line in sys.stdin]
    aeiou_words = [w for w in words if matches(w.lower(), 'aeiou')]
    for w in aeiou_words:
        print(w)

if __name__ == '__main__':
    main()
