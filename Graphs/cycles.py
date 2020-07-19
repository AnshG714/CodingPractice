from Graph import Graph


def findCycleInDirectedGraph(graph):
    visited = set()
    recursive = set()

    def findCycleUtil(node):
        recursive.add(node)
        visited.add(node)
        for neighbor in graph.graph[node]:
            if not neighbor in visited and findCycleUtil(neighbor):
                return True
            elif neighbor in recursive:
                return True
        recursive.remove(node)
        return False

    for node in graph.graph.keys():
        if node not in visited and findCycleUtil(node):
            return True

    return False
