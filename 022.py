# -*- coding: utf-8 -*-

with open('euler/ep22.txt','r') as f:
    data = f.read().replace('"',"").split(',')

def alphabet(word):
    alpha = lambda s : ord(s) - ord('A') + 1
    res = sum([alpha(x) for x in word])
    return res

def sum_name_score(data):
    name_score = lambda word : alphabet(word) * (sorted(data).index(word)+1)
    res = sum([name_score(word) for word in data])
    return res
