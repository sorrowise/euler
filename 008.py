# -*- coding: utf-8 -*-

data = ''
f = open("euler/ep08.txt")
for line in f.readlines():
    data = data + line.strip()

res = []
for i in range(988):
    sub = [int(x) for x in data[i:i+13]]
    prod = reduce(lambda x,y:x*y, sub)
    res.append(prod)

print max(res)
