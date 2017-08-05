# -*- coding: utf-8 -*-

def abundants(n):
    res = []
    for i in range(1,n+1):
        if sum_of_divs(i) > i:
            res.append(i)
    return res

up_bound = 28123
arr = brr = abundants(up_bound)
all_divs = list(set([x+y for x in arr for y in brr if (x+y)<up_bound]))
res = sum(range(1,up_bound))-sum(all_divs)
print res
