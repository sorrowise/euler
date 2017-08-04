# -*- coding: utf-8 -*-

large_sum = 0
f = open("euler/ep13.txt")
for line in f.readlines():
    large_sum += int(line)
print str(large_sum)[:10]
