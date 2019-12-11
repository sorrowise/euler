# time cost = 487 ms ± 2.44 ms

DT = {169:3,363601:3,1454:3,871:2,45361:2,872:2,45362:2,69:5,78:4,540:2}

def digit_fact_sum(x):
    fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    res = sum([fac[int(i)] for i in str(x)])
    return res

def chain_length(n):
    arr,m = [],n
    global DT
    while True:
        if n in DT:
            length = len(arr) + DT[n]
            break
        elif n in arr:
            length = len(arr)
            break
        else:
            arr.append(n)
            n = digit_fact_sum(n)
    DT[m] = length
    return length

def main(N=10**6):
    c = 0
    for i in range(1,N):
        if chain_length(i) == 60:
            c += 1
    return c
