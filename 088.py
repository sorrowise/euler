# time cost = 163 ms ± 1.13 ms

def main():
    
    def update_min_n_arr(p,s,f,start):
        k = p - s + f
        if k < 12001:
            min_n_arr[k] = min(min_n_arr[k],p)
            for i in range(start,12000//p*2):
                update_min_n_arr(p*i,s+i,f+1,i)
    
    min_n_arr = [24000]*12001
    update_min_n_arr(1,1,1,2)
    return sum(set(min_n_arr[2:]))
