# time cost = 194 µs ± 1.03 µs

from itertools import count

def main(N=2*10**6):
    for dist in count(1,1):
        c1,c2 = N-dist,N+dist
        limit = int(((8*c2**0.5+1)**0.5-1)/2) + 1
        for y in range(1,limit):
            t = y*(y+1)
            x1 = (-t+(t**2+16*c1*t)**0.5)/(2*t)
            x2 = (-t+(t**2+16*c2*t)**0.5)/(2*t)
            if x1.is_integer():
                return x1 * y
            if x2.is_integer():
                return x2 * y
