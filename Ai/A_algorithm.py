# Implement A* algorithm


import networkx as nx
import matplotlib.pyplot as plt
Graph_nodes = {  
    'A': [('B', 2), ('E', 3)],  
    'B': [('C', 1), ('G', 9)],  
    'C': [],  
    'E': [('D', 6)], 
    'D': [('G', 1)], 
    'G': []  
}  
def heuristic(n): 
    H_dist = {  
        'A': 11, 
        'B': 6,  
        'C': 99, 
        'D': 1,  
        'E': 7,  
        'G': 0,  
    }  
    return H_dist[n]  
def get_neighbors(v):  
    return Graph_nodes.get(v, [])  
def aStarAlgo(start_node, stop_node):  
    open_set = set([start_node])  
    closed_set = set()  
    g = {start_node: 0}  
    parents = {start_node: start_node}  
    while open_set:  
        n = None  
        for v in open_set:  
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):  
                n = v  
        if n is None:  
            print("Path does not exist!")  
            return None  
        if n == stop_node:  
            path = []  
            while parents[n] != n:  
                path.append(n)  
                n = parents[n]  
            path.append(start_node)  
            path.reverse()  
            print("Path found:", path)  
            return path  
        for (m, weight) in get_neighbors(n):  
            if m not in open_set and m not in closed_set:  
                open_set.add(m)  
                parents[m] = n  
                g[m] = g[n] + weight  
            else:  
                if g[m] > g[n] + weight:  
                    g[m] = g[n] + weight  
                    parents[m] = n  
                    if m in closed_set:  
                        closed_set.remove(m)  
                        open_set.add(m)  
        open_set.remove(n)  
        closed_set.add(n)  
    print("Path does not exist!")  
    return None  
path = aStarAlgo('A', 'G')  
G = nx.DiGraph()  
for node in Graph_nodes:  
    for neighbor, weight in Graph_nodes[node]:  
        G.add_edge(node, neighbor, weight=weight)  
pos = nx.spring_layout(G) 
plt.figure(figsize=(8, 6))  
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', 
        node_size=2000, font_size=10, font_weight='bold')  
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)} 
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)  
if path:  
    path_edges = list(zip(path, path[1:])) 
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', 
                           width=2.5)
plt.title("Graph Representation with A* Algorithm Path")
plt.show()