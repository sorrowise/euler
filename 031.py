# -*- coding: utf-8 -*-

import numpy as np
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = len(coins)

def coin_ways(target):
    x = np.ones((target,ways))
    for i in range(1,target):
        for j in range(1,ways):
            index = i+1-coins[j]
            res = x[index-1,j] if (index>=0) else 0
            x[i,j] = x[i,j-1] + res
    return x[target-1,ways-1]

print coin_ways(200)
