# -*- coding: utf-8 -*-

import numpy as np

def num_of_terms(n):
    collatz = lambda n : 3*n+1 if n%2==1 else n//2
    num = 1
    while n !=1:
        n = collatz(n)
        num += 1
    return num

def max_start(n):
    terms_arr = np.array([num_of_terms(x) for x in range(1,n+1)])
    index = terms_arr.argmax() + 1
    return index

print max_start(1000000)
