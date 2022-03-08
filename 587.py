# time cost = 2.92 ms ± 98.5 µs

from math import sqrt,asin,pi    

def t(n):
    res = (n**2+n-sqrt(2)*n**1.5)/(n**2+1)
    return res

def area(t,n):
    res = 1/(2*n) - asin(1-t)/2 + (1-t)*(1-1/n)/2
    return res

def main(N=0.001):
    i = 100
    while True:
        if area(t(i),i)/(1-pi/4) < N:
            return i
        else:
            i = i + 1
