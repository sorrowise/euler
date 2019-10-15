# time cost = 5.29 s ± 7.2 ms

from itertools import permutations

def main():
    res,ans = [],0
    for i in permutations(range(10),10):
        d_by_three = (i[2]+i[3]+i[4])%3==0
        d_by_seven = (10*i[4]+i[5]-i[6]*2)%7==0
        d_by_eleven = (i[5]-i[6]+i[7])%11==0
        d_by_thirteen = (100*i[6]+10*i[7]+i[8])%13==0
        d_by_seventeen = (100*i[7]+10*i[8]+i[9])%17==0
        cond = d_by_three and d_by_seven and d_by_eleven and d_by_thirteen and d_by_seventeen
        if i[0]!=0 and i[5]==5 and i[3]%2==0 and cond:
            ans += sum([x*10**y for x,y in zip(i,range(9,-1,-1))])
    return ans
