#!usr/bin/env python

import sys

def main():
    linelist = []
    for line in sys.stdin:
        linelist.append(line.strip())

    print("Words containing 17 letters:", [c for c in linelist if len(c) == 17])
    print("Words containing 18+ letters:", [c for c in linelist if len(c) > 17])
    vowels = set('aeiou')
    print("Shortest word containing all vowels:", min([c for c in linelist if vowels.issubset(c.lower())], key=len))
    print("Words with 4 a's:", [c for c in linelist if c.lower().count('a') == 4])
    print("Words with 2+ q's:", [c for c in linelist if c.lower().count('q') >= 2])
    print("Words containing cie:", [c for c in linelist if 'cie' in c.lower()])
    print("Anagrams of angle:", [c for c in linelist if sorted(c.lower()) == sorted('angle') and c.lower() != 'angle'])
    print("Words ending in iary:", len([c for c in linelist if c.lower()[-4:] == 'iary']))
    max_count = max([c.count('e') for c in linelist if c.lower().__contains__('e')])
    print("Words with most e's:", [c for c in linelist if c.lower().count('e') == max_count])

if __name__ == '__main__':
    main()
