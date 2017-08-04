# -*- coding: utf-8 -*-

from math import sqrt

def find_pytha():
    upBoundary = int(sqrt(500)) + 1
    for i in range(upBoundary,1,-1):
        if 500%i == 0:
            n = 500/i - i
            if i > n:
                return i,n

i,n = find_pytha()
a = i**2 + n**2
b = 2*i*n
c = i**2 - n**2
print a*b*c
