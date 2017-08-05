# -*- coding: utf-8 -*-

def fib_digit(bound):
    x = 1
    y = 1
    n = 2
    fib = [1,1]
    while len(str(fib[-1])) < bound:
        x,y = y,x+y
        fib.append(y)
        n = n+1
    return n

print fib_digit(1000)
