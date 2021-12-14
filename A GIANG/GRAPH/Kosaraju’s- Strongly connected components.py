"""
Create empty stack 'S' and do DFS. After visited all of child vertex, we put the parent vertex in stack
Reverse directions of all edges
Pop vertices from 'S', After visited all of child vertex, we have a strong component

"""

from collections import defaultdict


class Graph():

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, v, u):
        self.graph[v].append(u)

    def DFS(self, v, visited):
        # mark the current node as visited and print it
        visited[v] = True
        print(v, end="")

        # recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[v]:
            if not visited[neighbor]:  # visited[i] == False
                self.DFS(neighbor, visited)

    def fillOrder(self, vertex, visited, stack):
        visited[vertex] = True

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:  # visited[i] == False
                self.fillOrder(neighbor, visited, stack)
        stack = stack.append(vertex)

    def reverse_graph(self):
        g = Graph(self.V)  # create a new graph

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def SCC(self):
        stack = []

        # mark all vertices are unvisited
        visited = [False] * self.V

        # fill vertices in stack according to their finishing times
        for neighbor in range(self.V):
            if not visited[neighbor]: # visited[i] == False
                self.fillOrder(neighbor, visited, stack)

        # create reverse graph
        gr = self.reverse_graph()

        # mark all vertices are unvisited
        visited = [False] * self.V

        # now process all vertices in order defined by Stack
        while stack:
            vertex = stack.pop()  # pop from the top
            for neighbor in self.graph[vertex]:
                if not visited[neighbor]: # visited[i] == False
                    gr.DFS(neighbor, visited)
                    print("")


# Create a graph given in the above diagram
g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

print("Following are strongly connected components " +
      "in given graph")
g.SCC()



