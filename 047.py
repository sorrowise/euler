# time cost = 2.07 s ± 3.09 ms

from sympy import primefactors,nextprime

def first_int(arr):
    f = lambda x : len(primefactors(x))
    for i in range(len(arr)-3):
        if f(arr[i])==4 and f(arr[i+1])==4 and f(arr[i+2])==4 and f(arr[i+3])==4:
            return arr[i]
    return False

def main():
    p = 211
    while True:
        nextp = nextprime(p)
        if (nextp - p) > 4:
            ans = first_int(range(p+1,nextp))
            if ans != False:
                return ans
        p = nextp
