# time cost = 791 µs ± 3.81 µs 

def quad_solver(a,b,c):
    delta = b**2-4*a*c
    x1 = (-b+delta**0.5)/(2*a)
    x2 = (-b-delta**0.5)/(2*a)
    return x1,x2

def next_point(x0,y0,x1,y1):
    i = (y1-y0)/(x1-x0)
    n = y1/(4*x1)
    r = (-i+2*n+i*n**2)/(1+2*i*n-n**2)
    m = y1-r*x1
    x21,x22 = quad_solver(4+r**2,2*m*r,m**2-100)
    if abs(x21-x1)>abs(x22-x1):
        x_new = x21
    else:
        x_new = x22
    y_new = r * x_new + m
    return x_new,y_new

def main():
    n = 1
    x0,y0,x1,y1 = 0,10.1,1.4,-9.6
    while True:
        x_new,y_new = next_point(x0,y0,x1,y1)
        if abs(x_new)<=0.01 and y_new>0:
            return n
        else:
            x0,y0,x1,y1 = x1,y1,x_new,y_new
            n += 1
