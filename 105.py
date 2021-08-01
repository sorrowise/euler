# time cost = 13.7 s ± 736 ms

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

def main():
    res = 0
    with open('data/pe105.txt') as f:
        sets = [[int(x) for x in row.strip().split(',')] for row in f.readlines()]
    for s in sets:
        if is_special_sumsets(s):
            res += sum(s)
    return res
