# time cost = 3.85 s ± 3.71 ms

def main(N=10**6):
    c,length = 0,2
    while c < N:
        length = length + 1
        for wph in range(3,2*length):
            sq = (length**2 + wph**2)**0.5
            if sq % 1 == 0:
                c += (wph//2) if length>wph else (length-(wph+1)//2+1)
    return length  
