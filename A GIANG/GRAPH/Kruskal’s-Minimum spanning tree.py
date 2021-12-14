class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # find: recursively find highest parent
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        parent = []
        rank = []
        i, edges = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        print(self.graph)
        for node in range(self.V):
            parent.append(node)  # make node is its parent
            rank.append(0)

        while edges < self.V - 1:  # only need to find edges which V -1
            u, v, w = self.graph[i]  # graph[i] is smallest weight now
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                edges += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        for u, v, weight in result:
            print(u, v, weight)
        print(parent, rank)


g = Graph(6)
g.add_edge(0, 1, 3)
g.add_edge(0, 3, 1)
g.add_edge(1, 3, 3)
g.add_edge(1, 2, 1)
g.add_edge(2, 3, 1)
g.add_edge(3, 4, 6)
g.add_edge(2, 4, 5)
g.add_edge(2, 5, 4)
g.add_edge(4, 5, 2)

g.kruskal()
