with open('data/ep18.txt') as f:
    table = [list(map(int,s.split())) for s in f.readlines()]

# approach 1: bottom-up method, time cost = 62.1 µs ± 5.71 µs

def main():
    for row in range(len(table)-1, 0, -1):
        for col in range(0, row):
            table[row-1][col] += max(table[row][col], table[row][col+1])
    return table[0][0]

# approach 2: top-down method, time cost = 131 ns ± 8.97 ns

from functools import lru_cache

@lru_cache(maxsize=128)
def mps(r=0,c=0):
    if r == len(table)-2:
        return table[r][c] + max(table[r+1][c],table[r+1][c+1])
    else:
        return table[r][c] + max(mps(r+1,c),mps(r+1,c+1))
