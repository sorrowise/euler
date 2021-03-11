# time cost = 12.8 µs ± 176 ns

def main():
    c = 1504170715041707
    nc = 8912517754604
    res = c + nc
    while nc > 0:
        c,nc = nc,(-c)%nc
        res += nc
    return res
