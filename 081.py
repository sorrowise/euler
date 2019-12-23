# time cost = 8.01 ms

from functools import lru_cache

with open('data/ep81.txt') as f:
    table = [list(map(int,s.split(','))) for s in f.readlines()]

@lru_cache(maxsize=2048)
def min_path_sum(r,c):
    if r == 0 and c == 0:
        return table[0][0]
    elif r == 0 and c >= 1:
        return sum(table[r][:c+1])
    elif c == 0 and r >= 1:
        return sum(x[0] for x in table[:r+1])
    else:
        return table[r][c] + min(min_path_sum(r-1,c),min_path_sum(r,c-1))  

def main(N=80):
    return min_path_sum(N-1,N-1)
