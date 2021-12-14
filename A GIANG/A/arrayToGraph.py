import collections


def arrayToGraph(dislikes):
    graph = collections.defaultdict(list)
    for u, v in dislikes:
        graph[u].append(v)
        graph[v].append(u)  # non direct graph

def arrayToGraph(dislikes):
    graph = collections.defaultdict(list)
    for u, v in dislikes:
        graph[u].append(v)
        graph[v].append(u)
