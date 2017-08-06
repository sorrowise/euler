# -*- coding: utf-8 -*-

def repeat_num(n):
    rem = [1]
    while True:
        rem.append(10*rem[-1]%n)
        if rem[-1] == 0:
            return 0
        elif rem[-1] in rem[:-1]:
            return (len(rem)-1-rem.index(rem[-1]))

reps = [repeat_num(x) for x in range(1,1001)]
max_rep = reps.index(max(reps)) + 1
print max_rep
