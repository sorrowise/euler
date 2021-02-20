# time cost = 5.9 ms ± 75.7 µs

import numpy as np
import networkx as nx

def convert_matrix_to_graph():
    with open('data/pe107.txt') as f:
        network = []
        for line in f.readlines():
            line = line.replace('-','0').strip()
            network.append([int(x) for x in line.split(',')])
        g = nx.from_numpy_array(np.array(network))
        return g

def main():
    g = convert_matrix_to_graph()
    mst = nx.minimum_spanning_tree(g)
    g_weights = g.size(weight='weight')
    mst_weights = t.size(weight='weight')
    return g_weights-mst_weights
