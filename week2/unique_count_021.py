#!/usr/bin/env python

import sys
from string import punctuation

print(len(set(''.join(x for x in sys.stdin.read().lower()if x not in __import__('string').punctuation).split())))




