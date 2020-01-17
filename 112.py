# time cost = 6.44 s ± 32.2 ms

from itertools import count

def is_bouncy_number(n):
    digits = [int(x) for x in str(n)]
    diff = [x-y for x,y in zip(digits[1:],digits[:-1])]
    if min(diff) < 0 and max(diff) > 0:
        return True
    else:
        return False

def main(pert=0.99):
    n = 0
    for i in count(100,1):
        if is_bouncy_number(i):
            n = n + 1
            if n/i >= pert:
                return i
