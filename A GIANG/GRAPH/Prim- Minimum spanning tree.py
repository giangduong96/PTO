example_graph = {
    'A': {'D': 1, 'B': 3},
    'B': {'D': 3, 'C': 1, 'A': 3},
    'C': {'D': 1, 'B': 1, 'F': 4},
    'D': {'A': 1, 'C': 1, 'E': 6},
    'E': {'C': 5, 'D': 6, 'F': 2},
    'F': {'C': 4, 'E': 2}
}



"""
Prim: 
Start with a weighted graph
Choose a vertex
Choose the shortest edge from this vertex and add it
Choose the nearest not yet in solution, if there are multiple choices, choose one at random
Repeat until you have Spanning Tree
"""

from collections import defaultdict
import heapq
def create_spanning_tree(graph, start_vertex):
    mst = defaultdict(set)
    visited = set([start_vertex])
    edges = [(cost, start_vertex, to) for to, cost in graph[start_vertex].items()]
    heapq.heapify(edges)
    # sum = 0
    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            # sum += cost
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst


print(create_spanning_tree(example_graph, "A"))

