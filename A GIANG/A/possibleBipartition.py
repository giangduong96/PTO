# DFS
def possibleBipartition(N, dislikes):
    # Build bi-directional graph
    import collections
    graph = collections.defaultdict(list)
    for i, j in dislikes:
        graph[i].append(j)
        graph[j].append(i)
    print(graph)
    color = {}

    # Color nodes, if a node is colored as '0', color the disliked nodes as '1'
    # Check if we've already visited a node that there isn't a conflict
    def dfs(node, c=0):
        if node in color:
            # print("TT", node)
            return color[node] == c
        color[node] = c
        # print("KK", node, c)
        m = all(dfs(neighbor, c ^ 1) for neighbor in graph[node])
        # print("mm", m)
        return m

    # DFS all nodes & make sure all are valid

    t = all(dfs(node)
            for node in range(1, N + 1)
            if node not in color)

    return t


array = [[1, 2], [1, 3], [2, 4]]
array2 = [[1, 2], [1, 3], [2, 3]]
possibleBipartition(3, array2)

"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
"""

import collections
def bipartition(N, array):
    graph = collections.defaultdict(list)

    for i, j in array:
        graph[i].append(j)
        graph[j].append(i)

    seen = {}

    def dfs(node, color = 0):
        if node in seen:
            return seen[node] == color
        seen[node] = color
        return all(dfs(neighbor, color ^ 1) for neighbor in graph[node])

    return all(dfs(node) for node in range(1, N+1) if node not in seen)

