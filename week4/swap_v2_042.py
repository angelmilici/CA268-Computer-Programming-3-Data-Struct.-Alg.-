import sys

def swap_unique_keys_values(d):
    new_d = {}
    sets = set()
    for x, y in d.items():
        if y in new_d:
            sets.update([y])
            del new_d[y]
        elif y not in sets:
            new_d[y] = x
    return new_d

def main():
    dicti = {'a': 1, 'b': 2, 'c': 2}
    print(swap_unique_keys_values(dicti))

if __name__ == '__main__':
    main()
