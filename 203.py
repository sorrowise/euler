# time cost = 465 µs ± 3.78 µs

def main(n=51):
    squares = [4,9,25,49]
    res = set()
    pt = [1,1]
    for r in range(n-2):
        pt = [x+y for x,y in zip(pt+[0],[0]+pt)]
        for comb in pt[:(r+3)//2+2]:
            if all([comb%s for s in squares]) != 0:
                res.add(comb)
    return sum(res)
