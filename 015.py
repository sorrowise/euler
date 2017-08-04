# -*- coding: utf-8 -*-

def comb_num(n,k):
    fac = lambda n:reduce(lambda x,y:x*y,range(1,n+1))
    num = fac(n)/(fac(n-k)*fac(k))
    return num

def lattice_paths(n,k):
    return comb_num(n+k,k)

print lattice_paths(20,20)
