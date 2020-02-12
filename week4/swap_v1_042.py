import sys

def swap_keys_values(d):
    new_d = {}
    for x, y in d.items():
        new_d[y] = x

    return new_d
