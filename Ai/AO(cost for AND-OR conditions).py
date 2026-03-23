# Function to calculate cost for AND-OR conditions


def Cost(H, condition, weight=1):
    cost = {}
    if 'AND' in condition:  
        AND_nodes = condition['AND']  
        Path_A = ' AND '.join(AND_nodes)  
        PathA = sum(H[node] + weight for node in AND_nodes)  
        cost[Path_A] = PathA  
    if 'OR' in condition:  
        OR_nodes = condition['OR']  
        Path_B = ' OR '.join(OR_nodes)  
        PathB = min(H[node] + weight for node in OR_nodes)  
        cost[Path_B] = PathB  
    return cost  
def update_cost(H, Conditions, weight=1): 
    Main_nodes = list(Conditions.keys())  
    Main_nodes.reverse()  
    least_cost = {}  
    for key in Main_nodes:  
        condition = Conditions[key]  
        print(key, ':', Conditions[key], '>>>', Cost(H, condition, weight)) 
        c = Cost(H, condition, weight)  
        H[key] = min(c.values())  
        least_cost[key] = Cost(H, condition, weight) 
    return least_cost  
def shortest_route(Start, Updated_cost, H): 
    Path = Start
    if Start in Updated_cost.keys(): 
        Min_cost = min(Updated_cost[Start].values())  
        key = list(Updated_cost[Start].keys())  
        values = list(Updated_cost[Start].values())  
        Index = values.index(Min_cost)
        Next = key[Index].split()
        if len(Next) == 1: 
            Start = Next[0]  
            Path += '<--' + shortest_route(Start, Updated_cost, H)  
        else:  
            Path += '<--(' + key[Index] + ') '  
            Start = Next[0]  
            Path += '[' + shortest_route(Start, Updated_cost, H) + ' + '  
            Start = Next[-1]  
            Path += shortest_route(Start, Updated_cost, H) + ']'  
    return Path  
import networkx as nx
import matplotlib.pyplot as plt
def visualize_graph(conditions, updated_cost, H): 
    G = nx.DiGraph()  
    for node, condition in conditions.items():  
        if 'AND' in condition:  
            for n in condition['AND']:  
                G.add_edge(node, n, label='AND', color='green') 
        if 'OR' in condition:  
            for n in condition['OR']:  
                G.add_edge(node, n, label='OR', color='blue')  
    pos = nx.planar_layout(G) 
    labels = nx.get_edge_attributes(G, 'label')  
    colors = [G[u][v]['color'] for u, v in G.edges]  
    plt.figure(figsize=(8, 6))   
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=2000, font_size=10, font_weight='bold',
            edge_color=colors, arrows=True)  
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red') 
    plt.title('AND-OR Path Graph')  
    plt.show() 
H = {'A': -1, 'B': 5, 'C': 2, 'D': 4, 'E': 7, 'F': 9, 'G': 3, 'H': 0, 'I': 0, 'J': 0}  
Conditions = {  
    'A': {'OR': ['B'], 'AND': ['C', 'D']}, 
    'B': {'OR': ['E', 'F']},  
    'C': {'OR': ['G'], 'AND': ['H', 'I']},
    'D': {'OR': ['J']}  
}
weight = 1  
print('Updated Cost:') 
Updated_cost = update_cost(H, Conditions, weight)
print('*' * 75) 
print('Shortest Path:\n', shortest_route('A', Updated_cost, H))
visualize_graph(Conditions, Updated_cost, H) 