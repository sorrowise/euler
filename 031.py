# top-down method, time cost = 88.6 ns ± 0.468 ns

from functools import lru_cache

@lru_cache(maxsize=128)
def ways(x,y=8):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    if x == 1 or y == 1:
        return 1
    elif x < coins[y-1]:
        return ways(x,y-1)
    else:
        return ways(x,y-1) + ways(x-coins[y-1],y)

# bottom up method, time cost = 221 µs ± 686 ns

def dp(target=200):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    d = {i:1 for i in range(target+1)}
    for j in range(1,len(coins)):
        for i in range(coins[j],target+1):
            d[i] = d[i] + d[i-coins[j]]
    return d[target] 
