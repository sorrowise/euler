# time cost = 1.95 ms ± 12.1 µs

from functools import lru_cache
from math import log10

def is_happy(n):

    cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    while n != 1 and n not in cycle_members:
        n = get_next(n)

    return n == 1

@lru_cache(maxsize=None)
def f(n,k):
    if n == k == 0:
        return 1
    elif n < 0:
        return 0
    elif n > 0 and k ==0:
        return 0
    else:
        return sum([f(n-i**2,k-1) for i in range(10)])

def main(N=10**7):
    power = int(log10(N))
    u = 9**2*power
    happy_numbers = [i for i in range(1,u+1) if is_happy(i)]
    ways = sum([f(x,power) for x in happy_numbers])
    return (N - ways - 1)
