# time cost = 1.51 ms ± 24.9 µs

from math import log10

def main():
    with open('data/ep99.txt') as f:
        pairs = [list(map(int,s.split(','))) for s in f.readlines()]
    log_pairs = [x[1]*log10(x[0]) for x in pairs]
    return log_pairs.index(max(log_pairs))+1
