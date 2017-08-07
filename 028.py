# -*- coding: utf-8 -*-

f1 = lambda n : n**2-n+1
f2 = lambda n : 4*n**2 + 1
f3 = lambda n : (2*n+1)**2
upleft_downright = sum([f1(x) for x in range(1,1002)])
upright = sum([f3(x) for x in range(1,501)])
downleft = sum([f2(x) for x in range(1,501)])
print (upleft_downright + upright + downleft)
