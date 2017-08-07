# -*- coding: utf-8 -*-

r = range(2,101)
print len({a**b for a in r for b in r})
