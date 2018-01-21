# ans = 73162890, time cost = 288 µs 

from functools import reduce
from operator import add

data = []
with open("euler/ep79.txt") as f:
    for line in f.readlines():
        data.append(int(line))

def after_num(x,i):
    after = x[x.find(str(i))+1:]
    if len(after) == 2:
        return list((after[0],after[1]))
    else:
        return list(after)   

def main():
    nums = [0,1,2,3,6,7,8,9]
    after_length = {}
    for i in nums:
        lst = [str(x) for x in set(data) if str(i) in str(x)]
        afters = set(reduce(add,[after_num(x,i) for x in lst]))
        after_length.update({i:len(afters)})
    res = sorted(after_length.items(),key=lambda x:x[1],reverse=True)
    return reduce(add,[str(x[0]) for x in res])
