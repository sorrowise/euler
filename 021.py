# -*- coding: utf-8 -*-

from math import sqrt

def divisors(n):
    divs = []
    for i in range(1,int(sqrt(n))+1):
        if n%i == 0:
            divs.append(i)
            divs.append(n/i)
    return list(set(divs))

sum_of_divs = lambda n : sum(divisors(n))-n

def amicable_num(n):
    arr = []
    for i in range(1,n+1):
        if sum_of_divs(sum_of_divs(i)) == i and sum_of_divs(i) !=i:
            arr.append(i)
    return arr   

print sum(amicable_num(10000))
