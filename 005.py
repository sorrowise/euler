# -*- coding: utf-8 -*-

from fractions import gcd

def lcm(numbers):
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers)

print lcm(range(1,21))
