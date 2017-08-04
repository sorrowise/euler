# -*- coding: utf-8 -*-

fac = lambda n:reduce(lambda x,y:x*y,range(1,n+1))
print sum([int(x) for x in str(fac(100))])
