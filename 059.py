# time cost = 668 µs ± 3.63 µs

from collections import Counter

def main():
    with open('data/ep59.txt') as f:
        cipher = list(map(int,f.read().split(',')))
    space_ascii = ord(' ')
    key = [Counter(cipher[i::3]).most_common(1)[0][0] ^ space_ascii for i in range(3)]
    cycles = len(cipher)//3
    res = sum([x^y for x,y in zip(cipher,key*cycles)])
    return res
