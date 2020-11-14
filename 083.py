# time cost = 98.2 ms ± 580 µs

import networkx as nx

def main():
    with open('data/pe083.txt') as f:
        matrix = [[int(x) for x in row.split(',')] for row in f.readlines()]
    G = nx.DiGraph()
    for i in range(n):
        for j in range(m):
            neighbors = [(i+x, j+y) for x, y in [(-1,0), (0,-1), (1,0), (0,1)] if 0 <= i+x < n and 0 <= j+y < m]
            for ix, jy in neighbors:
                G.add_edge((i, j), (ix, jy), weight = matrix[ix][jy])
    path_length = nx.dijkstra_path_length(G, source=(0,0), target=(n-1,m-1))
    return path_length + matrix[0][0]
