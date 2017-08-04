# -*- coding: utf-8 -*-

def max_prime_factor(n):
    i = 2
    while i * i < n:
        while n%i == 0:
            n /= i
        i += 2 if i>2 else 1
    return n

print max_prime_factor(600851475143)
