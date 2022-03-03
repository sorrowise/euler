# time cost = 764 ms ± 12.5 ms


from math import sqrt,gcd
from itertools import combinations
from functools import reduce


def cods(a,b,r):
    x = ((a+b)**2+(r+a)**2-(r+b)**2)/(2*a+2*b)
    y = sqrt((a+r)**2-x**2)
    return x,y

def inner_point(a,b,c):
    xa,ya = 0,0
    xb,yb = a+b,0
    xc,yc = cods(a,b,c)
    x = ((b+c)*xa+(a+c)*xb+(a+b)*xc)/(2*(a+b+c))
    y = ((b+c)*ya+(a+c)*yb+(a+b)*yc)/(2*(a+b+c))
    return x,y

def soddy_circle_radius(a,b,c):
    return (a*b*c)/(a*b+a*c+b*c+2*sqrt(a*b*c*(a+b+c)))

def dist(a,b,c):
    xd,yd = inner_point(a,b,c)
    xe,ye = cods(a,b,soddy_circle_radius(a,b,c))
    return sqrt((xd-xe)**2+(yd-ye)**2)

def ggcd(numbers):
    return reduce(gcd,numbers)

def main():
    res = [x for x in combinations(range(1,101),3) if ggcd(x)==1]
    return sum(dist(*x) for x in res)/len(res)
