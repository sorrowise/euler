from sympy import sieve

def euler_phi_sieve(n):
    arr = list(range(n+1))
    for i in range(2,n+1):
        if arr[i] == i:
            for j in range(i,n+1,i):
                arr[j] -= arr[j]//i
    return arr

def phi(m,n,premob):
    res = 0
    for i in range(1,n+1):
        if m % i == 0:
            res += (premob[i-1]*(n//i))
    return res

def main(N=3141592653589793):
    res = 0
    u = int((N/2)**0.5)+1
    prephi = euler_phi_sieve(u)
    premob = list(sieve.mobiusrange(1,u))
    for m in range(2,u):
        if m % 2 == 0:
            res += prephi[m]
        else:
            res += phi(m,m//2,premob)
    for m in range(u,int(N**0.5)+1):
        v = int((N-m**2)**0.5)
        if m % 2 == 0:
            res += phi(m,v,premob)
        else:
            res += phi(m,v//2,premob)
    return res
