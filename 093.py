# time cost = 22.4 s ± 26.2 ms

from itertools import permutations,product,count
from fractions import Fraction

def eval_arith_expression(dp,op):
    arr = []
    expr = (dp[0],op[0],dp[1],op[1],dp[2],op[2],dp[3])
    s1 = "%d%s%d%s%d%s%d" % expr
    s2 = "(%d%s%d)%s(%d%s%d)" % expr
    s3 = "(%d%s(%d%s%d))%s%d" % expr
    s4 = "%d%s((%d%s%d)%s%d)" % expr
    s5 = "%d%s(%d%s(%d%s%d))" % expr
    for s in [s1,s2,s3,s4,s5]:
        try:
            arr.append(eval(s))
        except ZeroDivisionError:
            pass
    return arr

def consecutive_integers_number(integers):
    c = 0
    numbers = []
    digits = [Fraction(x,1) for x in integers]
    operators = list(product(["+","-","*","/"],repeat=3))
    digits_perm = list(permutations(digits,4))
    for dp in digits_perm:
        for op in operators:
            numbers += eval_arith_expression(dp,op)
    targets = {x for x in set(numbers) if x>0 and x%1==0}
    for i in count(1):
        if i in targets:
            c += 1
        else:
            return c

def main():
    d = {}
    perm = [x for x in permutations(range(10),4) if x[0]<x[1]<x[2]<x[3]]
    for p in perm:
        d[tuple(p)] = consecutive_integers_number(p)
    res = max(d,key=d.get)
    return "".join([str(x) for x in res])
