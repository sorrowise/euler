# time cost = 421 ms ± 88.1 ms

from itertools import combinations

def is_valid(B,tup):
    L,S = tup
    if len(B) == L:
        return sum(B) != S
    else:
        return (sum(B)-S)*(len(B)-L)>0

def is_special_sumsets(s):
    arr = [(1,x) for x in sorted(s)]
    for r in range(2,len(s)):
        for i in combinations(sorted(s),r):
            for j in arr:
                if not is_valid(i,j):
                    return False
            arr.append((len(i),sum(i)))
    return True

def main(arr=[11,18,19,20,22,25],n=7):
    optimum = set(arr[len(arr)//2:] + sorted([x+y for x in arr for y in arr]))
    for i in combinations(optimum,n):
        if is_special_sumsets(i):
            return "".join([str(x) for x in i])
