# ans = 134043, time cost = 5.08 s

from sympy.ntheory import factorint

def main():
    start = 646
    while True:
        lst = [start+i for i in range(4)]
        factor_num = [len(factorint(x)) for x in lst]
        if all(x==4 for x in factor_num):
            return start
        start += 1
