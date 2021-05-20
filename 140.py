# time cost = 8.72 ms ± 64.4 µs

import numpy as np
from sympy.solvers.diophantine.diophantine import diop_DN

def pelleq_solution_generator(d,n):
    u,v = diop_DN(d,1)[0]
    uv_zero = np.mat([[u],[v]])
    uv_mat = np.mat([[u,d*v],[v,u]])
    xy_mat = [np.mat([[x,d*y],[y,x]]) for x,y in diop_DN(d,n)]
    new_mat = np.identity(2,dtype=int)
    while True:
        yield [np.abs(x @ new_mat @ uv_zero) for x in xy_mat]
        new_mat = new_mat @ uv_mat

def main(N=30):
    arr = [2]
    for sol in pelleq_solution_generator(5,44):
        for ans in sol:
            if ans[0,0] % 5 == 2:
                arr.append((ans[0,0]-7)//5)
                if len(arr) == N:
                    return sum(arr)
