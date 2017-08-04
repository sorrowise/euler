# -*- coding: utf-8 -*-

arr = [x**2 for x in range(1,101)]
res = (sum(range(1,101)))**2 - sum(arr)
print res
