#!usr/bin/env python

import sys
import string

linelist = []
for line in sys.stdin:
    linelist.append(line.strip())

print('Words with q but no u:', [c for c in linelist if 'qu' not in c.lower() and "q'u" not in c.lower()])
