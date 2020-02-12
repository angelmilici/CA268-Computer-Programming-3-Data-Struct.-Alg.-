import sys
import math

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if dist == r1 + r2:
        return False
    if dist > r1 + r2:
        return False
    if dist < r1 + r2:
        return True
