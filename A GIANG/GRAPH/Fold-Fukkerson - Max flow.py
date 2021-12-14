from collections import defaultdict

# BFS
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(self.graph)

    # using BFS as searching augmenting paths between source and parent
    def searching_algo_BFS(self, source, sink, parent):
        visited = [False] * self.ROW
        queue = [source]
        visited[source] = True

        while queue:
            u = queue.pop(0)
            # backward
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[sink] else False

    # applying fold fulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # adding the path flows
            max_flow += path_flow

            # update residual values of edges
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow       # this create augmenting path, since the min path will remove
                # they will form a new graph
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow


graph1 = [[0, 8, 0, 0, 3, 0],
          [0, 0, 9, 0, 0, 0],
          [0, 0, 0, 0, 7, 2],
          [0, 0, 0, 0, 0, 5],
          [0, 0, 7, 4, 0, 0],
          [0, 0, 0, 0, 0, 0]]

g = Graph(graph1)

source = 0
sink = 5

print("Max Flow: %d " % g.ford_fulkerson(source, sink))
