#!/usr/bin/env python

import sys
import string

def palindrome(s):
    for i in s:
        
        if i in string.punctuation:
            s = s.replace(i, ' ')
    return s.strip()
    if s.strip() == s[::-1].strip():
        return True
    else:
        return False



def main():
    for line in sys.stdin:
        line = line.lower().strip()
        print(palindrome(line))




if __name__ == '__main__':
    main()
