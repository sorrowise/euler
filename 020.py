# time cost = 27.2 µs ± 149 ns

from math import factorial as fac

def main():
    ans = sum(map(int,str(fac(100))))
    return ans
