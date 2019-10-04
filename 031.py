# time cost = 1.82 ms ± 19.9 µs

def main(target=200):
    import numpy as np
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    x = np.ones((target,len(coins)))
    for i in range(1,target):
        for j in range(1,len(coins)):
            left = x[i][j-1]
            up = x[i-coins[j]][j] if (i+1-coins[j])>=0 else 0
            x[i][j] = left + up
    return int(x[-1,-1])
