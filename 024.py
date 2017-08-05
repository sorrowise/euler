# -*- coding: utf-8 -*-

from math import factorial, floor

def kthperm(S, kth):
    P = []
    k = kth - 1
    S = list(S)
    while S != []:
        f = factorial(len(S)-1)
        i = int(floor(k/f))
        x = S[i]
        k = k%f
        P.append(x)
        S.remove(x)
    return int(reduce(lambda x,y:x+y,P,''))

S = '0123456789'
print kthperm(S,1000000)
