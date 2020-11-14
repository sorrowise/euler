# time cost = 2.79 s ± 10.9 ms

from itertools import count

def is_bouncy_number(n):
    sort = sorted(str(n))
    lst = list(str(n))
    if sort == lst or sort == lst[::-1]:
        return False
    else:
        return True

def main(pert=0.99):
    n = 0
    for i in count(100,1):
        if is_bouncy_number(i):
            n = n + 1
            if n/i >= pert:
                return i
