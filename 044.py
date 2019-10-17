# time cost = 1.55 s ± 10.6 ms

from math import sqrt

def is_pantagon(x):
    if (sqrt(24*x+1)+1) % 6 == 0:
        return True
    return False

def main():
    pantagon = lambda n : n*(3*n-1)/2
    pt = [pantagon(n) for n in range(1,2000)]
    for i in range(1,2000):
        for j in range(0,i):
            s1,s2 = pt[i] + 2*pt[j], 2*pt[i] + pt[j]
            pk = pt[i] + pt[j]
            if is_pantagon(pk):
                if is_pantagon(s1):
                    return pt[i]
                if is_pantagon(s2):
                    return pt[j]
