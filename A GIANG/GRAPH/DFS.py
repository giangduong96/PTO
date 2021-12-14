graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}



"""
    Pick a node. If its un-visited, mark it as visited and recur on all its adjacent nodes
    Repeat until all the nodes are visited, or the node to be search is found
"""

visited = [] # List to keep track of visited nodes.
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

if __name__ == '__main__':
    #dfs(visited, graph, "A")
    print(graph.pop("A"))
    print(graph.popitem())
    print(graph.popitem())
    print(graph)


