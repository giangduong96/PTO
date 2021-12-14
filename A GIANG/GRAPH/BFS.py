graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue

""" 
use queue, graph uses dictionary
    Pick any node, visit the adjacent un-visited vertex -> mark it as visited, displace it 
    , and insert it in a queue
    If there are no remaining adjacent vertices left, remove the first vertex from the queue 
    Repeat step 1 and step 2 until the queue defis empty or the desired node is found 
O(V+E)

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)


    while queue:
        s = queue.pop(0)
        print(s, end= " ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    bfs(visited, graph, "A")
"""






def dfs(graph, visited, node):
    if node not in visited:
        visited.append(node)
        print(node)

        for neighbor in graph[node]:
            dfs(graph, visited, neighbor)


def bfs2(graph, node):
    visited = []  # List to keep track of visited nodes.
    queue = []  # Initialize a queue
    visited.append(node)
    queue.append(node)

    while queue:
        s = visited.pop(0)
        print(s)

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)




def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph,neighbor, visited)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue

""" 
use queue, graph uses dictionary
    Pick any node, visit the adjacent un-visited vertex -> mark it as visited, displace it 
    , and insert it in a queue
    If there are no remaining adjacent vertices left, remove the first vertex from the queue 
    Repeat step 1 and step 2 until the queue defis empty or the desired node is found 
O(V+E)

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)


    while queue:
        s = queue.pop(0)
        print(s, end= " ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    bfs(visited, graph, "A")
"""






def dfs(graph, visited, node):
    if node not in visited:
        visited.append(node)
        print(node)

        for neighbor in graph[node]:
            dfs(graph, visited, neighbor)


def bfs2(graph, node):
    visited = []  # List to keep track of visited nodes.
    queue = []  # Initialize a queue
    visited.append(node)
    queue.append(node)

    while queue:
        s = visited.pop(0)
        print(s)

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)




def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)

        for neighbor in graph[node]:
            dfs(graph,neighbor, visited)

def bfs(graph, node):
    queue =[]
    visited = []

    visited.append(node)
    queue.append(node)

    while queue:
        start = queue.pop(0)

        for neighbor in graph[start]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

