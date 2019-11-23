# time cost = 2.8 µs ± 29.8 ns

from math import log10

def main():
    c = 0
    for n in range(1,10):
        c += int(1/(1-log10(n)))
    return c
