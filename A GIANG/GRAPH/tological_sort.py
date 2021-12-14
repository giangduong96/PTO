from collections import defaultdict
# same as kosaraju

class Graph():
    def __init__(self, vertice):
        self.graph = defaultdict(list)
        self.V = vertice

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, visited, vertex):
        visited[vertex] = True
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.DFS(visited, neighbor)

    def tological_sort(self):
        stack = []
        visited = [False] * self.V
        result = []

        for neighbor in range(self.V):
            if not visited[neighbor]:
                stack.append(neighbor)
                self.DFS(visited, neighbor)

        while stack:
            v = stack.pop()
            result.append(v)
        return result


g = Graph(6)
g.add_edge(5, 2);
g.add_edge(5, 0);
g.add_edge(4, 0);
g.add_edge(4, 1);
g.add_edge(2, 3);
g.add_edge(3, 1);


print("Following is a Topological Sort of the given graph")
print(g.tological_sort())
