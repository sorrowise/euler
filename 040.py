from functools import reduce
from operator import add,mul

def main():
    res_str = reduce(add,[str(x) for x in range(1,190000)])
    power = [10**x for x in range(7)]
    return reduce(mul,[int(res_str[i-1]) for i in power])
