# time cost = 2.27 s ± 11.3 ms

from collections import Counter
from itertools import count

def cubic_perm(res):
    for i in count(5,1):
        c = Counter(str(i**3))
        if len([x for x in res if x==c]) == 5:
            return i**3

def main():
    res = [Counter(str(i**3)) for i in range(5,10001)]
    return cubic_perm(res)
