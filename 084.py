# time cost = 3.52 ms ± 9.31 µs

import numpy as np

def get_dice_mat():
    n,s = 40,4
    freq = {2:1,3:2,4:3,5:4,6:3,7:2,8:1}
    prob = {k:v/s**2 for k,v in freq.items()}
    mat = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            mat[i,j] = prob.get((j-i)%40,0)
    return mat

def get_card_mat():
    n = 40
    card_mat = np.zeros((n,n))
    for i in range(n):
        if i in [2,17,33]:
            card_mat[i,0] = 0.0625
            card_mat[i,i] = 0.875
            card_mat[i,10] = 0.0625
        elif i == 30:
            card_mat[i,10] = 1
        elif i == 7:
            card_mat[i,i] = 0.375
            card_mat[i,15] = 0.125
            for j in [0,4,5,10,11,12,24,39]:
                card_mat[i,j] = 0.0625
        elif i == 22:
            card_mat[i,i] = 0.375
            card_mat[i,25] = 0.125
            for j in [0,5,10,11,19,24,28,39]:
                card_mat[i,j] = 0.0625  
        elif i == 36:
            card_mat[i,i] = 0.375
            card_mat[i,5] = 0.1875
            for j in [0,10,11,12,24,33,39]:
                card_mat[i,j] = 0.0625
        else:
            card_mat[i,i] = 1.0
    return card_mat 

def get_steady_vector():
    C = get_card_mat()
    D = get_dice_mat()
    T = D @ C
    vec_i = np.array([1]+[0]*39)                                 
    while True:
        vec_s = vec_i @ T
        if np.array_equal(vec_s,vec_i):
            return vec_s
        else:
            vec_i = vec_s    

def main(n=3):
    v = get_steady_vector()
    rank = (-v).argsort()[:n]
    return "".join([str(x) for x in rank])
