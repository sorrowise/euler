# -*- coding: utf-8 -*-

from math import sqrt

def num_of_divisor(n):
    if n == 1:
        return 1
    else:
        up_bound = int(sqrt(n)) + 1
        num = 0
        for i in range(1,up_bound):
            if n%i == 0:
                num = num + 1
        return (2*num) - (1 if (up_bound-1)**2 == n else 0)

def numd_of_triangle():
    n = 7
    while True:
        triangle = n*(n+1)//2
        num_d = num_of_divisor(triangle)
        if num_d <= 500:
            n = n + 1
        else:
            return triangle

print numd_of_triangle()
