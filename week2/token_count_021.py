#!/usr/bin/env python

import sys

tokens = ['--', '--', '--', '--', '--', '--', '--', '1863', '19,', 'Abraham', 'But,', 'Four', 'God,', 'It', 'It', 'It', 'Liberty,', 'Lincoln', 'November', 'Now', 'The', 'The', 'We', 'We', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'above', 'add', 'advanced.', 'ago', 'all', 'altogether', 'and', 'and', 'and', 'and', 'and', 'and', 'any', 'are', 'are', 'are', 'as', 'battle-field', 'be', 'be', 'before', 'birth', 'brave', 'brought', 'but', 'by', 'can', 'can', 'can', 'can', 'can', 'cause', 'civil', 'come', 'conceived', 'conceived', 'consecrate', 'consecrated', 'continent,', 'created', 'dead', 'dead', 'dead,', 'dedicate', 'dedicate', 'dedicated', 'dedicated', 'dedicated', 'dedicated,', 'detract.', 'devotion', 'devotion', 'did', 'died', 'do', 'earth.', 'endure.', 'engaged', 'equal.', 'far', 'far', 'fathers', 'field,', 'final', 'fitting', 'for', 'for', 'for', 'for', 'for', 'forget', 'forth', 'fought', 'freedom', 'from', 'from', 'full', 'gave', 'gave', 'government', 'great', 'great', 'great', 'ground.', 'hallow', 'have', 'have', 'have', 'have', 'have', 'here', 'here', 'here', 'here', 'here', 'here,', 'here,', 'here.', 'highly', 'honored', 'in', 'in', 'in', 'in', 'increased', 'is', 'is', 'is', 'it', 'it,', 'larger', 'last', 'little', 'live.', 'lives', 'living', 'living,', 'long', 'long', 'measure', 'men', 'men,', 'met', 'might', 'nation', 'nation', 'nation,', 'nation,', 'nation,', 'never', 'new', 'new', 'nobly', 'nor', 'not', 'not', 'not', 'not', 'not', 'note,', 'of', 'of', 'of', 'of', 'of', 'on', 'on', 'or', 'or', 'our', 'our', 'people,', 'people,', 'people,', 'perish', 'place', 'poor', 'portion', 'power', 'proper', 'proposition', 'rather', 'rather,', 'remaining', 'remember', 'resolve', 'resting', 'say', 'score', 'sense,', 'seven', 'shall', 'shall', 'shall', 'should', 'so', 'so', 'so', 'struggled', 'take', 'task', 'testing', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'their', 'these', 'these', 'they', 'they', 'they', 'this', 'this', 'this', 'this.', 'those', 'thus', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'under', 'unfinished', 'us', 'us', 'us', 'vain', 'war,', 'war.', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'what', 'what', 'whether', 'which', 'which', 'who', 'who', 'who', 'will', 'work', 'world', 'years']

def counter(s):
    return tokens[7]

def main():
    for line in sys.stdin:
        line = line.strip()
        print(counter(line))



if __name__ == '__main__':
    main()
