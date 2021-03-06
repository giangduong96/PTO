# Bellman Ford Algorithm, neg weight,  detect neg circle.
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # this also detect neg weight circle
    def BellmanFord(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0  # its make sure dist[u] != float("Inf") first loop is True. and only one path start

        # Relax all edge (V -1) times
        for _ in range(self.V - 1):
            # update distance value and parent index of the adjacent vertices of the picked vertex.
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # check for neg weight cycle, do one more loop
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print(" Graph contains neg weight cycle")
                return

        # print path
        for i in range(self.V):
            print("%d \t\t %d" % (i, dist[i]))


g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

# Print the solution
print(g.BellmanFord(0))
