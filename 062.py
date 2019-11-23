# time cost = 1.65 s ± 7.11 ms

from itertools import count

perm = lambda x : "".join(sorted(str(x)))

def cubic_perm(res):
    for i in count(5,1):
        c = perm(i**3)
        if len([x for x in res if x==c]) == 5:
            return i**3

def main():
    res = [perm(i**3) for i in range(5,10001)]
    return cubic_perm(res)
