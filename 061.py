# time cost = 34.6 ms ± 635 µs

class Poly:
    def __init__(self,s,n):
        self.s = s
        self.n = n
        self.v = (self.n**2*(self.s-2)-self.n*(self.s-4))//2
        self.ftd = self.v // 100
        self.ltd = self.v % 100

        
def fig_num_dict():
    res,d = [],{}
    
    for s in range(3,9):
        for n in range(19,141):
            num = Poly(s,n)
            if 999 < num.v < 10000:
                res.append(num)
    
    for x in res:
        arr = []
        for y in res:
            if x.s != y.s and x.ltd == y.ftd:
                arr.append((y.s,y.v))
        d[(x.s,x.v)] = arr
    
    return d


def main():
    d = fig_num_dict()
    
    def find_next(types,data):
        if len(types) == 6 and (data[0]//100 == data[-1]%100):
            print(sum(data))
        else:
            for t,n in d.get((types[-1],data[-1]),[]):
                if t not in types:
                    find_next(types+[t],data+[n])
    
    for k,v in d:
        find_next([k],[v])
