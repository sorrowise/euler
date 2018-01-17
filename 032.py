def is_pandgit(x):
    pandgit_set = {int(x) for x in str(x)}
    if pandgit_set == set(range(1,len(str(x))+1)):
        return True
    return False

res = set()
for a in range(1,100):
    start = 1234 if a <=9 else 123
    for b in range(start,10000//a):
        prod = a * b
        total_num = int(str(a) + str(b) + str(prod))
        if is_pandgit(total_num):
            res.add(prod)
print(sum(res))
