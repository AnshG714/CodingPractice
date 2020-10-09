from Graph import Graph


def topologicalSortUtil(g: Graph, visited, stack, node):
    visited.add(node)
    for nei in g.graph[node]:
        if not nei in visited:
            topologicalSortUtil(g, visited, stack, nei)

    stack.append(node)


def topologicalSort(graph):

    visited = set()
    stack = []
    for node in graph.graph:
        if not node in visited:
            topologicalSortUtil(graph, visited, stack, node)

    return stack[::-1]
