from itertools import permutations

def tsp(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    for perm in permutations(nodes):
        cost = 0
        k = start
        for j in perm:
            cost += graph[k][j]
            k = j
        cost += graph[k][start]
        if cost < min_cost:
            min_cost = cost
            min_path = (start,) + perm + (start,)
    return min_path, min_cost

# Example Graph (Adjacency Matrix as Dict of Dicts)
graph = {
    0: {0:0,1:10,2:15,3:20},
    1: {0:10,1:0,2:35,3:25},
    2: {0:15,1:35,2:0,3:30},
    3: {0:20,1:25,2:30,3:0}
}
path, cost = tsp(graph, 0)
print("Shortest Path:", path)
print("Total Cost:", cost)
