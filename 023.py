# time cost = 798 ms ± 1.93 ms

def sigma(n):
    res = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            res += (i + n//i) if i**2 != n else i
    return res-n

def main():
    limit = 28123
    res,abn = 0,set()
    for i in range(1,limit+1):
        if sigma(i)>i:
            abn.add(i)
        if not any((i-x in abn) for x in abn):
            res += i
    return res
