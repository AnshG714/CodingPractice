from collections import defaultdict


def findRedundantConnection(edges: [[int]]):
    """
    In this problem, a tree is an undirected graph that is connected and has no cycles.

    The given input is a graph that started as a tree with N nodes (with distinct 
    values 1, 2, ..., N), with one additional edge added. The added edge has two 
    different vertices chosen from 1 to N, and was not an edge that already existed.

    The resulting graph is given as a 2D-array of edges. Each element of edges is 
    a pair [u, v] with u < v, that represents an undirected edge connecting nodes 
    u and v.

    Return an edge that can be removed so that the resulting graph is a tree of N 
    nodes. If there are multiple answers, return the answer that occurs last in 
    the given 2D-array. The answer edge [u, v] should be in the same format, with 
    u < v.

    Example 1:

    Input: [[1,2], [1,3], [2,3]]
    Output: [2,3]
    Explanation: The given undirected graph will be like this:
      1
    /  \ 
    2 - 3

    FIRST GO: DFS
    Try to connect two nodes of an edge with pre-existing edges. If you can 
    connect them, cycle is found. Otherwise, add this edge. 
    """

    graph = defaultdict(list)

    def dfs(source, target):
        seen.add(source)
        if source == target:
            return True
        for node in graph[source]:
            if node not in seen:
                if dfs(node, target):
                    return True

        return False

    for edge in edges:
        seen = set()
        if dfs(*edge):
            return edge
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])


class DSU:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [1 for _ in range(N)]

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi == pj:
            return False
        elif self.rank[pi] > self.rank[pj]:
            self.parent[pj] = pi
            self.rank[pi] += self.rank[pj]
        else:
            self.parent[pi] = pj
            self.rank[pj] += self.rank[pi]

        return True


def findRedundantConnection2(edges):
    """
    Use Disjoint Set Union Data Structure!!
    """
    dsu = DSU(1001)
    for edge in edges:
        if not dsu.union(*edge):
            return edge
