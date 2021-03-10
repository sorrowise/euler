# time cost = 428 ms ± 4.64 ms

from numba import njit

@njit
def nth_start_with(target=123,N=678910):
    n,power,k = 0,2,1
    while n<N:
        power = power * 2
        while power >= 10**3:
            power = power / 10.0
        if int(power) == target:
            n = n + 1
        k = k + 1
    return k
