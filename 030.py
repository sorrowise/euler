# -*- coding: utf-8 -*-

def is_equal(num,n=5):
    res = [(int(x))**n for x in str(num)]
    return num == sum(res)

def digit_powers():
    ub = 6*(9**5)
    res = [x for x in range(1000,ub) if is_equal(x)]
    return res

print sum(res)
