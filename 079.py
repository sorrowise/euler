# time cost = 367 µs ± 2.94 µs

import networkx as nx

def get_data_from_file(file_name="data/ep79.txt"):
    data = set()
    with open(file_name) as f:
        for line in f.readlines():
            data.add(line)
    return data

def main():
    data = get_data_from_file()
    G = nx.DiGraph()
    for i in data:
        G.add_edges_from([(i[0],i[1]),(i[1],i[2])])
    ans = list(nx.all_topological_sorts(G))[0]
    return int(''.join(ans))
