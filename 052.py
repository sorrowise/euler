# time cost = 314 ms ± 5.06 ms

from itertools import count

def main():
    for x in count(10,1):
        if all(set(str(k*x))==set(str(x)) for k in range(6,1,-1)):
            return x
