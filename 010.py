# -*- coding: utf-8 -*-

from sympy import sieve
print sum(list(sieve.primerange(1,2e6)))
