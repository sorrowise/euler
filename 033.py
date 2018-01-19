# ans = 100, time cost = 33.7 µs

from math import gcd

def main():
    nom,den = 1,1
    for i in range(1,10):
        for d in range(1,i):
            for n in range(1,d):
                if d*(10*n+i) == n*(10*i+d):
                    nom *= n
                    den *= d
    return den//gcd(nom,den)
