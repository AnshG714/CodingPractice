from Graph import Graph
from collections import deque


def BFS(graph, node):
    visited = set()

    queue = deque()
    queue.append(node)
    res = []
    visited.add(node)

    while queue:
        size = len(queue)
        temp = []

        for _ in range(size):
            top = queue.popleft()

            for i in graph.graph[top]:
                if not i in visited:
                    queue.append(i)
                    visited.add(i)

            temp.append(top)

        res.append(temp)

    return res


def DFS(graph, node):
    stack = []
    visited = set()
    res = []

    stack.append(node)
    visited.add(node)

    while stack:
        top = stack.pop()

        for i in graph.graph[top]:
            if not i in visited:
                stack.append(i)
                visited.add(i)

        res.append(top)

    return res


def DFSRec(graph, node):
    visited = set()
    res = []

    def helper(node):
        res.append(node)
        visited.add(node)
        for i in graph.graph[node]:
            if not i in visited:
                helper(i)

    helper(node)
    return res
