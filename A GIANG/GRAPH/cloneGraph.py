"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.


"""


# O(N) O(N) BFS
class Node:
    def __init__(self, val=0, neighor=None):
        self.val = val
        self.neighbor = neighor

    def cloneGraph(self, node):
        if node is None:
            return None

        clone_node = Node(node.val)
        clonedGraph, queue = {node: clone_node}, [node]

        while queue:
            current = queue.pop()
            for neighbor in current.neighbors:
                if neighbor not in clonedGraph:
                    queue.append(neighbor)
                    clonedGraph_neighbor = Node(neighbor.val)
                    clonedGraph[neighbor] = clonedGraph_neighbor
                # update the self.neighbor
                clonedGraph[current].neighbors.append(clonedGraph[neighbor])
        return clonedGraph[node]

