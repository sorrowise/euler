from functools import reduce
from operator import add,mul

def main():
    res_str = reduce(add,[str(x) for x in range(1,190000)])
    power = [10**x for x in range(7)]
    return reduce(mul,[int(res_str[i-1]) for i in power])

'''
Timer unit: 5.68829e-07 s

Total time: 3.93698 s
File: <ipython-input-18-69ecdce8ac3e>
Function: main at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           def main():
     5         1      6921134 6921134.0    100.0      res_str = reduce(add,[str(x) for x in range(1,190000)])
     6         1           40     40.0      0.0       power = [10**x for x in range(7)]
     7         1           25     25.0      0.0       return reduce(mul,[int(res_str[i-1]) for i in power])
'''
