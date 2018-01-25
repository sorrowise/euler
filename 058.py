# ans = 26241, time cost = 3.69s

from sympy.ntheory import isprime

def repeat(u):
    a = []
    b = [1]*4
    for i in range(1,u):
        lst = [x*2*i for x in b]
        a = a + lst
    return a

def corner_nums(side_length):
    repeat_num = (side_length-1)//2
    lst = [1] * (4*repeat_num+1)
    r = repeat(repeat_num+1)
    for i in range(1,4*repeat_num+1):
        lst[i] = lst[i-1] + r[i-1]
    return lst

def main():
    start = 26239
    lst = corner_nums(start)
    prev = len([x for x in lst if isprime(x)])
    while True:
        ratio = prev/len(lst)
        if ratio<0.1:
            return start
        else:
            start += 2
            new = corner_nums(start)[-4:]
            prev = prev + len([x for x in new if isprime(x)])
            lst = lst + new

print(main())
