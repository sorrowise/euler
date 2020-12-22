# time cost = 153 ms ± 1.19 ms

def main(n=10**5,k=10**4):
    arr = [[1,i] for i in range(n+1)]
    for i in range(2,n+1):
        if arr[i][0] == 1:
            for j in range(i,n+1,i):
                arr[j][0] *= i
    return sorted(arr)[k][1]
