# -*- coding: utf-8 -*-

with open('euler/ep11.txt','r') as f:
    data = [map(int, s.split()) for s in f.readlines()]

def grid_largest_prod(data):
    import numpy as np
    length = len(data)
    res = np.zeros((length,length))
    right = down = down_right = left_down = 0
    for i in range(length):
        for j in range(length):
            right_exist = all([x<length for x in [i,i+1,i+2,i+3]])
            down_exist = all([x<length for x in [j,j+1,j+2,j+3]])
            left_exist = all([x>=0 for x in [i,i-1,i-2,i-3]])
            if right_exist:
                right = data[i][j]*data[i+1][j]*data[i+2][j]*data[i+3][j]
            if down_exist:
                down = data[i][j]*data[i][j+1]*data[i][j+2]*data[i][j+3]
            if right_exist and down_exist:
                down_right = data[i][j]*data[i+1][j+2]*data[i+2][j+2]*data[i+3][j+3]
            if left_exist and down_exist:
                left_down = data[i][j]*data[i-1][j+1]*data[i-2][j+2]*data[i-3][j+3]
            res[i][j] = max(right,down,down_right,left_down)
    max_res = np.max(res)
    return max_res

print grid_largest_prod(data)
