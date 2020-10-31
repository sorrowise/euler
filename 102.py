# time cost = 9.9 ms ± 310 µs

def area_of_triangle(xa,ya,xb,yb,xc,yc):
    area = abs((xa-xc)*(yb-ya)-(xa-xb)*(yc-ya)) / 2
    return area

def main():
    counter = 0
    with open('ep102.txt') as f:
        coords = [x.strip().split(',') for x in f.readlines()]
        for coord in coords:
            xa,ya,xb,yb,xc,yc = [int(x) for x in coord]
            abc = area_of_triangle(xa,ya,xb,yb,xc,yc)
            aob = area_of_triangle(xa,ya,0,0,xb,yb)
            aoc = area_of_triangle(xa,ya,0,0,xc,yc)
            boc = area_of_triangle(xb,yb,0,0,xc,yc)
            if abc == aob + aoc + boc:
                counter += 1
    return counter
