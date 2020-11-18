# time cost = 15.3 ms ± 102 µs

import numpy as np

def minimal_path_sum(matrix):
    n = len(matrix)
    mat = np.array(matrix)
    cost = mat.cumsum(axis=1)
    for j in range(1,n):
        for i in range(1,n):
                cost[i,j] = mat[i,j] + min(cost[i,j-1],cost[i-1,j])
        for i in range(n-2,-1,-1):
                cost[i,j] = min(cost[i,j],cost[i+1,j]+mat[i,j])
    return min(cost[:,-1])

def main():
    with open('data/pe082.txt') as f:
        matrix = [[int(x) for x in row.split(',')] for row in f.readlines()]
    return minimal_path_sum(matrix)
