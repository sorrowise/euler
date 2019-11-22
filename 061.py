# time cost = 92.1 ms ± 1.28 ms

from collections import namedtuple

def poly_numbers(s,n):
    Pn = namedtuple('Pn','s v ftd ltd')
    v = (n**2*(s-2)-n*(s-4))//2
    ftd,ltd = v // 100, v % 100
    pn = Pn(s,v,ftd,ltd)
    return pn

def poly_number_graph():
    arr,graph = [],{}
    for s in range(3,9):
        for n in range(19,141):
            pn = poly_numbers(s,n)
            if 999 < pn.v < 10000 and pn.ltd>9:
                arr.append(pn)
    for pn in arr:
        res = []
        for apn in arr:
            if pn.s != apn.s and pn.ltd == apn.ftd:
                res.append(apn)
        graph[pn] = res
    return graph        

def dfs(graph,types,numbers):
    if len(types) == 6 and numbers[-1].ltd == numbers[0].ftd:
        print(sum([x.v for x in numbers]))
    else:
        for pn in graph.get(numbers[-1],[]):
            if pn.s not in types:
                dfs(graph,types+[pn.s],numbers+[pn])

def main():
    graph = poly_number_graph()
    for pn in graph:
        dfs(graph,[pn.s],[pn])
