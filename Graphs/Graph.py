from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def __str__(self):
        res = ""
        for k in self.graph.keys():
            res += str(k) + ' -> '
            res += str(self.graph[k])
            res += '\n'
        return res
