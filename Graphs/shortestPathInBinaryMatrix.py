import math
from collections import deque


def shortestPath(grid):
    """
    In an N by N square grid, each cell is either empty (0) or blocked (1).

    A clear path from top-left to bottom-right has length k if and only if it is 
    composed of cells C_1, C_2, ..., C_k such that:

    Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are 
    different and share an edge or corner)

    C_1 is at location (0, 0) (ie. has value grid[0][0])
    C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
    If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
    Return the length of the shortest such clear path from top-left to bottom-right.  
    If such a path does not exist, return -1.


    IDEA + CONCEPT: BFS to find shortest path in unweighted graph
    """

    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1

    n = len(grid)
    visited = [[False for _ in range(n)] for _ in range(n)]
    dist = [[math.inf for _ in range(n)] for _ in range(n)]

    dist[0][0] = 1

    q = deque()
    q.append((0, 0))

    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                 (0, 1), (1, -1), (1, 0), (1, 1)]

    while q:
        x, y = q.popleft()

        for dx, dy in neighbors:
            if 0 <= x + dx < n and 0 <= y + dy < n and not visited[x + dx][y + dy]:
                visited[x + dx][y + dy] = True
                if grid[x + dx][y + dy] == 0:
                    dist[x + dx][y + dy] = 1 + dist[x][y]
                    q.append((x + dx, y + dy))

    if dist[-1][-1] == math.inf:
        return -1
    else:
        return dist[-1][-1]
