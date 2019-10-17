# time cost = 18.1 ms ± 30.1 µs

from math import sqrt

def is_pantagon(x):
    if (sqrt(24*x+1)+1) % 6 == 0:
        return True
    return False

def main():
    i = 144
    while True:
        h = i*(2*i-1)
        if is_pantagon(h):
            return h
        else:
            i += 1
