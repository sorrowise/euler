# -*- coding: utf-8 -*-

def fibs_below(n,a=1,b=2):
    fib = [a,b]
    while True:
        a,b = b,a+b
        if b <= n:
            fib.append(b)
        else:
            return fib

print sum([x for x in fibs_below(4e6) if x%2==0])
