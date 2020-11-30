# time cost = 3.28 ms ± 59.5 µs

from math import gcd

def main(N=50):
    count = 0
    for x in range(1,N+1):
        for y in range(1,N+1):
            g = gcd(x,y)
            low = max(-g*x/y,(y-N)*g/x)
            up = min(g*(N-x)/y,g*y/x)
            count += (int(up)-int(low))
    return count + 3*50**2
