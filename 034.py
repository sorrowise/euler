from math import factorial
fac_list = [factorial(n) for n in range(10)]
res = 0
for i in range(10,2177282):
    if sum([fac_list[int(x)] for x in str(i)]) == i:
        res += i
print(res)
