# time cost = 1.92 ms ± 111 µs

from sympy import prevprime

def main():
    start = 7654321
    while True:
        prevp = prevprime(start)
        if set(str(prevp)) == set('1234567'):
            return prevp
        else:
            start = prevp   
