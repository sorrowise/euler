t = lambda n : n*(n+1)/2
p = lambda n : n*(3*n-1)/2
h = lambda n : n*(2*n-1)

up = 301
while True:
    ts = set([t(n) for n in range(286,up)])
    ps = set([p(n) for n in range(166,up)])
    hs = set([h(n) for n in range(144,up)])
    if (ts & ps & hs) == set():
        up += 10000
    else:
        print(ts & ps & hs)
        break
