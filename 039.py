max_p = 2
max_num = 0
for p in range(2,1001,2):
    num = 0
    for a in range(1,p//3):
        if (p**2-2*p*a)%(2*p-2*a) == 0:
            num += 1
    if num > max_num:
        max_p = p
        max_num = num
print(max_p)
